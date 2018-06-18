#
import socket

ip = "127.0.0.1"
port = 5001
f= open("/home/pabitra/ITR/Codes/reader.txt")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in f:
    print(type(i))
    s.sendto(i,(ip,port))
    #print(i)
f.close()
s.close()
