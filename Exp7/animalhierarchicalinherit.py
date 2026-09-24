class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")

    def behavior(self):
        print("Dog is loyal and friendly.")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")

    def behavior(self):
        print("Cat is calm and playful.")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo Moo")

    def behavior(self):
        print("Cow is gentle and peaceful.")


# Create objects
d = Dog("Tommy", 3)
c = Cat("Kitty", 2)
w = Cow("Gauri", 5)

print("----- Dog -----")
d.display()
d.sound()
d.behavior()

print("\n----- Cat -----")
c.display()
c.sound()
c.behavior()

print("\n----- Cow -----")
w.display()
w.sound()
w.behavior()