from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited in Savings Account:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn from Savings Account:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited in Current Account:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn from Current Account:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


# Create objects
savings = SavingsAccount(10000)
current = CurrentAccount(20000)

# Savings Account operations
savings.deposit(5000)
savings.withdraw(3000)

print()

# Current Account operations
current.deposit(5000)
current.withdraw(4000)