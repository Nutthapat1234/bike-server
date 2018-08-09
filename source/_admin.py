import socket

class Admin:
    def __init__(self):
        self.connection = socket.socket()

    def connectToSever(self,ipAdress,port):
        self.connection.connect((ipAdress,port))

a = Admin()
hostName = socket.gethostbyname('localhost')
a.connectToSever(hostName,1995)

while True:
    line = input()
    line = line.encode('utf-8')
    p.connection.send(line)
    
