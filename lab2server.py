import socket
import re
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")

prevNumber = 0
count = 0
start = 0
lostPackages = []

while True:
    message, clientAddress = serverSocket.recvfrom(1000)
    print(message, clientAddress)
    print("Inside server")
    if count < 1:
        num = re.findall(':(\d+)', str(message))
        count = int(num[0])
        start = int(num[0])
    if message.decode() == 'closed':
        count = 0

    try:
        num = re.findall(':(\d+)', str(message))
        amountSend = re.findall('(\d+):', str(message))
        if count != int(num[0]):
            print("oh no, you lost the package: " + str(int(num[0])))
            lostPackages.append(int(num[0]))
        else:
            count += 1
            modifiedMessage = message.decode()
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
            if count == (start + int(amountSend[0])):
                count = 0
    except IndexError:
        print("Restarting")
    finally:
        print(count, lostPackages)
