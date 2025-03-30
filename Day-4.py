#Functions including return:
def sum1(a,b):
    return (a+b)

a=sum1(1,2)
print(a)

def subtract(a,b):
    if a>b:
        return a-b
    else:
        return b-a
b=subtract(1,2)
print(b)

def division(a,b):
    if b ==0:
        print("Unvalid")
    else:
        return a/b
c=division(0,1)
print(c)

def product(a,b):
    return (a*b)
d=product(1,33)
print(d)

def floor_div(a,b):
    if b==0:
        print("Unvalid")
    else:
        return a//b
e=floor_div(1,2)
print(e)

def modulo(a,b):
    if b==0:
        print("Unvalid")
    else:
        return a%b
f=modulo(1,2)
print(f)

#Project_Mating:
def sex(a,b):
    male="male"
    female="female"
    if (a==male and b==female) or (a==female and b==male):
        return "Straight_combination"
    if a==female and b==female:
        return "lesbian_combination"
    else:
        return "GAY"
g=sex("male","female")
print(g)
g=sex("female","female")
print(g)
g=sex("male","male")
print(g)
g=sex("female","male")
print(g)

#Using loops inside the Functions:
n=int(input("Enter the number: "))
i=1
for x in range(1,n+1):
    i*=x
print(i)

def factorial(n):
    i=1
    for x in range(1,n+1):
        i*=x
    print(i)
factorial(5)
factorial(10)

x=int(input("Enter the num: "))
i=1
while x>0:
    i*=x
    x-=1
print(i)

def factorail_1(n):
    i=1
    while n>0:
        i*=n
        n-=1
    print(i)
    return
factorail_1(5)
factorail_1(3)


#Keyword Argument:
"Until we were working on positional argument"
"Here in the keyword argumnet we pass the particular identifier for the respective parameter"
def greeting(first,last,age):
    print(f"Hello, {first} {last} you are {age} years old")
    return
greeting(first="Piyush",last="Shukla",age=20)
greeting(first="Vibhav",last="Shukla",age=8)


#Nested function calls:
"Here we can call the function inside the function"
def greeting(name):
    print(f"hello there {name}")
    def wish(age):
        if (age<=20 and name=="Piyush") or (age>=20 and name=="Piyush"):
            print(f"Wish you a very happy Birthday day {name}")
            print(f"This is your day {name}")
        else:
            print(f"Congrats you are {age} years old")
            print(f"We hope you are fine stranger")
        return
    wish(age=int(input("age: ")))
greeting("Piyush")

#Variable Scope:
"Here we can see the variable scope"

"Global Version"
name=input("Enter your name: ")
def name_1(name):
    print(name)
    return print(f"hello {name}")
print(name)
name_1("Piyush")

"Local Version"
def name_1():
    name="Piyush"
    print(name)
    return print(f"hello {name}")
name_1()
"Here the (name) variabe is accessible becoz assigned as global variable"
"The (name_3) is not accesible becoz of local variable inside the function"
"LEGB=LOCAL ENCLOSING GLOBAL BUILTIN"

