# car example
class car:

    # class attribute
    wheels = 4

    def __init__(self, color, model):

        # instance attributes
        self.color = color
        self.model = model

    # method
    def describe(self):

        return f'this car is a {self.color} {self.model}.'

    # method
    def start_engine(self):

        print(f'{self.model} engine started!')


# creating objects
car_1 = car('red', 'toyota corolla')
car_2 = car('green', 'lamborghini revuelto')


# accessing car attributes

print('\n----- car attributes -----\n')

print(car_1.model)
print(car_1.color)

print()

print(car_2.model)
print(car_2.color)


# calling car methods

print('\n----- car methods -----\n')

print(car_1.describe())
print(car_2.describe())

print()

car_1.start_engine()
car_2.start_engine()


# class attribute sharing

print('\n----- class attribute sharing -----\n')

print(car_1.wheels)
print(car_2.wheels)

# both objects share same class attribute