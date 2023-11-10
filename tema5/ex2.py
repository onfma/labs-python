from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal amount exceeds overdraft limit.")
        else:
            super().withdraw(amount)

    def calculate_interest(self):
        print("Checking accounts do not earn interest.")

# Example usage:
savings_account = SavingsAccount(1001, "John Doe", 5000, 0.03)
savings_account.deposit(1000)
savings_account.withdraw(500)
savings_account.calculate_interest()

print("\n")

checking_account = CheckingAccount(2001, "Jane Smith", 2000, 200)
checking_account.deposit(500)
checking_account.withdraw(250)
checking_account.calculate_interest()
