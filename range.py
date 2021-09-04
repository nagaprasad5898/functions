def kanna(b,a=1,c=1):
    """the sequenc must be in stop start and step"""
    e=[]
    if a!=0:
        d=a
    else:
        d=0
    while b>d :
        if c==1:
            e.append(d)
            d=d+1
        else:
            e.append(d)
            d=d+c
    print(e)
kanna(10,2,3)
