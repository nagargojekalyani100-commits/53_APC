class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def display_account_details(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# Create object
a1 = ATM(1001, "Kalyani", 10000)

# Menu-driven program
while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a1.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        a1.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        a1.withdraw(amount)

    elif choice == 4:
        a1.display_account_details()

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")