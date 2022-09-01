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
language_dict = {
    "Common": "The Common language is spoken by all creatures. It uses Common script",
    "Dwarvish": "The Dwarvish language is spoken by the Dwarves. It uses Dwarvish script.",
    "Elvish": "The Elvish language is spoken by the Elves. It uses Elvish script.",
    "Giant": "The Giant language is spoken by Giants and Ogres. It uses Dwarvish script.",
    "Gnomish": "The Gnomish language is spoken by Gnomes. It uses Dwarvish script.",
    "Goblin": "The Goblin language is spoken by Goblins. It uses Dwarvish script.",
    "Halfling": "The Halfling language is spoken by Halflings. It uses Common script.",
    "Orc": "The Orc language is spoken by Orcs. It uses Dwarvish script.",
    "Abyssal": "The Abyssal language is spoken by Demons. It uses Infernal script.",
    "Celestial": "The Celestial language is spoken by Celestials. It uses Celestial script.",
    "Deep Speech": "The Deep Speech language is spoken by Deep Speech creatures. It uses no known script.",
    "Draconic": "The Draconic language is spoken by Dragons and Dragonborn. It uses Draconic script.",
    "Infernal": "The Infernal language is spoken by Devils. It uses Infernal script.",
    "Primordial": "The Primordial language is spoken by Elementals. It uses Dwarvish script.",
    "Sylvan": "The Sylvan language is spoken by Fey creatures. It uses Elvish script.",
    "Undercommon": "The Undercommon language is spoken by Underworld Traders. It uses Elvish script."}
lang_race = ["Human", "Half-Elf"]
skill_list = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana",
              "History", "Investigation", "Nature", "Religion", "Animal Handling",
              "Insight", "Medicine", "Perception", "Survival", "Deception",
              "Intimidation", "Performance", "Persuasion"]

import random

monsters = {
    "Goblin": {"health": 10, "power": 2, "armor_class": 0},
    "Orc": {"health": 15, "power": 3, "armor_class": 13},
    "Troll": {"health": 30, "power": 6, "armor_class": 15},
    "Ogre": {"health": 50, "power": 9, "armor_class": 16},
    "Dragon": {"health": 75, "power": 12, "armor_class": 18},
}


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Enemy:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.attack_hit_chance = power
        self.attack_damage = power
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.attack_hit_chance + Dice(20).roll() >= enemy.armor_class:
            battle_damage = self.attack_damage + Dice(6).roll()
            enemy.health -= battle_damage
            print("{} attacks {} and does {} damage".format(self.name, enemy.name, battle_damage))
            print("{} has {} health remaining".format(enemy.name, enemy.health))
        else:
            print("{} attacks {} and misses!".format(self.name, enemy.name))
            print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.attack_damage))


class Character:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.attack_hit_chance = power
        self.attack_damage = power
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.attack_hit_chance + Dice(20).roll() >= enemy.armor_class:
            battle_damage = self.attack_damage + Dice(6).roll()
            enemy.health -= battle_damage
            print("{} attacks {} and does {} damage".format(self.name, enemy.name, battle_damage))
            print("{} has {} health remaining".format(enemy.name, enemy.health))
        else:
            print("{} attacks {} and misses!".format(self.name, enemy.name))
            print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.attack_damage))


random_mob = (random.choice(list(monsters.items())))
hero = Character("Hero", 10, 2, 13)
monster = Enemy(random_mob[0], random_mob[1]["health"], random_mob[1]["power"], random_mob[1]["armor_class"])


# Run StatGen
def startstats():
    dicerolls = []
    for d6Roll in range(4):
        rolls = random.randint(1, 6)
        dicerolls.append(rolls)
    del dicerolls[dicerolls.index(min(dicerolls))]  # deletes the lowest number
    stat = sum(dicerolls)  # totals the remaining 3 numbers
    return stat


