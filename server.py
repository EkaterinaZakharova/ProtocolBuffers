import sys
from person_pb2 import Person
import socket
sock = socket.socket()
sock.bind(('',1337))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:', addr)
s=";"

while True:
    buff = sock.recv(1024)
    Man = Person()
    Man.ParseFromString(buff.decode())
    s.join(Man)
    if len(buff)==0:
        break
    conn.send(s.encode())
    
conn.close()
