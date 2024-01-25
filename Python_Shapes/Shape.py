class Shape: #shape class (parent of all th shapes)
    currentId = 1  #id 

    def __init__(self):
        self.id = Shape.currentId 
        Shape.currentId += 1  #increment id after every shape
    
    def print(self): #print method 
        return f"{self.id}:{self.__class__.__name__}, perimeter: {self.perimeter()}, area: {self.area()}"


    def perimeter(self): #perimeter
        return None
    
    def area(self): #area 
        return None
    
    def __eq__(self, other): #equals method
        return isinstance(other, Shape)
     
    def __hash__(self): #equals method
        return hash(type(self))
    
    def attributes(self): #attributes 
         return f"{self.__class__.__name__.lower()}"
     
    def __str__(self): #string method 
        return f""
    
    
