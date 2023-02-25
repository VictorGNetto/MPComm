from socket import *
from constMP import *
from pickle import dumps

def send_msg(msg):
    for peer in PEERS:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((peer, 4569))
        msgPack = dumps(msg)
        s.send(msgPack)
        s.close()

while True:
    cmd = input('>>> ')
    if cmd == 'exit':
        send_msg('exit')
        break
    elif cmd == 'run':
        send_msg('run')