class LivingThing:
    def __init__(self, species):
        self.species = species


class Animal(LivingThing):
    def __init__(self, species, location=None):
        super().__init__(species)
        self.location = location

    def set_location(self, location):
        self.location = location


class Human(Animal):
    def __init__(self, species, gender=None, location=None):
        super().__init__(species, location)
        self.gender = gender

    def set_gender(self, gender):
        self.gender = gender


# Example usage:
if __name__ == "__main__":
    dog = Animal("dog")
    dog.set_location("amazon")
    print(f"The {dog.species} is located in the {dog.location}")

    human = Human("updated monkey", "Male")
    human.set_location("Earth")
    human.set_gender("Female")
    print(f"The {human.species} is located on {human.location} and is {human.gender}.")
