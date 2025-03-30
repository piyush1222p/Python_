print("Hello World!")
print("This world is full of warriors and cowards too!")

#Variables in Python 
"Introducing String data-type"
first_name = "Piyush"

print(first_name)

"Merging one or more variables with string"
print("My name is "+first_name+" and i am 20 years old")

"Also to know the data-type of the variable use of type function"
print(type(first_name))

"Combining two or more variable in a string"
last_name = "Shukla"
Full_name = first_name +" "+last_name
print(Full_name)

"Introducing Integer data-type"
age = 20
print(age)

print(type(age))

"""Using assignment Operator to perform some task"""
age = age + 1
print(age)

age-=1
print(age)

"""Concatenation can only happen between same type of data-type"""
age = 20
print(age+age)
print("My age is "+str(age))

"Introduciing the float data-type"
height = 162.34
print(height)
print(type(height))
print("Your height is "+str(height)+" cm")

"Introducing the boolean data-type"
is_adult = True
print(is_adult)
print("Are you a human: "+str(is_adult))
print(type(is_adult))

#Multiple assignment in Python
name="piyush"
age=20
attractive=True
print(name,age,attractive)
"""Alternative way to print the multiple lines of code in one line is"""
name,age,attractive="Piyush",21,True

"""Now the above program is efficient and spaced saver"""
print(name,age,attractive)

#String methods
name="piyush"
print(len(name))

print(name.find("P"))
print(name.find("i"))
print(name.find("y"))

print(name.capitalize())

print(name.upper())

print(name.lower())

print(name.isdigit())

print(name.isalpha())

print(name.count("p"))

print(name.replace("i","e"))

print(name*10)

#Type-casting
x=1
y=2.8
z="Piyush"
print(type(x))
print(type(y))
print(type(z))

"""Performing the type casting in the variables"""
x=str(x)
y=int(y)
print(type(x))
print(type(y))
print(type(z))

"""We cannot convert the string into float value"""
#print(float(z))

#User_input

name=input("Enter your name: ")
print("Hello",name)

age= int(input("Enter your age: "))
print("Your age is",age)

height= float(input("Enter your height: "))
print("Your height is",height,"cm")

#Maths functions

from math import pi 
import math
x=1
y=2
z=3

print(round(pi))

print(math.ceil(pi))

print(math.floor(pi))

print(abs(pi))

print(pow(pi,2))

print(math.sqrt(pi))

print(max(x,y,z))

print(min(x,y,z))
