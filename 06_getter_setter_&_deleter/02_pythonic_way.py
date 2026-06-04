# pythonic way of getters and setters
# getter,setter and deleter
# Deleter -> Used to control what happens when an attribute is deleted.

# These are connected through PROPERTIES.

# Property (@property) => A property allows us to use getter and 
# setter methods like normal attributes. Useful for cleaner syntax, 
# Better readability and provide Encapsulation with simplicity

class Student:
    def __init__(self,age):
        # Although getter and setter are mostly used for protected and private
        # but just for understanding here i have also demonstrated it's use 
        # for public attributes as well 
        self.student_name = None # public attribute 
        self._rollno = None # protected attribute
        self.__age = age # private attribute
    
    # getter for name
    @property
    def name(self):
        return f'Name: {self.student_name}' # don't used self.name because it will trigger infinite loop
    
    # setter for name
    @name.setter
    def name(self,value):
        self.student_name = value

    # getter for rollno
    @property 
    def rollno(self):
        return f'rollno: {self._rollno}'
    
    # setter for rollno
    @rollno.setter
    def rollno(self,rollno):
        self._rollno = rollno

    # getter for age
    @property
    def age(self):
        return f'Age: {self.__age}'
    
    # setter for age
    @age.setter
    def age(self,age):
        if age >= 0:
            self.__age = age
        else:
            print("Age can't be negative")
    
    # deleting name attribute
    @name.deleter
    def name(self):
        del self.student_name
    
    # deleting age attribute
    @age.deleter
    def age(self):
        del self.__age
    

student = Student(18)

# Assigning and retrieving value of name attribute
print(student.name)
student.name = "Hamza"
print(student.name)

print()

# Assigning and retrieving value of rollno attribute
print(student.rollno)
student.rollno = 30
print(student.rollno)

print()

# Assigning and retrieving value of age attribute
print(student.age)
student.age = 30
print(student.age)
student.age = -1

# accessing deleted name attribute
del student.name
try:
    print(student.name) # attribute error
except AttributeError as e:
    print(f"No name attribute: {e}")

# deleting age attribure
del student.age
try:
    print(student.age) # attribute error
except AttributeError as e:
    print(f"No age attribute: {e}")

