def a_mean(x,*a):
    c=0
    for i in a:
        c=c+i

    print((x+c)/(len(a)+1))
a_mean(4,7,9)
a_mean(4,7,9,45,-3,7,99)
