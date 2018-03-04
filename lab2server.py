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
    if message.decode() == 'closed':
        count = 0

    try:
        num = re.findall(':(\d+)', str(message))
        amountSend = re.findall('(\d+):', str(message))
        me = (int(num[0]) - prevNumber)
        print(count, int(num[0]))
        # print(amountSend)
        if count != int(num[0]):
            print("oh no, you lost package: " + str(int(num[0])))
        # if count > 0:
        #     if me > 2 or me < 0:
        #         print(int(num[0]))
        prevNumber = int(num[0])
        count += 1
        modifiedMessage = message.decode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        prevNumber = int(num[0])
        if count == int(amountSend[0]):
            count = 0
    except IndexError:
        print("Restarting")
