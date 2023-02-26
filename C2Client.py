from socket import *
from constMP import *
from pickle import loads
from os import system

myAddresses = gethostbyname_ex(gethostname())

s = socket(AF_INET, SOCK_STREAM)
s.bind((myAddresses[2][0], 4569))
s.listen(1)

#Find out who am I
myself = 0
for addr in PEERS:
    if addr in myAddresses[2]:
        break
    myself = myself + 1
print('I am process ', str(myself))

while True:
    (conn, addr) = s.accept()
    msgPack = conn.recv(1024)
    print(msgPack)
    cmd, n, n_msgs = loads(msgPack).split(' ')
    conn.close()
    if cmd == 'run' and myself < int(n):
        system('python3 ./peerCommunicatorUDP.py {} {}'.format(n, n_msgs))
    elif cmd == 'exit':
        break

s.close()