def show_pri_skills():
    print("Your primary skills are: ", mychar.dndclass.pri_skills)

    print("Your final stats are: ")
    mychar.str_mod = Modcal.Modcal(mychar.strength + mychar.race.str_ability_bonus)
    print("Strength: ", mychar.strength + mychar.race.str_ability_bonus, "Modifier: ", mychar.str_mod)
    mychar.dex_mod = Modcal.Modcal(mychar.dexterity + mychar.race.dex_ability_bonus)
    print("Dexterity: ", mychar.dexterity + mychar.race.dex_ability_bonus, "Modifier: ", mychar.dex_mod)
    mychar.con_mod = Modcal.Modcal(mychar.constitution + mychar.race.con_ability_bonus)
    print("Constitution: ", mychar.constitution + mychar.race.con_ability_bonus, "Modifier :", mychar.con_mod)
    mychar.int_mod = Modcal.Modcal(mychar.intelligence + mychar.race.int_ability_bonus)
    print("Intelligence: ", mychar.intelligence + mychar.race.int_ability_bonus, "Modifier :", mychar.int_mod)
    mychar.wis_mod = Modcal.Modcal(mychar.wisdom + mychar.race.wis_ability_bonus)
    print("Wisdom: ", mychar.wisdom + mychar.race.wis_ability_bonus, "Modifier :", mychar.wis_mod)
    mychar.cha_mod = Modcal.Modcal(mychar.charisma + mychar.race.cha_ability_bonus)
    print("Charisma: ", mychar.charisma + mychar.race.cha_ability_bonus, "Modifier :", mychar.cha_mod)


