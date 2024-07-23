import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def random_person():
    firstnames = ['ali', 'hasan', 'hosein', 'barbod', 'ahmad', 'siavash']
    lastnames = ['alavi', 'hasani', 'hoseini', 'imani', 'ahmadi', 'siavashi']
    ages = [21, 22, 23, 24, 44, 55, 67, 89, 90]
    random_people = []

    for _ in range(100):  # Create 100 persons
        random_age = random.choice(ages)
        random_firstname = random.choice(firstnames)
        random_lastname = random.choice(lastnames)
        person = Person(f"{random_firstname} {random_lastname}", random_age)
        random_people.append(person)

    winner = random.choice(random_people)
    return winner


# Test the random_person function
winner = random_person()
print(f"The winner is {winner.name} with age {winner.age}.")
