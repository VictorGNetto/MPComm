from socket import *
from constMP import *
from pickle import dumps

def send_msg(msg):
    msgPack = dumps(msg)
    for peer in PEERS:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((peer, 4569))
        s.send(msgPack)
        s.close()
    
def send_cmd(cmd):
    cmd, n, n_msgs = cmd.split(' ')
    n = int(n)
    n_msgs = int(n_msgs)

    msgPack = dumps((cmd, n, n_msgs))
    for peer in PEERS:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((peer, 4569))
        s.send(msgPack)
        s.close()

while True:
    cmd = input('>>> ')
    if cmd == 'exit':
        send_msg('exit')
        break

    send_msg(cmd)