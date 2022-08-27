import random

import Modcal

skill_dict = {
    "Acrobatics": "Acrobatics covers your attempt to stay on your feet in a tricky situation, such as when you’re "
                  "\ntrying to run across a sheet of ice, balance on a tightrope, or stay upright on a rocking ship’s "
                  "\ndeck.",
    "Animal Handling": "Your skill with animals allows you to befriend them and even command them.",
    "Arcana": "Arcana covers the study of the magical and the supernatural.",
    "Athletics": "Athletics covers your ability to perform simple physical tasks, such as jumping, climbing, "
                 "\nswimming, or performing other manual tasks.",
    "Deception": "Deception covers your ability to convincingly hide the truth.",
    "History": "History covers the study of past events and your ability to recall lore about them.",
    "Insight": "Insight covers your ability to notice details and hidden qualities in people and things.",
    "Intimidation": "Intimidation covers your ability to convincingly force others to do what you want.",
    "Investigation": "Investigation covers your ability to look into the nature of things, such as the origin of "
                     "\nplants and animals, the causes of things, or the effects of things.",
    "Medicine": "Medicine covers the study of the sick and the wounded.",
    "Nature": "Nature covers the study of the natural world, including the study of the animals, plants, and "
              "\nminerals found in the world.",
    "Perception": "Perception covers your ability to notice things that are nearby, in the room, or at the "
                  "\nconvenience of others.",
    "Performance": "Performance covers your ability to act in a manner that draws attention to you.",
    "Persuasion": "Persuasion covers your ability to convincingly force others to do what you want.",
    "Religion": "Religion covers the study of the gods, their history, and their relationship to you.",
    "Sleight of Hand": "Sleight of Hand covers your ability to move objects without being seen.",
    "Stealth": "Stealth covers your ability to hide from enemies without being seen.",
    "Survival": "Survival covers your ability to recognize the signs of danger, notice the location of hidden "
                "\nthings, and avoid or outsmart groups of enemies."

}
simple_weapon_dict = {
    "Club": ["A simple weapon consisting of a club with a handle.", "1d4 Bludgeoning",
             "Light - Ideal for two-weapon fighting"],
    "Dagger": ["A sharp, light, and pointy weapon.", "1d4 Piercing",
               "Finesse - You may use your Dexterity modifier instead"
               "of your Strength modifier for attack rolls."],
    "Greatclub": ["A heavy and large club that requires both hands.", "1d8 Bludgeoning", "Two-Handed - Requires "
                                                                                         "both hands"],
    "Handaxe": ["A light and sharp axe cable of being thrown.", "1d6 Slashing", "Light - Ideal for two-weapon fighting",
                "Thrown - Range is 20ft for normal throws and 60ft for long throws."],
    "Javelin": ["A long slender piece of wood with a sharp metal tip.", "1d6 Piercing", "Thrown - Range is 30ft for "
                                                                                        "normal throws and 120ft "
                                                                                        "for long throws."],
    "Light Hammer": ["A simple light-weight hammer.", "1d4 Bludgeoning", "Light - Ideal for two-weapon fighting",
                     "Thrown - Range is 20ft for normal throws and 60ft for long throws."],
    "Mace": ["A short piece of wood that has a rounded metal head for clubbing.", "1d6 Bludgeoning"],
    "Quarterstaff": ["A long carved piece of wood made for walking and fighting.", "1d6 Bludgeoning", "Versatile - "
                                                                                                      "May be used "
                                                                                                      "with two hands "
                                                                                                      "to do 1d8 "
                                                                                                      "damage instead "
                                                                                                      "of 1d6."],
    "Sickle": ["A curved piece of metal with a handle ment for farming.", "1d4 Slashing",
               "Light - Ideal for two-weapon "
               "fighting"],
    "Spear": ["A long piece of wood with a sharp metal tip.", "1d6 Piercing", "Thrown - Range is 20ft for normal "
                                                                              "throws and 60ft for long throws.,"
                                                                              "Versatile - May be used with two hands "
                                                                              "to do 1d8 damage instead of 1d6."],
    "Light Crossbow": ["A ranged weapon ment to propel light bolts at a distance.", "1d8 Piercing", "Ammunition - This "
                                                                                                    "weapon has a "
                                                                                                    "range of 80ft "
                                                                                                    "for normal shots "
                                                                                                    "and 320ft for "
                                                                                                    "long shots.",
                       "Loading - You may "
                       "only fire this weapon once per Action, Bonus Action, or Reaction.", "Two-handed - Requires "
                                                                                            "two hands to use."],
    "Dart": ["A small piece of metal with a sharp tip ment for throwing.", "1d4 Piercing", "Thrown - Range is 20ft for "
                                                                                           "normal throws and 60ft "
                                                                                           "for long throws.",
             "Finesse - You may use your Dexterity modifier instead of your "
             "Strength modifier for attack rolls."],
    "Shortbow": ["A short piece of wood with a draw string to fire arrows.", "1d6 Piercing", "Ammunition - This weapon "
                                                                                             "has a range of 80ft for "
                                                                                             "normal shots and 320ft "
                                                                                             "for long shots.",
                 "Two-handed - Requires two hands to "
                 "use."],
    "Sling": ["A simple sling made for throwing small objects.", "1d4 Bludgeoning", "Ammunition - This weapon has a "
                                                                                    "range of 30ft for normal shots "
                                                                                    "and 120ft for long shots."]}
