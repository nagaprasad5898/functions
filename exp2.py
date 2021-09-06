def typesofparameters(a,b,/,f=2,*,e=10,g=583):
    print(a,b,)
    print(d,f)
    print(e,g)
typesofparameters(1,2,3,5)
typesofparameters(1,2,4,d=5)
typesofparameters(1,8,5,6,5)
#typesofparameters(a=1,b=10,c=56,d=2,f=4,e=6,g=9)#typesofparameters()
# got some positional-only arguments passed as keyword arguments: 'a, b, c'
typesofparameters(1,8,5,d=6,f=5,e=5,g=6)