#if we are using empty list or tuple we want defind the function like a()
def kanna(lucky=[]):
    lucky.append("***")
    return lucky
c=kanna()
print(c)
c=kanna()
print(c)

def a(b=[]):
    if b==[]:
        b=["***"]
    else:
        b=[b]
    return b
c=a(1)
print(c)
c=a()
print(c)

