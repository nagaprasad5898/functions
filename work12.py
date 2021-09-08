def common(a,b):
    c=''
    for i in a:
        if i in b:
            c=c+i
    print(c)
common("aa","aa")
