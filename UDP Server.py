from socket import *
serverPort = input("Enter port: ")
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('10.0.0.32', serverPort)) # add IP address here
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)