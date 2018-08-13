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
    def getFrequency(self,tagname):
        command = str(tagname)+',"getFrequency",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result
    
    def getVelocity(self,tagname):
        command = str(tagname)+',"getVelocity",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    def getPosition(self,tagname):
        command = str(tagname)+',"getPosition",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        
        return result

    def getPlayerState(self,tagnmae):
        command = str(tagname)+'"getPlayerState",'+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    ###################
    ## PUBLIC SETTER ##
    ###################
    def setFrequency(self,frequency,tagname):
        command = str(tagname)+',"setFrequency",' + str(frequency)+"\n"
        command = command.encode("utf-8")
        self.connection.send(command)

    def setClientTag(self,tagname):
        command = str(tagname)+',"setClientTag",'+str(tagname)+"\n"
        command = command.encode("utf-8")
        self.connection.send(command)
        
        
#s = socket.socket()
#s.connect(("192.168.1.8",1995))
        
p =  Player()
hostName = socket.gethostbyname('localhost')
p.connectToSever(hostName,1995)

tag = "\'Player1\'"
p.setClientTag(tag)

while True:
##    b = randint(1,50)
    b = 10
    p.setFrequency(b,tag)
    p.getFrequency(tag)
    p.getVelocity(tag)
    a = float(p.getPosition(tag))
    print(a)
    #print(p.getPlayerState())
    
