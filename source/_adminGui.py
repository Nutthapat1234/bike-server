from tkinter import *

import socket
from _admin import Admin
from config import IP, PORT

if __name__ == "__main__":
    windows = Tk()
    admin = Admin()
    hostname = socket.gethostbyname(IP)
    admin.connectToSever(hostname,PORT)
    startButt = Button(windows,text="Start",command = admin.start).pack()
    resetButt = Button(windows,text="Reset",command = admin.reset).pack()
    
    windows.mainloop()
