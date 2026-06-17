# Types of Variable-Length Arguments
# Python provides two ways:
# *args → Variable number of positional arguments
# **kwargs → Variable number of keyword arguments

# Variable length positional arguments (*args)
# The * collects all extra positional arguments into a tuple.

def add(*args):
    print(args)

add(2,3)
add(2,5,1,4,8)

# sum all numbers
print("\nAdd numbers")
def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))