# dunder methods/magic methods/special methods in python
# dunder methods (double underscore methods) are special built-in methods
# that allow us to define how python objects behave with built-in functions
# and operators.
# they are called "dunder" because they start and end with double underscores (__).

# examples:
# __init__(), __str__(), __len__(), __eq__()
# __add__(), __contains__(), __getitem__(), __iter__()

# Python automatically calls them behind the scenes

# Example:
# 3 + 4
# actually runs:
# 3.__add__(4)

print()

# basic example without special methods
class bookwithoutmethods:

    def __init__(self, title, pages):

        self.title = title
        self.pages = pages


book1 = bookwithoutmethods("python mastery", 400)
book2 = bookwithoutmethods("learn ai", 400)

# print(len(book1))
# typeerror because python does not know how to get length

print(book1) # default ugly object representation

# false because python compares memory addresses
print(book1 == book2)

print()


# using special methods
class book:

    # __init__() => initializes object attributes
    def __init__(self, title, pages):

        self.title = title
        self.pages = pages


    # __len__() => called when len(object) is used
    def __len__(self):

        return self.pages


    # __str__() => controls readable string representation
    def __str__(self):

        return f"'{self.title}' has {self.pages} pages"


    # __eq__() => controls equality comparison using ==
    def __eq__(self, other):

        return self.pages == other.pages


# creating objects
book1 = book("built wealth like a boss", 420)
book2 = book("be your own start", 420)
book3 = book("python basics", 250)


# __len__()
print(len(book1))
print(len(book2))
print(len(book3))

print()

# __str__()
print(book1)
print(book2)
print(book3)

print()

# __eq__()
print(book1 == book2)  # true because pages are same
print(book1 == book3)  # false

print()


# special methods are automatically called
# these are equivalent

print(len(book1))
print(book1.__len__())

print()

print(str(book1))
print(book1.__str__())


