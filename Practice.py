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