#Project 1 - UDP Client
#Jasmin Adzic ID: 999883011, My Nguyen ID: 914329026

from socket import *
from datetime import *
from time import *

serverName = 'localhost'
serverPort = 12000

dayOfWeek = {"Mon": 'M', "Tue": 'T', "Wed": 'W', "Thu": 'R', "Fri": 'F', "Sat": 'S', "Sun": 'U'}

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1) 	#sets timeout after message has been sent to the sever

for i in range(1, 11):
	message = 'Ping ' + str(i) + ' ' + datetime.utcnow().strftime("%Y-%m-%d ") + dayOfWeek[datetime.utcnow().strftime("%a")] +  datetime.utcnow().strftime(" %H:%M ") + strftime("%Z", gmtime())
	print(message)
	clientSocket.sendto(str.encode(message),(serverName, serverPort))
	start_time = clock()
	
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print (bytes.decode(modifiedMessage), "\nRTT:", round(((clock() - start_time)*1000),3), "\n")
	except timeout:
		print ("Request timed out\n")

clientSocket.close()