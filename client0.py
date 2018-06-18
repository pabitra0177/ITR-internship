import socket

s=socket.socket()
#host=socket.gethostname()
#print(host)
host=''
port=112

s.connect((host,port))
print(s.recv())

s.close()
