#method overloading
from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    print("result",a*b)

@dispatch(int,float,int)
def product(a,b,c):
    print("result",a*b*c)

@dispatch(float,float,float,float)
def product(a,b,c,d):
    print("result",a*b*c*d)

product(2,3)            
product(2,3.3,4)            
product(2.2,3.4,4.6,5.1)            
          