def suma(a,b):
    salida = a + b
    return salida

def function1(a,b,c=50,d="default"):
    if type(a) == str and type(b)== str :
        print(a + b + d)
    else:
        print(a + b + c)
    return d

class ComplexNumbers:
    def __init__(self,real, imag):
        self.real = real
        self.imag = imag
    def print(self):
        print(f'La parte real es {self.real} y la parte imaginaria es {self.imag}')
    def set_real(self,real):
        self.real = real
    def set_imag(self,imag):
        self.imag = imag
    def suma(self, complex_number):
        self.real = self.real + complex_number.real
        self.imag += complex_number.imag
    def __mul__(self,complex_number):
        real = self.real*complex_number.real - self.imag*complex_number.imag
        imag = self.real*complex_number.imag + self.imag*complex_number.real
        output = ComplexNumbers(real, imag)
        return output
    def __add__(self,complex_number):
        output = ComplexNumbers(
            self.real+complex_number.real,
            self.imag+complex_number.imag)
        return output
    def __repr__(self):
        return f'La parte real es {self.real} y la parte imaginaria es {self.imag}'

class TriplexNumbers(ComplexNumbers):
    def __init__(self, real, imag,tres):
        super().__init__(real,imag)
        self.tres = tres
    def __repr__(self):
        return f'La parte real es {self.real}, la parte imaginaria es {self.imag} y la parte tres es {self.tres}'
    def __add__(self, number):
        print("Is complex:", isinstance(number, ComplexNumbers))
        print("Is triplex:", isinstance(number, TriplexNumbers))
        if not isinstance(number,TriplexNumbers):
            output = super().__add__(number)
        else:
            output = TriplexNumbers(
            self.real+number.real,
            self.imag+number.imag,
            self.tres+number.tres,
            )
        return output

if __name__ == "__main__":
    a = 4
    b = 5
    print(a+b)
