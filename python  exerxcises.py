#swapping numbers
x=int(input("enter the first number" ))
y=int(input("enter the second number" ))
print(x,y)

y=x+y
y=x-y

print(x,y)

#program to extract each digit

n=input("enter the number:")
y=n[::-1]
k="".join(y)
print(k)

#sum of digits
x=int(input("enter three digit number"))
a=x%10
num=x//10
b=num%10
c=num//10
print(a+b+c)

#Program to reverse a 4 digit number

x=int(input("enter the four digit number"))
a=x%10
num_1=x//10
b=num_1%10
num_2=num_1//10
c=num_2%10
d=num_2//10
rev=a*1000+b*100+c*10+d
print(rev)
if x==rev:
      print(True)
else:
    print(False)

#find the eucliean education

import math
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
x=[x1,y1]
y=[x2,y2]
print("="*100)
print("eucledian distance for given co-ordinates will be",round(math.dist(x,y),2))

#write a program that will take three digits from the user and add the square of each digit

n=int(input("Enter the three digit number:"))
a=n%10
num=n//10
b=num%10
c=num//10
if(a**3 + b**3 + c**3)==n:
    print("the number is armstrong number")
else:
        print("the number is not armstrong number")

#write a program that will take user input of (4 digits numbers) and check whether the number is narcissit number or not

n=int(input(" enter four digit number: "))

a=n%10
num=n//10
b=num%10
num_1=num//10
c=num_1%10
d=num_1//10
if(a**4 + b**4 + c**4+d**4)==n:
    print("the number is narcissist number")
else:
    print("the number is not narcissit number")



        
