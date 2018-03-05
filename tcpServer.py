import socket
import re
import sys
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print ("The TCP server is ready to recieve")

count = 0
start = 0

while True:
    connection, clientAddress = serverSocket.accept()
    try:

        while True:
            message = connection.recv(1000)
            try:
                num = re.findall(':(\d+)', str(message))
                if count < 1:
                    count = int(num[0])
                    start = int(num[0])

                if count != int(num[0]):
                    print("oh no, you lost package: " + str(int(num[0])))
            except IndexError:
                pass
            if message:
                count += 1
                connection.sendto(message, clientAddress)
            else:
                break
    finally:
        count = 0
        connection.close()
