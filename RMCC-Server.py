from PyUserInput.pymouse import PyMouse
from PyUserInput.pykeyboard import PyKeyboard
from tkinter import *

import time
import socket
import tkinter as tk

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

ipaddressTest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ipaddressTest.connect(('8.8.8.8',0))
local_ip_address = ipaddressTest.getsockname()[0]

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()

#Done with other initialisation so lets build a window

RmccWin = tk.Tk()
RmccWin.title("Minecraft Remote Control Server")
RmccWin.geometry("330x300")
RmccWin.wm_iconbitmap('Browsersettings.ico')

btnStart = tk.Button(RmccWin, text="Start", font=("Tahoma", 16))
btnStart.pack()
btnStart.place(x=0, y=256)

btnStop = tk.Button(RmccWin, text="Stop", font=("Tahoma", 16))
btnStop.pack()
btnStop.place(x=270, y=256)

lblIPaddressTitle = tk.Label(RmccWin,text="IP Address:",font=("Tahoma", 14))
lblIPaddressTitle.pack()
lblIPaddress = tk.Label(RmccWin, text=local_ip_address,font=("Tahoma", 14))
lblIPaddress.pack()

lblServerStatus = tk.Label(RmccWin, text="Server not running", font=("Tahoma", 12))
lblServerStatus.place(x=150, y=250)
lblServerStatus.pack()

lblInstructions = tk.Label(RmccWin, text="Start this program first. \nMake a note of the IP address shown above. Enter this address into the Client program so it can communicate with this program and Minecraft. \nClick Start and this program will start. \nStart Minecraft and put it in Fullscreen mode (F11)", wraplength=300, anchor=W, justify=LEFT)
lblInstructions.pack()

RmccWin.mainloop()

while 1:
    client, address = s.accept()
    data = client.recv(size)
    #Now work out what was sent and act accordingly
    if data == 'viewLeft':
        client.send(data)
        m.move((x_dim / 2) - ((x_dim / 100) * 5), y_dim / 2)
        client.close()
    elif data == 'viewRight':
        client.send(data)
        m.move((x_dim / 2) + ((x_dim / 100) * 5), y_dim / 2)
        client.close()
    elif data == 'viewUp':
        client.send(data)
        m.move(x_dim / 2, (y_dim / 2) - ((y_dim / 100) * 5))
        client.close()
    elif data == 'viewDown':
        client.send(data)
        m.move(x_dim / 2, (y_dim / 2) + ((y_dim / 100) * 5))
        client.close()
    elif data == 'moveForward':
        k.press_key('w')
        time.sleep(0.5)
        k.release_key('w')
        client.send(data)
        client.close()
    elif data == 'moveBackward':
        k.press_key('s')
        time.sleep(0.5)
        k.release_key('s')
        client.send(data)
        client.close()
    elif data == 'moveLeft':
        k.press_key('a')
        time.sleep(0.5)
        k.release_key('a')
        client.send(data)
        client.close()
    elif data == 'moveRight':
        k.press_key('d')
        time.sleep(0.5)
        k.release_key('d')
        client.send(data)
        client.close()

    elif data == 'moveUp':
        k.press_key(' ')
        time.sleep(0.5)
        k.release_key(' ')
        client.send(data)
        client.close()

    elif data == 'moveDown':
        k.press_key(k.shift_l_key)
        time.sleep(0.5)
        k.release_key(k.shift_l_key)
        client.send(data)
        client.close()

    elif data == 'flyMode':
        k.press_key(' ')
        time.sleep(0.1)
        k.release_key(' ')
        time.sleep(.1)
        k.press_key(' ')
        time.sleep(0.1)
        k.release_key(' ')
        client.send(data)
        client.close()
