import socket
import re
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")

prevNumber = 0
count = 0

while True:
    message, clientAddress = serverSocket.recvfrom(506)
    num = re.findall('\d+', str(message))
    amountSend = re.findall('(\d+):', str(message))
    me = (int(num[0]) - prevNumber)
    if count > 0:
        if me > 2 or me < 0:
            print(int(num[0]))
    prevNumber = int(num[0])
    count += 1
    modifiedMessage = message.decode()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    prevNumber = int(num[0])
    if count == amountSend[0]:
        count = 0
