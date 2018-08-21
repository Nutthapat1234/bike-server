from tkinter import*
import threading
import socket

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
        self.sendToSever(command)

    def sendToSever(self,command):
        try:
            self.connection.send(command)
        except socket.error:
            self.isConnect = False
            self.connection.close()
            self.__init__()
            while(not(self.isConnect)):
                self.tryConnect()
            

    def tryConnect(self):
        result = self.connection.connect_ex((self.ip,self.port))
        if(result == 0):
            self.isConnect = True
        else:
            self.isConnect = False


if __name__ == "__main__":
    windows = Tk()
    windows.title('Admin')
    admin = Admin()
    hostname = socket.gethostbyname('localhost')
    admin.connectToSever(hostname,1995)
    startButt = Button(windows,text="Start",command = admin.start,height = 20,width=50).pack(fill=BOTH)
    resetButt = Button(windows,text="Reset",command = admin.reset,height = 20,width=50).pack(fill=BOTH)
    
    windows.mainloop()
