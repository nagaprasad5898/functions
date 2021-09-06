def vowel(a):
    if a in "aeiouAEIOU":
        print("{} is vowel".format(a))
    else:
        print("{} it is not a vowel".format(a))
vowel("a")

def sum(a):
    b=0
    for i in a:
        b=b+i
    print(b)
sum([1,2,3,4])

def mul(a):
    b=1
    for i in a:
        b=b*i
    print(b)
mul([1,2,3,4])