# Dynamic Attributes in Python

# A dynamic attribute is an attribute that is added, modified, or removed
# from an object while the program is running.

# Normally attributes are created inside __init__():
class Person:
    def __init__(self, name):
        self.name = name

# Example of Dynamic Attribute
class Car:
    pass


my_car = Car()

# Dynamically adding attributes
my_car.brand = "Toyota"
my_car.model = "Corolla"

print(my_car.brand) # Toyota
print(my_car.model) # Corolla

# Dynamic Attribute Deletion
class Student:
    pass

s1 = Student()

s1.age = 20
print(s1.age)

del s1.age
# print(s1.age)  -> AttributeError
