"""
    Create a Triangle class and have the following methods in it:
    is valid()
    side_Classification()
    angle_classification()
    Area()
"""
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Is_valid(self):
        if (self.a + self.b > self.c and 
            self.a + self.c > self.b and 
            self.b + self.c > self.a):
            return "valid"
        else:
            return "Invalid"
    
    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isosceles"
        else:
            return "Scalene"
    
    def Angle_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        sides = [self.a, self.b, self.c]
        sides.sort()
        small1, small2, largest = sides[0], sides[1], sides[2]
        
        sum_squares_small = small1**2 + small2**2
        largest_square = largest**2
        
        if sum_squares_small > largest_square:
            return "Acute"
        elif sum_squares_small == largest_square:
            return "Right"
        else:
            return "Obtuse"
    
    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

a = int(input())
b = int(input())
c = int(input())
T = Triangle(a, b, c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
