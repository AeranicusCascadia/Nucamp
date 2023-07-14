# Need to define method: clear_vars_for_new_turn()
# Need to define method to end game play
# need to limit multi resource input variables to least input - calc_max_envoys works! Use as example
import random
game_running = True


def main():

    class Game:
        def __init__(self, turn, score, length):
            self.turn = turn
            self.score = score
            self.length = length

        def get_turn(self):
            return self.turn

        def get_score(self):
            return self.score

        def get_length(self):
            return self.length

        def increment_turn(self):
            self.turn += 1

        def adjust_score(self, value):
            value = round(value/10)
            self.score += value

        def ask_play_again(self):
            print("")
            print("Would you like to play again? (y/n)")
            response = input("--> ")
            if response.lower() == "y":
                return True
            elif response.lower() == "n":
                print("Thanks for playing!")
                return False
            else:
                print("Please enter 'y' or 'n'.")

        def lose(self):
            print("")
            print("Sadly, your reign has come to an end!")
            print(f"Final Score: {self.get_score()}")
            if self.ask_play_again():
                main()
            else:
                exit()

        def win(self):
            print("")
            print(
                f"Congradulations! You have survived the full {self.length} turns.")
            print(f"Final Score: {self.get_score()}")
            if self.ask_play_again():
                main()
            else:
                exit()

    # game object instantiate
    game = Game(0, 0, 10)

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

        def get_influence(self):
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
            self.culture += value

        # City methods
        def show_city_stats(self):
            print("")
            print('-'*37)
            print(
                f"CITY STATISTICS    Turn {game.get_turn()}, Score: {game.get_score()}")
            print('-'*37)
            print(f"Population: {self.get_population()}")
            print(f"Food stockpile: {self.get_food()}")
            print(f"Gold reserves: {self.get_gold()}")
            print(f"Land available: {self.get_land()}")
            print(f"Military strength: {self.get_strength()}")
            print(f"Influence level: {self.get_influence()}")
            print(f"Cultural richness: {self.get_culture()}")
            print("")

        def reset(self):
            self.population = 50
            self.food = 75
            self.gold = 75
            self.land = 50
            self.strength = 25
            self.influence = 10
            self.culture = 10

    city = City(50, 75, 75, 50, 25, 10, 10)

    class Turn:
        def __init__(self, pop_investment, acres_planted, food_sold, forrays_sent, recruits, envoys_sent, buildings):
            self.pop_investment = pop_investment  # increases population, decreases gold
            self.acres_planted = acres_planted  # increases food, decreases land
            self.food_sold = food_sold  # increases gold, decreases food
            self.forrays_sent = forrays_sent  # increases land, decreases strength
            self.recruits = recruits  # increases strength, decreases gold and food
            self.envoys_sent = envoys_sent  # increases influence, decreases gold and culture
            self.buildings = buildings  # increases culture, decreases gold and influence

        max_recruits = 0
        max_envoys = 0
        max_buildings = 0
        tax_revenue = 0
        pop_growth = 0

        def get_max_recruits(self):
            return self.max_recruits

        def get_max_envoys(self):
            return self.max_envoys

        def get_max_buildings(self):
            return self.max_buildings

        def set_tax_revenue(self, value):
            self.tax_revenue = value

        def set_pop_growth(self, value):
            self.pop_growth = value

        def clear_properties(self):
            self.pop_investment = 0
            self.acres_planted = 0
            self.food_sold = 0
            self.forrays_sent = 0
            self.recruits = 0
            self.envoys_sent = 0
            self.buildings = 0
            self.max_buildings = 0
            self.max_envoys = 0
            self.max_recruits = 0
            self.tax_revenue = 0
            self.pop_growth = 0

        def choose_population_investment(self):
            print("")
            print(
                f"How many units of gold (0-{city.get_gold()}) would you like to spend to encourage immigration from neighbooring kingdoms?")
            print("--- Population will generate some gold through taxes each turn.")
            pop_investment = input("--> ")
            try:
                pop_investment = int(pop_investment)
                if (pop_investment <= city.get_gold()) and (pop_investment >= 0):
                    city.set_gold(-pop_investment)
                    self.pop_investment += pop_investment
                    # testing results of input
                    print(
                        f"{pop_investment} gold invested in encouraging immigration.")
                    # testing
                    print(f"City gold reserves remaining: {city.get_gold()}")
                    print("")
                    return
                else:
                    print(f"Please enter between 0-{city.get_gold()}.")
                    self.choose_population_investment()
            except:
                print(f"Please enter between 0-{city.get_gold()}.")
                self.choose_population_investment()

        def plant_crops(self):
            max_planting = min(city.get_population(), city.get_land())
            print("")
            print(
                f"How many acres of land (0-{max_planting}, cost: 1 land + 1 population each) would you like to plant to with food crops?")
            acres_planted = input("--> ")
            try:
                acres_planted = int(acres_planted)
                if (acres_planted <= city.get_land()) and (acres_planted >= 0) and (acres_planted < city.get_population()):
                    city.set_land(-acres_planted)
                    self.acres_planted += acres_planted
                    city.set_population(-acres_planted)
                    # testing results of input
                    print(f"{acres_planted} acres of land planted with crops.")
                    # testing
                    print(f"Land remaining: {max_planting}")
                    print("")
                    return
                else:
                    print(
                        f"Please enter a number between 0-{max_planting}.")
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
                if (food_sold <= city.get_food()) and (food_sold >= 0):
                    city.set_food(-food_sold)
                    self.food_sold += food_sold
                    # testing results of input
                    print(f"{food_sold} bushells of food sold at market.")
                    # testing
                    print(f"Food reserves remaining: {city.get_food()}")
                    print("")
                    return
                else:
                    print(f"Please enter between 0-{city.get_food()}.")
                    self.sell_food()
            except:
                print(f"Please enter between 0-{city.get_food()}.")
                self.sell_food()

        def send_forrays(self):
            print("")
            print(
                f"How many units of soldiers  (0-{city.get_strength()}) would you like to send on forrays to try to capture territory?")
            forrays_sent = input("--> ")
            try:
                forrays_sent = int(forrays_sent)
                if (forrays_sent <= city.get_strength()) and (forrays_sent >= 0):
                    city.set_strength(-forrays_sent)
                    self.forrays_sent += forrays_sent
                    # testing results of input
                    print(
                        f"{forrays_sent} military units set to attempt to capture territory.")
                    print(
                        f"Military units remain in the city to strengthen the garrison.: {city.get_strength()}")
                    print("")
                    return
                else:
                    print(f"Please enter between 0-{city.get_strength()}.")
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
                lesser_input = min(gold_input, food_input)
                if (self.max_recruits > lesser_input):
                    self.max_recruits = lesser_input

        def recruit_soldiers(self):

            self.calc_max_recruits(city.get_food(), city.get_gold())

            print("")
            print(
                f"How many units of new troops (0-{self.get_max_recruits()}, cost: 1 food + 1 gold each) would you like to recruit into your military forces?")
            troops_recruited = input("--> ")
            try:
                troops_recruited = int(troops_recruited)
                if (troops_recruited <= self.get_max_recruits()) and (troops_recruited >= 0):
                    city.set_food(-troops_recruited)
                    city.set_gold(-troops_recruited)
                    self.recruits += troops_recruited
                    # testing results of input
                    print(
                        f"{troops_recruited} fresh troops recruited into your military.")
                    print(f"Food reserves remaining: {city.get_food()}")
                    print(f"City gold reserves remaining: {city.get_gold()}")
                    print("")
                    return
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

        def calc_max_envoys(self, culture_input, gold_input):
            if (culture_input < 1) or (gold_input < 1):
                print("Looks like you are lacking either culture or gold.")
                self.max_envoys = 0
            else:
                self.max_envoys = ((gold_input + culture_input)) // 2
                lesser_input = min(gold_input, culture_input)
                if (self.max_envoys > lesser_input):
                    self.max_envoys = lesser_input

        def send_envoys(self):

            self.calc_max_envoys(city.get_culture(), city.get_gold())

            print("")
            print(
                f"How many envoys (0-{self.get_max_envoys()} cost: 1 gold + 1 culture each) would you like to send on missions to neighbooring kingdoms in order to increase your Infleunce?")
            envoys_sent = input("--> ")
            try:
                envoys_sent = int(envoys_sent)
                # continue to define function from here
                if (envoys_sent <= self.get_max_envoys()) and (envoys_sent >= 0):
                    city.set_culture(-envoys_sent)
                    city.set_gold(-envoys_sent)
                    self.envoys_sent += envoys_sent
                    return
                elif envoys_sent < 0:
                    print(
                        f"Please enter a positive whole number between 0-{self.get_max_envoys()}.")
                    self.send_envoys()
                else:
                    print(
                        "Looks like you are lacking either gold or culture to send that many envoys.")
                    self.send_envoys()
            except:
                print(f"Please enter between 0-{self.get_max_envoys()}.")
                self.send_envoys()

        def calc_max_buildings(self, influence_input, gold_input):
            if (influence_input < 1) or (gold_input < 1):
                self.max_buildings = 0
            else:
                self.max_buildings = ((gold_input + influence_input)) // 2
                lesser_input = min(gold_input, influence_input)
                if (self.max_buildings > lesser_input):
                    self.max_buildings = lesser_input

        def construct_buildings(self):

            self.calc_max_buildings(city.get_influence(), city.get_gold())

            print("")
            print(
                f"How many monuments (0-{self.get_max_buildings()} cost: 1 gold + 1 influence each) would you like to construct in order to increase the culture of your city?")
            buildings_constructed = input("--> ")
            try:
                buildings_constructed = int(buildings_constructed)
                # continue to define function from here
                if (buildings_constructed <= self.get_max_buildings()) and (buildings_constructed >= 0):
                    city.set_influence(-buildings_constructed)
                    city.set_gold(-buildings_constructed)
                    self.buildings += buildings_constructed
                    return
                elif buildings_constructed < 0:
                    print(
                        f"Please enter a positive whole number between 0-{self.get_max_buildings()}.")
                    self.construct_buildings()
                else:
                    print(
                        "Looks like you are lacking either gold or influence to build that many monuments.")
                    self.construct_buildings()
            except:
                print(f"Please enter between 0-{self.get_max_buildings()}.")
                self.construct_buildings()

        def show_player_choices_summary(self):
            print("")
            print("----------------------------------------------------")
            print("You have decreed the following orders for this turn:")
            print("----------------------------------------------------")
            print(
                f"Gold Invested to encourage immigration: {self.pop_investment}")
            print(
                f"Acres of farmland planted with crops: {self.acres_planted}")
            print(f"Food sold at market for gold: {self.food_sold}")
            print(
                f"Military units sent on forrays to capture enemy territory: {self.forrays_sent}")
            print(
                f"Fresh troops recruited into your military forces: {self.recruits}")
            print(
                f"Envoys sent on diplomatic missions to increase your influence: {self.envoys_sent}.")
            print(
                f"Monuments built for the cultural glory of your city: {self.buildings}.")

        # randomization of resource allocation outcomes
        fate_list = [
            "terrible",
            "poor",
            "fair",
            "good",
            "excellent"
        ]

        fate_modifier_dict = {
            "terrible": 0.25,
            "poor": 0.5,
            "fair": 1,
            "good": 1.2,
            "excellent": 1.5
        }

        def outcomes(self):
            print("")
            print("------------")
            print("Turn Summary")
            print("------------")

            # population investment
            if turn.pop_investment == 0:
                print("You did not invest in immigration this turn.")
            else:
                population_fate_description_key = random.choice(self.fate_list)
                population_fate_modifier = self.fate_modifier_dict[population_fate_description_key]
                population_change = round(
                    (turn.pop_investment * population_fate_modifier))
                city.set_population(population_change)
                print(
                    f"The results of your immigration efforts were {population_fate_description_key}. You have gained {population_change} subjects.")

            # acres planted
            if turn.acres_planted == 0:
                print("You did not command any crops to be planted this turn.")
            else:
                acres_fate_description_key = random.choice(self.fate_list)
                acres_fate_modifier = self.fate_modifier_dict[acres_fate_description_key]
                acres_change = round(
                    (turn.acres_planted * acres_fate_modifier))
                city.set_food(acres_change)
                print(
                    f"The harvest was {acres_fate_description_key}. You have added {acres_change} bushels of crops to your granary.")

            # food sold
            if turn.food_sold == 0:
                print("You did not sell any food at market this turn.")
            else:
                food_fate_description_key = random.choice(self.fate_list)
                food_fate_modifier = self.fate_modifier_dict[food_fate_description_key]
                gold_change = round(
                    (turn.food_sold * food_fate_modifier))
                city.set_gold(gold_change)
                print(
                    f"Market conditions were {food_fate_description_key}. You have gained {gold_change} gold through food sales.")

            # forrays sent
            if turn.forrays_sent == 0:
                print(
                    "You did not send any military forrays try to capture land this turn.")
            else:
                forrays_fate_description_key = random.choice(self.fate_list)
                forrays_fate_modifier = self.fate_modifier_dict[forrays_fate_description_key]
                land_change = round(
                    (turn.forrays_sent * forrays_fate_modifier))
                city.set_land(land_change)
                print(
                    f"Battlefield conditions were {forrays_fate_description_key}. Your military forrays have gained {land_change} acres of land through conquest.")

            # recruits
            if turn.recruits == 0:
                print("You did not attempt to recruit any new soldiers this turn.")
            else:
                recruits_fate_description_key = random.choice(self.fate_list)
                recruits_fate_modifier = self.fate_modifier_dict[recruits_fate_description_key]
                strength_change = round(
                    (turn.recruits * recruits_fate_modifier))
                city.set_strength(strength_change)
                print(
                    f"Military recruiting results were {recruits_fate_description_key}. You have added {strength_change} troops to your forces.")

            # envoys sent
            if turn.envoys_sent == 0:
                print("You did not send any envoys on diplomatic missions this turn.")
            else:
                envoys_fate_description_key = random.choice(self.fate_list)
                envoys_fate_modifier = self.fate_modifier_dict[envoys_fate_description_key]
                influence_change = round(
                    (turn.envoys_sent * envoys_fate_modifier))
                city.set_influence(influence_change)
                print(
                    f"Diplomatic relations were {envoys_fate_description_key}. Your city has gained {influence_change} influence in the region.")

            # buildings
            if turn.buildings == 0:
                print("You did not build any monuments this turn.")
            else:
                buildings_fate_description_key = random.choice(self.fate_list)
                buildings_fate_modifier = self.fate_modifier_dict[buildings_fate_description_key]
                culture_change = round(
                    (turn.buildings * buildings_fate_modifier))
                city.set_culture(culture_change)
                print(
                    f"Monument construction progress was {buildings_fate_description_key}. Your city has gained {culture_change} culture.")

            print("")

    # turn object instantiate
    turn = Turn(0, 0, 0, 0, 0, 0, 0)

    # Player set up
    print("")
    print('*'*40)
    print("*                                      *")
    print("*    Welcome to the city of Ashkagar   *")
    print("*                                      *")
    print('*'*40)
    print(
        f"You are the ruler of this ancient city-state. Try to survive {game.get_length()} turns!")
    print("")
    print("Your Score is based on the combination of your Culture and Influence.")
    print("")
    print("Remember that you will need resources in order to maintain and defend your city, as well as investing them in growing your power.")
    print("")

    while game_running == True:
        print("")
        player_name = input("What is your name, mighty ruler? --> ")
        if player_name != "":
            print("")
            print(
                f"Very well, {player_name}. May your reign be long and prosperous!")
            break
        else:
            print("")
            print("Our scribes could not understand this. Please declare your name.")

    while True:  # start main game loop

        def pause_loop():
            while True:
                print("")
                foo = input("*** Press the 'Enter' key to continue *** --> ")
                print("")
                break
        # here are functions defined within the main gameplay loop function

        def run_player_prompts():
            turn.choose_population_investment()
            turn.plant_crops()
            turn.sell_food()
            turn.send_forrays()
            turn.recruit_soldiers()
            turn.send_envoys()
            turn.construct_buildings()

        def check_population():
            if city.get_population() < 1:
                print("")
                print("Your city is empty! You have no more people to rule.")
                game.lose()

        def check_food():
            food_available = city.get_food()
            food_needed = city.get_population() // 2
            if food_available < food_needed:
                print("")
                print("You do not have enough food to feed your people!")
                print(f"You have {food_available} and need {food_needed}.")
                print("There are riots in the streets! You are deposed as ruler.")
                game.lose()
            else:
                print(f"{food_needed} units of food consumed to feed the populace.")

        def check_gold():
            gold_available = city.get_gold()
            gold_needed = city.get_strength() // 2
            if gold_available < gold_needed:
                print("")
                print("You do not have gold in your treasury to pay your troops!!")
                print(f"You have {gold_available} and need {gold_needed}.")
                print("Your generals rise up in a coup and depose you.")
                game.lose()
            else:
                print(f"{gold_needed} gold pieces paid in wages to your military.")

        def check_strength():
            strength_available = city.get_strength()
            strength_needed = round(city.get_population() // 4)
            if strength_available < strength_needed:
                print("")
                print("You do not have enough military strength to defend your borders!")
                print(
                    f"You have {strength_available} troops and need {strength_needed}.")
                print("Your enemies invade and conquer your city.")
                game.lose()
            else:
                print(
                    f"{strength_needed} troops are assigned to defend your land.")

        def levy_taxes():
            tax_income = round(city.get_population() // 5)
            turn.set_tax_revenue(tax_income)
            city.set_gold(tax_income)
            print(
                f"{turn.tax_revenue} gold was collected through taxing the populace.")

        def natural_population_growth():
            pop_growth = (round(city.get_population() // 10))
            if pop_growth < 1:
                pop_growth = 1
            # turn.set_pop_growth(pop_growth)
            city.set_population(pop_growth)
            print(f"Your population grows naturally by {pop_growth}")

        def check_upkeep():
            print("-----------------")
            print("Upkeep and Income")
            print("-----------------")
            check_population()
            check_food()
            check_gold()
            check_strength()
            levy_taxes()
            natural_population_growth()

        def check_turn():
            if (game.turn > game.get_length()):
                game.win()

        # Below is the core gameplay loop
        game.increment_turn()
        check_turn()

        pause_loop()
        city.show_city_stats()

        run_player_prompts()
        turn.show_player_choices_summary()

        pause_loop()
        turn.outcomes()

        check_upkeep()
        game.adjust_score(city.get_culture() + city.get_influence())

        turn.clear_properties()


while game_running == True:
    main()
