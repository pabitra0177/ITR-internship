import socket

s=socket.socket()
#host=socket.gethostname()
host='127.0.0.1'
port=112
s.bind((host,port))

s.listen(5)

while True:
    c,addr=s.accept()
    print("Got connection from ",addr)
    c.send("Hello world !")
    c.close()
