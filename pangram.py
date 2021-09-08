def panagram(a):
    b=''
    c=0
    for i in a.lower():
         if ord("a")<=ord(i)<=ord("z"):
            if i not in b:
                b+=i
                c+=1
         elif c==26:
             return True

    else:
        return False
'''                
    if c==26:
        return True
    else:
        return False
'''
print(panagram("the quick brown fox xkbwsgi jumps 456 over the  lazy dog  ") )