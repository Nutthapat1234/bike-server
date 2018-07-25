import socket
import threading

import config
from data import GameData
from communication import CommunicationThread
from calculation import GameCalculationThread


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionList = []
        self.gameData = GameData()

    def startConnection(self, ipAddr):
        self.socket.bind((ipAddr, config.PORT))
        self.socket.listen(config.CLIENT_LIMIT)
        
        print("binded at : " + str(ipAddr) + " : " + str(config.PORT))
        self.mainLoop()

    def mainLoop(self):
        calculationThread = GameCalculationThread(self.gameData)
        calculationThread.start()
        
        while True:
            conn, addr = self.socket.accept()
            
            print("Client connected from ip : " + str(addr))
            newCommuThread = CommunicationThread(conn, addr, self.gameData)
            newCommuThread.start()
            self.connectionList.append(newCommuThread)

if __name__ == '__main__':
    hostName = socket.gethostbyname(socket.gethostname())
    
    server = Server()
    server.startConnection(hostName)