martial_weapon_dict = {
    "Battleaxe": ["A two-headed axe that would be used with two hands.", "1d8 Slashing", "Versatile - May be "
                                                                                         "used with two "
                                                                                         "hands to do 1d10 "
                                                                                         "damage instead of 1d8."],
    "Flail": ["A spiked ball on a chain.", "1d8 Bludgeoning"],
    "Glaive": ["A long pole of wood with a long curved piece of metal on the end.", "1d10 Slashing",
               "Heavy - Small creatures have disadvantage on attack rolls.", "Reach - Adds 5ft to your attack range.",
               "Two-Handed - This weapon must be used with both hands."],
    "Greataxe": ["A large two-handed and grand axe ment for battle.", "1d12 Slashing", "Heavy - Small creatures have "
                                                                                       "disadvantage on attack rolls.",
                 "Two-Handed - Must be used with both hands."]}


# Run StatGen
def startstats():
    dicerolls = []
    for d6Roll in range(4):
        rolls = random.randint(1, 6)
        dicerolls.append(rolls)
    del dicerolls[dicerolls.index(min(dicerolls))]  # deletes the lowest number
    stat = sum(dicerolls)  # totals the remaining 3 numbers
    return stat


class DNDClass:
    def __init__(self, name):
        self.equipment_list = []
        self.name = name
        self.allowed_skills = []
        self.skill_points = 0
        self.pri_skills = []
        self.class_features = []
        self.allowed_equipment_choice_one = []
        self.allowed_equipment_choice_two = []
        self.static_equipment = []
        self.is_a_spell_caster = False

    def select_pri_skills(self):
        self.pri_skills = []
        escape = False
        while not escape:
            for x in range(self.skill_points):
                for i, skill in enumerate(self.allowed_skills, start=1):
                    print(i, skill)
                add_skill_index = input(f'Please select skill : ')
                try:
                    add_skill_index = int(add_skill_index) - 1
                except ValueError:
                    print("This is not a valid number.")
                    add_skill_index = -1
                while add_skill_index < 0 or add_skill_index > (len(self.allowed_skills) - 1):
                    add_skill_index = input(f'That skill is not in the allowed skills. Please select skill : ')
                    try:
                        add_skill_index = int(add_skill_index) - 1
                    except ValueError:
                        print("This is not a valid number.")
                        add_skill_index = -1
                add_skill = self.allowed_skills.pop(add_skill_index)
                for y in dict.keys(skill_dict):
                    if y == add_skill:
                        print(f'{skill_dict[y]}')
                        choice_skill = input("Do you want to be proficient in this skill? Yes or No: ")
                        if choice_skill.lower() in ["y", "yes"]:
                            self.pri_skills.append(add_skill)
                            escape = True
                        else:
                            self.allowed_skills.insert(add_skill_index, add_skill)
                            if self.skill_points < 2:
                                self.skill_points += 1
                                continue
                            else:
                                continue

    def select_equipment(self):
        print("Please select from the following list of equipment:")
        for i, equipment in enumerate(self.allowed_equipment_choice_one, start=1):
            print(i, equipment)
        choice_one = input("Please select equipment 1: ")
        try:
            choice_one = int(choice_one) - 1
        except ValueError:
            print("This is not a valid number.")
            choice_one = -1
        while choice_one < 0 or choice_one > (len(self.allowed_equipment_choice_one) - 1):
            choice_one = input(f'That equipment is not in the allowed equipment. Please select equipment 1: ')
            try:
                choice_one = int(choice_one) - 1
            except ValueError:
                print("This is not a valid number.")
                choice_one = -1
        choice_one = self.allowed_equipment_choice_one.pop(choice_one)
        print("Please select from the following list of equipment:")
        for i, equipment in enumerate(self.allowed_equipment_choice_two, start=1):
            print(i, equipment)
        choice_two = input("Please select equipment 2: ")
        try:
            choice_two = int(choice_two) - 1
        except ValueError:
            print("This is not a valid number.")
            choice_two = -1
        while choice_two < 0 or choice_two > (len(self.allowed_equipment_choice_two) - 1):
            choice_two = input(f'That equipment is not in the allowed equipment. Please select equipment 2: ')
            try:
                choice_two = int(choice_two) - 1
            except ValueError:
                print("This is not a valid number.")
                choice_two = -1
        choice_two = self.allowed_equipment_choice_two.pop(choice_two)
        self.equipment_list.append(choice_one)
        self.equipment_list.append(choice_two)
        self.equipment_list.append(self.static_equipment)
        while "Any Simple Weapon" in self.equipment_list:
            self.select_simple_weapon()

    def select_simple_weapon(self):
        selections = dict(enumerate(simple_weapon_dict))
        for i, weapon in enumerate(simple_weapon_dict, start=1):
            print(i, weapon)
        choice_weapon = input("Please select a simple weapon: ")
        try:
            choice_weapon_a = int(choice_weapon) - 1
        except ValueError:
            print("This is not a valid number.")
            choice_weapon_a = -1
        while choice_weapon_a < 0 or choice_weapon_a > (len(simple_weapon_dict) - 1):
            choice_weapon = input(f'That weapon is not in the allowed weapons. Please select a simple weapon: ')
            try:
                choice_weapon_a = int(choice_weapon) - 1
            except ValueError:
                print("This is not a valid number.")
                choice_weapon_a = -1
        choice_weapon_a = selections[choice_weapon_a]
        for y in dict.keys(simple_weapon_dict):
            if y == choice_weapon_a:
                print(f'{simple_weapon_dict[y]}')
                choice_skill = input("Do you want this Weapon? Yes or No: ")
                if choice_skill.lower() in ["y", "yes"]:
                    self.equipment_list.append(choice_weapon_a)
                    self.equipment_list.remove("Any Simple Weapon")
                    break
                else:
                    continue


