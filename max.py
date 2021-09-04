def max1(a):
    """hi frnds"""
    b=ord(a[0])
    for i in a:
        if ord(i)>b:
            b=ord(i)
    print(chr(b))
max1("kanna")
print(max1.__doc__)