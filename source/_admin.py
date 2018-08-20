import socket
from config import IP, PORT
class Admin:
    def __init__(self):
        self.connection = socket.socket()

    def connectToSever(self,ipAdress,port):
        self.connection.connect((ipAdress,port))

    def start(self):
        command = "'start'," + "\n"
        command = command.encode("utf-8")
        self.connection.send(command)

    def reset(self):
        command = '"reset",'+"\n"
        command = command.encode("utf-8")
        self.connection.send(command)

    
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
