# getters and setters
# getter  -> used to retrieve a value
# setter  -> used to set/update a value safely
# they are usefull for controlled access,data validation and better encapsulation
# useful for privated attributes access

# Traditional way of getter and setters (non pythonic way)
class Student():
    def __init__(self,age):
        self.__name = None # private attribute
        self.__age = age

    # getter for name
    def get_name(self):
        return f'I am {self.__name}'   

    # setter for name
    def set_name(self,name):
        self.__name = name
    
    # getter for name
    def age_get(self):
        return f"My age is {self.__age}"
    
    # setter for age
    def age_set(self,age_value):
        self.__age = age_value

student = Student(20)

print(student.get_name())
student.set_name("Zain")
print(student.get_name())

print(student.age_get())
student.age_set(19)
print(student.age_get())

