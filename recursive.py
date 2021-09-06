'''
def rc(a):
    a+=1
    print(a)
    rc(a)
rc(10)
'''
def factorial(a):
    if a==1 or a==1:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(5))