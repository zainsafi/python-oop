# In Python, access specifiers are used to control the visibility and
# accessibility of class members (variables and methods).

# Unlike languages such as Java or C++, Python does not have strict
# access modifiers. Instead, it follows a naming convention.

# There are three types of access specifiers in Python:
# 1. Public
# 2. Protected
# 3. Private


# public access specifier
# Members are accessible from anywhere (inside or outside the class).
# By default, all class members in Python are public.


# protected access specifier
# Defined using a single underscore (_variable)
# It indicates that the variable is intended for internal use
# and for use in subclasses.
# However, it can still be accessed outside the class (not strictly enforced).


# private access specifier
# Defined using double underscore (__variable)
# It cannot be accessed directly outside the class.
# Python applies name mangling to make it harder to access,
# by internally changing the name to _ClassName__variable.


class Student:
    def __init__(self, name, age, marks):
        self.name = name # public attribute
        self._age = age # protected attribute
        self.__marks = marks # private attribute

    # Method to display all data inside the class
    def display(self):
        print("\nInside Class Method")
        print("Name (Public):", self.name)
        print("Age (Protected):", self._age)
        print("Marks (Private):", self.__marks)


# Child class inheriting Student
class Child(Student):
    def show(self):
        print("\n--- Inside Child Class ---")
        # Public variable is fully accessible
        print("Public Name:", self.name)
        # Protected variable is accessible in subclass
        print("Protected Age:", self._age)
        # Private variable is NOT directly accessible
        # print(self.__marks)  # This will cause an error


s1 = Child("Ali", 20, 95)

print("\nOutside Class Access")
# Public variable: accessible anywhere
print("Public:", s1.name)

# Protected variable: accessible but NOT recommended
print("Protected:", s1._age)

# Private variable: direct access NOT allowed
# print(s1.__marks)  # This will cause AttributeError
# but we can still access it using name mangling (not recommended)
print("\nName Mangling")
print("Private Marks:", s1._Student__marks)

# access through class method
s1.display()

# access through child class method
s1.show()

