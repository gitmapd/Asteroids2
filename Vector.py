import math
import numpy as np

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self,other):
        if isinstance(other,Vector):
            return (self.x * other.x, self.y * other.y)
        if isinstance(other,(float,int)):
            return (self.x * other,self.y * other)

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)

    def dot(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return x+y


