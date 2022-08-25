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


class Character:

    def __init__(self, name):
        self.strength = None
        self.stats = []
        self.name = name
        self.race = None
        self.dndclass = None
        self.stat_choice()

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
        self.strength = int(input("Enter your Strength stat: "))
        while self.strength not in self.stats:
            print("Please choose a valid stat.")
            self.strength = int(input("Enter your Strength stat: "))
        self.stats.remove(self.strength)
        print("Please choose your Dexterity stat:")
        self.dexterity = int(input("Enter your Dexterity stat: "))


class DNDClass:
    def __init__(self, name):
        self.name = name
        self.allowed_skills = []
        self.skill_points = 0
        self.pri_skills = []

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
                    choice_skill = input("Do you want to be proficent in this skill? Yes or No: ")
                    if choice_skill.lower() in ["y", "yes"]:
                        self.pri_skills.append(add_skill)
                    else:
                        continue


myname = input('enter a name: ')
mychar = Character(myname)
barbarian_class = DNDClass("Barbarian")
barbarian_class.allowed_skills = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival']
barbarian_class.skill_points = 2
mychar.dndclass = barbarian_class

mychar.dndclass.select_pri_skills()

print("Your primary skills are: ", mychar.dndclass.pri_skills)

print("Your final stats are: ")
print("Strength: ", strength)
print("Dexterity: ", dexterity)
print("Constitution: ", constitution)
print("Intelligence: ", intelligence)
print("Wisdom: ", wisdom)
print("Charisma: ", charisma)
