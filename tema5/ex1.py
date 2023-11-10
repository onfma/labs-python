import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def GetArea(self):
        pass
    def GetPerimeter(self):
        pass

class Circle(Shape):
    def __init__(self, raza):
        self.raza = raza
    
    def GetArea(self):
        return math.pi * self.raza**2

    def GetPerimeter(self):
        return 2 * math.pi * self.raza
    
class Rectangle(Shape):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def GetArea(self):
        return self.lungime * self.latime

    def GetPerimeter(self):
        return 2 * (self.lungime + self.latime)
    
class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def GetPerimeter(self):
        return self.l1 + self.l2 + self.l3

    def GetArea(self):
        sp = self.GetPerimeter() / 2
        return math.sqrt(sp * (sp - self.l1) * (sp - self.l2) * (sp - self.l3)) 

circle = Circle(1)
print(f"arie cerc: {circle.GetArea()}")
print(f"perimetru cerc: {circle.GetPerimeter()} \n")

rectangle = Rectangle(2,3)
print(f"arie dreptunchi: {rectangle.GetArea()}")
print(f"perimetru dreptunchi: {rectangle.GetPerimeter()} \n")

traingle = Triangle(3,4,5)
print(f"arie triunghi: {traingle.GetArea()}")
print(f"perimetru triunghi: {traingle.GetPerimeter()}")