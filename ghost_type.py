import random
from pokemon import Pokemon


class GhostType(Pokemon):
    basic_attack = "Lick"
    prob = 0.3

    def __init__(self, name, trainer, hp=50):
        super().__init__(name, trainer, hp)

    def __repr__(self):
        return f"GhostType({self.name})"

    def attack(self, other):
        super().attack(other)

        if random.random() < self.prob:
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")

        self.damage = Pokemon.damage  # Reset damage
