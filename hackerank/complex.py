
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)
        
    def __add__(self, no):
        a = self.real 
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a+c,b+d)
    def __sub__(self, no):
        a = self.real 
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a-c,b-d)
        
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        a = self.real 
        b = self.imaginary
        mod = math.sqrt(a*a + b*b)
        return Complex(mod,0.00)

    def __str__(self):
        if self.imaginary == 0.00:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0.00:
            if self.imaginary >= 0.00:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0.00:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    a,b = input().split()
    c,d = input().split()
    first = Complex(a,b)
    second = Complex(c,d)
    print(first + second)
    print( first - second)
    print(first * second)
    print(first / second)
    print(first.mod())
    print(second.mod())