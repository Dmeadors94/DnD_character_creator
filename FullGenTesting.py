import random

import Modcal

skill_dict = {
    "Acrobatics": "The ability to move through the air with ease. This skill is used to make graceful jumps and to "
                  "make graceful glides.",
    "Animal Handling": "The ability to calm and control wild animals. This skill is used to calm and control "
                       "wild animals.",
    "Arcana": "The ability to read the magical symbols and to interpret magical effects. This skill is used to "
              "read the magical symbols and to interpret magical effects.",
    "Athletics": "The ability to perform physical feats of strength and dexterity. This skill is used to perform "
                 "physical feats of strength and dexterity.",
    "Intimidation": "The ability to intimidate people. This skill is used to intimidate people.",
    "Nature": "The ability to control the natural world. This skill is used to control the natural world.",
    "Perception": "The ability to notice things around you. This skill is used to notice things around you.",
    "Survival": "The ability to survive in the wild. This skill is used to survive in the wild.",
}


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
        self.name = name
        self.allowed_skills = []
        self.skill_points = 0
        self.pri_skills = []
        self.class_features = []

    def select_pri_skills(self):
        self.pri_skills = []

        for x in range(self.skill_points):
            for i, skill in enumerate(self.allowed_skills, start=1):
                print(i, skill)
            add_skill_index = input(f'Please select skill {x + 1}: ')
            try:
                add_skill_index = int(add_skill_index) - 1
            except ValueError:
                print("This is not a valid number.")
                add_skill_index = -1
            while add_skill_index < 0 or add_skill_index > (len(self.allowed_skills) - 1):
                add_skill_index = input(f'That skill is not in the allowed skills. Please select skill {x + 1}: ')
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
        self.stat_choice()
        self.race_choice()
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
                barbarian_class.skill_points = 2
                barbarian_class.class_features = ["Rage", "Unarmored Defense"]
                self.dndclass = barbarian_class


myname = input('enter a name: ')
mychar = Character(myname)

mychar.dndclass.select_pri_skills()

print("Your primary skills are: ", mychar.dndclass.pri_skills)

print("Your final stats are: ")
print("Strength: ", mychar.strength + mychar.race.ability_bonuses)
print("Dexterity: ", mychar.dexterity + mychar.race.ability_bonuses)
print("Constitution: ", mychar.constitution + mychar.race.ability_bonuses)
print("Intelligence: ", mychar.intelligence + mychar.race.ability_bonuses)
print("Wisdom: ", mychar.wisdom + mychar.race.ability_bonuses)
print("Charisma: ", mychar.charisma + mychar.race.ability_bonuses)
