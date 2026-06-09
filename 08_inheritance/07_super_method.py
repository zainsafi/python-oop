# super() allows us to access methods and 
# attributes of the parent class.
# Useful when we want to extend parent behavior instead 
# of completely replacing it.

class Person:
    def __init__(self,name):
        self.name = name
    
    def quality(self):
        return f"{self.name} is a person"
    
class Student(Person):
    def __init__(self, name,rollno):
        super().__init__(name)
        self.rollno = rollno
    
    def quality(self):
        base = super().quality()
        return f"{base} and {self.name} is a student and his rollno is {self.rollno}"
    
student = Student("Zain Ul Islam",9)
print(student.quality())