class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [
    Rectangle(5, 4),
    Circle(3)
]

for shape in shapes:
    print(shape.area())

# Output:
# 20
# 28.26

# Same method:
# area()

# Different implementation:
# Rectangle.area()
# Circle.area()