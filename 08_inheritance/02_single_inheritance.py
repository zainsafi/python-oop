# single inheritance
# one parent → one child

# Parent Class (Base Class)
class Animal:

    # Parent constructor
    def __init__(self, name):
        self.name = name

    # Parent method
    def sound(self):
        return f"{self.name} makes a sound"


# Child Class
# Dog inherits everything from Animal
class Dog(Animal):

    # Class attribute
    bark = "woof! woof!! woof!!!"


# Creating object of child class
jack = Dog("Jack")

# Dog object can access parent method
print(jack.sound())   # Jack makes a sound

# Dog object can access its own attribute
print(jack.bark)      # woof! woof!! woof!!!