"""print("hello world")

#variables:
name="Piyush"
age=20
print(name,age)

#Data_types:
#1.integers
print(10)
#2.float
print(10.5)
#3.string
print("hello world")
#4.boolean
print(True)
#5.list
list_1=[1,"piyush",20.3,True]
print(list_1)
#6.tuple
tuple_1=("Piyush","Shukla",12,22.3,True)
print(tuple_1)
#7.dictionary
dict_1={
    "name":"Piyush",
    "age":20,
    "city":"lucknow"
}
print(dict_1)
#sets:
set_1={1,2,2,3,2,4,3,5}
print(set_1)"""

"""Methods for data_type"""
"""#1.string
name="Piyush Shukla"
print(name.upper())
print(name.endswith("w"))
print(name.count("h"))
print(name.find("P"))
print(name.replace("P","p"))
"""
"Indesxing"
#String:
"""print(name[0])
print(name[1])
print(name[2])"""
"\n"
"""print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])"""

"""#number:
#1.integers
print(10+20)
print(10-20)
print(10*20)
print(10/20)
print(10%20)
print(10**20)
print(10//20)"""

"conditional statement"
#1.if
#2.elif
#3.else

""""if-elif-else example"
#voting system:
age=int(input("Enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")"""

"Loops"
#1.for loop
#2.while loop

"""#1.for loop
"iteration"
num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)
"""
"""num=range(1,10,2)
for i in num:
    print(i)"""

'''WAP to print the elements of the following list using a loop'''
"""A=[1,4,9,16,36,49,64,81,100]
for i in A:
    print(i)"""

"""B=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,11,2):
    pro=i*i
    print(pro)
"""
'''WAP to print the multiplication of till number n'''
"""n=int(input("Enter the number: "))
for i in range(1,n+1):
    pro=i*i
    print(pro)
"""
"WAP to multiplication table of number n"
"""n=int(input("Enter the number: "))
for i in range(1,11):
    pro=n*i
    print(pro)
"""
#While loop:
"""age=int(input("Enter the age: "))
while age>=18:
    print("you are eligible to vote")
    break
"""
module="pass,break,continue"
#1.pass
#2.break
#3.continue

#1.pass
#pass is a null operation, it does nothing
#it is used to pass the control to the next line of code

"""while age>20:
    pass

while age>20:
    continue
    for i in range(11):
        print(i)

while age>20:
    print("Hello World",age)
    break
"""

'''WAP to search a number x in this tuple using loop'''
"""B=(1,4,9,16,36,49,64,81,100)
store=0
for i in B:
    if i==36:
        print("Found the Number...")
        break
"""
