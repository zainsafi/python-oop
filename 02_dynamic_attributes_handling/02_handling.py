# Dynamic object attribute handling means Accessing, creating, updating, or deleting 
# object attributes dynamically at runtime using special built-in functions e.g 
# 1. getattr() -> get/read attribute dynamically
# 2. setattr() -> create/update attribute dynamically
# 3. hasattr() -> check if attribute exists
# 4. delattr() -> delete/remove attribute dynamically
# 5. dir()     -> list all attributes and methods of an object

# simple class
class Person:

    # initializer method automatically runs when object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John Doe", 30)


# getattr()
# used to access attributes dynamically
# useful when attribute name comes from user input,
# file, configuration, etc.
# syntax: getattr(object, attribute_name, default_value)

print("Name ->", getattr(person, "name"))
print("Age ->", getattr(person, "age"))

# if attribute does not exist, default value is returned
print("City ->", getattr(person, "city", "Milano"))


# dynamic attribute access using variable
attribute_name = "name"
print("Dynamic access ->", getattr(person, attribute_name))
attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))



# dir()
# returns all attributes & methods of an object
print("\nAll attributes & methods:")
print(dir(person))

# printing only custom attributes
# skipping dunder methods (__init__, __str__, etc.)
print("\nCustom attributes only:")
for attr in dir(person):
    # skip dunder methods & functions/methods
    if not attr.startswith("__") and not callable(getattr(person, attr)):
        print(f"{attr} -> {getattr(person, attr)}")
        # In the loop above, callable() is a built-in function that returns True 
        # if the object passed to it can be called like a function or method



# setattr()
# syntax: setattr(object, attribute_name, value)

# adding new attribute dynamically
setattr(person, "city", "New York")

print("\nNew attribute added dynamically:")
print("City ->", person.city)

# updating existing attribute dynamically
setattr(person, "age", 35)
print("Updated age ->", person.age)


# hasattr()
# syntax: hasattr(object, attribute_name)

print("\nChecking attributes:")
print("Has name? ->", hasattr(person, "name"))
print("Has salary? ->", hasattr(person, "salary"))


# practical example using hasattr()
required_attributes = ["name", "age", "email"]

for attr in required_attributes:
    if hasattr(person, attr):
        print(f"{attr} exists -> {getattr(person, attr)}")
    else:
        print(f"{attr} does not exist")


# delattr()
# syntax: delattr(object, attribute_name)
# deleting city attribute
delattr(person, "city")
print("\nAfter deleting city attribute:")
print("Has city? ->", hasattr(person, "city"))

