import random
from pokemon import Pokemon


class GrassType(Pokemon):
    basic_attack = "Stun Spore"
    prob = 1.0

    def __init__(self, name, trainer, hp=50):
        super().__init__(name, trainer, hp)

    def __repr__(self):
        return f"GrassType({self.name})"

    def attack(self, other):
        if isinstance(other, GrassType):
            self.damage = Pokemon.damage / 2  # Weak
        else:
            self.damage = Pokemon.damage * 2  # Strong

        super().attack(other)

        if random.random() < self.prob:
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")

        self.damage = Pokemon.damage  # Reset damage
