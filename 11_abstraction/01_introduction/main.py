# * is used to import all public names (classes, functions, variables)
# from a module.

from importing_abstract_class import *

b = Bike(2,"white")
print("Bike details")
b.start()
b.display()

print("\nCar details")
c = Car(4)
c.start()
c.display()