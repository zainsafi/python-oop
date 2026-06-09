# Parent Class 1
class Walker:

    def walk(self):
        return "I can walk on land"


# Parent Class 2
class Swimmer:

    def swim(self):
        return "I can swim in water"


# Child inherits from BOTH Walker and Swimmer
class Amphibian(Walker, Swimmer):

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return (
            f"I'm {self.name} the frog. "
            f"{self.walk()} and {self.swim()}."
        )


frog = Amphibian("Freddy")

print(frog.introduce())

# Output:
# I'm Freddy the frog.
# I can walk on land and I can swim in water.

