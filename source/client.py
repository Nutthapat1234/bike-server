import socket
from random import randint

class Player:
    def __init__(self):
        self.position = 0
        self.zVelocity = 0
        self.playerState = 0
        self.connection = socket.socket()

    def connectToSever(self,ipAdress,port):
        self.connection.connect((ipAdress,port))

    ###################
    ## PUBLIC GETTER ##
    ###################
    def getVelocity(self):
        command = '"getVelocity",'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    def getPosition(self):
        command = '"getPosition",'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        
        return result

    def getPlayerState(self):
        command = '"getPlayerState",'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    ###################
    ## PUBLIC SETTER ##
    ###################
    def setFrequency(self,frequency):
        command = '"setFrequency",' + str(frequency)
        command = command.encode("utf-8")
        self.connection.send(command)
        
        
#s = socket.socket()
#s.connect(("192.168.1.8",1995))
        
p =  Player()
hostName = socket.gethostbyname('localhost')
p.connectToSever(hostName,1995)

while True:
##    b = randint(1,50)
    b = 10
    p.setFrequency(b)
    p.getVelocity()
    a = float(p.getPosition())
    print(a)
    print(p.getPlayerState())
    
