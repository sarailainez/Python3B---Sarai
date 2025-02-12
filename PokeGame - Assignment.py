import random
from pokemon import Pokemon # My base code
from grass_type import GrassType  #My code
from ghost_type import GhostType  #Class by Gianna Calderon


class PokeGame:
    def __init__(self):
        self.game_master = []
        self.setup()

    def setup(self):
        """ Seven instances + to list."""
        self.game_master.append(GrassType("Bob", "Trainer A"))
        self.game_master.append(GrassType("Charlie", "Trainer B"))
        self.game_master.append(GhostType("Peach", "Trainer C"))
        self.game_master.append(GhostType("Hunter", "Trainer D"))
        self.game_master.append(Pokemon("Piya", "Trainer E"))
        self.game_master.append(Pokemon("Carson", "Trainer F"))
        self.game_master.append(Pokemon("Stuart", "Trainer G"))

    def drawPokemon(self):

        if self.game_master:
            opponent = random.choice(self.game_master)  # Select a random opponent
            self.game_master.remove(opponent)  # Remove from list
            print(f"Opponent Pokemon: {opponent.name} ({opponent.__class__.__name__})")
            return opponent
        else:
            print("Game Over")
            return None

def main():
    game = PokeGame()
    opponent = game.drawPokemon()

    if not opponent:
        return

    valid_types = {"Grass": GrassType, "Ghost": GhostType, "Base": Pokemon}
    print("Choose a name to battle:")
    for key in valid_types:
        print(f"- {key}")

    choice = input("Enter a Pokemon type: ")
    if choice not in valid_types:
        print("Invalid choice!")
        return

    name = input("Enter your characters name: ")
    hp = int(input("Enter HP value: "))
    player_pokemon = valid_types[choice](name, "You", hp)

    player_pokemon.attack(opponent)


if __name__ == "__main__":
    main()
