class BankAccount:
   def __init__(self, name, balance=0):
      self.name=name
      self.balance=balance

   def display(self):
      print("Name is",self.name)
      print("Balance is",self.balance)

   def with_draw(self, amount):
      self.balance-=amount

   def deposit(self, amount):
      self.balance+=amount

# ba=BankAccount("Neethu")
ba=BankAccount("xxxx",2000)
ba.deposit(10000)
ba.with_draw(500)
ba.display()