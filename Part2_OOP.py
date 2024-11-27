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
"""

