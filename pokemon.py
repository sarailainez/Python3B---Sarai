class Pokemon:
    damage = 10

    def __init__(self, name, trainer, hp=50):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = hp
        self.paralyzed = False

    def attack(self, other):
        other.hp -= self.damage
        print(f"{self.name} attacks {other.name} for {self.damage} damage!")
