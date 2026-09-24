class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = Rectangle(10, 5)

print("Length:", r1.length)
print("Breadth:", r1.breadth)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())