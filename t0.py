import threading
from time import  sleep
import sys

x=int()
p=int()
def c():
    global x,p
    while 1:
        x=input()
        #x=x+p


def printer():
    global x,p
    while 1:
        #q=q+x
        print(x)
        sleep(1)


t1=threading.Thread(target=c)
t1.daemon=True
t1.start()
printer()
