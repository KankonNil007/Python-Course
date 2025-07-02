# Method Overriding in Python(OOPs)

from math import pi

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return pi * super().area()
    
a = Shape(4, 5)
b = Circle(3)

print(a.area())
print(b.area())