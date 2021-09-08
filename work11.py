def max_len(a,b):
    if len(a)==len(b):
        print(a)
        print(b)
    elif len(a)>len(b):
        print(a,len(a))
    else:
        print(b,len(b))

max_len("kanna",'lucky1')