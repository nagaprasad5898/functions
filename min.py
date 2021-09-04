def min1(a):
    b=ord(a[0])
    for i in a:
        if ord(i)<b:
            b=ord(i)
    print(chr(b))
min1("kanna")