# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agenda.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agenda.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x61genda.proto\"\xc3\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12#\n\x06phones\x18\x04 \x03(\x0b\x32\x13.Person.PhoneNumber\x1a>\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.Person.PhoneType\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"\x16\n\x08PersonId\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1a\n\nPersonName\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x0b\x41\x64\x64ressBook\x12\x17\n\x06person\x18\x01 \x03(\x0b\x32\x07.Person\"&\n\x0bPersonReply\x12\x17\n\x06person\x18\x01 \x01(\x0b\x32\x07.Person\"\x1d\n\x0c\x42ooleanReply\x12\r\n\x05reply\x18\x01 \x01(\x08\"\'\n\x0f\x43ontactsRequest\x12\x14\n\x0clistContacts\x18\x01 \x01(\x08\x32\xed\x01\n\x07Manager\x12%\n\tAddPerson\x12\x07.Person\x1a\r.BooleanReply\"\x00\x12\'\n\tDelPerson\x12\t.PersonId\x1a\r.BooleanReply\"\x00\x12\x31\n\x10SearchPersonName\x12\x0b.PersonName\x1a\x0c.AddressBook\"\x00\x30\x01\x12+\n\x0eSearchPersonId\x12\t.PersonId\x1a\x0c.PersonReply\"\x00\x12\x32\n\x0cListContacts\x12\x10.ContactsRequest\x1a\x0c.AddressBook\"\x00\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=169,
  serialized_end=212,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Person.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=167,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phones', full_name='Person.phones', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=212,
)


_PERSONID = _descriptor.Descriptor(
  name='PersonId',
  full_name='PersonId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PersonId.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=236,
)


_PERSONNAME = _descriptor.Descriptor(
  name='PersonName',
  full_name='PersonName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PersonName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=264,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='AddressBook.person', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=304,
)


_PERSONREPLY = _descriptor.Descriptor(
  name='PersonReply',
  full_name='PersonReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='PersonReply.person', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=344,
)


_BOOLEANREPLY = _descriptor.Descriptor(
  name='BooleanReply',
  full_name='BooleanReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='BooleanReply.reply', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=375,
)


_CONTACTSREQUEST = _descriptor.Descriptor(
  name='ContactsRequest',
  full_name='ContactsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listContacts', full_name='ContactsRequest.listContacts', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=416,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phones'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_ADDRESSBOOK.fields_by_name['person'].message_type = _PERSON
_PERSONREPLY.fields_by_name['person'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['PersonId'] = _PERSONID
DESCRIPTOR.message_types_by_name['PersonName'] = _PERSONNAME
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['PersonReply'] = _PERSONREPLY
DESCRIPTOR.message_types_by_name['BooleanReply'] = _BOOLEANREPLY
DESCRIPTOR.message_types_by_name['ContactsRequest'] = _CONTACTSREQUEST

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_PHONENUMBER,
    __module__ = 'agenda_pb2'
    # @@protoc_insertion_point(class_scope:Person.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _PERSON,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

PersonId = _reflection.GeneratedProtocolMessageType('PersonId', (_message.Message,), dict(
  DESCRIPTOR = _PERSONID,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:PersonId)
  ))
_sym_db.RegisterMessage(PersonId)

PersonName = _reflection.GeneratedProtocolMessageType('PersonName', (_message.Message,), dict(
  DESCRIPTOR = _PERSONNAME,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:PersonName)
  ))
_sym_db.RegisterMessage(PersonName)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)

PersonReply = _reflection.GeneratedProtocolMessageType('PersonReply', (_message.Message,), dict(
  DESCRIPTOR = _PERSONREPLY,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:PersonReply)
  ))
_sym_db.RegisterMessage(PersonReply)

BooleanReply = _reflection.GeneratedProtocolMessageType('BooleanReply', (_message.Message,), dict(
  DESCRIPTOR = _BOOLEANREPLY,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:BooleanReply)
  ))
_sym_db.RegisterMessage(BooleanReply)

ContactsRequest = _reflection.GeneratedProtocolMessageType('ContactsRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTSREQUEST,
  __module__ = 'agenda_pb2'
  # @@protoc_insertion_point(class_scope:ContactsRequest)
  ))
