from abstract_class import Vehicle

class Bike(Vehicle):
    def __init__(self, n,color):
        super().__init__(n)
        self.color = color
    
    def start(self):
        print("Start with kick")
    
    def display(self):
        super().display()
        print(f"Color {self.color}")

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start(self):
        print("Start with key")
    
