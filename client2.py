import socket
import time

# ? HOW to check the connection does exist
# ? How to unbind
# ? socket.error: [Errno 111] Connection refused

s=socket.socket()

host='127.0.0.1'
port=1121

while  s.connect((host,port)):
    print s.recv(1024)
    time.sleep(0.5)
