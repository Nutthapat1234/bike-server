import socket

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



    
