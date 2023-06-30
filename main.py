
class Game:
    def __init__(self, running, turn, score):
        self.running = running
        self.turn = turn
        self.score = score

    def get_turn(self):
        return self.turn

    def get_score(self):
        return self.score


# game object instantiate
game = Game(True, 0, 0)


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
        print(
            f"CITY STATISTICS    Turn {game.get_turn()}, Score: {game.get_score()}")
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

    def reset(self):
        self.population = 100
        self.food = 150
        self.gold = 25
        self.land = 50
        self.strength = 10
        self.influence = 10
        self.culture = 10

# unbound functions


def check_play_again():

    while True:

        play_again = input("Do you want to play again? y/n: ")
        if play_again.lower() == "y":
            print(f"Ok, {player_name}. You chose to play again.\n")
            city.reset()
            game.running = True
            break
        elif play_again.lower() == "n":
            print(f"Ok, {player_name}. You chose not to play again.\n")
            game.running = False
            break
        else:
            print("Enter 'y' or 'n', please.")


city = City(100, 150, 25, 50, 10, 10, 5)


class Turn:
    def __init__(self, pop_investment, acres_planted, trade, forrays, recruits, diplomacy, patronage):
        self.pop_investment = pop_investment
        self.acres_planted = acres_planted
        self.trade = trade
        self.forrays = forrays
        self.recruits = recruits
        self.diplomacy = diplomacy
        self.patronage = patronage

    def choose_population_investment(self):
        print("")
        print(
            f"How many units of gold (0-{city.get_gold()}) would you like to spend to encourage immigration from neighbooring kingdomw?")
        pop_investment = input("--> ")
        try:
            pop_investment = int(pop_investment)
            if pop_investment <= city.get_gold():
                city.set_gold(-pop_investment)
            else:
                print("Looks like you cannot afford to invest that much gold.")
                self.choose_population_investment()

        except:
            print(f"Please enter between 0-{city.get_gold()}.")
            self.choose_population_investment()


# turn object instantiate
turn = Turn(0, 0, 0, 0, 0, 0, 0)


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
    city.show_city_stats()
    turn.choose_population_investment()
    city.show_city_stats()

    check_play_again()
