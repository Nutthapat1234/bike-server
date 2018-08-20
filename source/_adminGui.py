from tkinter import *

import socket
from _admin import Admin


if __name__ == "__main__":
    windows = Tk()
    windows.title('Admin')
    admin = Admin()
    hostname = socket.gethostbyname('localhost')
    #admin.connectToSever(hostname,1995)
    startButt = Button(windows,text="Start",command = admin.start,height = 5,width=30).pack(fill=BOTH)
    resetButt = Button(windows,text="Reset",command = admin.reset,height = 5,width=30).pack(fill=BOTH)
    
    windows.mainloop()
