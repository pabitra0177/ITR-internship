# ? HOw to bind to local address of the computer

import socket

s=socket.socket()
port=1121

s.bind(('',port))
s.listen(5)

print("binded port is",port)
print("server is ready to send")

x=[ a for a in range(10) ]

i=0
while i<len(x):
    c,addr=s.accept()
    print("Got connected from ",addr)
    c.send('x[i]')
    i+=1
c.close()