class DNDClass:
    def __init__(self, name):
        self.god_choice = None
        self.cantrip_list = []
        self.first_level_spell_list = []
        self.professions = []
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
            for s in range(self.skill_points):
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

    def god_choice(self):
        print("As a Cleric, you must choose a God to follow. This will give you additional powers.")
        print("Please choose a god from the following list:")
        print("1. Leven - The God of Life. Their domain focuses on healing.")
        print("2. Ohen - The God of Light. Their domain focuses on the sun and fire")
        print("3. Raiz - The God of Nature. Their domain focuses on the animals and plants")
        print("4. Tempest - The God of Storms. Their domain focuses on the weather and the elements")
        print("5. Viden - The God of Knowledge. Their domain focuses on the accumulation of knowledge")
        print("6. Komik - The God of Trickery. Their domain focuses on the use of thievery and trickery")
        print("7. Slag - The God of War. Their domain focuses on the use of weapons and combat")
        print("8. Opas - The God of Death. Their domain focuses on the use of death, darkness, and blight")
        while True:
            try:
                god_choice_input = int(input("Enter your choice: "))
                if god_choice_input == 1:
                    print("You have chosen Leven. You have the following powers:")
                    print("=================================================================================")
                    print("You gain Proficiency in Heavy Armor.")
                    print("=================================================================================")
                    print("You gain the Class Feature: starting at 1st level, your healing spells are more")
                    print("effective. Whenever you use a spell of 1st level or higher to restore hit points "
                          "to a")
                    print(
                        "creature, the creature regains additional hit points equal to 2 + the spell's level.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Leven.")
                        self.god_choice = "Leven"
                        self.professions.append("Armor: Heavy")
                        self.class_features.append("Divine Domain: Life")
                        self.class_features.append("Disciple of Life")
                        self.first_level_spell_list.append("Cure Wounds")
                        self.first_level_spell_list.append("Bless")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 2:
                    print("You have chosen Ohen. You have the following powers:")
                    print("=================================================================================")
                    print("You gain the light cantrip.")
                    print("=================================================================================")
                    print("You gain the Class Feature: Warding Flare")
                    print("At 1st level, you can interpose divine light between yourself and an attacking")
                    print("enemy. When you are attacked by a creature within 30 feet of you that you can see,")
                    print("you can use your reaction to impose disadvantage on the attack roll, causing light "
                          "to")
                    print("flare before the attacker before it hits or misses. An attacker that can't be "
                          "blinded")
                    print("is immune to this feature. You can use this feature a number of times equal to your")
                    print("Wisdom modifier (a minimum of once). You regain all expended uses when you finish a")
                    print("long rest.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Ohen.")
                        self.god_choice = "Ohen"
                        self.class_features.append("Divine Domain: Light")
                        self.class_features.append("Warding Flare")
                        self.cantrip_list.append("Light")
                        self.first_level_spell_list.append("Burning Hands")
                        self.first_level_spell_list.append("Faire Fire")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 3:
                    print("You have chosen Raiz. You have the following powers:")
                    print("=================================================================================")
                    print(
                        "Acolyte of Nature: At 1st level, you learn one cantrip of your choice from the druid")
                    print("spell list. This cantrip counts as a cleric cantrip for you, but it doesn’t count")
                    print("against the number of cleric cantrips you know. You also gain proficiency in one of")
                    print("the following skills of your choice: Animal Handling, Nature, or Survival.")
                    print("=================================================================================")
                    print("You gain proficiency in Heavy Armor.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Raiz.")
                        self.god_choice = "Raiz"
                        self.class_features.append("Divine Domain: Nature")
                        self.professions.append("Armor: Heavy")
                        self.first_level_spell_list.append("Animal Friendship")
                        self.first_level_spell_list.append("Speak with Animals")
                        # TODO add skill select for god
                        print("Please choose a cantrip from the following list: ")
                        # TODO add cantrip choice for god
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 4:
                    print("You have chosen Tempest. You have the following powers:")
                    print("=================================================================================")
                    print("You gain proficiency with martial weapons and heavy armor.")
                    print("=================================================================================")
                    print("You gain the Class Feature: Wrath of the Storm")
                    print("Also at 1st level, you can thunderously rebuke attackers. When a creature within 5")
                    print("feet of you that you can see hits you with an attack, you can use your reaction to")
                    print(
                        "cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning")
                    print(
                        "or thunder damage (your choice) on a failed saving throw, and "
                        "half as much damage on a")
                    print("successful one. You can use this feature a number of times equal to your Wisdom")
                    print(
                        "modifier (a minimum of once). You regain all expended uses when you finish a "
                        "long rest.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Viden.")
                        self.god_choice = "Viden"
                        self.class_features.append("Divine Domain: Tempest")
                        self.professions.append("Armor: Heavy")
                        self.professions.append("Weapon: Martial")
                        self.first_level_spell_list.append("Fog Cloud")
                        self.first_level_spell_list.append("Thunderwave")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 5:
                    print("You have chosen Viden. You have the following powers:")
                    print("=================================================================================")
                    print("You gain the Class Feature: Blessings of Knowledge")
                    print("At 1st level, you learn two languages of your choice. You also become proficient in")
                    print(
                        "your choice of two of the following skills: Arcana, History, Nature, or "
                        "Religion. Your")
                    print(
                        "proficiency bonus is doubled for any ability check you make that uses either of those")
                    print("skills.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Viden.")
                        self.god_choice = "Viden"
                        self.class_features.append("Divine Domain: Knowledge")
                        self.class_features.append("Blessings of Knowledge")
                        self.first_level_spell_list.append("Identify")
                        self.first_level_spell_list.append("Command")
                        print("Please choose two of the following skills: ")
                        # TODO add skill select for knowledge cleric
                elif god_choice_input == 6:
                    print("You have chosen Komik. You have the following powers:")
                    print("=================================================================================")
                    print("You gain the Class Feature: Blessing of the Trickster")
                    print("Starting when you choose this domain at 1st level, you can use your action to "
                          "touch a")
                    print("willing creature other than yourself to give it advantage on Dexterity (Stealth)")
                    print("checks. This blessing lasts for 1 hour or until you use this feature again.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Komik.")
                        self.god_choice = "Komik"
                        self.class_features.append("Divine Domain: Trickery")
                        self.class_features.append("Blessing of the Trickster")
                        self.first_level_spell_list.append("Charm Person")
                        self.first_level_spell_list.append("Disguise Self")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 7:
                    print("You have chosen Slag. You have the following powers:")
                    print("=================================================================================")
                    print("You gain proficiency in martial weapons and heavy armor.")
                    print("=================================================================================")
                    print("You gain the Class Feature: War Priest")
                    print(
                        "From 1st level, your god delivers bolts of inspiration to you while "
                        "you are engaged in")
                    print("battle. When you use the Attack action, you can make one weapon attack as a bonus")
                    print("action. You can use this feature a number of times equal to your Wisdom modifier")
                    print("(a minimum of once). You regain all expended uses when you finish a long rest.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Slag.")
                        self.god_choice = "Slag"
                        self.class_features.append("Divine Domain: War")
                        self.class_features.append("War Priest")
                        self.professions.append("Weapon: Martial")
                        self.professions.append("Armor: Heavy")
                        self.first_level_spell_list.append("Divine Favor")
                        self.first_level_spell_list.append("Shield of Faith")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                elif god_choice_input == 8:
                    print("You have chosen Opas. You have the following powers:")
                    print("=================================================================================")
                    print("You gain proficiency in martial weapons.")
                    print("=================================================================================")
                    print("You gain the Class Feature: Reaper")
                    print("At 1st level, you learn one necromancy cantrip of your choice from any spell list.")
                    print("When you cast a necromancy cantrip that normally targets only one creature,")
                    print("the spell can instead target two creatures within range and within 5 feet of each")
                    print("other.")
                    print("=================================================================================")
                    print("Are you sure you want to choose this god? Yes or No?")
                    god_choice_input = input("Enter your choice: ")
                    if god_choice_input.lower() == "yes" or god_choice_input.lower() == "y":
                        print("You have chosen Opas.")
                        self.god_choice = "Opas"
                        self.class_features.append("Divine Domain: Death")
                        self.class_features.append("Reaper")
                        self.professions.append("Weapon: Martial")
                        self.first_level_spell_list.append("False Life")
                        self.first_level_spell_list.append("Ray of Sickness")
                        break
                    else:
                        print("Please Choose a God.")
                        continue
                else:
                    print("Invalid input")
                    continue
            except ValueError:
                print("Invalid input")
                continue
            except IndexError:
                print("Invalid input")
                continue
            break


