# one child inherits from multiple parents.
# A,B -> C

class Walker:
    def walk(self):
        print("I can walk")


class Swimmer:
    def swim(self):
        print("I can swim")


# Child inherits from both
class Duck(Walker, Swimmer):
    def quack(self):
        print("Duck quacks")


d = Duck()

d.walk()
d.swim()
d.quack()