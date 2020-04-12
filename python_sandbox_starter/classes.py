# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
  #Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  
  def greeting(self):
    return f'My name is {self.name} and my age is {self.age}'

  def is_birthday(self):
    self.age += 1

# Customer Class
class Customer:
  def __init__(self, fname, lname, age, balance):
    self.name = fname + ' ' + lname
    self.age = age
    self.balance = 0
  
  def greeting(self):
    return f'Name is {self.name}, age is {self.age} and balance is {self.balance}'

  def add_balance(self, amount):
    self.balance += self.balance + amount

# Init User Object
dv = User('Deepak Vadithala', 'test@test.com', 39)
gopi = User('Gopi Ravi', 'gopi@jpmchase.com', 41)


# Edit Property
dv.age = 40


# Init Customer Oject
john = Customer('John', 'Doe', 40, 500)
print(john.greeting())
john.add_balance(500)
print(john.greeting())