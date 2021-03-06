# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import agenda_pb2
import agenda_pb2_grpc

def inputPerson():
    person = agenda_pb2.Person()
    person.name = input('Nome: ')
    person.id = int(input('ID: '))
    email = input('Email: ')
    if email != '':
        person.email = email
    otherPhone = 's'
    while otherPhone.lower() == 's':
        phone = person.phones.add()
        phone.number = input('Telefone de contato: ')
        typeNumber = int(input('Mobile = 0, Home = 1, Work = 2: '))
        if typeNumber == 0:
            phone.type = agenda_pb2.Person.MOBILE
        elif typeNumber == 1:
            phone.type = agenda_pb2.Person.HOME
        else:
            phone.type = agenda_pb2.Person.WORK
        otherPhone = input('Deseja inserir outro contato (s/n): ').lower()
    return person

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = agenda_pb2_grpc.ManagerStub(channel)
    option = 0

    while option != 6:
        print('1 - Adicionar contato')
        print('2 - Remover contato')
        print('3 - Consultar contato pelo ID')
        print('4 - Consultar contatos pelo nome')
        print('5 - Listar todos os contatos')
        print('6 - Sair')
        option = int(input('Option: '))
        
        if option == 1:
            person = inputPerson()
            response = stub.AddPerson(person)
            if response.reply:
                print('Contato inserido com sucesso!')
            else:
                print('Contato não foi inserido!')
        elif option == 2:
            identifier = int(input('Insira o id do contato: '))
            response = stub.DelPerson(agenda_pb2.PersonId(id = identifier))
            if response.reply:
                print('Contato removido com sucesso!')
            else:
                print('Contato inexistente')
        elif option == 3:
            identifier = int(input('Insira o id do contato: '))
            response = stub.SearchPersonId(agenda_pb2.PersonId(id = identifier))
            if response != None:
                print(response)
            else:
                print('Contato inexistente')
        elif option == 4:
            name = input('Insira o nome do contato: ')
            contactslist = stub.SearchPersonName(agenda_pb2.PersonName(name = name))
            for person in contactslist:
                print(person)
        elif option == 5:
            contactslist = stub.ListContacts(agenda_pb2.ContactsRequest(listContacts = True))
            for person in contactslist:
                print(person)


  # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  # print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
