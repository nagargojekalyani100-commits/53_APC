# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Overload == operator
    def __eq__(self, other):
        return self.price == other.price

    # Overload > operator
    def __gt__(self, other):
        return self.price > other.price


# Create product objects
product1 = Product("Laptop", 50000)
product2 = Product("Mobile", 30000)

# Compare products
if product1 == product2:
    print("Both products have the same price")
else:
    print("Products have different prices")

if product1 > product2:
    print(product1.name, "is more expensive than", product2.name)