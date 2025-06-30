# Shape Area Calculator

# Topics: Inheritance, Method Overriding

# 📝 Task:
# Create a base class Shape with method area().
# Then create child classes:

# Circle(radius) → area = πr²

# Rectangle(length, width) → area = lw

# Square(side) → inherits from Rectangle

from math import pi

class Circle:
    def area1(self, radius):
        area = pi * radius * radius
        return area
    
class Rectangle:
    def area2(self, length, width):
        area = length * width
        return area
    
class Square:
    def area3(self, side):
        area = side * side
        return area
    
a = Square()
b = Rectangle()
c = Circle()
    
inpShape = input("Enter desired Shape(square/rectangle/square): ")
inpShape = inpShape.capitalize()

if (inpShape == "Square"):
    inpSide = int(input("Enter Side: "))

    print(f"The Area of the Square: {a.area3(inpSide)}")
elif (inpShape == "Rectangle"):
    inpLen = int(input("Enter Length: "))
    inpWid = int(input("Enter Width: "))

    print(f"The Area of the Rectangle: {b.area2(inpLen, inpWid)}")
elif (inpShape == "Circle"):
    inpRad = int(input("Enter Radius: "))

    print(f"The Area of the Circle: {c.area1(inpRad)}")