class DNDRace:

    def __init__(self, name):
        self.name = name
        self.speed = None
        self.size = None
        self.languages = None
        self.ability_bonuses = None
        self.traits = None
        self.features = None
        self.racial_skills = None
        self.racial_prof = None


class Character:

    def __init__(self, name):
        self.equipment_list = []
        self.strength = None
        self.str_mod = None
        self.dexterity = None
        self.dex_mod = None
        self.constitution = None
        self.con_mod = None
        self.intelligence = None
        self.int_mod = None
        self.wisdom = None
        self.wis_mod = None
        self.charisma = None
        self.cha_mod = None
        self.stats = []
        self.name = name
        self.race = None
        self.dndclass = None
        # self.stat_choice()
        # self.race_choice()
        self.class_choice()

    def stat_choice(self):
        print("Please assign the stats to the following stats:")
        print("Strength: Your physical power")
        print("Dexterity: Your agility and swiftness")
        print("Constitution: Your endurance")
        print("Intelligence: Your reasoning and memory")
        print("Wisdom: Your perception and insight")
        print("Charisma: Your force of personality")
        while True:
            self.stats = []
            for stat in range(6):
                self.stats.append(startstats())
            print("Your stats are: ", self.stats)
            reroll_choice = input("Do you want to re-roll your stats? Yes or No: ")
            if reroll_choice.lower() in ["y", "yes"]:
                continue
            elif reroll_choice.lower() in ["n", "no"]:
                break
            else:
                print("Please choose Yes or No.")
                continue
        print("Your stats are: ", self.stats)
        print("Please choose your Strength stat:")
        try:
            self.strength = int(input("Enter your Strength stat: "))
        except ValueError:
            print("Please enter a number.")
            self.strength = -1
        while self.strength not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.strength = int(input("Enter your Strength stat: "))
            except ValueError:
                print("Please enter a number.")
                self.strength = -1
        self.stats.remove(self.strength)
        self.str_mod = Modcal.Modcal(self.strength)
        print("Your Strength Modifier is: ", self.str_mod)
        print(self.stats)
        print("Please choose your Dexterity stat:")
        try:
            self.dexterity = int(input("Enter your Dexterity stat: "))
        except ValueError:
            print("Please enter a number.")
            self.dexterity = -1
        while self.dexterity not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.dexterity = int(input("Enter your Dexterity stat: "))
            except ValueError:
                print("Please enter a number.")
                self.dexterity = -1
        self.stats.remove(self.dexterity)
        self.dex_mod = Modcal.Modcal(self.dexterity)
        print("Your Dexterity Modifier is: ", self.dex_mod)
        print(self.stats)
        print("Please choose your Constitution stat:")
        try:
            self.constitution = int(input("Enter your Constitution stat: "))
        except ValueError:
            print("Please enter a number.")
            self.constitution = -1
        while self.constitution not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.constitution = int(input("Enter your Constitution stat: "))
            except ValueError:
                print("Please enter a number.")
                self.constitution = -1
        self.stats.remove(self.constitution)
        self.con_mod = Modcal.Modcal(self.constitution)
        print("Your Constitution Modifier is: ", self.con_mod)
        print(self.stats)
        print("Please choose your Intelligence stat:")
        try:
            self.intelligence = int(input("Enter your Intelligence stat: "))
        except ValueError:
            print("Please enter a number.")
            self.intelligence = -1
        while self.intelligence not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.intelligence = int(input("Enter your Intelligence stat: "))
            except ValueError:
                print("Please enter a number.")
                self.intelligence = -1
        self.stats.remove(self.intelligence)
        self.int_mod = Modcal.Modcal(self.intelligence)
        print("Your Intelligence Modifier is: ", self.int_mod)
        print(self.stats)
        print("Please choose your Wisdom stat:")
        try:
            self.wisdom = int(input("Enter your Wisdom stat: "))
        except ValueError:
            print("Please enter a number.")
            self.wisdom = -1
        while self.wisdom not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.wisdom = int(input("Enter your Wisdom stat: "))
            except ValueError:
                print("Please enter a number.")
                self.wisdom = -1
        self.stats.remove(self.wisdom)
        self.wis_mod = Modcal.Modcal(self.wisdom)
        print("Your Wisdom Modifier is: ", self.wis_mod)
        print(self.stats)
        print("Please choose your Charisma stat:")
        try:
            self.charisma = int(input("Enter your Charisma stat: "))
        except ValueError:
            print("Please enter a number.")
            self.charisma = -1
        while self.charisma not in self.stats:
            print("Please choose a valid stat.")
            try:
                self.charisma = int(input("Enter your Charisma stat: "))
            except ValueError:
                print("Please enter a number.")
                self.charisma = -1
        self.stats.remove(self.charisma)
        self.cha_mod = Modcal.Modcal(self.charisma)
        print("Your Charisma Modifier is: ", self.cha_mod)
        print("Your stats are: ")
        print("Strength: ", self.strength, "Modifier: ", self.str_mod)
        print("Dexterity: ", self.dexterity, "Modifier: ", self.dex_mod)
        print("Constitution: ", self.constitution, "Modifier: ", self.con_mod)
        print("Intelligence: ", self.intelligence, "Modifier: ", self.int_mod)
        print("Wisdom: ", self.wisdom, "Modifier: ", self.wis_mod)
        print("Charisma: ", self.charisma, "Modifier: ", self.cha_mod)

    def race_choice(self):
        print("Please select a Race: ")
        print("1. Human")
        race_selection = input("Enter your choice: ")
        if race_selection == "1":
            print("Humans come in all shapes and sizes. Humans get +1 to all stats and a extra language"
                  "of your choice.")
            print("Are you sure you want to be a Human? Yes or No: ")
            human_choice = input("Enter your choice: ")
            if human_choice.lower() in ["y", "yes"]:
                human_race = DNDRace
                human_race.name = "Human"
                human_race.speed = "30ft"
                human_race.size = "Medium"
                human_race.languages = ["Common"]
                human_race.ability_bonuses = 1
                self.race = human_race

    def class_choice(self):
        print("Please select a Class: ")
        print("1. Barbarian")
        print("2. Bard")
        class_selection = input("Enter your choice: ")
        if class_selection == "1":
            print("Barbarians are strong and tough. They can Rage, causing them to have the following effects:\n"
                  "-They get advantage on Strength checks and Strength saving throws.\n"
                  "-They get +2 to their damage rolls for melee attacks.\n"
                  "-They get resistance to bludgeoning, piercing, and slashing damage.\n\n"
                  "Barbarians also have Unarmored Defense, which gives them +2 to AC while they are not wearing any "
                  "armor.")
            print("Are you sure you want to be a Barbarian? Yes or No: ")
            barb_choice = input("Enter your choice: ")
            if barb_choice.lower() in ["y", "yes"]:
                barbarian_class = DNDClass("Barbarian")
                barbarian_class.allowed_skills = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature',
                                                  'Perception',
                                                  'Survival']
                barbarian_class.allowed_equipment_choice_one = ['A Battleaxe', 'Any Martial Melee Weapon']
                barbarian_class.allowed_equipment_choice_two = ['Two Handaxes', 'Any Simple Weapon']
                barbarian_class.static_equipment = ["An Explorer's pack", 'Four Javelins']
                barbarian_class.skill_points = 2
                barbarian_class.class_features = ["Rage", "Unarmored Defense"]
                barbarian_class.is_a_spell_caster = False
                self.dndclass = barbarian_class
        elif class_selection == "2":
            print("Bards are quick and pretty. They can Sing, Dance, and Play an Instrument, causing them to give "
                  "Bardic Inspiration, which they can use on their allies to grant a Inspiration die of 1d6 to them")
            print("Are you sure you want to be a Bard? Yes or No: ")
            bard_choice = input("Enter your choice: ")
            if bard_choice.lower() in ["y", "yes"]:
                bard_class = DNDClass("Bard")
                bard_class.allowed_skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
                                             "History", "Insight", "Intimidation",
                                             "Investigation", "Medicine", "Nature", "Perception", "Performance",
                                             "Persuasion", "Religion",
                                             "Sleight of Hand", "Stealth", "Survival"]
                bard_class.allowed_equipment_choice_one = ["A Rapier", "A Longsword", "Any Simple Weapon"]
                bard_class.allowed_equipment_choice_two = ["A Diplomat's pack", "Entertainer's Pack"]
                bard_class.allowed_equipment_choice_three = ["A Lute", "Any other Musical Instrument"]
                bard_class.static_equipment = ["Leather Armor", "A Dagger"]
                bard_class.skill_points = 3
                bard_class.featurelist = ["Bardic Inspiration"]
                bard_class.is_a_spell_caster = True
                self.dndclass = bard_class


