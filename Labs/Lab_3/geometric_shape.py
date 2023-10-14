from math import pi
# from math import sqrt // for triangles
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Geometric_shape:
    
    def area(self):
        '''Calculate area of object'''
        raise NotImplementedError
    
    def circumference(self): 
        '''Calculate circumference of object'''
        raise NotImplementedError
        
    def __eq__(self, other):
        '''Check if self is equal to other object'''
        if self.area() == other.area() and self.circumference() == other.circumference():
            return True
        else:
            return False

        
    def __lt__(self, other): 
        '''Check if self area is less than other object area of same class'''
        raise NotImplementedError
        
    def __gt__(self, other): 
        '''Check if self area is greather than other object area of same class'''
        raise NotImplementedError
    
    def __leq__(self, other): 
        ''''''
        raise NotImplementedError
        
    def __geq__(self, other):
        ''''''
        raise NotImplementedError
        
    def __repr__():
        NotImplementedError
        
    def __str__():
        
    def transpose(self, x, y):
        NotImplementedError
           
    def is_inside(self, x, y):
        NotImplementedError
        
        
    
    
    
class Square(Geometric_shape):
    NotImplementedError
    
    
    
    
    
class Cirkle(Geometric_shape):
    NotImplementedError
    