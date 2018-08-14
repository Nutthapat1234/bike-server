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

    def ClientTag(self,tag):
        self.tag = tag

    ###################
    ## PUBLIC GETTER ##
    ###################
    def setPlayerTag(self):
        command = self.tag + ',"setPlayerTag",'+self.tag+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        
    def getFrequency(self):
        command = self.tag + ',"getFrequency",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result
    
    def getVelocity(self):
        command = self.tag + ',"getVelocity",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    def getPosition(self):
        command = self.tag + ',"getPosition",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        
        return result

    def getPlayerState(self):
        command = self.tag + ',"getPlayerState",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    ###################
    ## PUBLIC SETTER ##
    ###################
    def setFrequency(self,frequency):
        command = self.tag + ',"setFrequency",' + str(frequency)+"\n"
        command = command.encode("utf-8")
        self.connection.send(command)
        
        
#s = socket.socket()
#s.connect(("192.168.1.8",1995))
        
p =  Player()
hostName = socket.gethostbyname('localhost')
p.connectToSever(hostName,1995)
p.ClientTag('"Player1"')
p.setPlayerTag()

while True:
##    b = randint(1,50)
    b = 10
    p.setFrequency(b)
    p.getFrequency()
    p.getVelocity()
    a = float(p.getPosition())
    print(a)
    #print(p.getPlayerState())
    
