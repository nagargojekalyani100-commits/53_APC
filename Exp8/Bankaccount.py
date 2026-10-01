# Base class
class BankAccount:
    def calculate_interest(self, amount):
        print("Calculating interest")


# Savings Account
class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        rate = 4
        return amount * rate / 100


# Current Account
class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        rate = 2
        return amount * rate / 100


# Fixed Deposit Account
class FixedDepositAccount(BankAccount):
    def calculate_interest(self, amount):
        rate = 7
        return amount * rate / 100


# Create objects
savings = SavingsAccount()
current = CurrentAccount()
fixed_deposit = FixedDepositAccount()

# Runtime polymorphism
accounts = [
    (savings, 10000),
    (current, 10000),
    (fixed_deposit, 10000)
]

for account, amount in accounts:
    print("Interest:", account.calculate_interest(amount))