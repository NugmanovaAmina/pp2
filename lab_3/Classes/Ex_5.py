class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self):
        amount_of_deposit = float(input("Enter the value to deposit: "))
        if amount_of_deposit < 0:
            return self.deposit()
        self.balance += amount_of_deposit
        print(f"Your balance = {self.balance}")

    def withdraw(self):
        amount_of_withdraw = float(input("Enter the amount of withdraw: "))
        if 0 > amount_of_withdraw:
            return self.withdraw()
        if amount_of_withdraw > self.balance:
            return self.withdraw()
        self.balance -= amount_of_withdraw
        print(f"Your balance = {self.balance}")

account_use = Account("Amina")
account_use.deposit()
account_use.withdraw()