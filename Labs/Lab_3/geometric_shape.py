from math import pi
# from math import sqrt // for triangles
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Geometric_shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def area(self):
        '''Calculate area of object'''
        raise NotImplementedError
    
    @property
    def circumference(self): 
        '''Calculate circumference of object'''
        raise NotImplementedError
        
    def __eq__(self, other):
        '''Check if self is equal to other object'''
        return self.area == other.area and self.circumference == other.circumference
        
    def __lt__(self, other): 
        '''Check if self area is less than other object area of same class'''
        return self.area < other.area
        
    def __gt__(self, other): 
        '''Check if self area is greather than other object area of same class'''
        return self.area > other.area
    
    def __leq__(self, other): 
        ''''''
        self.area <= other.area
        
    def __geq__(self, other):
        ''''''
        return self.area >= other.area
        
    def __repr__(self):
        raise NotImplementedError
        
    def __str__(self):
        raise NotImplementedError
    
    def transpose(self, x, y):
        raise NotImplementedError

    def is_inside(self, x, y):
        raise NotImplementedError
        
        
    
    
    
class Square(Geometric_shape):
    NotImplementedError
    
    
    
    
    
class Cirkle(Geometric_shape):
    NotImplementedError
    