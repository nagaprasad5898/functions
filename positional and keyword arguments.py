#if we are using both positional and key word 1st we want to provide positional arguments like given below
def kanna(a,b,c,d):
    f=a//b
    g=c*d
    return f,g

#div1,mul1=kanna(10,5,c="kanna",d=5)
#div1,mul1=kanna(d=1,b=5,"kanna",a=5)#==>it will through an error
# because we are not providing the positional at strting
#div1,mul1=kanna(10,d=6,b=5,a=1)#it will also through the error because it follows the postional sequency
#so we want to give in sequency
div1,mul1=kanna(1,5,d="kanna ",c=5)# we can give the key word arguments after the positional like in this exmple
print("division:{}\nmultipltication:{}".format(div1,mul1))
