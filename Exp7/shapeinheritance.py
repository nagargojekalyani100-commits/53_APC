import math

class Shape:
    def display_name(self):
        print("This is a shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Create objects
c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Circle Area:", c.calculate_area())
print("Rectangle Area:", r.calculate_area())
print("Triangle Area:", t.calculate_area())