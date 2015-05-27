import sys
import socket
from person_pb2 import Person
sock = socket . socket ()
sock . connect (( 'localhost', 1337))
Man = Person()
man_id=input("Enter identifyer")
name=input("Enter name")
Man.id=man_id
Man.name=name
body=Man.SerializeToString()
sock.send(body.encode())
while True:
    data = sock.recv (1024)
    print(data.decode())
    if not data:
        break
sock . close ()
