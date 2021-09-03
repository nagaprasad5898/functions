#functions:
def operations1(a,b,c,d):
    f=a+b
    e=a*b
   # print("inside function:",f,e)
    return f,e
k=operations1(a=int(input("enter a number")),
b=int(input("enter a number")),
c=int(input("enter a number")),d=int(input("enter a number")))
q,e=k
print(q)
#print(operations1(2,1,3,4))
