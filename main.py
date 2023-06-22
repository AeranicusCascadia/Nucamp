
# classes
class Game:
    def __init__(self, running):
        self.running = running


class City:
    def __init__(self, population, food, gold, land, might, influence, culture):

        self.population = population
        self.food = food
        self.gold = gold
        self.land = land
        self.might = might
        self.influence = influence
        self.culture = culture
    # City getters

    def get_population(self):
        return self.population

    def get_food(self):
        return self.food

    def get_gold(self):
        return self.gold

    def get_land(self):
        return self.land

    def get_might(self):
        return self.might

    def get_infulence(self):
        return self.influence

    def get_culture(self):
        return self.culture

    # City setters

    def set_population(self, value):
        self.population = value

    def set_food(self, value):
        self.food = value

    def set_gold(self, value):
        self.gold = value

    def set_land(self, value):
        self.land = value

    def set_might(self, value):
        self.might = value

    def set_influence(self, value):
        self.influence = value

    def set_culture(self, value):
        self.culture = value


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Players getters
    def get_name(self):
        return self.name
    # Players setters

    def set_name(self):
        self.name = input("What is your name? ")

# unbound functions


def check_play_again():

    while True:
        player_name_str = player.get_name()

        play_again = input("Do you want to play again? y/n")
        if play_again.lower() == "y":
            print(f"Ok, {player_name_str}. You chose to play again.\n")
            game.running = True
            break
        elif play_again.lower() == "n":
            print(f"Ok, {player_name_str}. You chose not to play again.\n")
            game.running = False
            break
        else:
            print("Enter 'y' or 'n', please.")


# city set up
city = City(100, 150, 25, 50, 10, 10, 5)

# player set up
player = Player("Anonymous", 0)
player.set_name()
player_name_str = player.get_name()
print(f"Ok, {player_name_str}, get ready to play!\n")


# start main game loop
game = Game(True)

while game.running:
    print("We have played the game!")
    check_play_again()
