class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance


account = BankAccount("1001", 5000, "2026-09-05", "John")
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())
