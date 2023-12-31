# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.struct_pb2 as struct__pb2


class MyMafiaEventsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GameEvents = channel.unary_stream(
                '/mafia.MyMafiaEvents/GameEvents',
                request_serializer=struct__pb2.GameEventsRequest.SerializeToString,
                response_deserializer=struct__pb2.GameEventsResponse.FromString,
                )
        self.ShowUsersInRoom = channel.unary_unary(
                '/mafia.MyMafiaEvents/ShowUsersInRoom',
                request_serializer=struct__pb2.ShowUsersInRoomRequest.SerializeToString,
                response_deserializer=struct__pb2.ShowUsersInRoomResponse.FromString,
                )
        self.UpdateTimeInfo = channel.unary_unary(
                '/mafia.MyMafiaEvents/UpdateTimeInfo',
                request_serializer=struct__pb2.UpdateTimeInfoRequest.SerializeToString,
                response_deserializer=struct__pb2.UpdateTimeInfoResponse.FromString,
                )
        self.CreateRoom = channel.unary_unary(
                '/mafia.MyMafiaEvents/CreateRoom',
                request_serializer=struct__pb2.CreateRoomRequest.SerializeToString,
                response_deserializer=struct__pb2.CreateRoomResponse.FromString,
                )
        self.JoinRoom = channel.unary_unary(
                '/mafia.MyMafiaEvents/JoinRoom',
                request_serializer=struct__pb2.JoinRoomRequest.SerializeToString,
                response_deserializer=struct__pb2.JoinRoomResponse.FromString,
                )
        self.Eliminated = channel.unary_unary(
                '/mafia.MyMafiaEvents/Eliminated',
                request_serializer=struct__pb2.EliminatedRequest.SerializeToString,
                response_deserializer=struct__pb2.EliminatedResponse.FromString,
                )
        self.ShowRole = channel.unary_unary(
                '/mafia.MyMafiaEvents/ShowRole',
                request_serializer=struct__pb2.ShowRoleRequest.SerializeToString,
                response_deserializer=struct__pb2.ShowRoleResponse.FromString,
                )
        self.OfficerStatement = channel.unary_unary(
                '/mafia.MyMafiaEvents/OfficerStatement',
                request_serializer=struct__pb2.OfficerStatementRequest.SerializeToString,
                response_deserializer=struct__pb2.OfficerStatementResponse.FromString,
                )
        self.GetUsersInfo = channel.unary_unary(
                '/mafia.MyMafiaEvents/GetUsersInfo',
                request_serializer=struct__pb2.GetUsersInfoRequest.SerializeToString,
                response_deserializer=struct__pb2.GetUsersInfoResponse.FromString,
                )
        self.GetUserInfo = channel.unary_unary(
                '/mafia.MyMafiaEvents/GetUserInfo',
                request_serializer=struct__pb2.GetUserInfoRequest.SerializeToString,
                response_deserializer=struct__pb2.GetUserInfoResponse.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/mafia.MyMafiaEvents/AddUser',
                request_serializer=struct__pb2.AddUserRequest.SerializeToString,
                response_deserializer=struct__pb2.AddUserResponse.FromString,
                )
        self.EditUser = channel.unary_unary(
                '/mafia.MyMafiaEvents/EditUser',
                request_serializer=struct__pb2.EditUserRequest.SerializeToString,
                response_deserializer=struct__pb2.EditUserResponse.FromString,
                )


class MyMafiaEventsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GameEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowUsersInRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTimeInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Eliminated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OfficerStatement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyMafiaEventsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GameEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.GameEvents,
                    request_deserializer=struct__pb2.GameEventsRequest.FromString,
                    response_serializer=struct__pb2.GameEventsResponse.SerializeToString,
            ),
            'ShowUsersInRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.ShowUsersInRoom,
                    request_deserializer=struct__pb2.ShowUsersInRoomRequest.FromString,
                    response_serializer=struct__pb2.ShowUsersInRoomResponse.SerializeToString,
            ),
            'UpdateTimeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTimeInfo,
                    request_deserializer=struct__pb2.UpdateTimeInfoRequest.FromString,
                    response_serializer=struct__pb2.UpdateTimeInfoResponse.SerializeToString,
            ),
            'CreateRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRoom,
                    request_deserializer=struct__pb2.CreateRoomRequest.FromString,
                    response_serializer=struct__pb2.CreateRoomResponse.SerializeToString,
            ),
            'JoinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinRoom,
                    request_deserializer=struct__pb2.JoinRoomRequest.FromString,
                    response_serializer=struct__pb2.JoinRoomResponse.SerializeToString,
            ),
            'Eliminated': grpc.unary_unary_rpc_method_handler(
                    servicer.Eliminated,
                    request_deserializer=struct__pb2.EliminatedRequest.FromString,
                    response_serializer=struct__pb2.EliminatedResponse.SerializeToString,
            ),
            'ShowRole': grpc.unary_unary_rpc_method_handler(
                    servicer.ShowRole,
                    request_deserializer=struct__pb2.ShowRoleRequest.FromString,
                    response_serializer=struct__pb2.ShowRoleResponse.SerializeToString,
            ),
            'OfficerStatement': grpc.unary_unary_rpc_method_handler(
                    servicer.OfficerStatement,
                    request_deserializer=struct__pb2.OfficerStatementRequest.FromString,
                    response_serializer=struct__pb2.OfficerStatementResponse.SerializeToString,
            ),
            'GetUsersInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersInfo,
                    request_deserializer=struct__pb2.GetUsersInfoRequest.FromString,
                    response_serializer=struct__pb2.GetUsersInfoResponse.SerializeToString,
            ),
            'GetUserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserInfo,
                    request_deserializer=struct__pb2.GetUserInfoRequest.FromString,
                    response_serializer=struct__pb2.GetUserInfoResponse.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=struct__pb2.AddUserRequest.FromString,
                    response_serializer=struct__pb2.AddUserResponse.SerializeToString,
            ),
            'EditUser': grpc.unary_unary_rpc_method_handler(
                    servicer.EditUser,
                    request_deserializer=struct__pb2.EditUserRequest.FromString,
                    response_serializer=struct__pb2.EditUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mafia.MyMafiaEvents', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyMafiaEvents(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GameEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mafia.MyMafiaEvents/GameEvents',
            struct__pb2.GameEventsRequest.SerializeToString,
            struct__pb2.GameEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShowUsersInRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/ShowUsersInRoom',
            struct__pb2.ShowUsersInRoomRequest.SerializeToString,
            struct__pb2.ShowUsersInRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTimeInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/UpdateTimeInfo',
            struct__pb2.UpdateTimeInfoRequest.SerializeToString,
            struct__pb2.UpdateTimeInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/CreateRoom',
            struct__pb2.CreateRoomRequest.SerializeToString,
            struct__pb2.CreateRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/JoinRoom',
            struct__pb2.JoinRoomRequest.SerializeToString,
            struct__pb2.JoinRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Eliminated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/Eliminated',
            struct__pb2.EliminatedRequest.SerializeToString,
            struct__pb2.EliminatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShowRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/ShowRole',
            struct__pb2.ShowRoleRequest.SerializeToString,
            struct__pb2.ShowRoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OfficerStatement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/OfficerStatement',
            struct__pb2.OfficerStatementRequest.SerializeToString,
            struct__pb2.OfficerStatementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/GetUsersInfo',
            struct__pb2.GetUsersInfoRequest.SerializeToString,
            struct__pb2.GetUsersInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/GetUserInfo',
            struct__pb2.GetUserInfoRequest.SerializeToString,
            struct__pb2.GetUserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/AddUser',
            struct__pb2.AddUserRequest.SerializeToString,
            struct__pb2.AddUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.MyMafiaEvents/EditUser',
            struct__pb2.EditUserRequest.SerializeToString,
            struct__pb2.EditUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
