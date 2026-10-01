from abc import ABC, abstractmethod


class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 50


# Create objects
restaurant = RestaurantOrder(500)
home_delivery = HomeDeliveryOrder(500)

# Display Restaurant Order
print("Restaurant Order")
print("Food Bill:", restaurant.calculate_bill())
print("Delivery Charge:", restaurant.delivery_charge())
print("Total Bill:", restaurant.calculate_bill() + restaurant.delivery_charge())

print()

# Display Home Delivery Order
print("Home Delivery Order")
print("Food Bill:", home_delivery.calculate_bill())
print("Delivery Charge:", home_delivery.delivery_charge())
print("Total Bill:", home_delivery.calculate_bill() + home_delivery.delivery_charge())