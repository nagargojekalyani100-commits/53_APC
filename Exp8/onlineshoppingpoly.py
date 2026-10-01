# Base class
class Payment:
    def make_payment(self, amount):
        print("Making payment")


# UPI Payment
class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Payment of ₹", amount, "made using UPI")


# Card Payment
class CardPayment(Payment):
    def make_payment(self, amount):
        print("Payment of ₹", amount, "made using Card")


# Wallet Payment
class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Payment of ₹", amount, "made using Wallet")


# Common function
def process_payment(payment, amount):
    payment.make_payment(amount)


# Create objects
upi = UPIPayment()
card = CardPayment()
wallet = WalletPayment()

# Demonstrate polymorphism
process_payment(upi, 1000)
process_payment(card, 2000)
process_payment(wallet, 1500)