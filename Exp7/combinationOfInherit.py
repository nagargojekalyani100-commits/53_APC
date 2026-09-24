class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_car(self):
        self.display_vehicle()
        print("Number of Doors:", self.doors)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.display_vehicle()
        print("Engine:", self.engine_cc, "cc")


class SportsCar(Car):
    def __init__(self, brand, model, doors, top_speed):
        super().__init__(brand, model, doors)
        self.top_speed = top_speed

    def display_sports_car(self):
        self.display_car()
        print("Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine_cc, battery):
        super().__init__(brand, model, engine_cc)
        self.battery = battery

    def display_electric_bike(self):
        self.display_bike()
        print("Battery:", self.battery, "kWh")


# Create SportsCar object
car = SportsCar("BMW", "M4", 2, 280)

# Create ElectricBike object
bike = ElectricBike("Ola", "S1 Pro", 0, 4)

print("----- Sports Car -----")
car.display_sports_car()

print("\n----- Electric Bike -----")
bike.display_electric_bike()