def max1(a,b):
    if a>b:
        print("largest number is:",a)
    else:
        print("largest number is:",b)

max1(10, 20)
# take 3 integers as inputs and print largest number
def max2(a,b,c):
     if a>b and a>c:
         print("largest number is:",a)
     elif b>a and b>c:
         print("largest number is:",b)
     else:
         print("largest number is:",c)

max2(1,2,3)

def max_all(*a):
     b=a[0]
     for i in a:
         if b<i:
             b=i
     print("largest number is:",b)
max_all(1,2,5,4,8,7)
