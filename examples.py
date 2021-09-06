#using of "/" and "*"and definding the parameters all the perameters before "/" are required
# and after "/" are requried and keyword parameters and after "*" all are keyword parameters
def typesofparameters(a,b,c,/,d,f=2,*,e=10,g=58):
    print(a,b,c)
    print(d,f)
    print(e,g)
typesofparameters(1,2,3,5)
typesofparameters(1,2,4,d=5)
typesofparameters(1,8,5,6,5)
typesofparameters(1,2,8,d=2,f=4,e=6,g=9)#typesofparameters()
# got some positional-only arguments passed as keyword arguments: 'a, b, c'
#typesofparameters(c=1,a=8,b=5,d=6,f=5,e=5,g=6)