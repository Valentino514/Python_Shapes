import math
from Shape import Shape


class Rhombus(Shape): #rhombus class

    def __init__(self, p,q): #constructor
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self): #perimeter
     return round(2*math.sqrt((self.p**2+self.q**2)), 5) #equation


    def area(self): #area
        return round(((self.p*self.q)/2),5) #equation
    
    def side(self): #side 
        return round((math.sqrt(self.p**2+self.q**2)/2),5) #equation
    
    def inradius(self): #inradius
        try:
         inRadius = self.p*self.q/(2*math.sqrt(self.p**2+self.q**2))
         return round(inRadius,5)
        except ZeroDivisionError:# in case we divide by 0
            return None

    def __eq__(self, other): #equals method
        return isinstance(other, Rhombus) and self.p == other.p and self.q == other.q   
    
    def __hash__(self):#hash method
        return hash((self.p,self.q))
    
    def attributes(self):#attributes
        return f"{self.__class__.__name__.lower()} {self.p} {self.q}"
    
    def __str__(self):#string method
        return f"in-radius: {self.inradius()}, side: {self.side()}"