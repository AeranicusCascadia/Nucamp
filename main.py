# Need to define method: clear_vars_for_new_turn()
# fix Turn.recruit.soldiers
# Turn.sell_food seems like a good example

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
        print(f"Land available: {self.get_land()}")
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
        print("")
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
    def __init__(self, pop_investment, acres_planted, food_sold, forrays_sent, recruits, diplomacy, patronage):
        self.pop_investment = pop_investment
        self.acres_planted = acres_planted
        self.food_sold = food_sold
        self.forrays_sent = forrays_sent
        self.recruits = recruits
        self.diplomacy = diplomacy
        self.patronage = patronage

    max_recruits = 0

    # getter for max number of recruits this turn
    def get_max_recruits(self):
        return self.max_recruits

    # setter for max number of recruits this turn
    def set_max_recruits(self):
        self.max_recruits += 1

    def clear_vars_for_new_turn(self):
        pass

    def choose_population_investment(self):
        print("")
        print(
            f"How many units of gold (0-{city.get_gold()}) would you like to spend to encourage immigration from neighbooring kingdomw?")
        pop_investment = input("--> ")
        try:
            pop_investment = int(pop_investment)
            if pop_investment <= city.get_gold():
                city.set_gold(-pop_investment)
                self.pop_investment += pop_investment
            else:
                print("Looks like you cannot afford to invest that much gold.")
                self.choose_population_investment()
        except:
            print(f"Please enter between 0-{city.get_gold()}.")
            self.choose_population_investment()

    def plant_crops(self):
        print("")
        print(
            f"How many acres of land (0-{city.get_land()}) would you like to plant to with food crops?")
        acres_planted = input("--> ")
        try:
            acres_planted = int(acres_planted)
            if acres_planted <= city.get_land():
                city.set_land(-acres_planted)
                self.acres_planted += acres_planted
            else:
                print("Looks like you don't have that much land available to plant.")
                self.plant_crops()
        except:
            print(f"Please enter between 0-{city.get_land()}.")
            self.plant_crops()

    def sell_food(self):
        print("")
        print(
            f"How many bushels of food (0-{city.get_food()}) would you like to sell at the market?")
        food_sold = input("--> ")
        try:
            food_sold = int(food_sold)
            if food_sold <= city.get_food():
                city.set_food(-food_sold)
                self.food_sold += food_sold
            else:
                print(
                    "Looks like you don't have that much food available to sell at market.")
                self.sell_food()
        except:
            print(f"Please enter between 0-{city.get_land()}.")
            self.sell_food()

    def send_forrays(self):
        print("")
        print(
            f"How many units of soldiers  (0-{city.get_strength()}) would you like to send on forrays to try to capture territory?")
        forrays_sent = input("--> ")
        try:
            forrays_sent = int(forrays_sent)
            if forrays_sent <= city.get_strength():
                city.set_strength(-forrays_sent)
                self.forrays_sent += forrays_sent
            else:
                print(
                    "Looks like you don't have enough military strength to send out that many forrays to capture land.")
                self.send_forrays()
        except:
            print(f"Please enter between 0-{city.get_strength()}.")
            self.send_forrays()

    def calc_max_recruits(self, food_input, gold_input):
        if (food_input < 1) or (gold_input < 1):
            print("Looks like you are lacking either gold or food.")
            self.max_recruits = 0
        else:
            self.max_recruits = ((gold_input + food_input)) // 2
            print(
                f"You have enough gold and food for {self.max_recruits} troops.")

    def recruit_soldiers(self):
        print("")
        print(
            f"How many units of new troops (0-{self.get_max_recruits()}) would you like to recruit into your military forces?")
        troops_recruited = input("--> ")
        try:
            troops_recruited = int(troops_recruited)
            if (troops_recruited <= self.get_max_recruits()) and (troops_recruited >= 0):
                city.set_strength(+troops_recruited)
                city.set_food(-troops_recruited)
                city.set_gold(-troops_recruited)
                self.recruits += troops_recruited
            elif troops_recruited < 0:
                print(
                    f"Please enter a positive whole number between 0-{self.get_max_recruits()}.")
                self.recruit_soldiers()
            else:
                print(
                    "Looks like you don't have that much gold available to recruit troops.")
                self.recruit_soldiers()
        except:
            print(f"Please enter between 0-{self.get_max_recruits()}.")
            self.recruit_soldiers()

        """ while True:
            try:
                int(troops_recruited)
                break
            except:
                print(f"Please enter between 0-{str(self.max_recruits())}.")
                self.recruit_soldiers()

        if (int(troops_recruited) <= self.get_max_recruits()) and (troops_recruited >= 0):
            city.set_strength(+ troops_recruited)
            city.set_food(-troops_recruited)
            city.set_gold(-troops_recruited)
            self.recruits += self.recruits
        else:
            print(
                "Looks like you don't have enough food or gold to recruit that many troops.")
            self.recruit_soldiers() """

    def show_summary(self):
        print("")
        print(f"Invested gold to encourage immigration: {self.pop_investment}")
        print(f"Acres of farmland planted with crops: {self.acres_planted}")
        print(f"Food sold at market for gold: {self.food_sold}")
        print(
            f"Military units sent on forrays to capture enemy territory: {self.forrays_sent}")
        print(
            f"Fresh troops recruited into your military forces: {self.recruits}")


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


while game.running:  # start main game loop

    # main game loop functions
    def run_player_prompts():
        turn.choose_population_investment()
        turn.plant_crops()
        turn.sell_food()
        turn.send_forrays()
        turn.recruit_soldiers()

    city.show_city_stats()
    turn.calc_max_recruits(city.get_food(), city.get_gold())
    run_player_prompts()
    turn.show_summary()
    city.show_city_stats()

    check_play_again()
