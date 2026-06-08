# inheritance in python
# inheritance allows one class (child/subclass) to 
# reuse attributes and methods of another class (parent/base/super class).

# benefits:
# 1. code reusability
# 3. easier maintenance

# Types of inheritance
# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarical inheritance

# Example
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def sound(self):
        print("Dog woof...")
    
dog = Dog()

dog.eat()
dog.sound()