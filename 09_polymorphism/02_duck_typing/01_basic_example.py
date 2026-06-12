#Duck typing => Duck typing is a programming concept where the 
# suitability of an object is determined by its behavior (the 
# methods and properties it has), rather than its explicit class or type. 

# The philosophy is: "If it walks like a duck and quacks like a 
# duck, it must be a duck."

class Cat:
   def speak(self):
       return "A cat meow"

class Bird:
   def speak(self):
       return "A bird tweet"
  
class Monkey:
   def speak(self):
       return "A monkey ooh ooh aah aah ooh ooh aah aah"

def animal_sound(animal):
   print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())
