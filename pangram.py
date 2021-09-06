def panagram(a):
    b=' '
    c=0
    for i in a.lower():
         if 96<=ord(i)<=122:
            if i not in b:
                b+=i
                c+=1
                print(c)
    print(b)
    if c==26:
        return True
    else:
        return False
print(panagram("the quick brown for jumps 456 over the  lazy dog x ") )