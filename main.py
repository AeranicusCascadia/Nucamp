# unbound variables
player_name = "Anonymous"
score = 0
turn = 0

# classes


class Game:
    def __init__(self, running):
        self.running = running


class City:
    def __init__(self, population, food, gold, land, strength, influence, culture):

        self.population = population
        self.food = food
        self.gold = gold
        self.land = land
        self.strength = strength
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

    def get_strength(self):
        return self.strength

    def get_infulence(self):
        return self.influence

    def get_culture(self):
        return self.culture

    # City setters

    def set_population(self, value):
        self.population += value

    def set_food(self, value):
        self.food += value

    def set_gold(self, value):
        self.gold += value

    def set_land(self, value):
        self.land += value

    def set_strength(self, value):
        self.strength += value

    def set_influence(self, value):
        self.influence += value

    def set_culture(self, value):
        self.culture = +value

    # City methods
    def show_city_stats(self):
        print("")
        print(f"CITY STATISTICS    Turn {turn}, Score: {score}")
        print("---------------")
        print(f"Population: {self.get_population()}")
        print(f"Food stockpile: {self.get_food()}")
        print(f"Gold reserves: {self.get_gold()}")
        print(f"Land area occupied: {self.get_land()}")
        print("")
        print(f"Military strength: {self.get_strength()}")
        print(f"Influence level: {self.get_infulence()}")
        print(f"Cultural richness: {self.get_culture()}")
        print("")


# unbound functions
def increase_score(amount):
    global score
    score += amount


def check_play_again():

    while True:

        play_again = input("Do you want to play again? y/n: ")
        if play_again.lower() == "y":
            print(f"Ok, {player_name}. You chose to play again.\n")
            game.running = True
            break
        elif play_again.lower() == "n":
            print(f"Ok, {player_name}. You chose not to play again.\n")
            game.running = False
            break
        else:
            print("Enter 'y' or 'n', please.")


# city instantiate
city = City(100, 150, 25, 50, 10, 10, 5)

# game instantiate
game = Game(True)


# Player set up
print("")
print("Welcome to the city of Ashkagar!")
print("")

while True:
    player_name = input("What is your name, mighty ruler? ")
    if player_name != "":
        print(
            f"Very well, {player_name}. May your reign be long and prosperous!")
        break
    else:
        print("")
        print("Our scribes could not understand this. Please declare your name.")

# start main game loop
while game.running:
    city.set_food(15)
    city.show_city_stats()
    print("We have played the game!")
    check_play_again()
