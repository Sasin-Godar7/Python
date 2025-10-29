class BankAccount:
    def __init__(self,balance,accountnum):
        self.accountnum = accountnum
        self.balance = balance

    def deposit(self,amount):
     if self.accountnum:
        self.balance += amount
        print(f"Your current balance is {self.balance}")
     else:
        print("Failed to deposit the amount")   
   
    def withdraw(self,amount):
       if self.balance > 0:
          self.balance -=amount
          print(f"Your current balance is {self.balance}")
       else:
          print("insufficeint amount")
            
    
        



b = int(input("Enter the balance: "))
a = input("Enter the account number: ")
amount = 2000
obj = BankAccount(a,b)
obj.deposit(amount)
obj.withdraw(amount)

