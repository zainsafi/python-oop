# polymorphism in python
# polymorphism means: many forms
# Polymorphism is an OOP concept that allows
# different objects to respond differently
# to the same method call.

# It is achieved in Python mainly through:
# 1. Duck Typing
# 2. Method Overriding
# 3. Operator Overloading
# 4. method overloading (not support in python) 
# instead python uses *args which mimics method overloading

# In polymorphism the behaviour depends depends upon the 
# arguments which we are passing

# Forexample
# print() built-in function
print("print() function")
print(5)
print(5 + 2)
print("5" + "2")
# Each behaves differently

# similarly len function
print("\nlen() function")
print(len("zain")) # 4
list1 = ["zain",2] 
print(len(list1)) # 2

