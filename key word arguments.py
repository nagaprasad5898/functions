#calling function by using keywords
def kanna(a,b,c,d):
    f=a//b
    g=c*d
    return f,g

#div1,mul1=kanna(a=10,b=5,c="kanna",d=5)
#div1,mul1=kanna(d=1,b=5,c="kanna",a=5)
#div1,mul1=kanna(c=10,d=6,b=5,a=1)
div1,mul1=kanna(a=1,d=5,c="kanna ",b=5)
print("division:{},\nmultipltication:{}".format(div1,mul1))
