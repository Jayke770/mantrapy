# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from cosmos.crisis.v1beta1 import tx_pb2 as cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2


class MsgStub:
    """Msg defines the bank Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VerifyInvariant = channel.unary_unary(
            '/cosmos.crisis.v1beta1.Msg/VerifyInvariant',
            request_serializer=cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.
            MsgVerifyInvariant.SerializeToString,
            response_deserializer=cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.
            MsgVerifyInvariantResponse.FromString,
        )


class MsgServicer:
    """Msg defines the bank Msg service.
    """

    def VerifyInvariant(self, request, context):
        """VerifyInvariant defines a method to verify a particular invariance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'VerifyInvariant':
        grpc.unary_unary_rpc_method_handler(
            servicer.VerifyInvariant,
            request_deserializer=cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.
            MsgVerifyInvariant.FromString,
            response_serializer=cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.
            MsgVerifyInvariantResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'cosmos.crisis.v1beta1.Msg',
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Msg:
    """Msg defines the bank Msg service.
    """

    @staticmethod
    def VerifyInvariant(
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
            '/cosmos.crisis.v1beta1.Msg/VerifyInvariant',
            cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.MsgVerifyInvariant.
            SerializeToString,
            cosmos_dot_crisis_dot_v1beta1_dot_tx__pb2.
            MsgVerifyInvariantResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
