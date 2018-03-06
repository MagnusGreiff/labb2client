import socket
import re
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")

expectedPackage = []
count = int (len(expectedPackage) -1)
lostPackages = []

while True:
    try:
        message, clientAddress = serverSocket.recvfrom(1000)
        # print(message, clientAddress)
        print("Inside server")
        num = re.findall(':(\d+)', str(message))
        amountSend = re.findall('(\d+):', str(message))
        count += 1

        amountExpected = int(amountSend[0]) - 1

        package = int(num[0])

        expectedPackage.append(package)


        if expectedPackage[-1] == count:
            print(package)
        elif int(expectedPackage[int((len(expectedPackage)) - 2)]) == (int(expectedPackage[-1]) - 1):
        # elif amountRecieved <= packageNum:
            print(package)
            # check number order
        elif int(expectedPackage[int((len(expectedPackage)) - 2)]) != (int(expectedPackage[-1]) - 1):
            print('skipped a package')

        if int(amountExpected) == int(count):
            print('all packages recieved OK')
            print(expectedPackage)
            # for x in range(int(expectedPackage[0]), int(expectedPackage[-1]) + 1):
            #     print(x)
            original_list = [x for x in range(int(expectedPackage[0]), int(expectedPackage[-1]) + 1)]
            print(original_list)
            num_list = set(expectedPackage)
            print(list(num_list ^ set(original_list)))

    # if count < 1:
    #     lostPackages = []
    #     num = re.findall(':(\d+)', str(message))
    #     start = int(num[0])
    #     expectedPackage = int(num[0])
    # if message.decode() == 'closed':
    #     count = 0
    #
    # try:
    #     num = re.findall(':(\d+)', str(message))
    #     amountSend = re.findall('(\d+):', str(message))
    #
    #
    #     if expectedPackage == int(num[0]):
    #         count += 1
    #         expectedPackage += 1
    #         if count == int(amountSend[0]):
    #             count = 0
    #     elif expectedPackage != int(num[0]):
    #         print("oh no, you lost the package: " + str(int(num[0])))
    #         lostPackages.append(int(num[0]))
    #         expectedPackage += 1
    #         count += 1

    except IndexError:
        print("Restarting")
    # finally:
    #     print(count, expectedPackage, int(num[0]))
    #
serverSocket.close()