myname = input('enter a name: ')
mychar = Character(myname)

# mychar.dndclass.select_pri_skills()
mychar.dndclass.select_equipment()

print("Your primary skills are: ", mychar.dndclass.pri_skills)

print("Your final stats are: ")
mychar.str_mod = Modcal.Modcal(mychar.strength + mychar.race.ability_bonuses)
print("Strength: ", mychar.strength + mychar.race.ability_bonuses, "Modifier: ", mychar.str_mod)
mychar.dex_mod = Modcal.Modcal(mychar.dexterity + mychar.race.ability_bonuses)
print("Dexterity: ", mychar.dexterity + mychar.race.ability_bonuses, "Modifier: ", mychar.dex_mod)
mychar.con_mod = Modcal.Modcal(mychar.constitution + mychar.race.ability_bonuses)
print("Constitution: ", mychar.constitution + mychar.race.ability_bonuses, "Modifier :", mychar.con_mod)
mychar.int_mod = Modcal.Modcal(mychar.intelligence + mychar.race.ability_bonuses)
print("Intelligence: ", mychar.intelligence + mychar.race.ability_bonuses, "Modifier :", mychar.int_mod)
mychar.wis_mod = Modcal.Modcal(mychar.wisdom + mychar.race.ability_bonuses)
print("Wisdom: ", mychar.wisdom + mychar.race.ability_bonuses, "Modifier :", mychar.wis_mod)
mychar.cha_mod = Modcal.Modcal(mychar.charisma + mychar.race.ability_bonuses)
print("Charisma: ", mychar.charisma + mychar.race.ability_bonuses, "Modifier :", mychar.cha_mod)
