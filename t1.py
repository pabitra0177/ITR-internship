# welcome  to threading
from  threading import *

def cube(x):
    print("Cube of x is {0}".format(x**3))
def square(x):
    print("Square of x is  {0} ".format(x*x))

while True:
    x=input()
    t1=Thread(target=cube,args=(x,))
    t2=Thread(target=square,args=(x,))
    t1.start()
    t2.start()
