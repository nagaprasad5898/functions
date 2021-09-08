def a(b):
    c=""
    for i in b.split( ):
        if i not in c:
            c+=i+' '
    d=c.split()
    print(" ".join(sorted(d)))

a("hello world and practice makes perfect and hello world again")

def s(h):
    f=sorted(set(h.split()))
    print(" ".join(f))
s("hello world and practice makes perfect and hello world again")
