class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __gt__(self, other):
        if self.age > other.age:
            return f"{self.name} will pay the bill"
        else:
            return f"{other.name} will pay the bill"
    
p1 = Person("Zain",21)
p2 = Person("Ali",23)

print(p1 > p2)

# __gt__ is normally used to return True/False => check next program

