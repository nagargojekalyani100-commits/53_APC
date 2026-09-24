class ShoppingCart:
    # Constructor
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    # Add product
    def add_product(self, product_name, price):
        self.products.append([product_name, price])
        print(product_name, "added to cart.")

    # Remove product
    def remove_product(self, product_name):
        for product in self.products:
            if product[0] == product_name:
                self.products.remove(product)
                print(product_name, "removed from cart.")
                return

        print(product_name, "not found in cart.")

    # Calculate total bill
    def calculate_total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        return total

    # Destructor
    def __del__(self):
        print("Shopping cart object is destroyed.")


#  object
cart = ShoppingCart("Kalyani", 101)

# Add products
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)


cart.remove_product("Mouse")


print("Customer Name:", cart.customer_name)
print("Cart ID:", cart.cart_id)
print("Total Bill:", cart.calculate_total_bill())