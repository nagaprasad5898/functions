def appnd(a):
    b=[]
    for i in a:
        b.append(i+"s")
    return b
c=[w for w in appnd(["a","b","c"])]
print(c)
