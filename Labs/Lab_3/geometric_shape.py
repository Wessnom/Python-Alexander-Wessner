from math import pi

class Geometric_shape:
    '''Represents a general geometric shape with a center position (x, y).'''

    def __init__(self, x, y):
        '''Initializes a geometric shape with a given center position.'''
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
        '''Check if self area is less than other object area of same class.'''
        return self.area < other.area
        
    def __gt__(self, other): 
        '''Check if self area is greather than other object area of same class.'''
        return self.area > other.area
    
    def __leq__(self, other): 
        '''Check if self area is lesser than or equal to the other object of same class.'''
        self.area <= other.area
        
    def __geq__(self, other):
        '''Check if self area is greather than or equal to the other object of the same class.'''
        return self.area >= other.area
        
    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
        
    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y}) with area {self.area} and circumference {self.circumference}"
    
    def transpose(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise ValueError("Translation values must be numbers.")
        self.x += dx
        self.y += dy

    def is_inside(self, x, y):
        '''Checks if a point (x, y) is inside the geometric shape or on the perimeter.'''
        raise NotImplementedError
        
        
class Circle(Geometric_shape):
    '''Represents a circle with a center position and a radius.'''

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        
    def __repr__(self):
        '''Returns a string representation of the circle object. '''
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self):
        '''Returns a string representation of the circle object describing its center and radius.'''
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"

    @property
    def area(self):
        return pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * pi * self.radius
    
    def is_inside(self, x, y):
        distance = ((x - self.x)**2 + (y - self.y)**2)**0.5  # calculate the distance from the point to the center of the circle
        return distance <= self.radius  # return True if the distance is less than or equal to the radius, else return False

    def is_unit(self):
        return self.radius == 1 and self.x == 0 and self.y == 0 # Enligt lab instruktioner ser det ut som en enhetscirkel endast ska utgå från Origo.
    
    
class Rectangle(Geometric_shape):
    '''Represents a rectangle with a center position and two sides (side1, side2).'''

    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        
    def __repr__(self):
        '''Returns a string representation of the rectangle object.'''
        return f"Rectangle(x={self.x}, y={self.y}, side1={self.side1}, side2={self.side2})"
    
    def __str__(self):
        '''Returns a string representation of the rectangle describing its center and sides.'''
        return f"Rectangle with center at ({self.x}, {self.y}) and sides of length {self.side1} and {self.side2}"

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def circumference(self):
        return 2 * (self.side1 + self.side2)
    
    def is_inside(self, x, y):
        half_width = self.side1 / 2
        half_height = self.side2 /2
        return self.x - half_width <= x <= self.x + half_width and self.y - half_height <= y <= self.y + half_height
    
    def is_square(self):
        return self.side1 == self.side2
    
