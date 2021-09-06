def sum(*a):
    b=0
    for i in a:
       b=b+i
    return (b)
print(sum(1,2,3,4))

def mul(*a):
    b=1
    for i in a:
       b=b*i
    return (b)
print(mul(1,2,3,4))

def sub(*a):
    b=0
    for i in a:
       b=i-b
    return b
print(sub(1,2,3,4))

def dev(*a):
    b = 1
    for i in a:
        b=i/b
    return (b)
print(dev(10,100))
#dev(1,2)

def dev1(a,b):
    return a/b
print(dev1(10,3))
"""
def quit1():
    breakpoint()

def dev1(a,b):
    quit1()
    return a/b
print(dev1(10,3))
"""


