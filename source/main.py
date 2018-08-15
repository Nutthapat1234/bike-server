import socket
import threading
from time import sleep as delay

from debugging import print
from data import GameData
from communication import CommunicationThread
from calculation import GameCalculationThread
from config import CLIENT_LIMIT, PLAYER_LIMIT, PORT

class Server:
    def __init__(self):
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        
        self.connectionList = []
        self.gameData = GameData()
        self.calculationThread = GameCalculationThread( self.gameData )
        self.calculationThread.start() 
        self.calculationThread.startGame()

    def startConnection(self, ipAddr):
        self.socket.bind((ipAddr, PORT))
        self.socket.listen(CLIENT_LIMIT)
        
        print("binded at : " + str(ipAddr) + " : " + str(PORT))
        self.__mainLoop()

    def __clearDeadClient(self):        
        if len(self.connectionList) == 0:
            return
        
        for client in self.connectionList:
            exc = client.getException()
            
            if exc is not None:
                client.exit()
                self.connectionList.remove(client)

    def __waitAndAcceptNewClient(self):
        conn, addr = self.socket.accept()            
        print("new client connected from : " + str(addr))
        
        newCommuThread = CommunicationThread(conn, addr,self.gameData)
        newCommuThread.start()

        self.connectionList.append(newCommuThread)

    def __mainLoop(self):
        while True:
            try:
                self.__clearDeadClient()
                connectedNum = len(self.connectionList)
                
                if connectedNum < CLIENT_LIMIT:
                    self.__waitAndAcceptNewClient()

                delay(1)
                
            except ConnectionResetError as msg:
                print('connection reset error', msg)
            
if __name__ == '__main__':
##    hostName = socket.gethostbyname(socket.gethostname())
    hostName = socket.gethostbyname('localhost')
    
    server = Server()
    server.startConnection(hostName)
