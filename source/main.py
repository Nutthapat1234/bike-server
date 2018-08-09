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

    def startConnection(self, ipAddr):
        self.socket.bind((ipAddr, PORT))
        self.socket.listen(CLIENT_LIMIT)
        
        print("binded at : " + str(ipAddr) + " : " + str(PORT))
        self.__mainLoop()

    def __mainLoop(self):
        while True:
            conn, addr = self.socket.accept()            
            print("new client connected from : " + str(addr))

            # todo : check connection limit properly
            if len(self.connectionList) >= CLIENT_LIMIT:
                print("reject connection from : " + str(addr))
                conn.close()
                continue

            newId = len(self.connectionList)
            print('client id :', newId)
            newCommuThread = CommunicationThread(conn, addr, self.gameData, newId)
            newCommuThread.start()
            
            self.connectionList.append(newCommuThread)
            
            
if __name__ == '__main__':
##    hostName = socket.gethostbyname(socket.gethostname())
    hostName = socket.gethostbyname('localhost')
    
    server = Server()
    server.startConnection(hostName)
