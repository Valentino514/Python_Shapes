import math
from Shape import Shape


class Circle (Shape): # circle class

    def __init__(self, radius): # constructor
        super().__init__()
        self.radius = radius

    def perimeter(self): #perimeter
        return round((2*math.pi*self.radius),5)
    
    def area(self): #area
        return round((math.pi * self.radius **2),5)

    def __eq__(self, other): #equals method (overriden)
        return isinstance(other, Circle) and self.radius == other.radius
        
    def __hash__(self): #hash (overriden)
        return hash((self.radius))
    
    def attributes(self): #attributes 
        return f"{self.__class__.__name__.lower()} {self.radius}"
    
