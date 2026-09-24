import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c1 = Circle(5)

print("Radius:", c1.radius)
print("Area:", c1.area())
print("Circumference:", c1.circumference())