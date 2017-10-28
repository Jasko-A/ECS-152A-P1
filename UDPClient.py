
from socket import *
import time as t
import string
import random
import datetime

def getDay(day,newDay):
	for item in newDay:
		if(day == item[0]):
			return item[1]
		'''
	for i, item in enumerate(newDay):
		if item[i][0] == day:
			print(item[i][1])'''

numPing = 0
serverName = 'localhost'
serverPort = 12000

dayOfWeek = [['Monday','M'],['Tuesday','T'],['Wednesday','W'],['Thursday','R'],['Friday','F'], ['Saturday','S'], ['Sunday','U']]
now = datetime.datetime.now()

clientSocket = socket(AF_INET, SOCK_DGRAM)



while numPing < 10:
	clientSocket.settimeout(1) 	#sets timeout after message has been sent to the sever. Now we
									#wait for the servers response
	start_time = t.clock()
	#day = now.strftime("%A")
	day = getDay(now.strftime("%A"),dayOfWeek)
	message = 'Ping ' + str(numPing + 1) + ' ' + now.strftime("%Y-%m-%d ") + day +  now.strftime(" %H:%M ") + 'UTC'
	#message = raw_input(’Input lowercase sentence:’)

	print(message)
	clientSocket.sendto(str.encode(message),(serverName, serverPort))

	
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print (bytes.decode(modifiedMessage), "\nRTT:", round(((t.clock() - start_time)*1000),3), "\n")
	except timeout:
		print ("Request timed out\n")
	numPing = numPing + 1

clientSocket.close()

