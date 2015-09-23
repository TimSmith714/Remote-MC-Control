# This server is intended to work as a test for work on the client
# The client depends on a response from the server so thats what this
# will provide.
# I will take out all of the PyUserInput code and maybe just print
#what was received for testing

import time
import socket

host = '127.0.0.1'
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    data = client.recv(size)
    print(data)
    #Now work out what was sent and act accordingly
