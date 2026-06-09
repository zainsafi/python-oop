# method overriding means redefining a parent method
# inside the child class.

class Animal:
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print(f"Animal {self.name} makes sound")
    
class Dog(Animal):
    bark = 'woof woof woof ...'
    def sound(self):
        print(f"Dog {self.name} makes sound {self.bark}")

jack = Dog("jack")
# child method executes instead of parent version
jack.sound() # Dog jack makes sound woof woof woof ...