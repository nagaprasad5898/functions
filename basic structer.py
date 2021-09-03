#functions:it is a set of instructions to perform some specific task
def operations1(a,b,c,d):#hear we def function by using def keyword and name of the function by using()
    """==>it is a discription of the code to see this we use (fun_name.__doc__)
    ==>in "()" we give parameters"""
    f=a+b #perfoming the addition operation
    e=a*b #perfoming the multiplication operation
   # print("inside function:",f,e)
    return f,e
k=operations1(10,20,30,40)#calling the function by passing the
#values of parameters called "arguments"
q,e=k
print(e,q)
print("discription:",operations1.__doc__)
print("name of the function:",operations1.__name__)
#print(operations1(2,1,3,4))
