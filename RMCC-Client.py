import socket
import time

host = '192.168.2.5'
port = 50000
size = 1024

def sendCommand(commandString):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(commandString)
    data = s.recv(size)
    s.close()
    print 'Received: ', data

while True:
    mcControl = raw_input("Command?")
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

