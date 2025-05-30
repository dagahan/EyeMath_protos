# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: external_api_gateway.proto
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
    'external_api_gateway.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x65xternal_api_gateway.proto\x12\x12\x45xternalApiGateway\"Q\n\x0fRegisterRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07surname\x18\x04 \x01(\t\"#\n\x10RegisterResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"?\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\x03\"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"!\n\x0eIsAdminRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"#\n\x0fIsAdminResponse\x12\x10\n\x08is_admin\x18\x01 \x01(\x08\"\'\n\x11MathSolverRequest\x12\x12\n\nexpression\x18\x01 \x01(\t\"\x80\x01\n\x12MathSolverResponse\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.ExternalApiGateway.MathSolverResponse.Status\x12\x0e\n\x06result\x18\x02 \x01(\t\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xea\x02\n\x12\x45xternalApiGateway\x12U\n\x08Register\x12#.ExternalApiGateway.RegisterRequest\x1a$.ExternalApiGateway.RegisterResponse\x12L\n\x05Login\x12 .ExternalApiGateway.LoginRequest\x1a!.ExternalApiGateway.LoginResponse\x12R\n\x07IsAdmin\x12\".ExternalApiGateway.IsAdminRequest\x1a#.ExternalApiGateway.IsAdminResponse\x12[\n\nMathSolver\x12%.ExternalApiGateway.MathSolverRequest\x1a&.ExternalApiGateway.MathSolverResponseB(Z&usov.external_api_gateway.v1;exapigateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'external_api_gateway_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&usov.external_api_gateway.v1;exapigate'
  _globals['_REGISTERREQUEST']._serialized_start=50
  _globals['_REGISTERREQUEST']._serialized_end=131
  _globals['_REGISTERRESPONSE']._serialized_start=133
  _globals['_REGISTERRESPONSE']._serialized_end=168
  _globals['_LOGINREQUEST']._serialized_start=170
  _globals['_LOGINREQUEST']._serialized_end=233
  _globals['_LOGINRESPONSE']._serialized_start=235
  _globals['_LOGINRESPONSE']._serialized_end=265
  _globals['_ISADMINREQUEST']._serialized_start=267
  _globals['_ISADMINREQUEST']._serialized_end=300
  _globals['_ISADMINRESPONSE']._serialized_start=302
  _globals['_ISADMINRESPONSE']._serialized_end=337
  _globals['_MATHSOLVERREQUEST']._serialized_start=339
  _globals['_MATHSOLVERREQUEST']._serialized_end=378
  _globals['_MATHSOLVERRESPONSE']._serialized_start=381
  _globals['_MATHSOLVERRESPONSE']._serialized_end=509
  _globals['_MATHSOLVERRESPONSE_STATUS']._serialized_start=482
  _globals['_MATHSOLVERRESPONSE_STATUS']._serialized_end=509
  _globals['_EXTERNALAPIGATEWAY']._serialized_start=512
  _globals['_EXTERNALAPIGATEWAY']._serialized_end=874
# @@protoc_insertion_point(module_scope)
