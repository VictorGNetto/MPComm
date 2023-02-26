import threading
from socket import *
import pickle
from constMP import *

N = -1
N_MSGS = -1

class ConstUpdater(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self, daemon=True)
	
	def run(self):
		global N, N_MSGS

		constUpdaterSocket = socket(AF_INET, SOCK_STREAM)
		constUpdaterSocket.bind(('127.0.0.1', 4570))
		constUpdaterSocket.listen(1)

		while True:
			(conn, addr) = constUpdaterSocket.accept()
			msgPack = conn.recv(1024)
			conn.close()
			N, N_MSGS = pickle.loads(msgPack)

constUpdater = ConstUpdater()
constUpdater.start()

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((SERVER_ADDR, SERVER_PORT))
serverSock.listen(5)

def compare():
	numMsgs = 0
	msgs = [] # each msg is a list of tuples (with the original messages received by the peer processes)

	# Receive the lists of messages from the peer processes
	while numMsgs < N:
		(conn, addr) = serverSock.accept()
		msgPack = conn.recv(2048)
		conn.close()
		msgs.append(pickle.loads(msgPack))
		numMsgs = numMsgs + 1

	unordered = 0

	# Compare the lists of messages
	for j in range(0,N_MSGS-1):
		firstMsg = msgs[0][j]
		for i in range(1,N-1):
			if firstMsg != msgs[i][j]:
				unordered = unordered + 1
				break
		
	print ('Found ' + str(unordered) + ' unordered message rounds')

# this code must be ended with a Crtl + C
while True:
	compare()

# TODO: The code execution never reaches the line bellow.. find a better way
# to close the socket
serverSock.close()