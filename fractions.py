"""
Task 4
Create a class Fraction. Class fields should store the following:
numerator and denominator. Implement class methods for data input and output,
provide access to individual fields through class methods.
Also, create class methods for arithmetic operations (add, subtract, multiply, divide, etc.).
"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other): # equal
        return self.denominator == other.denominator and self.numerator == other.numerator

    def __add__(self, other): # addition
        pass

    def __str__(self): #
        return f"{self.numerator}/{self.denominator}"

f = Fraction(1,2)
f2 = Fraction(1,2)

print("porovnání 1", f == f2)


# print(f == f2) # vysledek je false
