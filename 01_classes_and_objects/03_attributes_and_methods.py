# methods and attributes in python

# attributes -> variables inside a class
# methods    -> functions inside a class

# there are two main types of attributes:
# class attributes
# instance attributes


# class with class attribute and instance attribute
class dog:

    # class attribute
    # shared by all objects
    species = 'french bulldog'

    # constructor method
    def __init__(self, name, age):

        # instance attributes
        # unique for each object
        self.name = name
        self.age = age

    # method
    def bark(self):

        print(
            f'{self.name.upper()} says woof woof! '
            f'i am {self.age} years old.'
        )

    # another method
    def describe(self):

        print(
            f'{self.name} is a {dog.species} '
            f'and is {self.age} years old.'
        )

# accessing class attribute

# accessing class attribute directly using class name
print(dog.species)


# creating objects

dog_1 = dog('jack', 3)
dog_2 = dog('tom', 5)


# accessing instance attributes

print('\n----- instance attributes -----\n')

print(dog_1.name)
print(dog_1.age)

print()

print(dog_2.name)
print(dog_2.age)


# accessing class attribute through objects

print('\n----- class attribute through objects -----\n')

print(dog_1.species)
print(dog_2.species)


# calling methods

print('\n----- methods -----\n')

dog_1.bark()
dog_2.bark()

print()

dog_1.describe()
dog_2.describe()


# modifying instance attributes

print('\n----- modifying instance attributes -----\n')

dog_1.age = 4

print(f'{dog_1.name} is now {dog_1.age} years old.')
