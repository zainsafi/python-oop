# variable length Keyword Arguments (**kwargs)
# The ** collects all keyword arguments into a dictionary.

def display(**kwargs):
    print(kwargs)

display(name = "Zain",rollno = 9)

# Example
print('\nStudent data example')
def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student(
    name = "zain",
    age = 18,
    city = "Peshawar"
)

