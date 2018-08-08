import socket
import threading

from data import GameData
from config import CLIENT_LIMIT, PLAYER_LIMIT
from communication import CommunicationThread
from calculation import GameCalculationThread


class Server:
    def __init__(self):
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        
        self.connectionList = []
        self.gameData = GameData()
        self.calculationThread = GameCalculationThread( self.gameData )
        self.calculationThread.start()

    def startConnection(self, ipAddr):
        self.socket.bind((ipAddr, config.PORT))
        self.socket.listen(CLIENT_LIMIT)
        
        print("binded at : " + str(ipAddr) + " : " + str(config.PORT))
        self.__mainLoop()

    def __mainLoop(self):
        while True:
            conn, addr = self.socket.accept()            
            print("new client connected from : " + str(addr))

            # todo : check connection limit properly
            if len(self.connectionList) >= CLIENT_LIMIT:
                conn.close()
                continue

            newId = len(self.connectionList)
            newCommuThread = CommunicationThread(conn, addr, self.gameData, newId)
            newCommuThread.start()
            
            self.connectionList.append(newCommuThread)
            
            
if __name__ == '__main__':
    hostName = socket.gethostbyname(socket.gethostname())
    
    server = Server()
    server.startConnection(hostName)
