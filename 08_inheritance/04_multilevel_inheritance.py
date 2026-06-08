# Chain inheritance (grandparent → parent → child)
# A -> B -> C

class Animal:
    def eat(self):
        print("Eating...")


class Mammal(Animal):
    def walk(self):
        print("Walking...")


class Dog(Mammal):
    def bark(self):
        print("Barking...")


d = Dog()

d.eat()   # from Animal
d.walk()  # from Mammal
d.bark()  # from Dog