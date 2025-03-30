#Class and Objects:
#A class is a blueprint or a template that defines the properties and behavior of an object.
#An object is an instance of a class and has its own set of attributes (data) and
#methods (functions) that can be used to manipulate the object.

class Car:
    def __init__(self,Color,Model,Engine):
        self.Color=Color
        self.Model=Model
        self.Engine=Engine
    def start(self):
        print("The " +self.Model+ " is Moving")
    def Stop(self):
        print("The " +self.Model+ " is stopped")

BMW=Car("Light Blue","M5","Petrol_Cng")
print(BMW.Model)
print(BMW.Engine)
print(BMW.Color)
print(BMW.start())
print(BMW.Stop())

#Class Varirables:
#Class variables are variables that are shared by all instances of a class.
#Instance Variable are those on which class attributes are assigned.

class Home:
    concrete="Ambuja Cement"    #Class Variable
    district="Greater Noida"    #Class Variable

    def __init__(self,area,Windows,Ventilation):
        self.area=int(area)  #Instance Variable
        self.Windows=Windows    #Instance Variable
        self.Ventilation=Ventilation    #Instance Variable
    def Material(self):
        print("This Home is built of "+self.concrete)
    def Locality(self):
        print("This Home is located in "+self.district)
    
Piyush=Home(1440*1440,"French Window","Split-Aircondition")
print(Piyush.concrete)
print(Piyush.area)
print(Piyush.Windows)
print(Piyush.Ventilation)
print(Piyush.district)
print(Piyush.Material())
print(Piyush.Locality())

#Inheritance in  Class:
#There can be two type of classes one is Parent and other is Child class
#Child class will inherit all the properties aka attributes and methods of parent class.
#Inheritance is used to create a new class from an existing class.

class Animal:
    def alive():
        print("The animal is alive")
    def eat():
        print("The animal is eating")
class Hawk(Animal):
    def fly():
        print("The Hawk is flying")
    def Smart():
        print("The Hawk is very smart")
class Lion(Animal):
    def roar():
        print("The Lion is roaring")
    def King():
        print("The Lion is the king of Jungle")

print(Lion.alive())
print(Lion.eat())
print(Lion.roar())
print(Hawk.alive())
print(Hawk.Smart())
print(Hawk.fly())

#Multi-level Inheritance in Class:
#In multi-level inheritance, a child class inherits the properties and methods of a parent class and the
#parent class also inherits the properties and methods of another parent class.

class Organism:
    def eat(self):
        print("The organism is eating")
    def sleep(self):
        print("The organism is sleeping")
class Animal(Organism):
    def raw_food(self):
        print("The animal is eating raw food")
    def hunting(self):
        print(f"The animal is hunting")
class Dog(Animal):
    def bark(self):
        print("The dog is barking")
    def Loyal(self):
        print("This Dog is loyal to have")

rottweiler=Dog()
print(rottweiler.eat())
print(rottweiler.raw_food())
print(rottweiler.Loyal())

#Multiple Inheritance in Class:
#In multiple inheritance, a child class inherits the properties and methods of multiple parent classes.

class prey:
    def eat(self):
        print("The prey is eating")
class predator:
    def hunt(self):
        print("The predator is hunting")
class Fish(prey,predator):
    def swim(self):
        print("The fish is swimming")
    def cute(self):
        print("The fish is cute")

fish=Fish()
Prey=prey()
print(fish.hunt())
print(Prey.eat())
print(fish.swim())
