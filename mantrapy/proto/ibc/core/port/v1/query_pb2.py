# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/port/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cibc/core/port/v1/query.proto\x12\x10ibc.core.port.v1\x1a!ibc/core/channel/v1/channel.proto\"\xc1\x01\n\x16QueryAppVersionRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12,\n\x08ordering\x18\x03 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12\x37\n\x0c\x63ounterparty\x18\x04 \x01(\x0b\x32!.ibc.core.channel.v1.Counterparty\x12\x18\n\x10proposed_version\x18\x05 \x01(\t\";\n\x17QueryAppVersionResponse\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t2l\n\x05Query\x12\x63\n\nAppVersion\x12(.ibc.core.port.v1.QueryAppVersionRequest\x1a).ibc.core.port.v1.QueryAppVersionResponse\"\x00\x42\x38Z6github.com/cosmos/ibc-go/v2/modules/core/05-port/typesb\x06proto3',
)

_QUERYAPPVERSIONREQUEST = DESCRIPTOR.message_types_by_name[
    'QueryAppVersionRequest'
]
_QUERYAPPVERSIONRESPONSE = DESCRIPTOR.message_types_by_name[
    'QueryAppVersionResponse'
]
QueryAppVersionRequest = _reflection.GeneratedProtocolMessageType(
    'QueryAppVersionRequest',
    (_message.Message,),
    {
        'DESCRIPTOR': _QUERYAPPVERSIONREQUEST,
        '__module__': 'ibc.core.port.v1.query_pb2',
        # @@protoc_insertion_point(class_scope:ibc.core.port.v1.QueryAppVersionRequest)
    },
)
_sym_db.RegisterMessage(QueryAppVersionRequest)

QueryAppVersionResponse = _reflection.GeneratedProtocolMessageType(
    'QueryAppVersionResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _QUERYAPPVERSIONRESPONSE,
        '__module__': 'ibc.core.port.v1.query_pb2',
        # @@protoc_insertion_point(class_scope:ibc.core.port.v1.QueryAppVersionResponse)
    },
)
_sym_db.RegisterMessage(QueryAppVersionResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/cosmos/ibc-go/v2/modules/core/05-port/types'
    _QUERYAPPVERSIONREQUEST._serialized_start = 86
    _QUERYAPPVERSIONREQUEST._serialized_end = 279
    _QUERYAPPVERSIONRESPONSE._serialized_start = 281
    _QUERYAPPVERSIONRESPONSE._serialized_end = 340
    _QUERY._serialized_start = 342
    _QUERY._serialized_end = 450
# @@protoc_insertion_point(module_scope)
