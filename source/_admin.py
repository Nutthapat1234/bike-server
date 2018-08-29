from tkinter import*
import threading
import socket
from config import IP, PORT
from time import sleep as delay

class Admin:
    def __init__(self):
        self.connection = socket.socket()
        self.isConnect = False

    def connectToSever(self,ipAdress,port):
        self.ip = ipAdress
        self.port = port
        self.connection.connect((ipAdress,port))

    def start(self):
        command = "'start'," + "\n"
        command = command.encode("utf-8")
        self.sendToSever(command)

    def reset(self):
        command = '"reset",'+"\n"
        command = command.encode("utf-8")
        for i in range(10):
            self.connection.send(command)
            delay(0.05)

if __name__ == '__main__':
    admin = Admin()
    hostname = socket.gethostbyname(IP)
    admin.connectToSever(hostname,PORT)
    while True:
        line = input()
        if line == 'start':
            admin.start()
        if line == 'reset':
            admin.reset()

