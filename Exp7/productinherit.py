class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self, discount):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Discount:", discount, "%")
        print("Final Price:", self.final_price(discount))


# Create object
p1 = ElectronicProduct(
    101,
    "Laptop",
    50000,
    "Dell",
    2
)

p1.display(10)