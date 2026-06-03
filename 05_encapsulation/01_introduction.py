# Encapsulation in python

# OOP (Object-Oriented Programming) is a programming paradigm
# where code is organized into classes and objects.

# There are four main pillars of OOP:
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

# Encapsulation: means bundling the data (attributes) and the methods (functions) 
# that operate on that data into a single unit (a class), while restricting 
# direct access to some of the object's components
# In simple Encapsulation is an oop concept in which data (attributes) and methods 
# are combined in a single unit (class), and access to that data is controlled 
# using access specifiers like public, protected, and private.

# Example
class Wallet:
   def __init__(self):
       self.__balance = 0 # Private attribute

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount # Remove from the balance safely

   def get_balance(self):
       return self.__balance

acct_one = Wallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds