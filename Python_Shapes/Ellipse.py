import math
from Shape import Shape


class Ellipse (Shape): # ellipse class

    def __init__(self, a, b): #constructor
        super().__init__()
        self.a = a
        self.b = b
    
    def area(self): #area
        return round((math.pi*self.a*self.b),5)
    
    def eccentricity(self): #eccentricity
        if(self.a>self.b): 
            return round((math.sqrt((self.a**2) - (self.b**2))),5)
        elif(self.a<self.b):
            return round((math.sqrt((self.b**2) -(self.a**2))), 5)
        else:
            return None
        
    def __eq__(self, other): #equals method overriden
        return isinstance(other, Ellipse) and self.a == other.a and self.b == other.b

    def __hash__(self):#hash function overriden
        return hash((self.a,self.b))
    
    def attributes(self): #attributes of the shape
         return f"{self.__class__.__name__.lower()} {self.a} {self.b}"
     
    def __str__(self): #string method overriden
        return f"linear eccentricity: {self.eccentricity()}"