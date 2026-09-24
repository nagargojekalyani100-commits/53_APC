class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        final_price = self.price - (self.price * discount / 100)
        return final_price


m1 = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)

m1.display_specifications()

discount = 10
print("Price after discount:", m1.price_after_discount(discount))