class DNDRace:
    languages = []

    def __init__(self, name):
        self.race_cantrip = []
        self.allowed_skills = []
        self.skill_points = None
        self.race_skills = []
        self.tool_list = []
        self.name = name
        self.speed = None
        self.size = None
        self.languages = []
        self.str_ability_bonus = 0
        self.dex_ability_bonus = 0
        self.con_ability_bonus = 0
        self.int_ability_bonus = 0
        self.wis_ability_bonus = 0
        self.cha_ability_bonus = 0
        self.traits = None
        self.features = []
        self.racial_skills = None
        self.racial_prof = []
        self.tool_choice = False

    def select_language(self):
        if self.name in lang_race:
            selections = dict(enumerate(language_dict))
            for i, language in enumerate(language_dict, start=1):
                print(i, language)
            choice_language = input("Please select a language: ")
            try:
                choice_language = int(choice_language) - 1
            except ValueError:
                print("This is not a valid number.")
                choice_language = -1
            while choice_language < 0 or choice_language > (len(language_dict) - 1):
                choice_language = input(f'That language is not in the allowed languages. Please select a language: ')
                try:
                    choice_language = int(choice_language) - 1
                except ValueError:
                    print("This is not a valid number.")
                    choice_language = -1
            choice_language = selections[choice_language]
            for y in dict.keys(language_dict):
                if choice_language in self.languages:
                    print("You already have that language.")
                    return True
                elif y == choice_language:
                    print(f'{language_dict[y]}')
                    choice_language_a = input("Do you want this language? Yes or No: ")
                    if choice_language_a.lower() in ["y", "yes"]:
                        self.languages.append(choice_language)
                        break
                    elif choice_language_a.lower() in ["n", "no"]:
                        continue
                    else:
                        continue

        else:
            pass

    def tool_select(self):
        print("Please select from the following list of tools:")
        selections = list(enumerate(self.tool_list))
        for i, tool in enumerate(self.tool_list, start=1):
            print(i, tool)
        choice_tool = input("Please select a tool: ")
        try:
            choice_tool = int(choice_tool) - 1
        except ValueError:
            print("This is not a valid number.")
            choice_tool = -1
        while choice_tool < 0 or choice_tool > (len(self.tool_list) - 1):
            choice_tool = input(f'That tool is not in the allowed tools. Please select a tool: ')
            try:
                choice_tool = int(choice_tool) - 1
            except ValueError:
                print("This is not a valid number.")
                choice_tool = -1
        choice_tool = selections[choice_tool]
        self.racial_prof.append(choice_tool)

    def select_race_skills(self):
        escape = False
        while not escape:
            for s in range(self.skill_points):
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
                            self.race_skills.append(add_skill)
                            escape = True
                        else:
                            self.allowed_skills.insert(add_skill_index, add_skill)
                            if self.skill_points < 2:
                                self.skill_points += 1
                                continue
                            else:
                                continue

    def scale_choice(self):
        while True:
            print("Please choose a Dragon color from the list below, the damage type indicates your breath weapon "
                  "damage AND your damage resistance.: ")
            print("1. Black - Acid damage - 5 by 30 ft. line(Dex. save)")
            print("2. Blue - Lightning damage - 5 by 30 ft. line(Dex. save)")
            print("3. Brass - Fire damage - 5 by 30 ft. line(Dex. save)")
            print("4. Bronze - Lightning damage - 5 by 30 ft. line(Dex. save)")
            print("5. Copper - Acid damage - 5 by 30 ft. line(Dex. save)")
            print("6. Gold - Fire damage - 15ft. cone(Dex. save)")
            print("7. Green - Poison damage - 15ft. cone(Con. save)")
            print("8. Red - Fire damage - 15ft. cone(Dex. save")
            print("9. Silver - Cold damage - 15ft. cone(Con. save)")
            print("10. White - Cold damage - 15ft. cone(Con. save)")
            scale_choice_a = input("Scale Color Choice: ")
            if scale_choice_a == "1":
                self.features.append("Black - Acid damage - 5 by 30 ft. line(Dex. save)")
                break
            elif scale_choice_a == "2":
                self.features.append("Blue - Lightning damage - 5 by 30 ft. line(Dex. save)")
                break
            elif scale_choice_a == "3":
                self.features.append("Brass - Fire damage - 5 by 30 ft. line(Dex. save)")
                break
            elif scale_choice_a == "4":
                self.features.append("Bronze - Lightning damage - 5 by 30 ft. line(Dex. save)")
                break
            elif scale_choice_a == "5":
                self.features.append("Copper - Acid damage - 5 by 30 ft. line(Dex. save)")
                break
            elif scale_choice_a == "6":
                self.features.append("Gold - Fire damage - 15ft. cone(Dex. save)")
                break
            elif scale_choice_a == "7":
                self.features.append("Green - Poison damage - 15ft. cone(Con. save)")
                break
            elif scale_choice_a == "8":
                self.features.append("Red - Fire damage - 15ft. cone(Dex. save")
                break
            elif scale_choice_a == "9":
                self.features.append("Silver - Cold damage - 15ft. cone(Con. save)")
                break
            elif scale_choice_a == "10":
                self.features.append("White - Cold damage - 15ft. cone(Con. save)")
                break
            else:
                print("Not a valid option.")
                continue


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
        self.race_choice()

        # self.class_choice()

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
        while True:
            print("Please select a Race: ")
            print("1. Human")
            print("2. Dwarf")
            print("3. Elf")
            print("4. Half-Elf")
            print("5. Half-Orc")
            print("6. Gnome")
            print("7. Halfling")
            print("8. Tiefling")
            print("9. Dragonborn")
            race_selection = input("Enter your choice: ")
            if race_selection == "1":
                print("Humans come in all shapes and sizes. Humans get +1 to all stats and a extra language"
                      "of your choice.")
                print("Are you sure you want to be a Human? Yes or No: ")
                human_choice = input("Enter your choice: ")
                if human_choice.lower() in ["y", "yes"]:
                    human_race = DNDRace("Human")
                    human_race.name = "Human"
                    human_race.speed = "30ft"
                    human_race.size = "Medium"
                    human_race.languages.append("Common")
                    human_race.str_ability_bonus = 1
                    human_race.dex_ability_bonus = 1
                    human_race.con_ability_bonus = 1
                    human_race.int_ability_bonus = 1
                    human_race.wis_ability_bonus = 1
                    human_race.cha_ability_bonus = 1
                    self.race = human_race
                    break
                else:
                    continue
            elif race_selection == "2":
                print("Dwarves are stout and short people known widely for their skills in Brewing, Mining, and "
                      "Blacksmithing.\nThey get +2 to their constitution.\nThey have Darkvision to see better in the "
                      "dark. "
                      "\nThey have advantage on saving throws against poison and are resistant to poison damage.\n"
                      "They have proficiency in the artisan's tools of their choice: smith's tools, brewer's tools, "
                      "or mason's tools.\nThey have proficiency in the following weapons: battleaxe, handaxe, "
                      "light hammer, "
                      "warhammer, and war pick.\nThey also have Stonecunning, allowing them to be proficient and "
                      "double\n "
                      "their proficiency bonus in the History skill while working with Stonework.")
                print("Are you sure you want to be a Dwarf? Yes or No: ")
                dwarf_choice = input("Enter your choice: ")
                if dwarf_choice.lower() in ["y", "yes"]:
                    dwarf_race = DNDRace("Dwarf")
                    dwarf_race.name = "Dwarf"
                    dwarf_race.speed = "25ft"
                    dwarf_race.size = "Medium"
                    dwarf_race.languages.append("Common")
                    dwarf_race.languages.append("Dwarvish")
                    dwarf_race.features.append("Darkvision")
                    dwarf_race.features.append("Dwarven Resilience")
                    dwarf_race.features.append("Stonecunning")
                    dwarf_race.tool_list = ("Brewer's Tools", "Smith's Tools", "Mason's Tools")
                    dwarf_race.racial_prof.append("Battleaxe")
                    dwarf_race.racial_prof.append("Handaxe")
                    dwarf_race.racial_prof.append("Light Hammer")
                    dwarf_race.racial_prof.append("Warhammer")
                    dwarf_race.con_ability_bonus = 2
                    dwarf_race.tool_choice = True
                    self.race = dwarf_race
                    break
                else:
                    continue
            elif race_selection == "3":
                print("Elves are tall and slender. Known widely for their poetry and connection to nature, they tend "
                      "towards fanciful things in life.\nThey get +2 to their Dexterity.\nThey have Darkvision to "
                      "see better in the "
                      "dark. "
                      "\nDo to their connection with the wild Fey, Elves have advantage on saving throws against being "
                      "charmed and can not be put to sleep by magic.\nThey also have Trace, Elves do not need to "
                      "sleep, \nand they can instead meditate for four hours to reap the benefits of 8 hours of rest.")
                print("Are you sure you want to be a Elf? Yes or No: ")
                elf_choice = input("Enter your choice: ")
                if elf_choice.lower() in ["y", "yes"]:
                    elf_race = DNDRace("Elf")
                    elf_race.name = "Elf"
                    elf_race.speed = "30ft"
                    elf_race.size = "Medium"
                    elf_race.languages.append("Common")
                    elf_race.languages.append("Elvish")
                    elf_race.features.append("Darkvision")
                    elf_race.features.append("Keen senses")
                    elf_race.features.append("Trance")
                    elf_race.race_skills.append("Perception")
                    elf_race.dex_ability_bonus = 2
                    elf_race.tool_choice = False
                    self.race = elf_race
                    break
            elif race_selection == "4":
                print("Half-Elves are the offspring of Humans and Elves. They have traits of both races but tend to "
                      "\nfall closely to one or the other depending on upbringing "
                      "\nThey gain a +2 to Charisma due to their ability to socialize and adapt to two different "
                      "cultures.\nAlso due to their Human ancestry they can choose two ability scores to increase by "
                      "+1.\nThey have Darkvision to see better in the dark.\nThey are able two pick two skills to be "
                      "proficient in.\nThey have advantage on saving throws "
                      "against being charmed and can not be put to sleep by magic.\nThey also know both Common and "
                      "Elvish Languages, and can pick one additional language. ")

                print("Are you sure you want to be a Half-Elf? Yes or No: ")
                half_elf_choice = input("Enter your choice: ")
                if half_elf_choice.lower() in ["y", "yes"]:
                    half_elf_race = DNDRace("Half-Elf")
                    half_elf_race.name = "Half-Elf"
                    half_elf_race.speed = "30ft"
                    half_elf_race.size = "Medium"
                    half_elf_race.languages.append("Common")
                    half_elf_race.languages.append("Elvish")
                    half_elf_race.features.append("Darkvision")
                    half_elf_race.features.append("Fey Ancestry")
                    half_elf_race.features.append("Skill Versatility")
                    half_elf_race.cha_ability_bonus = 2
                    half_elf_race.skill_points = 2
                    half_elf_race.allowed_skills = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana",
                                                    "History", "Investigation", "Nature", "Religion", "Animal Handling",
                                                    "Insight", "Medicine", "Perception", "Survival", "Deception",
                                                    "Intimidation", "Performance", "Persuasion"]
                    half_elf_race.tool_choice = False
                    self.race = half_elf_race
                    break
            elif race_selection == "5":
                print("Half-Orcs are the offspring of Humans and Orcs. They tend to be larger and more brutish than "
                      "their human counterparts.\nThey have an increase to their Strength score by +2 and "
                      "Constitution score by +1.\nDue to their Orcish ancestry they have Darkvision. Allowing them to "
                      "see in Dark places better than others.\nDo to their Orcish heritage Half-Orcs have the "
                      "Intimidation skill be default.\nThey are able to survive being hit for more then their total "
                      "health pool, dropping to 1 health instead. They must finish a long rest to use this feature "
                      "again.\nWhen you score a critical hit with a melee weapon attack, you can roll one of the "
                      "weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")
                print("Are you sure you want to be a Half-Orc? Yes or No: ")
                half_orc_choice = input("Enter your choice: ")
                if half_orc_choice.lower() in ["y", "yes"]:
                    half_orc_race = DNDRace("Half-Orc")
                    half_orc_race.name = "Half-Orc"
                    half_orc_race.speed = "30ft"
                    half_orc_race.size = "Medium"
                    half_orc_race.languages.append("Common")
                    half_orc_race.languages.append("Orcish")
                    half_orc_race.features.append("Darkvision")
                    half_orc_race.features.append("Menacing")
                    half_orc_race.features.append("Relentless Endurance")
                    half_orc_race.features.append("Savage Attacks")
                    half_orc_race.race_skills.append("Perception")
                    half_orc_race.str_ability_bonus = 2
                    half_orc_race.con_ability_bonus = 1
                    half_orc_race.tool_choice = False
                    self.race = half_orc_race
                    break
            elif race_selection == "6":
                print("Gnomes are willy and cunning. They are typically very Intelligent creatures and are known for "
                      "their contributions to technology and magical arts.\nThey have a +2 to their Intelligence.\n"
                      "They have Darkvision to see better in the dark.\nThey have advantage against all Intelligence, "
                      "Wisdom, and Charisma saving throws against magic.")
                print("Are you sure you want to be a Gnome? Yes or No: ")
                gnome_choice = input("Enter your choice: ")
                if gnome_choice.lower() in ["y", "yes"]:
                    gnome_race = DNDRace("Gnome")
                    gnome_race.name = "Gnome"
                    gnome_race.speed = "25ft"
                    gnome_race.size = "Small"
                    gnome_race.languages.append("Common")
                    gnome_race.languages.append("Gnomish")
                    gnome_race.features.append("Darkvision")
                    gnome_race.features.append("Gnome Cunning")
                    gnome_race.int_ability_bonus = 2
                    gnome_race.tool_choice = False
                    self.race = gnome_race
                    break
            elif race_selection == "7":
                print("Halflings are laid backed but adventurous folk that like to keep to themselves but make an "
                      "exception for an opportunity for adventure.\n Due to their small size they have a +2 to their "
                      "Dexterity.\nThey are inherently nimble and can move through the space of any creature that is "
                      "smaller than them.\nThey are also inherently lucky, When you roll a 1 on the d20 for an attack "
                      "roll, ability check, or saving throw, you can reroll the die and must use the new roll.\nAnd "
                      "lastly they are Brave, resulting in advantage against being frightened.")
                print("Are you sure you want to be a Halfling? Yes or No: ")
                halfling_choice = input("Enter your choice: ")
                if halfling_choice.lower() in ["y", "yes"]:
                    halfling_race = DNDRace("Halfling")
                    halfling_race.name = "Halfling"
                    halfling_race.speed = "25ft"
                    halfling_race.size = "Small"
                    halfling_race.languages.append("Common")
                    halfling_race.languages.append("Halfling")
                    halfling_race.features.append("Lucky")
                    halfling_race.features.append("Brave")
                    halfling_race.features.append("Halfling Nimbleness")
                    halfling_race.dex_ability_bonus = 2
                    halfling_race.tool_choice = False
                    self.race = halfling_race
                    break
            elif race_selection == "8":
                print("Tieflings are creatures born with devil-like features caused by a deal with a devil somewhere "
                      "in their family line or a interbreeding of devil and human.\nThey are widely distrusted by are "
                      "a varied by personality as humans are.\nDue to their Infernal heritage, they gain the "
                      "following:\nDarkvison, which is the ability to see better in the dark.\nFire resistance.\nAnd "
                      "they start out knowing the cantrip 'Thaumaturgy'.")
                print("Are you sure you want to be a Tiefling? Yes or No: ")
                tiefling_choice = input("Enter your choice: ")
                if tiefling_choice.lower() in ["y", "yes"]:
                    tiefling_race = DNDRace("Tiefling")
                    tiefling_race.name = "Tiefling"
                    tiefling_race.speed = "30ft"
                    tiefling_race.size = "Medium"
                    tiefling_race.languages.append("Common")
                    tiefling_race.languages.append("Infernal")
                    tiefling_race.features.append("Darkvision")
                    tiefling_race.features.append("Hellish Resistance")
                    tiefling_race.features.append("Infernal Legacy")
                    tiefling_race.race_cantrip.append("Thaumaturgy")
                    tiefling_race.cha_ability_bonus = 2
                    tiefling_race.int_ability_bonus = 1
                    tiefling_race.tool_choice = False
                    self.race = tiefling_race
                    break
            elif race_selection == "9":
                print("Nobody knows the true origin of the Dragonborn, but they are bi-pedal humanoid Dragon-like "
                      "creatures. They tend to live in tribal societies and are considered very honorable "
                      "people.\nTheir Strength score increases by 2 and their Charisma score by 1.\nThey get a Breath "
                      "Weapon and damage resistance based on the color of Dragon they are.\n")
                print("Are you sure you want to be a Dragonborn? Yes or No: ")
                dragonborn_choice = input("Enter your choice: ")
                if dragonborn_choice.lower() in ["y", "yes"]:
                    dragonborn_race = DNDRace("Dragonborn")
                    dragonborn_race.name = "Dragonborn"
                    dragonborn_race.speed = "30ft"
                    dragonborn_race.size = "Medium"
                    dragonborn_race.languages.append("Common")
                    dragonborn_race.languages.append("Draconic")
                    dragonborn_race.features.append("Draconic Ancestry")
                    dragonborn_race.scale_choice()
                    dragonborn_race.dex_ability_bonus = 2
                    dragonborn_race.tool_choice = False
                    self.race = dragonborn_race
                    break

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
        elif class_selection == "3":
            print("Clerics are natural healers and defenders. They can call upon the powers of their deities to "
                  "heal their allies and themselves.\nThey can also use their powers to destroy enemies.\n")
            print("Are you sure you want to be a Cleric? Yes or No: ")
            cleric_choice = input("Enter your choice: ")
            if cleric_choice.lower() in ["y", "yes"]:
                cleric_class = DNDClass("Cleric")
                cleric_class.god_choice()
                cleric_class.allowed_skills = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
                cleric_class.allowed_equipment_choice_one = ["A Mace", "A Warhammer(If proficient)"]
                cleric_class.allowed_equipment_choice_two = ["Scale mail", "Leather Armor", "Chainmail(If proficient)"]
                cleric_class.allowed_equipment_choice_three = ["A Light Crossbow and 20 bolts", "Any Simple Weapon"]
                cleric_class.static_equipment = ["A Priest's pack", "Explorer's pack"]
                cleric_class.static_equipment = ["Shield", "Holy Symbol"]
                cleric_class.skill_points = 2
                cleric_class.featurelist = ["Spellcasting", "Divine Domain"]
                cleric_class.is_a_spell_caster = True
                self.dndclass = cleric_class


myname = input('enter a name: ')
mychar = Character(myname)
duplicate_lang = mychar.race.select_language()
while duplicate_lang:
    duplicate_lang = mychar.race.select_language()
    if not duplicate_lang:
        break
while mychar.race.tool_choice:
    mychar.race.tool_select()
mychar.race.select_race_skills()
# mychar.dndclass.select_pri_skills()
# mychar.dndclass.select_equipment()
# show_pri_skills()
