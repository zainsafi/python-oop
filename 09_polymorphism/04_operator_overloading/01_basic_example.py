# Operator overloading is a concept in Python where the same operator 
# (like +, -, *, etc.) can behave differently depending on the 
# objects it is used with.

# without operator overloading
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Point(2, 3)
# p2 = Point(4, 5)

# # This will NOT work:
# # p3 = p1 + p2  

# with operator overloading
# adding corresponding attributes of both objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # you can also dirctly return here
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        return f"{self.x}, {self.y}"

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # internally calls p1.__add__(p2)

print(p3.display())

