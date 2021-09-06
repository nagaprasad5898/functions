def longest_word(a):
    b=0
    for i in a:
        if b<len(i):
            b=b+len(i)
    return b
c=["kanna",'lucky','kannalucky']
print(longest_word(c))