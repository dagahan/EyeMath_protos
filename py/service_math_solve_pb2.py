# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service_math_solve.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'service_math_solve.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18service_math_solve.proto\x12\tmathsolve\"\x11\n\x0fMetadataRequest\"1\n\x10MetadataResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\"\n\x0cSolveRequest\x12\x12\n\nexpression\x18\x01 \x01(\t\"m\n\rSolveResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.mathsolve.SolveResponse.Status\x12\x0e\n\x06result\x18\x02 \x01(\t\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\x92\x01\n\x0fgRPC_math_solve\x12\x43\n\x08Metadata\x12\x1a.mathsolve.MetadataRequest\x1a\x1b.mathsolve.MetadataResponse\x12:\n\x05Solve\x12\x17.mathsolve.SolveRequest\x1a\x18.mathsolve.SolveResponseB\x1dZ\x1busov.mathsolve.v1;mathsolveb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_math_solve_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033usov.mathsolve.v1;mathsolve'
  _globals['_METADATAREQUEST']._serialized_start=39
  _globals['_METADATAREQUEST']._serialized_end=56
  _globals['_METADATARESPONSE']._serialized_start=58
  _globals['_METADATARESPONSE']._serialized_end=107
  _globals['_SOLVEREQUEST']._serialized_start=109
  _globals['_SOLVEREQUEST']._serialized_end=143
  _globals['_SOLVERESPONSE']._serialized_start=145
  _globals['_SOLVERESPONSE']._serialized_end=254
  _globals['_SOLVERESPONSE_STATUS']._serialized_start=227
  _globals['_SOLVERESPONSE_STATUS']._serialized_end=254
  _globals['_GRPC_MATH_SOLVE']._serialized_start=257
  _globals['_GRPC_MATH_SOLVE']._serialized_end=403
# @@protoc_insertion_point(module_scope)
