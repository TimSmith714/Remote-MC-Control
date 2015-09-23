#Removed the lines to receive data from the server
#As that didn't seem to be working

import socket
import time

host = '127.0.0.1'
port = 50000
size = 1024

def sendCommand(commandString):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(commandString.encode())
#    data = s.recv(size)
    s.close()
#    print ('Received: ', data)

while True:
    mcControl = input("Command?")
    if mcControl == 'h':
        sendCommand('viewLeft')
    elif mcControl == 'k':
        sendCommand('viewRight')
    elif mcControl == 'u':
        sendCommand('viewUp')
    elif mcControl == 'j':
        sendCommand('viewDown')
    elif mcControl == 'w':
        sendCommand('moveForward')
    elif mcControl == 'a':
        sendCommand('moveLeft')
    elif mcControl == 's':
        sendCommand('moveBackward')
    elif mcControl == 'd':
        sendCommand('moveRight')
    elif mcControl == 't':
        sendCommand('flyMode')
    elif mcControl == 'g':
        sendCommand('moveUp')
    elif mcControl == 'b':
        sendCommand('moveDown')

