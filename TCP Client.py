from socket import *
serverName = '10.0.0.32' # add IP address here
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input a lower case sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server : ' + modifiedSentence.decode())
clientSocket.close()
print("complete")