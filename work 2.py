def vowel(a):
    if a in "aeiouAEIOU":
        return "{} is vowel".format(a)
    else:
        return "{} it is not a vowel".format(a)
print(vowel("a"))

def sum(a):
    b=0
    for i in a:
        b=b+i
    return b
print(sum([1,2,3,4]))

def mul(a):
    b=1
    for i in a:
        b=b*i
    return b
print(mul([1,2,3,4]))