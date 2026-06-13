class Dog:
    def sound(self):
        return "Woof"
    
class Cat:
    def sound(self):
        return "Meow"

def make_sound(obj):
    return obj.sound()

dog = Dog()
cat = Cat()

print(f"Dog {make_sound(dog)}")
print(f"Cat {make_sound(cat)}")
