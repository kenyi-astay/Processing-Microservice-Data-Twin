# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto-files/TopographyFile.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'proto-files/TopographyFile.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto-files/TopographyFile.proto\"<\n\tFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04part\x18\x02 \x01(\x05\x12\x13\n\x0btotal_parts\x18\x03 \x01(\x05\"0\n\x0cUploadStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2B\n\x15TopographyFileService\x12)\n\nUploadFile\x12\n.FileChunk\x1a\r.UploadStatus(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto_files.TopographyFile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILECHUNK']._serialized_start=36
  _globals['_FILECHUNK']._serialized_end=96
  _globals['_UPLOADSTATUS']._serialized_start=98
  _globals['_UPLOADSTATUS']._serialized_end=146
  _globals['_TOPOGRAPHYFILESERVICE']._serialized_start=148
  _globals['_TOPOGRAPHYFILESERVICE']._serialized_end=214
# @@protoc_insertion_point(module_scope)
