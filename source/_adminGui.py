from tkinter import *

import socket
from _admin import Admin
from config import IP, PORT

if __name__ == "__main__":
    windows = Tk()
    windows.title('Admin')
    admin = Admin()
<<<<<<< HEAD
    hostname = socket.gethostbyname('localhost')
    #admin.connectToSever(hostname,1995)
    startButt = Button(windows,text="Start",command = admin.start,height = 5,width=30).pack(fill=BOTH)
    resetButt = Button(windows,text="Reset",command = admin.reset,height = 5,width=30).pack(fill=BOTH)
=======
    hostname = socket.gethostbyname(IP)
    admin.connectToSever(hostname,PORT)
    startButt = Button(windows,text="Start",command = admin.start).pack()
    resetButt = Button(windows,text="Reset",command = admin.reset).pack()
>>>>>>> master
    
    windows.mainloop()
