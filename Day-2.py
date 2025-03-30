#Indexing

str1="Piyush Shukla"
print(str1[0:6])
print(str1[7:13])
print(str1[7:])

"""Using the [start:stop:step]"""

print(str1[0:13:2])
print(str1[::2])
print(str1[::3])

"""Using reverse string"""

print(str1[::-1])
print(str1[-1:-7:-1])

#Slicing
website = "www.google.com"
website1 = "www.yahoo.com"
website2 = "www.youtube.com"
slice = slice(4,-4)
print(website[slice])
print(website1[slice])
print(website2[slice])

#Conditional Statement
age=int(input("Enter your age: "))
if age==100:
    print("You are a Century Old!")
elif age>=18:
    print("You are an Adult!")
else:
    print("You are a Minor!")

#Logical Operators
temp=int(input("Enter the temp outside"))

if not(temp>30 and temp<0):
    print("ok")
elif not(temp>20 or temp<0):
    print("not ok")
elif not(temp>100 or temp<0):
    print("all ok")

#Loop Statement
"While Loop"
x=int(input("Enter rating"))
while x>1:
    print("You are a good boy")
    x=x-1
    pass

num=2
while num<=20:
    print(num)
    num+=2

"For Loop"
for x in range(1,11):
    print(x)

for x in range(0,102,2):
    print(x)

num5=10
sum=0
for x in range(1,num5+1):
    sum+=x
print(sum)

#Timer 
import time

for x in range(10,0,-1):
    print(x)
    time.sleep(1)
print("Happy Birthday Piyush")

#Nested Loops
"The inner loop finish all of its iteration before finishing one iteration of the outer loop"

rows=int(input("Enter the number of rows: "))
coloumns=int(input("Enter the number of coloumns: "))
symbol=input("Enter the symbol: ")
for i in range(rows):
    for j in range(coloumns):
        print(symbol,end="")
    print()

#Loop Control Statemnet:
#break: Terminates the loop
#continue: Terminates the current iteration and continues with the next iteration
#pass: Does nothing

"Break"
for x in range(1,11):
    if x==6:
        break
    print(x)

"continue"
for x in range(1,11):
    if x==6:
        continue
    print(x)

"pass"
for x in range(1,11):
    if x==6:
        pass
    print(x)
