
###Networking stuff

http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib#

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
local_ip_address = s.getsockname()[0]

--------------------

from tkinter import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
local_ip_address = s.getsockname()[0]

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_text(150,100, text="There once was a man from Toulouse")
canvas.create_text(150,150, text=local_ip_address)
btn1 = Button(tk, text="hello world")
btn1.pack()
