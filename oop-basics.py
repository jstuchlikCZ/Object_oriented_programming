import self

"""
Class je manuál jak vyrobit objekt -> jaké má vlastnoti, co umí a co má dělat.
h1 = provedení


TASK1
"""

class Human:
    name = "Jan"
    age = 31

    def say_hello(self):        # Metoda volá se přes tečku h1.say_hello()
        print("Ahoj světe.")


# Jak vytvořit humana

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):        # Metoda volá se přes tečku h1.say_hello()
        print(f"Ahoj světe. Já jsem {self.name}")

l = list()
h1 = Human("Jan")
h2 = Human("Jane")
#h2.name = "Jane"

print(l)
print(h1)
print(h1.name)
print(h2.name)
h1.say_hello()



"""
TASK 2
Create a class City. Class fields should store the following: 
city name, region name, country name, number of citizens, zip code, area code. 
Implement class methods for data input and output, provide access to individual fields
 through class methods.
"""

class City:
    def __init__(self, name, kraj, zeme, obyvatele, psc):
        self.name = name
        self.kraj = kraj
        self.zeme = zeme
        self.obyvatele = obyvatele
        self.psc = psc

    def mesto(self):        # Metoda volá se přes tečku h1.say_hello()
        print(f"Výstup: {self.name, self.kraj, self.zeme, self.obyvatele, self.psc}")

c1 = City("Praha", "Hlavní město Praha", "Česká Republika",
              "1 400 000", "100 00")

c1.mesto()

"""
Task 3
Create a class Country. Class fields should store the following: 
country name, continent, population, calling code, capital, city names. 
Implement class methods for data input and output, 
provide access to individual fields through class methods.
"""

class Country:
    def __init__(self, name, kontinent, obyvatele, predvolba, capital):
        self.name = name
        self.kontinent = kontinent
        self.obyvatele = obyvatele
        self.predvolba = predvolba
        self.capital = capital

    def zeme(self):        # Metoda volá se přes tečku x1.say_hello()
        print(f"Výstup: {self.name, self.kontinent, self.obyvatele, self.predvolba, self.capital}")

z1 = Country("Česká Republika", "Evropa", "10 500 000",
              "+420", "Praha")

class Country1:
    def __init__(self, name):
        self.name = name

class kontinent:
    def __init__(self, kontinent):
        self.name = kontinent

class obyvatele:
    def __init__(self, obyvatele):
        self.name = obyvatele

class predvolba:
    def __init__(self, predvolba):
        self.name = predvolba

class capital:
    def __init__(self, capital):
        self.name = capital

z1.zeme()


