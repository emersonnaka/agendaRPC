# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import agenda_pb2 as agenda__pb2


class ManagerStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddPerson = channel.unary_unary(
        '/Manager/AddPerson',
        request_serializer=agenda__pb2.Person.SerializeToString,
        response_deserializer=agenda__pb2.BooleanReply.FromString,
        )
    self.DelPerson = channel.unary_unary(
        '/Manager/DelPerson',
        request_serializer=agenda__pb2.PersonId.SerializeToString,
        response_deserializer=agenda__pb2.BooleanReply.FromString,
        )
    self.SearchPersonName = channel.unary_stream(
        '/Manager/SearchPersonName',
        request_serializer=agenda__pb2.PersonName.SerializeToString,
        response_deserializer=agenda__pb2.Person.FromString,
        )
    self.SearchPersonId = channel.unary_unary(
        '/Manager/SearchPersonId',
        request_serializer=agenda__pb2.PersonId.SerializeToString,
        response_deserializer=agenda__pb2.PersonReply.FromString,
        )
    self.ListContacts = channel.unary_stream(
        '/Manager/ListContacts',
        request_serializer=agenda__pb2.ContactsRequest.SerializeToString,
        response_deserializer=agenda__pb2.Person.FromString,
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
          request_deserializer=agenda__pb2.Person.FromString,
          response_serializer=agenda__pb2.BooleanReply.SerializeToString,
      ),
      'DelPerson': grpc.unary_unary_rpc_method_handler(
          servicer.DelPerson,
          request_deserializer=agenda__pb2.PersonId.FromString,
          response_serializer=agenda__pb2.BooleanReply.SerializeToString,
      ),
      'SearchPersonName': grpc.unary_stream_rpc_method_handler(
          servicer.SearchPersonName,
          request_deserializer=agenda__pb2.PersonName.FromString,
          response_serializer=agenda__pb2.Person.SerializeToString,
      ),
      'SearchPersonId': grpc.unary_unary_rpc_method_handler(
          servicer.SearchPersonId,
          request_deserializer=agenda__pb2.PersonId.FromString,
          response_serializer=agenda__pb2.PersonReply.SerializeToString,
      ),
      'ListContacts': grpc.unary_stream_rpc_method_handler(
          servicer.ListContacts,
          request_deserializer=agenda__pb2.ContactsRequest.FromString,
          response_serializer=agenda__pb2.Person.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Manager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
