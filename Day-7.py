#Method Overriding:

#   - In Method overiding a child class will be taken in priority and later the parrent class is taken serious.
#   - A child class can override a method of its parent class.
#   - The child class method must have the same name, return type, and parameters as the parent class method.
#   - The child class method can have a different implementation than the parent class method.

class Animal:
    def eat(self):
        print("The animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("The rabbit is eating a carrot")
rabbit_1=Rabbit()
rabbit_1.eat() #The rabbit is eating a carrot

lion=Animal()
lion.eat() #The animal is eating

#Method Chaining:

#   - Method chaining is a technique where we call multiple methods on the same object in a single statement
#   - It is used to make the code more readable and efficient.
#   - You need to add return self at every method to call the multiple calling

class Car:
    def start(self):
        print("The car is started")
        return self
    def Acceleration(self):
        print("The car is accelerating")
        return self
    def Stop(self):
        print("The car is stopped")
        return self

buggati=Car()
buggati.start().Acceleration().Stop() #The car is started The car is accelerating The car

"Also way to do"

ferrari=Car()
ferrari.start()\
    .Acceleration()\
    .Stop()

#Super Function:
#   - The super() function is used to give access to methods and properties of a parent or sibling class.
#   - It returns a proxy object that allows you to call methods of its parent class.
#   - It is used to call the methods of the parent class from the child class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)  #It is used for simplicity for writing same methods in another class and methods
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
    def Volume(self):
        return self.length*self.width*self.height

rectangle=Rectangle(3,4)
square=Square(12,32)
cube=Cube(3,4,5)

print(square.area())
print(cube.Volume())
print(rectangle.area())

#Abstract Class:
#   - An abstract class is a class that is declared with one or more abstract methods.
#   - An abstract method is a method that is declared without an implementation.
#   - It is used to define an interface for other classes to follow.
#   - It actually prevents to create objects from abstract class.
#   - It only allows to create the objects from child class.
#   - It also compels user to override abstract method in a child class(the child class must have the objects which are present in parent class)

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("Car is going")
    def stop(self):
        print("Car is stopped")
class Motorcycle(Vehicle):
    def go(self):
        print("Motorcycle is going")
    def stop(self):
        print("Motorcycle is stopped")

#vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()

#vehicle.go()  #This will give an error because Vehicle class is an abstract class and it does not have any implementation for the method go()
car.go()
motorcycle.go()
motorcycle.stop()

#Object as Argument:
#   - We can pass an object as an argument to a function.
#   - This is useful when we want to perform some operation on an object without knowing the type of the object.
#   - We can use isinstance() function to check the type of the object.

class Car:
    color=None
def change_color(car,color):
    car.color=color

buggati=Car()
porsche=Car()
Maybach=Car()

change_color(buggati,"Red")
change_color(porsche,"Blue")
change_color(Maybach,"Green")
print(buggati.color)  #Red
print(porsche.color)  #None
print(Maybach.color)  #None

#Duck Typing:
#   - In Python, we don't need to declare the type of a variable before using it
#   - We can assign a value of any type to a variable
#   - This is known as duck typing
#   - The idea behind duck typing is "if it walks like a duck and talks like a duck, then it is a duck"
#   - In other words, if an object has the required methods and attributes, then it can be treated as if it were of the required type.

#   - This is a very powerful feature of Python, but it can also lead to bugs if not used carefully.
#   - For example, if we have a function that expects a list as an argument, but we pass a string instead, then the function will fail at runtime.
#   - This is because strings and lists are two different types in Python, and they have different methods and attributes.

class Duck:
    def walk(self):
        print("The Duck is walking")
    def talk(self):
        print("The Duck is talking")
class Chicken:
    def walk(self):
        print("The Chicken is walking")
    def talk(self):
        print("The Chicken is talking")
class Person:
    def walk(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the carrier")
duck=Duck()
chicken=Chicken()
person=Person()
person.walk(chicken)
person.walk(duck)  
#The Duck is walking
#The Duck is talking
#You caught the carrier
