class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully.")

    def calculate_rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate per Day:", self.rental_rate)
        print("Available:", self.availability)


# Create object
v1 = Vehicle("MH12AB1234", "Swift", 1500, True)

v1.display()

v1.rent_vehicle()

days = 3
print("Rental Charges for", days, "days:", v1.calculate_rental_charges(days))

v1.return_vehicle()