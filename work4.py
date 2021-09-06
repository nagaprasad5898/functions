def sum(*a):
    b=0
    for i in a:
       b=b+i
    return (b)
sum(1,2,3,4)

def mul(*a):
    b=1
    for i in a:
       b=b*i
    return (b)
mul(1,2,3,4)

def sub(*a):
    b=0
    for i in a:
       b=i-b
    print(b)
sub(1,2,3,4)