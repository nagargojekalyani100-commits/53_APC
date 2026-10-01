from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


# Distance in kilometers
distance = 100

# Create objects
bus = Bus()
train = Train()
taxi = Taxi()
flight = Flight()

# Display fares
print("Distance:", distance, "km")
print("Bus Fare: ₹", bus.calculate_fare(distance))
print("Train Fare: ₹", train.calculate_fare(distance))
print("Taxi Fare: ₹", taxi.calculate_fare(distance))
print("Flight Fare: ₹", flight.calculate_fare(distance))