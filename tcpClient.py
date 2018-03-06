import socket
import time
import sys
#serverName = 'hostname'
serverName = '193.11.184.120'

serverPort = 12000

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

amountSend = 500
amountSeconds = 1 / 50
count = 0
try:
    for x in range(0, amountSend):
        message = str(amountSend) + ":" + str(10000 + x) + ";" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage = clientSocket.recv(1000)
        print(modifiedMessage)
        print("Received from server: ", modifiedMessage.decode())
        time.sleep(amountSeconds)
except KeyboardInterrupt:
        message = "closed"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        clientSocket.close()
finally:
    clientSocket.close()

clientSocket.close()
