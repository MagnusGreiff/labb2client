import socket
import time
#serverName = 'hostname'
serverName = '193.11.186.159'

serverPort = 12000

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

amountSend = 11
amountSeconds = 1 / 50
try:
    for x in range(0, amountSend):
        message = str(amountSend) + ":" + str(10000 + x) + ";" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(506)
        print("Received from server: ", modifiedMessage.decode())
        time.sleep(amountSeconds)
except KeyboardInterrupt:
        message = "closed"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        clientSocket.close()

clientSocket.close()
