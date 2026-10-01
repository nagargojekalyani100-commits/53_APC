class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo Moo")



class Lion(Animal):
    def sound(self):
        print("Lion says: Roar Roar")


# Create objects
dog = Dog()
cat = Cat()
cow = Cow()
lion = Lion()

# Runtime polymorphism
animals = [dog, cat, cow, lion]

for animal in animals:
    animal.sound()