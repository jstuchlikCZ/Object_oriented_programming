# Máme definovaný nějaký objekt a ostatní objekty dědí jeho vlastnosti
# V OOP to funguje takto:
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello I am {self.name}")

class Dog(Animal): # Všechny vlastnoti Animal dostane i Dog
    def make_sound(self): # místo def můžeme dát i pass a chovat se to bude stejně
        print("Bark bark")

class Cat(Animal): # Všechny vlastnoti Animal dostane i Dog
    def make_sound(self): # místo def můžeme dát i pass a chovat se to bude stejně
        print("Meow meow")

class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class EBook(Book, File):
    def __init__(self, name, pages, size):
        Book.__init__(self, name, pages)
        File.__init__(self, name, pages)

print()
eb = EBook("<NAME>", 100, 200)
print(eb.name)
print(eb.pages)
print(eb.size)
print(EBook.mro())
print()

d1 = Dog("Alík")
d1.say_hello()
print()
c1 = Cat("Mourek")
c1.say_hello()
c1.make_sound()
print()
print(Cat.mro()) # Historie dědění, pokud chceme zjistit co vše obsahuje

print()
print()
print()

Task 1
Create a class Human that will contain info about a human.

Use inheritance to create a Builder class (contains info about a builder), 
a Sailor class (contains info about a sailor), a Pilot class (contains info about a pilot).

Each class must have the required methods.
"""

class Builder:
    def __init__(self, vehicle, experience):
        self.vehicle = vehicle
        self.experience = experience

class Sailor:
    pass


class Pilot:
    pass


class Human(Builder, Sailor, Pilot):
    def __init__(self, occupacation, sex, age):
        self.occupation = occupacation
        self.sex = sex
        self.age = age
        Builder.__init__(self, vehicle, experience)


print()
h1 = Human(Builder, male, 25)
print(Human.occupation)
print(Human.sex)
print(Human.age)
print(Builder.vehicle)
print(Builder.experience)
print()