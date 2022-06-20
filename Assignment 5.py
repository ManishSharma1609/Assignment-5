#Question 1
s=input("Enter a string :")
l=len(s)
s2=''
for i in range(l-1,-1,-1):
    s2=s2+s[i]
print("Reversed string is:",s2,"\n")

#Question 2
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
n=int(input("Enter number: "))
for i in range(x1,x2,1):
    if i%n==0:
        print(i)
        continue

#Question 3
import math
a=int(input("Enter first side of the triangle: "))
b=int(input("Enter second side of the triangle: "))
c=int(input("Enter third side of the triangle: "))
if a<0 or b<0 or c<0:
    print("Invalid input, side cannot be negative")
elif a+b<c or b+c<a or c+b<a:
    print("Combination of sides is not possible")
else:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area of the triangle is {area}","\n")


#Question 4
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("\n")

for i in range(n-1):
    for j in range (n-1-i):
        print("*", end=" ")
    print("\n")


#Question 5
n = int(input("Enter number of rows : "))
a=0

for i in range (n):
    for j in range(i+1):
        print(chr(65+a), end="")
        a+=1
    print("\n")


#Question 6
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
for i in range(x1,x2,1):
    c=0
    n=1
    while n<=i:
        if i%n==0:
            c+=1
            n+=1
            continue
        n=n+1
    if c==2:
        print(i,"\n")


#Question 7
for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i,"\n")


#Question 8
list=[]
for i in range(0,10,1):
    n=int(input(f"Enter {i+1} number: "))
    list.append(n)
print(list)

#a)
print("Positive numbers are: ")
for i in range(10):
    if list[i]>0:
        print(list[i])

#b)
print("Negative numbers are: ")
for i in range(10):
    if list[i]<0:
        print(list[i])

#c)
print("Odd numbers are: ")
for i in range(10):
    if list[i]%2!=0:
        print(list[i])

#d)
print("Even numbers are: ")
for i in range(10):
    if list[i]%2==0:
        print(list[i])

#e)
count=dict()
for no in list:
    if no in count:
        count[no]+=1
    else:
        count[no]=1

print("No of times each number occurs in the List: ",count,"\n" )


#Question 9
str=input("Enter a string: ")
counts = dict()
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1




