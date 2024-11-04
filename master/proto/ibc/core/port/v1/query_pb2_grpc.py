# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ibc.core.port.v1 import query_pb2 as ibc_dot_core_dot_port_dot_v1_dot_query__pb2


class QueryStub:
    """Query defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppVersion = channel.unary_unary(
            '/ibc.core.port.v1.Query/AppVersion',
            request_serializer=ibc_dot_core_dot_port_dot_v1_dot_query__pb2.
            QueryAppVersionRequest.SerializeToString,
            response_deserializer=ibc_dot_core_dot_port_dot_v1_dot_query__pb2.
            QueryAppVersionResponse.FromString,
        )


class QueryServicer:
    """Query defines the gRPC querier service
    """

    def AppVersion(self, request, context):
        """AppVersion queries an IBC Port and determines the appropriate application version to be used
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AppVersion':
        grpc.unary_unary_rpc_method_handler(
            servicer.AppVersion,
            request_deserializer=ibc_dot_core_dot_port_dot_v1_dot_query__pb2.
            QueryAppVersionRequest.FromString,
            response_serializer=ibc_dot_core_dot_port_dot_v1_dot_query__pb2.
            QueryAppVersionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ibc.core.port.v1.Query',
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Query:
    """Query defines the gRPC querier service
    """

    @staticmethod
    def AppVersion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.core.port.v1.Query/AppVersion',
            ibc_dot_core_dot_port_dot_v1_dot_query__pb2.QueryAppVersionRequest.
            SerializeToString,
            ibc_dot_core_dot_port_dot_v1_dot_query__pb2.
            QueryAppVersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )