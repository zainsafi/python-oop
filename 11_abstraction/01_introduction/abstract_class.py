# abstraction in python

# Abstraction is one of the four pillars of OOP.
# It means hiding implementation details and showing only the essential features.

# Real-life example:
# When driving a car, you use steering wheel, brake pedal, accelerator etc
# You don't need to know how the engine works, how fuel burns 
# and how gears operate internally
# The car hides complexity and exposes only the controls you need.

# Python implements abstraction using:
# 1. ABC (Abstract Base Class) from abc module
# 2. @abstractmethod decorator from abc module

# Abstract classes (have atleast one abstract method) act as blueprints.
# They define methods that child classes MUST implement.
# abstract class can't be instantiated.

# A child class must implement all abstract methods inherited
# from an abstract class. Concrete (normal) methods do not need
# to be implemented because they are already inherited and can
# be used directly. However, concrete methods can be overridden
# if custom behavior is needed.

from abc import ABC,abstractmethod

# abstract class
class Vehicle:
    def __init__(self,n):
        self.no_of_tyres = n

    # abstract method
    @abstractmethod 
    def start(self):  
        pass

    def display(self):
        print("Hi i am calling from vehicle class")

