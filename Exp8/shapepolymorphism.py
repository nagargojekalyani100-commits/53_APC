import math

# Base class
class Shape:
    def area(self):
        print("Area of shape")


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Derived class - Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Create objects
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

# Runtime polymorphism
shapes = [circle, rectangle, triangle]

for shape in shapes:
    print("Area =", shape.area())