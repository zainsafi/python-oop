# One parent, many children
# A -> B, A -> C
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.speak()
d.bark()

c.speak()
c.meow()