# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting")


# Car class
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


# Bike class
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


# Bus class
class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


# Create objects
car = Car()
bike = Bike()
bus = Bus()

# Runtime polymorphism
vehicles = [car, bike, bus]

for vehicle in vehicles:
    vehicle.start()