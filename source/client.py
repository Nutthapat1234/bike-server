import socket
from random import randint

class Player:
    def __init__(self):
        self.id = 0
        self.position = 0
        self.zVelocity = 0
        self.playerState = 0
        self.connection = socket.socket()

    def connectToSever(self,ipAdress,port):
        self.connection.connect((ipAdress,port))

    def setId(self, i):
        self.id = i
        
    ###################
    ## PUBLIC GETTER ##
    ###################

    def tagClient(self):
        command = '"tagClient",\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        
    def getFrequency(self):
        command = '"getFrequency",'+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result
    
    def getVelocity(self):
        command = '"getVelocity",'+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    def getPosition(self):
        command = '"getPosition",'+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        
        return result

    def getPlayerState(self):
        command = '"getPlayerState",'+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        result = self.connection.recv(1024)
        result = result.decode("utf-8")
        return result

    def getHeadset(self):
        command = '"getHeadset",'+str(self.id)+'\n'
        command  = command.encode("utf-8")
        self.connection.send(command)
        result =  self.connection.recv(1024)
        result =  result.decode("utf-8")
        result =  result.split(',')
        
        return result

    ###################
    ## PUBLIC SETTER ##
    ###################
    def setFrequency(self,frequency):
        command = '"setFrequency",' + str(frequency)+','+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)

    def setHeadset(self,w=0,x=0,y=0,z=0):
        command = '"setHeadset",'+str(w)+','+str(x)+','+str(y)+','+str(z)+','+str(self.id)+'\n'
        command = command.encode("utf-8")
        self.connection.send(command)
        
#s = socket.socket()
#s.connect(("192.168.1.8",1995))

if __name__ == '__main__':
    p =  Player()
    hostName = socket.gethostbyname('localhost')
    p.connectToSever(hostName,1995)
    p.tagClient()

    while True:
##      b = randint(1,50)
        b = 5
        p.setFrequency(b)
        p.setHeadset(randint(1,50),randint(1,50),randint(1,50),randint(1,50))
        print('freq:' + str(p.getFrequency()) + ', velo:' + str(p.getVelocity()) +', pos:' + str(p.getPosition()))
        print("Headset: "+str(p.getHeadset()))
        #print(p.getPlayerState())
    
