def kanna(*a):
    g=()
    if len(a)==1:
        c,d,e=0,1,0
    elif len(a)==2:
        c,d,e=a[0],1,1
    else:
        c,d,e=a[0],a[2],1
    while c<a[e]:
        g+=(c,)
        c+=d
    return g
print(kanna(1,10,2))