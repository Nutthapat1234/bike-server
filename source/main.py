import socket
import threading

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

    def __mainLoop(self):
        while True:
            if(len(self.connectionList)< 1): #change to client limit
                conn, addr = self.socket.accept()            
                print("new client connected from : " + str(addr))
                
                newCommuThread = CommunicationThread(conn, addr,self.gameData)
                newCommuThread.start()

                self.connectionList.append(newCommuThread)

            # to check exception form client
            for client in self.connectionList[:]:
                if len(self.connectionList) == 0:
                    break
                exc = client.getException()
                if exc is not None:
                    client.exit()
                    self.connectionList.remove(client)
                    print("Wait for connection...")
                    conn, addr = self.socket.accept()            
                    print("reconnect client connected from : " + str(addr))

                    newCommuThread = CommunicationThread(conn, addr, self.gameData)
                    newCommuThread.start()

                    self.connectionList.append(newCommuThread)

            # todo : check connection limit properly
            if len(self.connectionList) >= CLIENT_LIMIT:
                print("reject connection from : " + str(addr))
                conn.close()
                continue
            
            
if __name__ == '__main__':
##    hostName = socket.gethostbyname(socket.gethostname())
    hostName = socket.gethostbyname('localhost')
    
    server = Server()
    server.startConnection(hostName)
