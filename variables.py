#there are 3types of variables there are global, local,nonlocal
#global:we can call inside a function but we cant edit it with out using global key word
a="global"
def b():
    print("inside a function",a)
b()
#we can call and modife by using global
def c():
    global a
    a="kanna"
    print("inside c function",a)
c()
print(a)
#nonlocal variables
def d():
    a="lucky"
    def e():
        #global a
        #nonlocal a
        a="kannalucky"
        print("inside a e function ",a)
    e()
    print("inside a d function",a)
print("out side a function",a)
d()

