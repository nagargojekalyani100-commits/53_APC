from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike is started")

    def stop(self):
        print("Bike is stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus is started")

    def stop(self):
        print("Bus is stopped")


# Create objects
car = Car()
bike = Bike()
bus = Bus()

# Call methods
car.start()
car.stop()

bike.start()
bike.stop()

bus.start()
bus.stop()