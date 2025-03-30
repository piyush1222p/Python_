# *args:
"A parameter that packs all arguments into a tupple"
"Here we can pass x number of arguments to the function and we can access them in the form of tupple"

def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
    return sum
add(1,2,3,4,5,6,4,8,8,5)

"the args parameter is just name randomly and it follows all the properties of tupple"
"We can change the name of args to any random name as we like to name our tupple"
def pro(*stuff):
    pro=1
    for i in stuff:
        pro*=i
    print(pro)
    return pro
pro(1,2,3,4,5,6,7,8,9,10)

"""def add_1(*args):
    sum=0
    args[0]=0   #the tupple objects are not mutable 
    for i in args:
        sum+=i
    print(sum)
    return sum
add_1(12,23)"""

# **kwargs:
"A parameter that packs all arguments into a dictionary"
"Here we can pass x number of arguments to the function and we can access them by their keys"

def greet(**kwargs):
    print("Hello "+ kwargs["first"]+" "+ kwargs["last"])
    return kwargs
greet(first="John",last="Doe")

def greet(**kwargs):
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
greet(first="John",last="Doe")

def dic(**kwargs):
    print("\nWelcome to the Dictionary")
    for key,value in kwargs.items():
        print(key,":",value)
dic(name="Piyush",last_name="Shukla")

#String format:
name="Piyush"
role="Student"
roll_no=36
age=20
timing=7.23232
print("{} is a 2nd year {} ,his roll-no is {}".format(name,role,roll_no))
print("{} is a 2nd year {} ,his roll-no is {}".format(name,role,roll_no))
print("this is {} working as a {} ,his roll-no is {}".format(name,role,roll_no))
print("this is {} working area of {} so he can work here for {} hours in a week".format(role,name,timing))
print("thanks {} for working here as a {} , So kind of you to work here".format(name,role))
print("Thanks for the work {name} and i am {age} years old".format(name="Piyush",age=20))
print("hello my name is {:10} Nice to meet you ".format(name))
print("hello my name is {:^10} Nice to meet you ".format(name))
print("hello my name is {:>10} Nice to meet you ".format(name))
print("hello my name is {:<10} Nice to meet you ".format(name))
print("The number pi is {:.2f}".format(timing))

number=1000
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:x}".format(number))
print("The number pi is {:X}".format(number))

#Random Module:
import random
print(random.randint(1,100))
x=random.random()
print(x)
y=random.choice([1,2,3,4,5,6,7,8,9,10])
print(y)
cards=[1,2,3,4,5,6,"K","J","Q","A"]
random.shuffle(cards)
print(cards)

#Exception Handling:
"""Exceptions = Events detected during execution that interrupts the flow of a program """
try:
    numerator=int(input("Enter the numerator: "))
    denominator=int(input("Enter the denominator: "))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide the numerator by Zero!")
except Exception as e:
    print(e)
    print("Invalid Input!")
except ValueError as e:
    print(e)
    print("Not a valid input data!")
else:
    print(round(result,3))
finally:
    print("Program has been executed successfully!")

#File detection:
path="E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\test.txt"
path_1="E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\test_1"
import os
if os.path.exists(path):
    print("File exists")
    if os.path.isfile(path):
        print("This is a File")
    if os.path.isdir(path_1):
        print("This is a Directory")
if os.path.exists(path_1):
    print("File exists")
else:
    print("File does not exist")

#Reading a file:
try:    
    with open("E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\test.txt") as File:
        print(File.read())
    print(File.closed)
except FileNotFoundError as e:
    print(e)
    print("File does not exist!")
finally:
    print("File has been processed successfully!")

#Writing a File:
text="Hello World\nThis is Piyush"
with open("Text_1.txt","w") as File:
    File.write(text)
with open("Text_1.txt","a") as File:
    File.write("\nI am a Aspiring Machine learning Engineer")

#Copying a File:
import shutil
# Copy the file from the source to the destination
shutil.copyfile("E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\test.txt","copy.txt")
with open("copy.txt") as E:
    print(E.read())

#Move a File:
import os
# Move the file from the source to the destination
src="E:\\PYTHON\\Text_1.txt"
dst="E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\Text_1.txt"

try:
    if os.path.exists(dst):
        print("The file exist here")
    else:
        os.replace(src,dst)
        print("The File is successfully replaced ")
except:
    print({"The {} doesnot Exist"}.format(src))

#Deleting a File:
"This removes the File from the OS"
import os
# Delete the file from the source
try:    
    path="E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\test.txt"
    os.remove(path)
except FileNotFoundError as E:
    print(E,"The file doesnt exist")

"This will remove the Complete folder and file from it"
import shutil
# Delete the file from the source
try:
    path="E:\\PYTHON\\Python-Self-learning-main\\Complete Python series\\Test_dir"
    shutil.rmtree(path)
except FileExistsError as E:
    print(E)
    print("The path does not exist")
except PermissionError as E:
    print(E)
    print("You dont have the permission to delete the file")
except OSError as E:
    print(E)
    print("The path does not exist")
