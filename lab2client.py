import socket
import time
#serverName = 'hostname'
serverName = '172.19.0.1'

serverPort = 12000

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

amountSend = 200000
amountSeconds = 0
try:
    for x in range(0, amountSend):
        message = str(amountSend) + ":" + str(x) + ";" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(506)
        print("Received from server: ", modifiedMessage.decode())
        time.sleep(amountSeconds)
except KeyboardInterrupt:
        message = "closed"
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        clientSocket.close()

clientSocket.close()
