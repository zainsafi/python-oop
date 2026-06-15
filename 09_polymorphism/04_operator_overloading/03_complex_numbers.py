class ComplexNumbers:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return str(self.real + other.real) + " + " + str(self.imaginary + other.imaginary) + 'i' 
    
# Forexample add 6 + 3i and 5 + 4i
c1 = ComplexNumbers(6,3)
c2 = ComplexNumbers(5,4)

result = c1 + c2
print(result)
