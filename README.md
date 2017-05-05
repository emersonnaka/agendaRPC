Sistemas Distribuídos
=====================

Remote Procedure Call (RPC)
-----------------------------------------------------

Faça uma implementação usando Sun RPC ou gRPC para um serviço de agenda telefônica remota que possibilita adicionar, remover e consultar contatos.

Instalando gRPC
--------------
Pip versão 8 ou superior:
* python3 -m pip install --upgrade pip

Instalar gRPC:
* python3 -m pip install grpcio

Também é necessário instalar as ferramentas do gRPC:
* python3 -m pip install grpcio-tools

Implementação
------------------------
Esta tarefa foi implementada em Python3.

Para compilar o arquivo ".proto" entre na pasta pelo terminal e execute:
* python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. agenda.proto

Alunos
------
Emerson Yudi Nakashima 1451600

Gustavo Correia Gonzalez 1551787