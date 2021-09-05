#always sequencal perameters follows keyword perameters
def a(arg,kwdarg=1):
    print(arg)
    print(kwdarg)
a(5,10)
def b(*h,**j ):
    print(h)
    print(j)
b(5,5,5,a=1,d=5)
b(1,2,4,5,6,a=10)