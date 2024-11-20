"""
Task 3
Create an Airplane class. Implement the following using the operator overloading:

Check if the airplane types are equal (the == operator);
Increasing and decreasing the number of passengers in the cabin (the operators: + - + = - =);
Compare two airplanes for the maximum possible number of passengers on board (the operators: > < <= >=).
"""

class Airplane:
    def __init__(self, A_type, max_pas, cur_pas):
        self.A_type = A_type
        self.max_pas = max_pas
        self.cur_pas = cur_pas

    # Overloading the equality operator (==) to compare airplane types
    def __eq__(self, other):
        return self.A_type == other.A_type

    # Overloading the addition operator (+) to increase passengers
    def __add__(self, passangers):
        new_count = self.cur_pas + passangers
        if new_count > self.max_pas:
            raise ValueError("Number of passengers exceeds the airplane's capacity!")
        self.cur_passengers = new_count
        return self

        # Overloading the subtraction operator (-) to decrease passengers

    def __sub__(self, passengers):
        new_count = self.cur_pas - passengers
        if new_count < 0:
            raise ValueError("Number of passengers cannot be negative!")
        self.cur_passengers = new_count
        return self

        # Overloading the comparison operators for max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return (f"Airplane Type: {self.airplane_type}, "
                f"Max Passengers: {self.max_passengers}, "
                f"Current Passengers: {self.cur_passengers}")

# Example usage
plane1 = Airplane("Boeing 747", 416, 200)
plane2 = Airplane("Airbus A380", 853, 500)
plane3 = Airplane("Boeing 747", 416, 300)

# Checking equality of airplane types
print(plane1 == plane3)  # True
print(plane1 == plane2)  # False

# Increasing and decreasing passengers
try:
    plane1 + 50  # Add 50 passengers
    print(plane1)  # Updated passenger count
    plane1 - 100  # Remove 100 passengers
    print(plane1)  # Updated passenger count
except ValueError as e:
    print(e)

# Comparison of max_passengers
print(plane1 > plane2)  # False
print(plane1 < plane2)  # True
print(plane1 >= plane3)  # True
print(plane1 <= plane2)  # True


# Řešení od pana Čepana






















