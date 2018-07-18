# python3
import socket

ip = "127.0.0.1"
port = 5001
i=0
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(10):
    s.sendto(str(i).encode(),(ip,port))

s.close()
