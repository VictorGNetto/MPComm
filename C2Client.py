from socket import *
from constMP import *
from pickle import loads
from os import system

s = socket(AF_INET, SOCK_STREAM)
s.bind((gethostbyname_ex(gethostname())[2][0], 4569))
s.listen(1)

while True:
    (conn, addr) = s.accept()
    msgPack = conn.recv(1024)
    msg = loads(msgPack)
    conn.close()
    if msg == 'run':
        system('python3 ./peerCommunicatorUDP.py')
    elif msg == 'exit':
        break

s.close()