from tkinter import *

import socket
from _admin import Admin


if __name__ == "__main__":
    windows = Tk()
    admin = Admin()
    hostname = socket.gethostbyname('localhost')
    admin.connectToSever(hostname,1995)
    startButt = Button(windows,text="Start",command = admin.start).pack()
    resetButt = Button(windows,text="Reset",command = admin.reset).pack()
    
    windows.mainloop()
