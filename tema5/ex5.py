class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def move(self):
        pass

    def display_info(self):
        return f"Name: {self.name}\nHabitat: {self.habitat}"

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} gives birth to live young."

    def make_sound(self):
        return "Some generic mammal sound"

    def move(self):
        return "Walking on four legs"

class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def lay_eggs(self):
        return f"{self.name} lays eggs in a nest."

    def make_sound(self):
        return "Some generic bird sound"

    def move(self):
        return "Flying in the sky"

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def lay_eggs(self):
        return f"{self.name} lays eggs in the water."

    def make_sound(self):
        return "Some generic fish sound"

    def move(self):
        return "Swimming in the water"


mammal = Mammal("Lion", "Grasslands", "Golden")
print(mammal.display_info())
print(mammal.give_birth())
print(mammal.move())

print("\n")

bird = Bird("Eagle", "Mountains", "Brown")
print(bird.display_info())
print(bird.lay_eggs())
print(bird.move())

print("\n")

fish = Fish("Goldfish", "Aquarium", "Orange")
print(fish.display_info())
print(fish.lay_eggs())
print(fish.move())
