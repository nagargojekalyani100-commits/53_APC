class FoodOrder:
    # Constructor
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    # Calculate total bill including 5% tax
    def calculate_total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax
        return total

    # Destructor
    def __del__(self):
        print("Order completed successfully.")


# Create object
order = FoodOrder(101, "Kalyani", "Pizza", 2, 300)

print("Order ID:", order.order_id)
print("Customer Name:", order.customer_name)
print("Food Item:", order.food_item)
print("Quantity:", order.quantity)
print("Price per Item:", order.price)

print("Total Bill including Tax:", order.calculate_total_bill())