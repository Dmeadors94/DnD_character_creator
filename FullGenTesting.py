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
'''
# Run StatGen
def startstats():
    dicerolls = []
    for d6Roll in range(4):
        rolls = random.randint(1, 6)
        dicerolls.append(rolls)
    del dicerolls[dicerolls.index(min(dicerolls))]  # deletes the lowest number
    stat = sum(dicerolls)  # totals the remaining 3 numbers
    return stat


print("Please assign the stats to the following stats:")
print("Strength: Your physical power")
print("Dexterity: Your agility and swiftness")
print("Constitution: Your endurance")
print("Intelligence: Your reasoning and memory")
print("Wisdom: Your perception and insight")
print("Charisma: Your force of personality")
while True:
    stats = []
    for stat in range(6):
        stats.append(startstats())
    print("Your stats are: ", stats)
    reroll_choice = input("Do you want to re-roll your stats? Yes or No: ")
    if reroll_choice.lower() in ["y", "yes"]:
        continue
    elif reroll_choice.lower() in ["n", "no"]:
        break
    else:
        print("Please choose Yes or No.")
        continue
print("Your stats are: ", stats)
'''


class Character:

    def __init__(self, name):
        self.name = name
        self.race = None
        self.dndclass = None


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
            #
            add_skill = self.allowed_skills.pop(add_skill_index)
            self.pri_skills.append(add_skill)


myname = input('enter a name: ')
mychar = Character(myname)
barbarian_class = DNDClass("Barbarian")
barbarian_class.allowed_skills = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival']
barbarian_class.skill_points = 2
mychar.dndclass = barbarian_class

mychar.dndclass.select_pri_skills()

print("Your primary skills are: ", mychar.dndclass.pri_skills)

'''
while True:
    strength = input("Out of your stats, which one should be Strength?\n")
    try:
        strength = int(strength)
        if strength in stats:
            stats.remove(int(strength))
            str_mod = Modcal.Modcal(strength)
            print("Your Strength Modifier is: ", str_mod)
            print("Your remaining stats are: ", stats)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter one of your stats")
    except IndexError:
        print("Please enter one of your stats")

    continue
while True:
    dexterity = input("Out of your stats, which one should be Dexterity?\n")
    try:
        dexterity = int(dexterity)
        if dexterity in stats:
            stats.remove(int(dexterity))
            dex_mod = Modcal.Modcal(dexterity)
            print("Your Dexterity Modifier is: ", dex_mod)
            print("Your remaining stats are: ", stats)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter one of your stats")
    except IndexError:
        print("Please enter one of your stats")
    continue
while True:
    constitution = input("Out of your stats, which one should be Constitution?\n")
    try:
        constitution = int(constitution)
        if constitution in stats:
            stats.remove(int(constitution))
            con_mod = Modcal.Modcal(constitution)
            print("Your Constitution Modifier is: ", con_mod)
            print("Your remaining stats are: ", stats)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter one of your stats")
    except IndexError:
        print("Please enter one of your stats")
    continue
while True:
    intelligence = input("Out of your stats, which one should be Intelligence?\n")
    try:
        intelligence = int(intelligence)
        if intelligence in stats:
            stats.remove(int(intelligence))
            int_mod = Modcal.Modcal(intelligence)
            print("Your Intelligence Modifier is: ", int_mod)
            print("Your remaining stats are: ", stats)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter one of your stats")
    except IndexError:
        print("Please enter one of your stats")
    continue
while True:
    wisdom = input("Out of your stats, which one should be Wisdom?\n")
    try:
        wisdom = int(wisdom)
        if wisdom in stats:
            stats.remove(int(wisdom))
            wis_mod = Modcal.Modcal(wisdom)
            print("Your Wisdom Modifier is: ", wis_mod)
            print("Your remaining stat is: ", stats)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter one of your stats")
    except IndexError:
        print("Please enter one of your stats")
while True:
    charisma = input("Out of your stats, which one should be Charisma?\n")
    try:
        charisma = int(charisma)
        if charisma in stats:
            stats.remove(int(charisma))
            cha_mod = Modcal.Modcal(charisma)
            print("Your Charisma Modifier is: ", cha_mod)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter on of your stats")
    except IndexError:
        print("Please enter one of your stats")

print("Your final stats are: ")
print("Strength: ", strength)
print("Dexterity: ", dexterity)
print("Constitution: ", constitution)
print("Intelligence: ", intelligence)
print("Wisdom: ", wisdom)
print("Charisma: ", charisma)
'''
