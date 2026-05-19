# another example
class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def bark(self):

        print(
            f'{self.name.upper()} says woof woof! '
            f"I am {self.age} years old!"
        )


# creating dog objects
dog_1 = Dog('Jack', 3)
dog_2 = Dog('Thatcher', 5)

print('\n----- DOG OBJECTS -----\n')

dog_1.bark()
dog_2.bark()
