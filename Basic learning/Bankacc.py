class BankAccount:
    def __init__(self, accountnum, balance):
        self.accountnum = accountnum
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited Rs.{amount}. Current balance: Rs.{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"💸 Withdrawn Rs.{amount}. Current balance: Rs.{self.balance}")
        else:
            print("⚠️ Insufficient balance.")


# ---- main program ----
a = input("Enter your account number: ")
b = int(input("Enter your initial balance: "))

obj = BankAccount(a, b)

# ask user for deposit and withdraw amount
dep_amount = int(input("Enter amount to deposit: "))
obj.deposit(dep_amount)

with_amount = int(input("Enter amount to withdraw: "))
obj.withdraw(with_amount)
