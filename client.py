import grpc
import proto.struct_pb2 as pb2
import proto.struct_pb2_grpc as pb2_grpc
import asyncio
from pick import pick
from random import choice

ELIMINATE_VOTE = "Vote for eliminating player"
GET_ROOM_INFO = "Get info about this room"
DAY_END = "Stop actions for this day"
NIGHT_END = "Stop actions for this night"
SPIRIT_WATCHING = "Continue watching"
SHOW_ROLE = "Show role of the user"
OFFICER_STATEMENT = "SHOW USERS YOUR CHECK"
EXIT = "EXIT"
CREATE_ROOM = "Create a new room"
JOIN_ROOM = "Join the room"
DAY = True
NIGHT = False
MANUAL = "You choose actions"
AUTOMATIC = "Game is random"
END_GAME = 1
UNKNOWN_ROLE = "Unknown"
MAFIA_ROLE = "Mafia"
OFFICER_ROLE = "Officer"
CIVILIAN_ROLE = "Civilian"
SPIRIT_ROLE = "Spirit"


class Client:
    def __init__(self, stub, channel):
        self.stub = stub
        self.channel = channel
        self.users_in_room = dict()
        self.username = None
        self.role = None
        self.session_name = None
        self.current_time = DAY
        self.officer_statement = None

    async def start_game(self):
        self.username = input("Please enter username: ")
        while True:
            game_start, _ = pick([CREATE_ROOM, JOIN_ROOM], 'Select way you want to start playing:', indicator='->',
                                 default_index=0)
            if game_start == JOIN_ROOM:
                self.session_name = input("Please enter room name: ")
                print("Trying to join!\nWaiting for other players!")
                if not await self.join():
                    await asyncio.sleep(2)
                    continue
                break
            if game_start == CREATE_ROOM:
                if not await self.create():
                    await asyncio.sleep(2)
                    continue
                print(f"Room {self.session_name} successfully created!\nWaiting for others players...")
                await self.join()
                break

    async def join(self):
        response = await self.stub.JoinRoom(
            pb2.JoinRoomRequest(username=self.username, session_name=self.session_name)
        )
        if response.status:
            print("You successfully joined the room!")
            self.users_in_room = response.users
            self.role = response.role
            return True

        print(f"Can't join to room! Reason: {response.info}")
        return False

    async def create(self):
        self.session_name = input("Please enter new room name: ")
        room_size = int(input("Please input room size: "))
        response = await self.stub.CreateRoom(
            pb2.CreateRoomRequest(username=self.username, session_name=self.session_name, game_size=room_size))
        if response.status:
            return True
        print(f"Something went wrong. {response.info}")
        return False


async def message_handler(client):
    async for message in client.stub.GameEvents(
            pb2.GameEventsRequest(username=client.username, session_name=client.session_name)
    ):
        print(message.text)
        if message.format == END_GAME:
            await client.channel.close()
            exit(0)


def get_random_user(user_list, my_username, my_role):
    users = list()
    for username, role in user_list.items():
        if role != SPIRIT_ROLE and my_username != username and (my_role != MAFIA_ROLE or role != MAFIA_ROLE):
            users.append(username)

    return choice(users)


def get_alive_users(user_list, my_username):
    users = list()
    for username, role in user_list.items():
        if role != SPIRIT_ROLE and my_username != username:
            users.append(username)

    return users


async def automatic_night_game(client):
    random_user = get_random_user(client.users_in_room, client.username, client.role)
    if client.role == MAFIA_ROLE:
        await client.stub.Eliminated(pb2.EliminatedRequest(username=client.username,
                                                           session_name=client.session_name,
                                                           corpse_name=random_user))
        print(f"You voted for killing {random_user}")
    else:
        response = await client.stub.ShowRole(pb2.ShowRoleRequest(username=client.username,
                                                                  session_name=client.session_name,
                                                                  suspect=random_user))
        print(f"Well! Now you now that {random_user} is {response.role}")
        client.officer_statement = random_user
        response = await client.stub.OfficerStatement(pb2.OfficerStatementRequest(username=random_user,
                                                                                  session_name=client.session_name))