_sym_db.RegisterMessage(ContactsRequest)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class ManagerStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.AddPerson = channel.unary_unary(
          '/Manager/AddPerson',
          request_serializer=Person.SerializeToString,
          response_deserializer=BooleanReply.FromString,
          )
      self.DelPerson = channel.unary_unary(
          '/Manager/DelPerson',
          request_serializer=PersonId.SerializeToString,
          response_deserializer=BooleanReply.FromString,
          )
      self.SearchPersonName = channel.unary_stream(
          '/Manager/SearchPersonName',
          request_serializer=PersonName.SerializeToString,
          response_deserializer=AddressBook.FromString,
          )
      self.SearchPersonId = channel.unary_unary(
          '/Manager/SearchPersonId',
          request_serializer=PersonId.SerializeToString,
          response_deserializer=PersonReply.FromString,
          )
      self.ListContacts = channel.unary_stream(
          '/Manager/ListContacts',
          request_serializer=ContactsRequest.SerializeToString,
          response_deserializer=AddressBook.FromString,
          )


  class ManagerServicer(object):

    def AddPerson(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def DelPerson(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SearchPersonName(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SearchPersonId(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ListContacts(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AddPerson': grpc.unary_unary_rpc_method_handler(
            servicer.AddPerson,
            request_deserializer=Person.FromString,
            response_serializer=BooleanReply.SerializeToString,
        ),
        'DelPerson': grpc.unary_unary_rpc_method_handler(
            servicer.DelPerson,
            request_deserializer=PersonId.FromString,
            response_serializer=BooleanReply.SerializeToString,
        ),
        'SearchPersonName': grpc.unary_stream_rpc_method_handler(
            servicer.SearchPersonName,
            request_deserializer=PersonName.FromString,
            response_serializer=AddressBook.SerializeToString,
        ),
        'SearchPersonId': grpc.unary_unary_rpc_method_handler(
            servicer.SearchPersonId,
            request_deserializer=PersonId.FromString,
            response_serializer=PersonReply.SerializeToString,
        ),
        'ListContacts': grpc.unary_stream_rpc_method_handler(
            servicer.ListContacts,
            request_deserializer=ContactsRequest.FromString,
            response_serializer=AddressBook.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Manager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaManagerServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddPerson(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def DelPerson(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SearchPersonName(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SearchPersonId(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ListContacts(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaManagerStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddPerson(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AddPerson.future = None
    def DelPerson(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    DelPerson.future = None
    def SearchPersonName(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    def SearchPersonId(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    SearchPersonId.future = None
    def ListContacts(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()


  def beta_create_Manager_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Manager', 'AddPerson'): Person.FromString,
      ('Manager', 'DelPerson'): PersonId.FromString,
      ('Manager', 'ListContacts'): ContactsRequest.FromString,
      ('Manager', 'SearchPersonId'): PersonId.FromString,
      ('Manager', 'SearchPersonName'): PersonName.FromString,
    }
    response_serializers = {
      ('Manager', 'AddPerson'): BooleanReply.SerializeToString,
      ('Manager', 'DelPerson'): BooleanReply.SerializeToString,
      ('Manager', 'ListContacts'): AddressBook.SerializeToString,
      ('Manager', 'SearchPersonId'): PersonReply.SerializeToString,
      ('Manager', 'SearchPersonName'): AddressBook.SerializeToString,
    }
    method_implementations = {
      ('Manager', 'AddPerson'): face_utilities.unary_unary_inline(servicer.AddPerson),
      ('Manager', 'DelPerson'): face_utilities.unary_unary_inline(servicer.DelPerson),
      ('Manager', 'ListContacts'): face_utilities.unary_stream_inline(servicer.ListContacts),
      ('Manager', 'SearchPersonId'): face_utilities.unary_unary_inline(servicer.SearchPersonId),
      ('Manager', 'SearchPersonName'): face_utilities.unary_stream_inline(servicer.SearchPersonName),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Manager_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Manager', 'AddPerson'): Person.SerializeToString,
      ('Manager', 'DelPerson'): PersonId.SerializeToString,
      ('Manager', 'ListContacts'): ContactsRequest.SerializeToString,
      ('Manager', 'SearchPersonId'): PersonId.SerializeToString,
      ('Manager', 'SearchPersonName'): PersonName.SerializeToString,
    }
    response_deserializers = {
      ('Manager', 'AddPerson'): BooleanReply.FromString,
      ('Manager', 'DelPerson'): BooleanReply.FromString,
      ('Manager', 'ListContacts'): AddressBook.FromString,
      ('Manager', 'SearchPersonId'): PersonReply.FromString,
      ('Manager', 'SearchPersonName'): AddressBook.FromString,
    }
    cardinalities = {
      'AddPerson': cardinality.Cardinality.UNARY_UNARY,
      'DelPerson': cardinality.Cardinality.UNARY_UNARY,
      'ListContacts': cardinality.Cardinality.UNARY_STREAM,
      'SearchPersonId': cardinality.Cardinality.UNARY_UNARY,
      'SearchPersonName': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Manager', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
