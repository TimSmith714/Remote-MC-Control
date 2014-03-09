from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()

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
