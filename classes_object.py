class Person:
   def __init__(self, name, age):
      self.name=name
      self.age=age
   
   def person_name(self):
      print("I am, ", self.name)
   
   def person_age(self):
      self.person_name()
      if self.age>=60:
         print(f"My Age is {self.age}, so i am in high risk category.")
      else:
         print("Age is less than 60.")
   
p1=Person("xxxx",66)
p2=Person("yyyy",60)

p1.person_age()
p2.person_age()