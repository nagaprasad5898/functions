com=[]
dif=[]
def comn_num(a,b):
    for i in a:
        if i in b:
            com.append(i)
    print(com)
def def_num(a,b):
    for i in a:
        if i not in b:
            dif.append(i)
    for j in b:
        if j not in a and j not in dif:
            dif.append(j)
    print(dif)
c=[1,2,4,5,6]
d=[5,4,6,8]
comn_num(c,d)
def_num(c,d)
