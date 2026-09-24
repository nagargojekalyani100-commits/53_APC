class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def display_savings(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display_premium(self):
        self.display_savings()
        print("Additional Benefits:", self.benefits)


# Create object
p1 = PremiumSavingsAccount(
    1001,
    50000,
    6,
    "Free ATM, Priority Service"
)

p1.display_premium()