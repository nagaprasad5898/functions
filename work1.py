def max1(a,b):
    if a>b:
        return "largest number is:",a
    else:
        return "largest number is:",b

print(max1(10, 20))
# take 3 integers as inputs and print largest number
def max2(a,b,c):
     if a>b and a>c:
         return "largest number is:",a
     elif b>a and b>c:
         return "largest number is:",b
     else:
         return "largest number is:",c

print(max2(1,2,3))

def max_all(*a):
     b=a[0]
     for i in a:
         if b<i:
             b=i
     return "largest number is:",b
print(max_all(1,2,5,4,8,7))
