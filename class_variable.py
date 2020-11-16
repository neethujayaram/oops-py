class Person:

   #class variable
   rate=100

   def __init__(self):
       self.rate+=100


p1=Person()
print(p1.rate)