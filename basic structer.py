#functions:it is a set of instructions to perform some specific task
def operations1(a,b,c,d):#hear we def function by using def keyword and name of the function by using()
    """==>it is a discription of the code to see this we use (fun_name.__doc__)
    ==>in "()" we give parameters"""
    f=a+b #perfoming the addition operation
    e=a*b #perfoming the multiplication operation
   # print("inside function:",f,e)
    return f,e
k=operations1(a=int(input("enter a number")),
b=int(input("enter a number")),
c=int(input("enter a number")),d=int(input("enter a number")))#calling the function by passing the
#values of parameters called "arguments"
q,e=k
print(e,q)
print(operations1.__doc__)
#print(operations1(2,1,3,4))
