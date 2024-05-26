class BankAccount:
  def __init__(self, account_number, account_holder,balance = 0.0):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited {amount}. New balance: {self.balance}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount > 0 and self.balance >= amount:
      self.balance -= amount
      print(f"Withdraw {amount}. New balance: {self.balance}")
    else:
      print("error")

  def get_balance(self):
    return self.balance

  def __str__(self):
    s=self.account_number+" " +self.account_holder+ " "+str(self.balance)
    return s

class SavingsAccount(BankAccount):
  def __init__(self, account_number, account_holder, interest_rate,balance = 0.0):
    super().__init__(account_number, account_holder)
    self.interest_rate = interest_rate

  def apply_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Apply interest  {interest}  %%%% New balance: {self.balance}")

  def __str__(self):
    s = self.account_number + " " + self.account_holder + " " + str(self.balance)+ " " +str(self.interest_rate)+"%"
    return s

Nawal = BankAccount("2377", " نوال سهيل اسماعيل")
Nawal.deposit(1000)
Nawal.withdraw(500)
print(Nawal)
savings_account = SavingsAccount("2377", "نوال سهيل اسماعيل", 0.1)
savings_account.deposit(100)
savings_account.apply_interest()
print(savings_account)
