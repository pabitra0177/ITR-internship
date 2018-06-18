#
import socket

ip = "127.0.0.1"
port = 5001

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))
l=[]
i=0
while True:
    data, addr = s.recvfrom(1024)
    print "Received from ",addr
    print "Received  ",data
    l.append(data)
    f= open("/home/pabitra/ITR/Codes/writer.txt",'r+a')
    f.write(l[-1])
    f.close()

s.close()
