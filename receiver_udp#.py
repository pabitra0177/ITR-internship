# python3
import socket

ip = "127.0.0.1"
port = 5001

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))


i=0
while True:
	data, addr = s.recvfrom(1024)
	print ("Received from ",addr)
	#print ("Received  ",str(data))
	p=data.decode()
	print(p)
		
s.close()