async def night_game(client):
    action_list = [ELIMINATE_VOTE, GET_ROOM_INFO, NIGHT_END]
    if client.role == OFFICER_ROLE:
        action_list = [SHOW_ROLE, GET_ROOM_INFO, NIGHT_END]
    while True:
        input("Press Enter to choose an action")
        action, _ = pick(action_list, 'What do you want to do?', indicator='->', default_index=0)

        if action == SHOW_ROLE:
            action_list.remove(SHOW_ROLE)
            action_list.append(OFFICER_STATEMENT)
            users = get_alive_users(client.users_in_room, client.username)

            suspect, _ = pick(users, 'Choose a player to execute: ', indicator='->',
                              default_index=0)
            response = await client.stub.ShowRole(pb2.ShowRoleRequest(username=client.username,
                                                                      session_name=client.session_name,
                                                                      suspect=suspect))
            print(f"Well! Now you now that {suspect} is {response.role}")
            client.officer_statement = suspect

        if action == ELIMINATE_VOTE:
            action_list.remove(action)
            users = get_alive_users(client.users_in_room, client.username)

            corpse_name, _ = pick(users, 'Choose a player to execute: ', indicator='->',
                                  default_index=0)
            await client.stub.Eliminated(pb2.EliminatedRequest(username=client.username,
                                                               session_name=client.session_name,
                                                               corpse_name=corpse_name))
            print(f"You voted for the execution of {corpse_name}")

        if action == OFFICER_STATEMENT:
            action_list.remove(OFFICER_STATEMENT)
            response = await client.stub.OfficerStatement(pb2.OfficerStatementRequest(username=client.officer_statement,
                                                                                      session_name=client.session_name))

        if action == GET_ROOM_INFO:
            response = await client.stub.ShowUsersInRoom(
                pb2.ShowUsersInRoomRequest(username=client.username,
                                           session_name=client.session_name))
            for username, role in response.user_list.items():
                print(f"{username} - {role}")

        if action == NIGHT_END:
            break


async def automatic_day_game(client, is_it_preparing_time):
    if not is_it_preparing_time:
        random_user = get_random_user(client.users_in_room, client.username, client.role)
        await client.stub.Eliminated(pb2.Eliminated(username=client.username,
                                                    session_name=client.session_name,
                                                    corpse_name=random_user))
        print(f"You voted for the execution of {random_user}")


async def day_game(client, is_it_preparing_time):
    action_list = [ELIMINATE_VOTE, GET_ROOM_INFO, DAY_END]
    if is_it_preparing_time:
        action_list = [GET_ROOM_INFO, DAY_END]

    while True:
        input("Press Enter to choose an action")
        action, _ = pick(action_list, 'Choose an action: ', indicator='->', default_index=0)

        if action == ELIMINATE_VOTE:
            action_list.remove(ELIMINATE_VOTE)
            users = get_alive_users(client.users_in_room, client.username)

            victim, _ = pick(users, 'Choose a player to execute: ', indicator='->', default_index=0)
            await client.stub.Eliminated(pb2.Eliminated(username=client.username,
                                                        session_name=client.session_name,
                                                        corpse_name=victim))
            print(f"You voted for the execution of {victim}")

        if action == GET_ROOM_INFO:
            response = await client.stub.ShowUsersInRoom(pb2.ShowUsersInRoomRequest(username=client.username,
                                                                                    session_name=client.session_name))
            for username, role in response.user_list.items():
                print(f"{username} - {role}")

        if action == DAY_END:
            break


async def mafia_game(client):
    print(f"Greetings player! Today you are {client.role}")
    mode, _ = pick([AUTOMATIC, MANUAL], "Select the way you want to play: ", indicator="->",
                   default_index=0)
    is_it_preparing_time = True
    while True:
        if not client.current_time and client.role != CIVILIAN_ROLE:
            if mode == AUTOMATIC:
                await automatic_night_game(client)
            else:
                await night_game(client)
        elif client.current_time:
            if mode == AUTOMATIC:
                await automatic_day_game(client, is_it_preparing_time)
            else:
                await day_game(client, is_it_preparing_time)
            is_it_preparing_time = False

        response = await client.stub.UpdateTimeInfo(
            pb2.UpdateTimeInfoRequest(username=client.username, session_name=client.session_name))

        if response.is_end_game:
            print(response.end_game_message)
            await asyncio.sleep(5)
            await client.channel.close()
            exit(0)

        client.current_time = not client.current_time

        if response.role != SPIRIT_ROLE and client.current_time:
            if response.role == MAFIA_ROLE:
                print(f"Well good luck to be more and more peaceful!")
            else:
                print(f"{client.current_time} it is lucky night for you!")
        elif client.current_time:
            print("You have been eliminated!")
            if mode == AUTOMATIC:
                await client.channel.close()
                exit(0)
            input("Press Enter key to choose an action")
            action, _ = pick([EXIT, SPIRIT_WATCHING], 'Choose an action: ', indicator='->', default_index=0)
            if action == EXIT:
                await client.channel.close()
                exit(0)
            if action == SPIRIT_WATCHING:
                client.role = SPIRIT_ROLE
            break

        client.users_in_room = response.users
        client.officer_statement = None


async def my_mafia_game():
    try:
        channel = grpc.aio.insecure_channel("0.0.0.0:8080")
        stub = pb2_grpc.MyMafiaEventsStub(channel)
        client = Client(stub, channel)
        await client.start_game()
        await asyncio.gather(
            mafia_game(client),
            message_handler(client)
        )
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    asyncio.run(my_mafia_game())
