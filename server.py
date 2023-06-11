import grpc
import proto.struct_pb2 as pb2
import proto.struct_pb2_grpc as pb2_grpc

import asyncio
from random import shuffle, choice

DAY = True
NIGHT = False
UNKNOWN_ROLE = "Unknown"
CIVILIAN_ROLE = "Civilian"
MAFIA_ROLE = "Mafia"
OFFICER_ROLE = "Officer"
SPIRIT_ROLE = "Spirit"
INFO = 0
END_GAME = 1


class GameObject:
    def __init__(self, username, game_name, room_size):
        self.session_name = game_name
        self.size = room_size
        self.username = username
        self.sync_point = asyncio.Condition()
        self.joined = 0
        self.message_queue = list()
        self.officer_statement = None
        self.eliminated_list = dict()
        self.current_time = DAY
        self.game_is_running = False
        self.user_list = list()
        self.internal_roles = dict()
        self.external_roles = dict()
        self.still_alive = room_size
        self.mafia_number = 0
        self.civilian_number = 0


class GameServer(pb2_grpc.MyMafiaEventsServicer):
    def __init__(self):
        self.sessions = dict()

    async def CreateRoom(self, request, context):
        if request.session_name in self.sessions:
            return pb2.CreateRoomResponse(status=False, info="Room with this name already exists\n")
        if request.game_size < 4:
            return pb2.CreateRoomResponse(status=False, info="Room size must be at least 4 users\n")
        self.sessions[request.session_name] = GameObject(request.username, request.session_name, request.game_size)
        self.sessions[request.session_name].message_queue.append(
            pb2.GameEventsResponse(format=INFO, text=f"You successfully joined to {request.session_name}"))
        return pb2.CreateRoomResponse(status=True, info="Room was successfully created\n")

    async def JoinRoom(self, request, context):
        if request.session_name not in self.sessions:
            return pb2.JoinRoomResponse(status=False, info="Room doesn't exists\n", role='')
        if self.sessions[request.session_name].game_is_running:
            return pb2.JoinRoomResponse(status=False, info="Room already running\n", role='')
        if request.username in self.sessions[request.session_name].user_list:
            return pb2.JoinRoomResponse(status=False, info=f"{request.username} already in room\n", role='')

        session = self.sessions[request.session_name]

        session.user_list.append(request.username)
        session.external_roles[request.username] = UNKNOWN_ROLE

        if len(session.user_list) < session.size:
            async with session.sync_point:
                await session.sync_point.wait()
        else:
            async with session.sync_point:
                session.mafia_number = 1 + session.size // 6
                session.civilian_number = (session.size - session.mafia_number)
                roles = [MAFIA_ROLE] * session.mafia_number + [OFFICER_ROLE] + \
                        [CIVILIAN_ROLE] * (session.civilian_number - 1)
                shuffle(roles)
                for i, username in enumerate(session.user_list):
                    session.internal_roles[username] = roles[i]
                session.sync_point.notify_all()

        self.sessions[request.session_name].game_is_running = True

        return pb2.JoinRoomResponse(status=True, info="Successful join to game\n",
                                    role=session.internal_roles[request.username],
                                    users=session.external_roles)

    async def UpdateTimeInfo(self, request, context):
        session = self.sessions[request.session_name]
        session.joined += 1
        if session.joined == session.still_alive:
            session.joined = 0
            async with session.sync_point:
                spirit = None
                vote_info = "Nobody wos eliminated"
                if len(session.eliminated_list):
                    max_vote = max(session.eliminated_list.values())
                    spirit = choice(
                        list(filter(lambda x: session.eliminated_list[x] == max_vote, session.eliminated_list.keys())))
                session.eliminated_list = dict()
                if spirit:
                    vote_info = f"{spirit} was eliminated"
                    role = session.internal_roles[spirit]
                    session.internal_roles[spirit] = SPIRIT_ROLE
                    session.external_roles[spirit] = SPIRIT_ROLE

                    session.still_alive -= 1
                    if role == MAFIA_ROLE:
                        session.mafia_number -= 1
                    elif role == CIVILIAN_ROLE:
                        session.civilian_number -= 1

                replica = "Good Night! The city is falling asleep the mafia is waking up!"
                if session.current_time:
                    session.current_time = NIGHT
                else:
                    replica = "Good Morning! The city wakes up!"
                    session.current_time = DAY
                session.message_queue.append(pb2.GameEventsResponse(format=INFO,
                                                                    text=replica))
                session.sync_point.notify_all()
                session.message_queue.append(pb2.GameEventsResponse(format=INFO,
                                                                    text=vote_info))
                if session.officer_statement:
                    publish_user = session.officer_statement
                    publish_role = session.internal_roles[publish_user]
                    session.external_roles[publish_user] = publish_role
                    officer_info = f"The officer states that {publish_user} is {publish_role}!"
                    session.message_queue.append(pb2.GameEventsResponse(format=INFO,
                                                                        text=officer_info))
                    session.officer_statement = None

        else:
            async with session.sync_point:
                await session.sync_point.wait()

        end_game_flag = False
        end_game_message = ""
        if session.mafia_number >= session.civilian_number:
            end_game_flag = True
            end_game_message = "The game is over the mafia has won!"
            session.message_queue.append(pb2.GameEventsResponse(format=END_GAME,
                                                                text=end_game_message))
        if session.mafia_number == 0:
            end_game_flag = True
            end_game_message = "The game is over civilians have won!"
            session.message_queue.append(pb2.GameEventsResponse(format=END_GAME,
                                                                text=end_game_message))

        return pb2.UpdateTimeInfoResponse(role=session.internal_roles[request.username],
                                          is_end_game=end_game_flag,
                                          end_game_message=end_game_message,
                                          users=session.external_roles)

    async def Eliminated(self, request, context):
        session = self.sessions[request.session_name]
        session.vote[request.corpse_name] += 1
        return pb2.EliminatedResponse(status=True, info=f"vote for {request.corpse_name}")

    async def ShowRole(self, request, context):
        session = self.sessions[request.session_name]
        return pb2.ShowRoleResponse(role=session.internal_roles[request.suspect])

    async def OfficerStatement(self, request, context):
        session = self.sessions[request.session_name]
        session.officer_statement = request.username
        return pb2.OfficerStatementResponse(status=True, info=f'Officer submitted {request.username}')

    async def ShowUsersInRoom(self, request, context):
        session = self.sessions[request.session_name]
        return pb2.ShowUsersInRoomResponse(user_list=session.external_roles)

    async def GameEvents(self, request, context):
        number = 0
        while True:
            queue = self.sessions[request.session_name].message_queue
            if len(queue) <= number:
                continue
            yield queue[number]
            number += 1


async def start_server():
    server = grpc.aio.server()
    pb2_grpc.add_MyMafiaEventsServicer_to_server(GameServer(), server)
    server.add_insecure_port("0.0.0.0:8080")
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(start_server())
