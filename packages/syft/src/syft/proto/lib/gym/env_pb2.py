# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/gym/env.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/gym/env.proto",
    package="syft.lib.gym",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17proto/lib/gym/env.proto\x12\x0csyft.lib.gym"\x11\n\x03\x45nv\x12\n\n\x02id\x18\x01 \x01(\tb\x06proto3',
)


_ENV = _descriptor.Descriptor(
    name="Env",
    full_name="syft.lib.gym.Env",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.gym.Env.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=41,
    serialized_end=58,
)

DESCRIPTOR.message_types_by_name["Env"] = _ENV
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Env = _reflection.GeneratedProtocolMessageType(
    "Env",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENV,
        "__module__": "proto.lib.gym.env_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.gym.Env)
    },
)
_sym_db.RegisterMessage(Env)


# @@protoc_insertion_point(module_scope)
