#  classes and objects in python 
# a class is a blueprint/template for creating objects.
# an object is a real instance created from the class.

# creating a class
class Student:

    # it runs automatically when object is created
    # __init__ is a special constructor method

    def __init__(self, name, rollno, semester):

        # instance attributes
        self.name = name
        self.rollno = rollno
        self.semester = semester

    # instance method
    def introduce(self):
        print(
            f'My name is {self.name}. '
            f'My roll number is {self.rollno}. '
            f'I am in semester {self.semester}.'
        )

    # another method
    def study(self):

        print(f'{self.name} is studying Python.')


# creating objects

# object_1
student_1 = Student('Zain', 11, 6)

# object_2
student_2 = Student('Asim', 31, 5)


# accessing attributes

print('----- ACCESSING ATTRIBUTES -----')

print(student_1.name)
print(student_1.rollno)
print(student_1.semester)

print()

print(student_2.name)
print(student_2.rollno)
print(student_2.semester)


# calling methods

print('----- CALLING METHODS -----\n')

student_1.introduce()
student_1.study()

print()

student_2.introduce()
student_2.study()


# modifying object attributes

print('\n----- MODIFYING ATTRIBUTES -----\n')

student_1.semester = 7

print(f'{student_1.name} is now in semester {student_1.semester}.')


# understanding self

print('\n----- UNDERSTANDING self -----\n')

# self refers to the current object itself

print(student_1)
print(student_2)

# both objects are different in memory

