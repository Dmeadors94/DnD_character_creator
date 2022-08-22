import random

import pdfrw

import Modcal

# ============================================
# TO-DO LIST
# Explain tool profs
# ============================================
# Define all undefined variable
speed = None
hitdie = None
hitdietotal = None
wpn_name = None
wpn1_damage = None
wpn_name_2 = None
wpn2_damage = None
# Define all variables needed for StatGen
strength = None
str_mod = None
dexterity = None
dex_mod = None
constitution = None
con_mod = None
intelligence = None
int_mod = None
wisdom = None
wis_mod = None
charisma = None
cha_mod = None
# Define all variables needed for CharGen
race = None
dndclass = None
hit_points = None
AC = None
gold = None
martial_weapon_list = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword",
                       "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War pick",
                       "Warhammer", "Whip"]
simple_weapon_list = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light hammer", "Mace", "Quarterstaff",
                      "Sickle", "Spear"]
equipmentlist = []
traits = None
skills = None
skill_list = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation",
              "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion",
              "Sleight of Hand", "Stealth", "Survival"]
barb_skill_list = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
cleric_skill_list = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
druid_skill_list = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
fighter_skill_list = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception",
                      "Survival"]
monk_skill_list = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
paladin_skill_list = ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
ranger_skill_list = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth",
                     "Survival"]
rogue_skill_list = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception",
                    "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
sorcerer_skill_list = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
warlock_skill_list = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
knowledge_cleric_skill_list = ["Arcana", "History", "Nature", "Religion"]
spell_list_cantrip = ["Acid Splash", "Chill Touch", "Dancing Lights", "Druidcraft", "Eldritch Blast", "Fire Bolt",
                      "Guidance", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray",
                      "Prestidigitation", "Produce Flame", "Ray of Frost", "Sacred Flame", "Shillelagh",
                      "Shocking Grasp",
                      "Spare the Dying", "Thaumaturgy", "True Strike", "Vicious Mockery", "Resistance (Spell)"]
cleric_spell_list_1 = ["Bane", "Bless", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good",
                       "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Healing Word", "Inflict Wounds",
                       "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"]
druid_spell_list_1 = ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic",
                      "Detect Poison and Disease", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word",
                      "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"]
sorcerer_spell_list_1 = ["Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages", "Detect Magic",
                         "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud",
                         "Jump", "Mage Armor", "Magic Missile", "Shield", "Silent Image", "Sleep", "Thunderwave"]
warlock_spell_list_1 = ["Burning Hands", "Command", "Charm Person", "Comprehend Languages", "Expeditious Retreat",
                        "Hellish Rebuke", "Illusory Script", "Protection from Evil and Good", "Unseen Servant"]
druid_cantrip_spell_list = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance (Spell)",
                            "Shillelagh"]
warlock_cantrip_spell_list = ["Eldritch Blast", "Chill Touch", "Mage Hand", "Minor Illusion", "Poison Spray",
                              "Prestidigitation", "True Strike"]
sorcerer_cantrip_spell_list = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand",
                               "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation",
                               "Ray of Frost", "Shocking Grasp", "True Strike"]
bard_cantrip_spell_list = ["Dancing Lights", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion",
                           "Vicious Mockery", "Prestidigitation", "True Strike"]
cleric_cantrip_spell_list = ["Guidance", "Light", "Mending", "Resistance (Spell)", "Sacred Flame", "Thaumaturgy"]
# Define all variables needed for PDFconverter
pdf_template = "template.pdf"
pdf_output = "output.pdf"
playername = input("What is your Player Name?: ")
charactername = input("What is your Character's Name?: ")
featurelist = []
professionlist = []
cantrip_list = []
first_level_spell_list = []


# Run StatGen
def startstats():
    dicerolls = []
    for d6Roll in range(4):
        x = random.randint(1, 6)
        dicerolls.append(x)
    del dicerolls[dicerolls.index(min(dicerolls))]  # deletes the lowest number
    stat = sum(dicerolls)  # totals the remaining 3 numbers
    return stat


while True:
    stats = []
    Stat = startstats()
    stats.append(Stat)
    Stat = startstats()
    stats.append(Stat)
    Stat = startstats()
    stats.append(Stat)
    Stat = startstats()
    stats.append(Stat)
    Stat = startstats()
    stats.append(Stat)
    Stat = startstats()
    stats.append(Stat)
    print("Please assign the stats to the following stats:")
    print("Strength: Your physical power")
    print("Dexterity: Your agility and swiftness")
    print("Constitution: Your endurance")
    print("Intelligence: Your reasoning and memory")
    print("Wisdom: Your perception and insight")
    print("Charisma: Your force of personality")
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
while True:
    strength = input("Out of your stats, which one should be Strength?\n")
    try:
        strength = int(strength)
        if strength == stats[0] or strength == stats[1] or strength == stats[2] or strength == stats[3] or strength == \
                stats[4] or strength == stats[5]:
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
    continue
while True:
    dexterity = input("Out of your stats, which one should be Dexterity?\n")
    try:
        dexterity = int(dexterity)
        if dexterity == stats[0] or dexterity == stats[1] or dexterity == stats[2] or dexterity == stats[3] \
                or dexterity == stats[4]:
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
    continue
while True:
    constitution = input("Out of your stats, which one should be Constitution?\n")
    try:
        constitution = int(constitution)
        if constitution == stats[0] or constitution == stats[1] or constitution == stats[2] or constitution == stats[3]:
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
    continue
while True:
    intelligence = input("Out of your stats, which one should be Intelligence?\n")
    try:
        intelligence = int(intelligence)
        if intelligence == stats[0] or intelligence == stats[1] or intelligence == stats[2]:
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
    continue
while True:
    wisdom = input("Out of your stats, which one should be Wisdom?\n")
    try:
        wisdom = int(wisdom)
        if wisdom == stats[0] or wisdom == stats[1]:
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
while True:
    charisma = input("Out of your stats, which one should be Charisma?\n")
    try:
        charisma = int(charisma)
        if charisma == stats[0]:
            stats.remove(int(charisma))
            cha_mod = Modcal.Modcal(charisma)
            print("Your Charisma Modifier is: ", cha_mod)
            break
        else:
            print("Please enter one of your stats")
        continue
    except ValueError:
        print("Please enter on of your stats")

print("Your final stats are: ")
print("Strength: ", strength)
print("Dexterity: ", dexterity)
print("Constitution: ", constitution)
print("Intelligence: ", intelligence)
print("Wisdom: ", wisdom)
print("Charisma: ", charisma)
STstr = str_mod
STstr_box = False
STdex = dex_mod
STdex_box = False
STcon = con_mod
STcon_box = False
STint = int_mod
STint_box = False
STwis = wis_mod
STwis_box = False
STcha = cha_mod
STcha_box = False
# Define Skills
acrobatics = dex_mod
int(acrobatics)
acrobatics_box = False
animal_handling = wis_mod
int(animal_handling)
animal_handling_box = False
arcana = int_mod
int(arcana)
arcana_box = False
athletics = str_mod
int(athletics)
athletics_box = False
deception = cha_mod
int(deception)
deception_box = False
history = int_mod
int(history)
history_box = False
insight = wis_mod
int(insight)
insight_box = False
intimidation = cha_mod
int(intimidation)
intimidation_box = False
investigation = int_mod
int(investigation)
investigation_box = False
medicine = wis_mod
int(medicine)
medicine_box = False
nature = int_mod
int(nature)
nature_box = False
perception = wis_mod
int(perception)
perception_box = False
performance = cha_mod
int(performance)
performance_box = False
persuasion = cha_mod
int(persuasion)
persuasion_box = False
religion = int_mod
int(religion)
religion_box = False
slight_of_hand = dex_mod
int(slight_of_hand)
slight_of_hand_box = False
stealth = dex_mod
int(stealth)
stealth_box = False
survival = wis_mod
int(survival)
survival_box = False
# Run CharGen
while True:
    print("Please select a race from the following list: ")
    print("1.Human")
    print("2.Dwarf")
    print("3.Elf")
    print("4.Half-Elf")
    print("5.Half-Orc")
    print("6.Halfing")
    print("7.Gnome")
    print("8.Dragonborn")
    print("9.Tiefling")

    race_input = input("Race Choice: ")

    if race_input == "1":
        print("Ability Score Increase: Your ability scores each increase by 1.")
        print("========================")
        print("Age: Humans reach adulthood in their late teens and live less than a century.")
        print("========================")
        print("Alignment: Humans tend toward no particular alignment. The best and the worst are found among them.")
        print("========================")
        print(
            "Size: Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of "
            "your position in that range, your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Languages: You can speak, read, and write Common and one extra language of your choice.")
        print("Humans typically learn the languages of other peoples they deal with, including obscure dialects.")
        print(
            "They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, "
            "Elvish musical expressions, Dwarvish military phrases, and so on.")
        race_choice = input("Do you want to be a Human? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Human"
            strength += 1
            str_mod = Modcal.Modcal(strength)
            STstr = str_mod
            dexterity += 1
            dex_mod = Modcal.Modcal(dexterity)
            STdex = dex_mod
            constitution += 1
            con_mod = Modcal.Modcal(constitution)
            STcon = con_mod
            intelligence += 1
            int_mod = Modcal.Modcal(intelligence)
            STint = int_mod
            wisdom += 1
            wis_mod = Modcal.Modcal(wisdom)
            STwis = wis_mod
            charisma += 1
            cha_mod = Modcal.Modcal(charisma)
            STcha = cha_mod
            speed = "30ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            professionlist.append("Language: Common")
            lang_choice = input("Please enter ANY language:\nLanguage Choice: ")
            lang_choice = "Language: " + lang_choice
            professionlist.append(lang_choice)
            break
        else:
            continue
    elif race_input == "2":
        print("Ability Score Increase: Your Constitution score increases by 2.")
        print("========================")
        print(
            "Age: Dwarves mature at the same rate as humans, but they’re considered young until they reach the age of "
            "50. On average, they live about 350 years.")
        print("========================")
        print(
            "Alignment: Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They "
            "tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share "
            "in the benefits of a just order.")
        print("========================")
        print("Size: Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.")
        print("========================")
        print(
            "Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. You can "
            "see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim "
            "light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print(
            "Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against "
            "poison damage.")
        print("========================")
        print("Dwarven Combat Training: You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.")
        print("========================")
        print(
            "Tool Proficiency: You gain proficiency with the artisan’s tools of your choice: smith’s tools, "
            "brewer’s supplies, or mason’s tools.")
        print("========================")
        print(
            "Stonecunning: Whenever you make an Intelligence (History) check related to the origin of stonework, "
            "you are considered proficient in the History skill and add double your proficiency bonus to the check, "
            "instead of your normal proficiency bonus.")
        print("========================")
        print(
            "Languages: You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and "
            "guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.")
        race_choice = input("Do you want to be a Dwarf? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Dwarf"
            constitution += 2
            con_mod = Modcal.Modcal(constitution)
            STcon = con_mod
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            speed = "25ft"
            featurelist.append("Darkvison")
            featurelist.append("Dwarven Resilience")
            featurelist.append("Stonecunning")
            professionlist.append("Language: Common")
            professionlist.append("Language: Dwarvish")
            professionlist.append("Weapon: Battleaxe")
            professionlist.append("Weapon: Handaxe")
            professionlist.append("Weapon: Light Hammer")
            professionlist.append("Weapon: Warhammer")
            tool_choice = input(
                "Please choose one:\n1.Smith's Tools\n2.Brewer's Supplies\n3.Mason's Tools\nTool Choice: ")
            while True:
                if tool_choice == "1":
                    professionlist.append("Tool: Smith's Tools")
                    break
                elif tool_choice == "2":
                    professionlist.append("Tool: Brewer's Supplies")
                    break
                elif tool_choice == "3":
                    professionlist.append("Tool: Mason's Tools")
                    break
                else:
                    continue

            break
    elif race_input == "3":
        print("Ability Score Increase: Your Dexterity score increases by 2.")
        print("========================")
        print(
            "Age: Although elves reach physical maturity at about the same age as humans, the elven understanding of "
            "adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood "
            "and an adult name around the age of 100 and can live to be 750 years old.")
        print("========================")
        print(
            "Alignment: Elves love freedom, variety, and self- expression, so they lean strongly toward the gentler "
            "aspects of chaos. They value and protect others’ freedom as well as their own, and they are more often "
            "good than not.")
        print("========================")
        print("Size: Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print(
            "Darkvision: Accustomed to twilit forests and the night sky, you have superior vision in dark and dim "
            "conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness "
            "as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Keen Senses: You have proficiency in the Perception skill.")
        print("========================")
        print(
            "Fey Ancestry: You have advantage on saving throws against being charmed,"
            "and magic can’t put you to sleep.")
        print("========================")
        print(
            "Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a "
            "day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; "
            "such dreams are actually mental exercises that have become reflexive through years of practice. After "
            "resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        print("========================")
        print(
            "Languages: You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations "
            "and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among "
            "other races. Many bards learn their language so they can add Elvish ballads to their repertoires.")
        race_choice = input("Do you want to be a Elf? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Elf"
            dexterity += 2
            dex_mod = Modcal.Modcal(dexterity)
            STdex = dex_mod
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            perception += 2
            perception_box = True
            skill_list.remove("Perception")
            barb_skill_list.remove("Perception")
            speed = "30ft"
            professionlist.append("Language: Common")
            professionlist.append("Language: Elvish")
            featurelist.append("Darkvision")
            featurelist.append("Keen Senses")
            featurelist.append("Fey Ancestry")
            featurelist.append("Trance")
            break

        else:
            continue
    elif race_input == "4":
        print("Ability Score Increase: Your Charisma score increases by 2, and two other ability scores of your choice"
              "increase by 1.")
        print("========================")
        print(
            "Age: Half-elves mature at the same rate humans do and reach adulthood around the age of 20."
            "They live much longer than humans, however, often exceeding 180 years.")
        print("========================")
        print(
            "Alignment: Half-elves share the chaotic bent of their elven heritage. They value both personal freedom"
            "and creative expression, demonstrating neither love of leaders nor desire for followers."
            "They chafe at rules, resent others’ demands, and sometimes prove unreliable, or at least unpredictable.")
        print("========================")
        print("Size: Half-elves are about the same size as humans, ranging from 5 to 6 feet tall. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print(
            "Darkvision: Accustomed to twilit forests and the night sky, you have superior vision in dark and dim "
            "conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness "
            "as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print(
            "Fey Ancestry: You have advantage on saving throws against being charmed,"
            "and magic can’t put you to sleep.")
        print("========================")
        print("Skill Versatility: You gain proficiency in two skills of your choice.")
        print("========================")
        print("Languages: You can speak, read, and write Common, Elvish, and one extra language of your choice.")
        race_choice = input("Do you want to be a Half-Elf? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Half-Elf"
            charisma += 2
            while True:
                print("Please choose two ability scores to increase by 1.")
                print("1.Strength")
                print("2.Dexterity")
                print("3.Constitution")
                print("4.Intelligence")
                print("5.Wisdom")
                choice_a = input("First Stat Choice: ")
                if choice_a == "1":
                    strength += 1
                    str_mod = Modcal.Modcal(strength)
                    STstr = str_mod
                    break
                elif choice_a == "2":
                    dexterity += 1
                    dex_mod = Modcal.Modcal(dexterity)
                    STdex = dex_mod
                    break
                elif choice_a == "3":
                    constitution += 1
                    con_mod = Modcal.Modcal(constitution)
                    STcon = con_mod
                    break
                elif choice_a == "4":
                    intelligence += 1
                    int_mod = Modcal.Modcal(intelligence)
                    STint = int_mod
                    break
                elif choice_a == "5":
                    wisdom += 1
                    wis_mod = Modcal.Modcal(wisdom)
                    STwis = wis_mod
                    break
                else:
                    print("Invalid Choice")
                    continue
            while True:
                choice_b = input("Second Stat Choice: ")
                if choice_b == choice_a:
                    print("You can't choose the same stat twice.")
                    continue
                elif choice_b == "1":
                    strength += 1
                    str_mod = Modcal.Modcal(strength)
                    STstr = str_mod
                    break
                elif choice_b == "2":
                    dexterity += 1
                    dex_mod = Modcal.Modcal(dexterity)
                    STdex = dex_mod
                    break
                elif choice_b == "3":
                    constitution += 1
                    con_mod = Modcal.Modcal(constitution)
                    STcon = con_mod
                    break
                elif choice_b == "4":
                    intelligence += 1
                    int_mod = Modcal.Modcal(intelligence)
                    STint = int_mod
                    break
                elif choice_b == "5":
                    wisdom += 1
                    wis_mod = Modcal.Modcal(wisdom)
                    STwis = wis_mod
                    break
                else:
                    print("Invalid Choice")
                    continue
            print("Please Choose two skills to become proficient in.")
            for index, item in enumerate(skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want second: "))
                skill_choice_four = skill_list[skill_choice_he_input - 1]
                if skill_choice_four in skill_list:
                    if skill_choice_four == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue

            print("Please choose any language to learn.")
            he_lang = input("Language Choice: ")
            cha_mod = Modcal.Modcal(charisma)
            STcha = cha_mod
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            speed = "30ft"
            professionlist.append("Language: Common")
            professionlist.append("Language: Elvish")
            professionlist.append("Language: " + he_lang)
            featurelist.append("Darkvision")
            featurelist.append("Fey Ancestry")
            break
    elif race_input == "5":
        print("Ability Score Increase: Your Strength score increases by 2, and your Constitution score increases by 1.")
        print("========================")
        print("Age: Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably"
              "faster and rarely live longer than 75 years.")
        print("========================")
        print("Alignment: Half-orcs inherit a tendency toward chaos from their orc parents and are not strongly"
              "inclined toward good. Half-orcs raised among orcs and willing to live out their lives"
              "among them are usually evil.")
        print("========================")
        print(
            "Size: Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well"
            "over 6 feet tall. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Darkvision: Thanks to your orc blood, you have superior vision in dark and dim conditions."
              "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it"
              "were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Menacing: You gain proficiency in the Intimidation skill.")
        print("========================")
        print("Relentless Endurance: When you are reduced to 0 hit points but not killed outright,"
              "you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.")
        print("========================")
        print("Savage Attacks: When you score a critical hit with a melee weapon attack,"
              "you can roll one of the weapon’s damage dice one additional time and add it to the "
              "extra damage of the critical hit.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Orc. Orc is a harsh, grating language"
              "with hard consonants. It has no script of its own but is written in the Dwarvish script.")
        race_choice = input("Do you want to be a Half-Orc? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Half-Orc"
            strength += 2
            str_mod = Modcal.Modcal(strength)
            STstr = str_mod
            constitution += 1
            con_mod = Modcal.Modcal(constitution)
            STcon = con_mod
            speed = "30ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            intimidation += 2
            intimidation_box = True
            professionlist.append("Language: Common")
            professionlist.append("Language: Orcish")
            featurelist.append("Darkvision")
            featurelist.append("Menacing")
            featurelist.append("Relentless Endurance")
            featurelist.append("Savage Attacks")
            break
        else:
            continue
    elif race_input == "6":
        print("Ability Score Increase: Your Dexterity score increases by 2.")
        print("========================")
        print("Age: A halfling reaches adulthood at the age of 20 and generally lives into the middle of"
              "his or her second century.")
        print("========================")
        print("Alignment: Most Halflings are lawful good. As a rule, they are good-hearted and kind, hate to see"
              "others in pain, and have no tolerance for oppression. They are also very orderly and traditional, "
              "leaning "
              "heavily on the support of their community and the comfort of their old ways.")
        print("========================")
        print("Size: Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small.")
        print("========================")
        print("Speed: Your base walking speed is 25 feet.")
        print("========================")
        print("Lucky: When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll"
              "the die and must use the new roll.")
        print("========================")
        print("Brave: You have advantage on saving throws against being frightened.")
        print("========================")
        print("Halfling Nimbleness: You can move through the space of any creature that is of a size"
              "larger than yours.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Halfling. The Halfling language isn’t secret, "
              "but halflings are loath to share it with others. They write very little, so they don’t have a rich "
              "body of literature. Their oral tradition, however, is very strong. Almost all halflings speak Common "
              "to converse with the people in whose lands they dwell or through which they are traveling.")
        race_choice = input("Do you want to be a Halfling? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Halfling"
            dexterity += 2
            dex_mod = Modcal.Modcal(dexterity)
            STdex = dex_mod
            speed = "25ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            professionlist.append("Language: Common")
            professionlist.append("Language: Halfling")
            featurelist.append("Lucky")
            featurelist.append("Brave")
            featurelist.append("Halfling Nimbleness")
            break
        else:
            continue
    elif race_input == "7":
        print("Ability Score Increase: Your Intelligence score increases by 2.")
        print("========================")
        print("Age: Gnomes mature at the same rate humans do, and most are expected to settle down into an adult life "
              "by around age 40. They can live 350 to almost 500 years.")
        print("========================")
        print("Alignment: Gnomes are most often good. Those who tend toward law are sages, engineers, researchers, "
              "scholars, investigators, or inventors. Those who tend toward chaos are minstrels, tricksters, "
              "wanderers, or fanciful jewelers. Gnomes are good-hearted, and even the tricksters among them are more "
              "playful than vicious.")
        print("========================")
        print("Size: Gnomes are between 3 and 4 feet tall and average about 40 pounds. Your size is Small.")
        print("========================")
        print("Speed: Your base walking speed is 25 feet.")
        print("========================")
        print("Darkvision:Darkvision: Accustomed to life underground, you have superior vision in dark and dim "
              "conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness "
              "as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Gnome Cunning: You have advantage on all Intelligence, Wisdom, and "
              "Charisma saving throws against magic.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Gnomish. The Gnomish language, which uses the "
              "Dwarvish script, is renowned for its technical treatises and its catalogs of knowledge about the "
              "natural world.")
        race_choice = input("Do you want to be a Gnome? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Gnome"
            intelligence += 2
            int_mod = Modcal.Modcal(intelligence)
            STint = int_mod
            speed = "25ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            professionlist.append("Language: Common")
            professionlist.append("Language: Gnomish")
            featurelist.append("Darkvision")
            featurelist.append("Gnome Cunning")
            break
        else:
            continue
    elif race_input == "8":
        print("Ability Score Increase: Your Strength score increases by 2, and your Charisma score increases by 1.")
        print("========================")
        print("Age: Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of "
              "a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.")
        print("========================")
        print("Alignment: Dragonborn tend to extremes, making a conscious choice for one side or the other in the "
              "cosmic war between good and evil. Most dragonborn are good, but those who side with evil can be "
              "terrible villains.")
        print("========================")
        print(
            "Size: Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost "
            "250 pounds. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Breath Weapon: You can use your action to exhale destructive energy. Your draconic ancestry determines "
              "the size, shape, and damage type of the exhalation.")
        print("========================")
        print("Damage Resistance: You have resistance to the damage type associated with your draconic ancestry.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Draconic. Draconic is thought to be one of the "
              "oldest languages and is often used in the study of magic. The language sounds harsh to most other "
              "creatures and includes numerous hard consonants and sibilants.")
        race_choice = input("Do you want to be a Dragonborn? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Dragonborn"
            strength += 2
            str_mod = Modcal.Modcal(strength)
            STstr = str_mod
            charisma += 1
            cha_mod = Modcal.Modcal(charisma)
            STcha = cha_mod
            speed = "30ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            print("Please choose a dragon type:")
            print("1. Black - Damage Type: Acid - Breath Weapon: 5 by 30 ft. line (Dex. save)")
            print("2. Blue - Damage Type: Lightning - Breath Weapon: 5 by 30 ft. line (Dex. save)")
            print("3. Brass - Damage Type: Fire - Breath Weapon: 5 by 30 ft. line (Dex. save)")
            print("4. Bronze - Damage Type: Lightning - Breath Weapon: 5 by 30 ft. line (Dex. save)")
            print("5. Copper - Damage Type: Acid - Breath Weapon: 5 by 30 ft. line (Dex. save)")
            print("6. Gold - Damage Type: Fire - Breath Weapon: 15 ft. cone (Dex. save)")
            print("7. Green - Damage Type: Poison - Breath Weapon: 15 ft. cone (Con. save)")
            print("8. Red - Damage Type: Fire - Breath Weapon: 15 ft. cone (Dex. save)")
            print("9. Silver - Damage Type: Cold - Breath Weapon: 15 ft. cone (Con. save)")
            print("10. White - Damage Type: Cold - Breath Weapon: 15 ft. cone (Con. save)")
            while True:
                dragon_input = input("Please choose a dragon type: ")
                if dragon_input == "1":
                    dragon_type = "Black"
                    featurelist.append("Acid Breath Weapon - 5 by 30 ft. line (Dex. save)")
                    featurelist.append("Damage Resistance: Acid")
                    break
                elif dragon_input == "2":
                    dragon_type = "Blue"
                    featurelist.append("Lightning Breath Weapon - 5 by 30 ft. line (Dex. save)")
                    featurelist.append("Damage Resistance: Lightning")
                    break
                elif dragon_input == "3":
                    dragon_type = "Brass"
                    featurelist.append("Fire Breath Weapon - 5 by 30 ft. line (Dex. save)")
                    featurelist.append("Damage Resistance: Fire")
                    break
                elif dragon_input == "4":
                    dragon_type = "Bronze"
                    featurelist.append("Lightning Breath Weapon - 5 by 30 ft. line (Dex. save)")
                    featurelist.append("Damage Resistance: Lightning")
                    break
                elif dragon_input == "5":
                    dragon_type = "Copper"
                    featurelist.append("Acid Breath Weapon - 5 by 30 ft. line (Dex. save)")
                    featurelist.append("Damage Resistance: Acid")
                    break
                elif dragon_input == "6":
                    dragon_type = "Gold"
                    featurelist.append("Fire Breath Weapon - 15 ft. cone (Dex. save)")
                    featurelist.append("Damage Resistance: Fire")
                    break
                elif dragon_input == "7":
                    dragon_type = "Green"
                    featurelist.append("Poison Breath Weapon - 15 ft. cone (Con. save)")
                    featurelist.append("Damage Resistance: Poison")
                    break
                elif dragon_input == "8":
                    dragon_type = "Red"
                    featurelist.append("Fire Breath Weapon - 15 ft. cone (Dex. save)")
                    featurelist.append("Damage Resistance: Fire")
                    break
                elif dragon_input == "9":
                    dragon_type = "Silver"
                    featurelist.append("Cold Breath Weapon - 15 ft. cone (Con. save)")
                    featurelist.append("Damage Resistance: Cold")
                    break
                elif dragon_input == "10":
                    dragon_type = "White"
                    featurelist.append("Cold Breath Weapon - 15 ft. cone (Con. save)")
                    featurelist.append("Damage Resistance: Cold")
                    break
                else:
                    print("Please choose a valid dragon type.")
                    continue
            professionlist.append("Language: Common")
            professionlist.append("Language: Draconic")
            break
        else:
            continue
    elif race_input == "9":
        print("Ability Score Increase: Your Intelligence score increases by 1, and your Charisma score increases by 2.")
        print("========================")
        print("Age: Tieflings mature at the same rate as humans but live a few years longer.")
        print("========================")
        print("Alignment: Tieflings might not have an innate tendency toward evil, but many of them end up there. "
              "Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.")
        print("========================")
        print(
            "Size: Tieflings are about the same size and build as humans. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Darkvision: Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You "
              "can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were "
              "dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Hellish Resistance: You have resistance to fire damage.")
        print("========================")
        print("Infernal Legacy. You know the thaumaturgy cantrip. When you reach 3rd level, you can cast the hellish "
              "rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish "
              "a long rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain "
              "the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these "
              "spells.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Infernal.")
        race_choice = input("Do you want to be a Tiefling? Yes or No?: ")
        if race_choice.lower() in ["y", "yes"]:
            race = "Tiefling"
            intelligence += 1
            int_mod = Modcal.Modcal(intelligence)
            STint = int_mod
            charisma += 2
            cha_mod = Modcal.Modcal(charisma)
            STcha = cha_mod
            speed = "30ft"
            acrobatics = dex_mod
            int(acrobatics)
            animal_handling = wis_mod
            int(animal_handling)
            arcana = int_mod
            int(arcana)
            athletics = str_mod
            int(athletics)
            deception = cha_mod
            int(deception)
            history = int_mod
            int(history)
            insight = wis_mod
            int(insight)
            intimidation = cha_mod
            int(intimidation)
            investigation = int_mod
            int(investigation)
            medicine = wis_mod
            int(medicine)
            nature = int_mod
            int(nature)
            perception = wis_mod
            int(perception)
            performance = cha_mod
            int(performance)
            persuasion = cha_mod
            int(persuasion)
            religion = int_mod
            int(religion)
            slight_of_hand = dex_mod
            int(slight_of_hand)
            stealth = dex_mod
            int(stealth)
            survival = wis_mod
            int(survival)
            professionlist.append("Language: Common")
            professionlist.append("Language: Infernal")
            featurelist.append("Infernal Legacy")
            featurelist.append("Hellish Resistance")
            featurelist.append("Darkvision")
            break
        else:
            continue
    else:
        print("Choose a number.")
        continue

# Start Class Choice
while True:
    print("Please select a class from the following list: ")
    print("1.Barbarian")
    print("2.Bard")
    print("3.Cleric")
    print("4.Druid")
    print("5.Fighter")
    print("6.Monk")
    print("7.Paladin")
    print("8.Ranger")
    print("9.Rouge")
    print("10.Sorcerer")
    print("11.Warlock")
    # print("12.Wizard")

    class_input = input("Class Choice: ")
    # Barbarian Class Gen Start
    if class_input == "1":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d12 per barbarian level")
        print("Your Hit Points at 1st Level is: 12 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d12 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light, Medium, and Shields")
        print("Weapons: Simple, Martial")
        print("Tools: None")
        print("Saving Throws: Strength, Constitution")
        print("Choose two skills: Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival")
        print("========================")
        print("[EQUIPMENT]")
        print("You get a choice of any Martial Weapon.")
        print(
            "You get a choice of any Simple Weapon. If you pick Handaxe as your simple weapon,"
            "you recieve two of them.")
        print("You also get four Javelins.")
        print("========================")
        class_choice = input("Are you sure you want to be a Barbarian? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Barbarian"
            hit_points = 12 + con_mod
            STstr += 2
            STstr_box = True
            STcon += 2
            STcon_box = True
            featurelist.append("Rage")
            professionlist.append("Armor: Light")
            professionlist.append("Armor: Medium")
            professionlist.append("Armor: Shields")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Martial")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            hitdie = "1d12"
            hitdietotal = "1d12"
            equipmentlist.append("Four Javelin")
            for index, item in enumerate(barb_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = barb_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        barb_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(barb_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_four_input = int(input("Enter what skill you want for your second: "))
                skill_choice_four = barb_skill_list[skill_choice_four_input - 1]
                if skill_choice_four == skill_choice_three:
                    print("You can not choose the came skill twice.")
                    continue
                elif skill_choice_four in skill_list:
                    if skill_choice_four == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    elif skill_choice_four == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_four)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            print("Please choose your starting equipment from the following: ")
            for index, item in enumerate(martial_weapon_list, start=1):
                print(index, item)
            while True:
                start_equip_one = int(input("First Equipment Choice: "))
                start_equip_one = martial_weapon_list[start_equip_one - 1]
                if start_equip_one in martial_weapon_list:
                    if start_equip_one == "Battleaxe":
                        print(
                            "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the special "
                            "trait 'Versitile', which means you can use it with both hands, if you do, "
                            "then the damage is 1d10 Slashing Damage.")
                        equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Battleaxe"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Battleaxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Flail":
                        print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                        equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Flail"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Flail")
                            break
                        else:
                            continue
                    elif start_equip_one == "Glaive":
                        print("The Glaive does 1d10 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print(
                            "Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when "
                            "determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Glaive"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Glaive")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greataxe":
                        print("The Greataxe does 1d12 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Greataxe"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Greataxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greatsword":
                        print("The Greatsword does 2d6 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Greatsword"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Greatsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Halberd":
                        print("The Halberd does 1d10 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print(
                            "Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when "
                            "determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Halberd"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Halberd")
                            break
                        else:
                            continue
                    elif start_equip_one == "Lance":
                        print("The Lance does 1d12 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when "
                            "determining your reach for opportunity attacks with it.")
                        print(
                            "Special: You have disadvantage when you use a lance to attack a target within 5 feet of "
                            "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                        equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Lance"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Lance")
                            break
                        else:
                            continue
                    elif start_equip_one == "Longsword":
                        print("The Longsword does 1d8 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead.")
                        equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Longsword"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Longsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Maul":
                        print("The Maul does 2d6 Bludgeoning Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Maul"
                            wpn1_damage = "2d6"
                            equipmentlist.append("Maul")
                            break
                        else:
                            continue
                    elif start_equip_one == "Morningstar":
                        print("The Morningstar does 1d8 Piercing Damage.")
                        print("It has a Range of Zero.")
                        equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Morningstar"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Morningstar")
                            break
                        else:
                            continue
                    elif start_equip_one == "Pike":
                        print("The Pike does 1d10 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print(
                            "Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when "
                            "determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Pike"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Pike")
                            break
                        else:
                            continue
                    elif start_equip_one == "Rapier":
                        print("The Rapier does 1d8 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Rapier"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Rapier")
                            break
                        else:
                            continue
                    elif start_equip_one == "Scimitar":
                        print("The Scimitar does 1d6 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Scimitar"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Scimitar")
                            break
                        else:
                            continue
                    elif start_equip_one == "Shortsword":
                        print("The Shortsword does 1d6 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Shortsword"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Shortsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Trident":
                        print("The Trident does 1d6 Piercing Damage.")
                        print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged attacks.")
                        print("It has the special properties: ")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        print("Versatile: This weapon can be used with two hands. If you do, the damage is 1d8 instead")
                        equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Trident"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Trident")
                            break
                        else:
                            continue
                    elif start_equip_one == "War pick":
                        print("The War pick does 1d8 Piercing Damage.")
                        print("It has a Range of zero")
                        equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "War pick"
                            wpn1_damage = "1d8"
                            equipmentlist.append("War pick")
                            break
                        else:
                            continue
                    elif start_equip_one == "Warhammer":
                        print("The Warhammer does 1d8 Bludgeoning Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print(
                            "Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead")
                        equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Warhammer"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Warhammer")
                            break
                        else:
                            continue
                    elif start_equip_one == "Whip":
                        print("The Whip does 1d4 Slashing Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when "
                            "determining your reach for opportunity attacks with it.")
                        equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Whip"
                            wpn1_damage = "1d4"
                            equipmentlist.append("Whip")
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    print("Not a valid option")
                    continue
            print(
                "Please choose your second piece of starting equipment from the following, NOTE: If you choose "
                "'Handaxe' you recive TWO of them.")
            for index, item in enumerate(simple_weapon_list, start=1):
                print(index, item)
            while True:
                start_equip_one = int(input("Second Equipment Choice: "))
                start_equip_one = simple_weapon_list[start_equip_one - 1]
                if start_equip_one in simple_weapon_list:
                    if start_equip_one == "Club":
                        print("The Club does 1d4 Bludgeoning Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Club? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Club"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Club")
                            break
                        else:
                            continue
                    elif start_equip_one == "Dagger":
                        print("The Dagger does 1d4 Piercing Damage.")
                        print("It has a Range of 20 ft for short range. 60 ft for long range.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Dagger"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Dagger")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greatclub":
                        print("The Greatclub does 1d8 Bludgeoning Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Greatclub"
                            wpn2_damage = "1d8"
                            equipmentlist.append("Greatclub")
                            break
                        else:
                            continue
                    elif start_equip_one == "Handaxe":
                        print("The Handaxe does 1d6 Slashing Damage.")
                        print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Handaxe"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Handaxe")
                            equipmentlist.append("Handaxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Javelin":
                        print("The Javelin does 1d6 Piercing Damage.")
                        print("It has a short range of 30 ft, and a long range of 120 ft.")
                        print("It has the special properties: ")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Javelin"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Javelin")
                            break
                        else:
                            continue
                    elif start_equip_one == "Light hammer":
                        print("The Light hammer does 1d4 Bludgeoning Damage.")
                        print("It has a short range of 20 ft, and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Light hammer"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Light hammer")
                            break
                        else:
                            continue
                    elif start_equip_one == "Mace":
                        print("The Mace does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Mace"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Mace")
                            break
                        else:
                            continue
                    elif start_equip_one == "Quarterstaff":
                        print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Versatile: This weapon can be used with two hands, if you do so, then the damage is 1d8 "
                            "instead")
                        equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Quarterstaff"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Quarterstaff")
                            break
                        else:
                            continue
                    elif start_equip_one == "Sickle":
                        print("The Sickle does 1d4 Slashing Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Sickle"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Sickle")
                            break
                        else:
                            continue
                    elif start_equip_one == "Spear":
                        print("The Spear does 1d6 Piercing Damage.")
                        print("It has a short range of 20 ft and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        print(
                            "Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 instead.")
                        equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Spear"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Spear")
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    print("Not a valid choice")
                    continue
            break
        else:
            continue
    # Barbarian Class Gen End
    # Bard Class Gen Start
    elif class_input == "2":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Bard level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light")
        print("Weapons: Simple, Hand Crossbow, Longsword, Rapier, and Shortsword")
        print("Tools: Three musical instruments of your choice")
        print("Saving Throws: Dexterity, Charisma")
        print("Skills: Choose any three")
        print("========================")
        print("[EQUIPMENT]")
        print("You get a choice of a Rapier, a Longsowrd, or any Simple Weapon")
        print("You get a choice of either a Lute, or any other Musical Instrument")
        print("You also get Leather armor and a Dagger")
        print("========================")
        class_choice = input("Are you sure you want to be a Bard? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Bard"
            hit_points = 8 + con_mod
            STdex += 2
            STdex_box = True
            STcha += 2
            STcha_box = True
            featurelist.append("Spellcasing(Bard)")
            featurelist.append("Bardic Inspiration")
            professionlist.append("Armor: Light")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Hand Crossbow")
            professionlist.append("Weapon: Longsword")
            professionlist.append("Weapon: Rapier")
            professionlist.append("Weapon: Shortsword")
            hitdie = "1d8"
            hitdietotal = "1d8"
            equipmentlist.append("Leather Armor")
            equipmentlist.append("Dagger")
            wpn_name_2 = "Dagger"
            wpn2_damage = "1d4"
            while True:
                print("Please choose your first piece of starting equipment: ")
                print("1.Rapier")
                print("2.Longsword")
                print("3.A Simple Weapon")
                equip_choice = input("Equipment Choice: ")
                if equip_choice == "1":
                    print("The Rapier does 1d8 Piercing Damage.")
                    print("It has a Range of Zero.")
                    print("It has the special properties: ")
                    print(
                        "Finesse: When making an attack with a finesse weapon, you use your choice of your Strength "
                        "or Dexterity modifier for the attack and damage rolls. You must use the same modifier for "
                        "both rolls.")
                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        wpn_name = "Rapier"
                        wpn1_damage = "1d8"
                        equipmentlist.append("Rapier")
                        break
                elif equip_choice == "2":
                    print("The Longsword does 1d8 Slashing Damage.")
                    print("It has a Range of Zero.")
                    print("It has the special properties: ")
                    print("Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead.")
                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        wpn_name = "Longsword"
                        wpn1_damage = "1d8"
                        equipmentlist.append("Longsword")
                        break
                elif equip_choice == "3":
                    for index, item in enumerate(simple_weapon_list, start=1):
                        print(index, item)
                    while True:
                        start_equip_one = int(input("Please Choose a Simple Weapon: "))
                        start_equip_one = simple_weapon_list[start_equip_one - 1]
                        if start_equip_one in simple_weapon_list:
                            if start_equip_one == "Club":
                                print("The Club does 1d4 Bludgeoning Damage.")
                                print("It has a Range of Zero")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting with two weapons.")
                                equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Club"
                                    wpn1_damage = "1d4"
                                    equipmentlist.append("Club")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Dagger":
                                print("The Dagger does 1d4 Piercing Damage.")
                                print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                    "your Strength or Dexterity modifier for the attack and damage rolls. You must "
                                    "use the same modifier for both rolls.")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged attack. If the weapon is a melee weapon, you use the same ability "
                                    "modifier for that attack roll and damage roll that you would use for a melee "
                                    "attack with the weapon. For example, if you throw a handaxe, you use your "
                                    "Strength, but if you throw a dagger, you can use either your Strength or your "
                                    "Dexterity, since the dagger has the finesse property.")
                                equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Dagger"
                                    wpn1_damage = "1d4"
                                    equipmentlist.append("Dagger")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Greatclub":
                                print("The Greatclub does 1d8 Bludgeoning Damage.")
                                print("It has a Range of Zero.")
                                print("It has the special properties: ")
                                print("Two-Handed: This weapon requires two hands when you attack with it.")
                                equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Greatclub"
                                    wpn1_damage = "1d8"
                                    equipmentlist.append("Greatclub")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Handaxe":
                                print("The Handaxe does 1d6 Slashing Damage.")
                                print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged attack. If the weapon is a melee weapon, you use the same ability "
                                    "modifier for that attack roll and damage roll that you would use for a melee "
                                    "attack with the weapon. For example, if you throw a handaxe, you use your "
                                    "Strength, but if you throw a dagger, you can use either your Strength or your "
                                    "Dexterity, since the dagger has the finesse property.")
                                equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Handaxe"
                                    wpn1_damage = "1d6"
                                    equipmentlist.append("Handaxe")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Javelin":
                                print("The Javelin does 1d6 Piercing Damage.")
                                print("It has a short range of 30 ft, and a long range of 120 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged attack. If the weapon is a melee weapon, you use the same ability "
                                    "modifier for that attack roll and damage roll that you would use for a melee "
                                    "attack with the weapon. For example, if you throw a handaxe, you use your "
                                    "Strength, but if you throw a dagger, you can use either your Strength or your "
                                    "Dexterity, since the dagger has the finesse property.")
                                equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Javelin"
                                    wpn1_damage = "1d6"
                                    equipmentlist.append("Javelin")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Light hammer":
                                print("The Light hammer does 1d4 Bludgeoning Damage.")
                                print("It has a short range of 20 ft, and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged attack. If the weapon is a melee weapon, you use the same ability "
                                    "modifier for that attack roll and damage roll that you would use for a melee "
                                    "attack with the weapon. For example, if you throw a handaxe, you use your "
                                    "Strength, but if you throw a dagger, you can use either your Strength or your "
                                    "Dexterity, since the dagger has the finesse property.")
                                equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Light hammer"
                                    wpn1_damage = "1d4"
                                    equipmentlist.append("Light hammer")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Mace":
                                print("The Mace does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Mace"
                                    wpn1_damage = "1d6"
                                    equipmentlist.append("Mace")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Quarterstaff":
                                print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Versatile: This weapon can be used with two hands, if you do so, then the damage "
                                    "is 1d8 instead")
                                equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Quarterstaff"
                                    wpn1_damage = "1d6"
                                    equipmentlist.append("Quarterstaff")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Sickle":
                                print("The Sickle does 1d4 Slashing Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting with two weapons.")
                                equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Sickle"
                                    wpn1_damage = "1d4"
                                    equipmentlist.append("Sickle")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Spear":
                                print("The Spear does 1d6 Piercing Damage.")
                                print("It has a short range of 20 ft and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged attack. If the weapon is a melee weapon, you use the same ability "
                                    "modifier for that attack roll and damage roll that you would use for a melee "
                                    "attack with the weapon. For example, if you throw a handaxe, you use your "
                                    "Strength, but if you throw a dagger, you can use either your Strength or your "
                                    "Dexterity, since the dagger has the finesse property.")
                                print(
                                    "Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 "
                                    "instead.")
                                equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name = "Spear"
                                    wpn1_damage = "1d6"
                                    equipmentlist.append("Spear")
                                    break
                                else:
                                    continue
                            else:
                                continue
                    break
                else:
                    print("Please Choose a Number")
                    continue
            print("Please choose three skills from the following list: ")
            for index, item in enumerate(skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_three_input = int(input("Enter what skill you want first: "))
                skill_choice_three = skill_list[skill_choice_three_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_three_input = int(input("Enter what skill you want second: "))
                skill_choice_three = skill_list[skill_choice_three_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_three_input = int(input("Enter what skill you want third: "))
                skill_choice_three = skill_list[skill_choice_three_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            print("Please name any musical instrument to add it to your equipment.")
            instrument_choice = input("Instrument Choice: ")
            equipmentlist.append(instrument_choice)
            print("Please choose two cantrips from the following list: ")
            for index, item in enumerate(bard_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                print("Please enter the number of the cantrip you want to add: ")
                cantrip_choice_one_input = int(input("Cantrip Choice One: "))
                cantrip_choice_one = bard_cantrip_spell_list[cantrip_choice_one_input - 1]
                if cantrip_choice_one in bard_cantrip_spell_list:
                    cantrip_list.append(cantrip_choice_one)
                    bard_cantrip_spell_list.remove(cantrip_choice_one)
                    break
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(bard_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                print("Please enter the number of the cantrip you want to add: ")
                cantrip_choice_two_input = int(input("Cantrip Choice Two: "))
                cantrip_choice_two = bard_cantrip_spell_list[cantrip_choice_two_input - 1]
                if cantrip_choice_two in bard_cantrip_spell_list:
                    cantrip_list.append(cantrip_choice_two)
                    bard_cantrip_spell_list.remove(cantrip_choice_two)
                    break
                else:
                    print("Invalid Input")
                    continue
            break
        else:
            print("Invalid Input")
            continue
    # Bard Class Gen End
    # Cleric Class Gen Start
    elif class_input == "3":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Cleric level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light, Medium, Shields")
        print("Weapons: Simple Weapons")
        print("Tools: None")
        print("Saving Throws: Wisdom, Charisma")
        print("Skills: Choose two from History, Insight, Medicine, Persuasion, and Religion")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a mace or (b) a warhammer (if proficient)")
        print("(a) scale mail, (b) leather armor, or (c) chain mail (if proficient)")
        print("(a) a light crossbow and 20 bolts or (b) any simple weapon")
        print("A shield and a holy symbol")
        print("========================")
        class_choice = input("Are you sure you want to be a Cleric? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Cleric"
            hit_points = 8 + con_mod
            STwis += 2
            STwis_box = True
            STcha += 2
            STcha_box = True
            featurelist.append("Spellcasing(Cleric)")
            professionlist.append("Armor: Light")
            professionlist.append("Armor: Medium")
            professionlist.append("Armor: Shields")
            professionlist.append("Weapon: Simple")
            hitdie = "1d8"
            hitdietotal = "1d8"
            equipmentlist.append("Shield")
            equipmentlist.append("Holy Symbol")
            print("Please choose two of the following skills: ")
            for index, item in enumerate(cleric_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = cleric_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        cleric_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(cleric_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = cleric_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            cleric_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
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
                        while True:
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
                                god_choice = "Leven"
                                professionlist.append("Armor: Heavy")
                                featurelist.append("Divine Domain: Life")
                                featurelist.append("Disciple of Life")
                                first_level_spell_list.append("Cure Wounds")
                                first_level_spell_list.append("Bless")
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 2:
                        while True:
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
                                god_choice = "Ohen"
                                featurelist.append("Divine Domain: Light")
                                featurelist.append("Warding Flare")
                                cantrip_list.append("Light")
                                cleric_cantrip_spell_list.remove("Light")
                                first_level_spell_list.append("Burning Hands")
                                first_level_spell_list.append("Faire Fire")
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 3:
                        while True:
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
                                god_choice = "Raiz"
                                featurelist.append("Divine Domain: Nature")
                                professionlist.append("Armor: Heavy")
                                first_level_spell_list.append("Animal Friendship")
                                first_level_spell_list.append("Speak with Animals")
                                while True:
                                    skill_choice_input = input("Please choose a skill from the following list: ")
                                    if skill_choice_input == "Animal Handling":
                                        animal_handling += 2
                                        animal_handling_box = True
                                        skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Nature":
                                        nature += 2
                                        nature_box = True
                                        skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Survival":
                                        survival += 2
                                        survival_box = True
                                        skill_list.remove(skill_choice_input)
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                print("Please choose a cantrip from the following list: ")
                                for index, item in enumerate(druid_cantrip_spell_list, start=1):
                                    print(index, item)
                                while True:
                                    cantrip_choice_input = int(input("Enter your choice: "))
                                    if cantrip_choice_input == 1:
                                        cantrip_list.append("Druidcraft")
                                        break
                                    elif cantrip_choice_input == 2:
                                        cantrip_list.append("Guidance")
                                        break
                                    elif cantrip_choice_input == 3:
                                        cantrip_list.append("Mending")
                                        break
                                    elif cantrip_choice_input == 4:
                                        cantrip_list.append("Poison Spray")
                                        break
                                    elif cantrip_choice_input == 5:
                                        cantrip_list.append("Produce Flame")
                                        break
                                    elif cantrip_choice_input == 6:
                                        cantrip_list.append("Resistance")
                                        break
                                    elif cantrip_choice_input == 7:
                                        cantrip_list.append("Shillelagh")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue

                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 4:
                        while True:
                            print("You have chosen Viden. You have the following powers:")
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
                                god_choice = "Viden"
                                featurelist.append("Divine Domain: Tempest")
                                professionlist.append("Armor: Heavy")
                                professionlist.append("Weapon: Martial")
                                first_level_spell_list.append("Fog Cloud")
                                first_level_spell_list.append("Thunderwave")
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 5:
                        while True:
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
                                god_choice = "Viden"
                                featurelist.append("Divine Domain: Knowledge")
                                featurelist.append("Blessings of Knowledge")
                                first_level_spell_list.append("Identify")
                                first_level_spell_list.append("Command")
                                print("Please choose two of the following skills: ")
                                for index, item in enumerate(knowledge_cleric_skill_list, start=1):
                                    print(index, item)
                                while True:
                                    skill_choice_input = input("Please choose a skill from the above list: ")
                                    if skill_choice_input == "Arcana":
                                        arcana += 4
                                        arcana_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "History":
                                        history += 4
                                        history_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Nature":
                                        nature += 4
                                        nature_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Religion":
                                        religion += 4
                                        religion_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                print("Please choose a second skill from the following list: ")
                                for index, item in enumerate(knowledge_cleric_skill_list, start=1):
                                    print(index, item)
                                while True:
                                    skill_choice_input = input("Please choose a skill from the above list: ")
                                    if skill_choice_input == "Arcana":
                                        arcana += 4
                                        arcana_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "History":
                                        history += 4
                                        history_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Nature":
                                        nature += 4
                                        nature_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    elif skill_choice_input == "Religion":
                                        religion += 4
                                        religion_box = True
                                        skill_list.remove(skill_choice_input)
                                        knowledge_cleric_skill_list.remove(skill_choice_input)
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 6:
                        while True:
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
                                god_choice = "Komik"
                                featurelist.append("Divine Domain: Trickery")
                                featurelist.append("Blessing of the Trickster")
                                first_level_spell_list.append("Charm Person")
                                first_level_spell_list.append("Disguise Self")
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 7:
                        while True:
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
                                god_choice = "Slag"
                                featurelist.append("Divine Domain: War")
                                featurelist.append("War Priest")
                                professionlist.append("Weapon: Martial")
                                professionlist.append("Armor: Heavy")
                                first_level_spell_list.append("Divine Favor")
                                first_level_spell_list.append("Shield of Faith")
                                break
                            else:
                                print("Please Choose a God.")
                                continue
                    elif god_choice_input == 8:
                        while True:
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
                                god_choice = "Opas"
                                featurelist.append("Divine Domain: Death")
                                featurelist.append("Reaper")
                                professionlist.append("Weapon: Martial")
                                first_level_spell_list.append("False Life")
                                first_level_spell_list.append("Ray of Sickness")
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
                break
            print("Please choose your first piece of equipment: ")
            print("1. A Mace")
            print("2. A Warhammer (ONLY CHOOSE IF YOU ARE PROFECIENT IN MARTIAL WEAPONS)")
            while True:
                equipment_choice_input = input("Enter your choice: ")
                if equipment_choice_input == "1":
                    print("The Mace does 1d6 Bludgeoning Damage.")
                    print("It has a range of Zero.")
                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        wpn_name = "Mace"
                        wpn1_damage = "1d6"
                        equipmentlist.append("Mace")
                        break
                    else:
                        continue
                elif equipment_choice_input == "2":
                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                    print("It has a Range of Zero")
                    print("It has the special properties: ")
                    print(
                        "Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead")
                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        wpn_name = "Warhammer"
                        wpn1_damage = "1d8"
                        equipmentlist.append("Warhammer")
                        break
                    else:
                        continue
                else:
                    print("Invalid Input")
                    continue
            print("Please choose your second piece of equipment: ")
            print("1. Scale Mail")
            print("2. Leather Armor")
            print("3. Chain Mail (ONLY CHOOSE IF YOU ARE PROFECIENT IN HEAVY ARMOR)")
            while True:
                equipment_choice_input = input("Enter your choice: ")
                if equipment_choice_input == "1":
                    print("The Scale Mail has an Armor Class of 13.")
                    equip_choice = input("Are you sure you want the Scale Mail? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        armor_name = "Scale Mail"
                        armor_ac = "13"
                        equipmentlist.append("Scale Mail")
                        break
                    else:
                        continue
                elif equipment_choice_input == "2":
                    print("The Leather Armor has an Armor Class of 11.")
                    equip_choice = input("Are you sure you want the Leather Armor? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        armor_name = "Leather Armor"
                        armor_ac = "11"
                        equipmentlist.append("Leather Armor")
                        break
                    else:
                        continue
                elif equipment_choice_input == "3":
                    print("The Chain Mail has Armor Class of 16.")
                    equip_choice = input("Are you sure you want the Chain Mail? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        armor_name = "Chain Mail"
                        armor_ac = "16"
                        equipmentlist.append("Chain Mail")
                        break
                    else:
                        continue
                else:
                    print("Invalid Input")
                    continue
            print("Please choose your third piece of equipment: ")
            print("1. A light crossbow and 20 bolts ")
            print("2. any simple weapon")
            while True:
                equipment_choice_input = input("Enter your choice: ")
                if equipment_choice_input == "1":
                    print("The light crossbow has a range of 120 feet.")
                    equip_choice = input("Are you sure you want the light crossbow? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        weapon_name = "Light Crossbow"
                        weapon_range = "120"
                        equipmentlist.append("Light Crossbow")
                        break
                    else:
                        continue
                elif equipment_choice_input == "2":
                    print("Please choose a simple weapon: ")
                    for index, item in enumerate(simple_weapon_list, start=1):
                        print(index, item)
                    while True:
                        start_equip_one = int(input("Simple Weapon Choice: "))
                        start_equip_one = simple_weapon_list[start_equip_one - 1]
                        if start_equip_one in simple_weapon_list:
                            if start_equip_one == "Club":
                                print("The Club does 1d4 Bludgeoning Damage.")
                                print("It has a Range of Zero")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Club"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Club")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Dagger":
                                print("The Dagger does 1d4 Piercing Damage.")
                                print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                                    "Strength or Dexterity modifier for the attack and damage rolls. You must use the "
                                    "same "
                                    "modifier for both rolls.")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Dagger"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Dagger")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Greatclub":
                                print("The Greatclub does 1d8 Bludgeoning Damage.")
                                print("It has a Range of Zero.")
                                print("It has the special properties: ")
                                print("Two-Handed: This weapon requires two hands when you attack with it.")
                                equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Greatclub"
                                    wpn2_damage = "1d8"
                                    equipmentlist.append("Greatclub")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Handaxe":
                                print("The Handaxe does 1d6 Slashing Damage.")
                                print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Handaxe"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Handaxe")
                                    equipmentlist.append("Handaxe")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Javelin":
                                print("The Javelin does 1d6 Piercing Damage.")
                                print("It has a short range of 30 ft, and a long range of 120 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Javelin"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Javelin")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Light hammer":
                                print("The Light hammer does 1d4 Bludgeoning Damage.")
                                print("It has a short range of 20 ft, and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Light hammer"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Light hammer")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Mace":
                                print("The Mace does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Mace"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Mace")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Quarterstaff":
                                print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Versatile: This weapon can be used with two hands, if you do so, then the damage "
                                    "is 1d8 "
                                    "instead")
                                equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Quarterstaff"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Quarterstaff")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Sickle":
                                print("The Sickle does 1d4 Slashing Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Sickle"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Sickle")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Spear":
                                print("The Spear does 1d6 Piercing Damage.")
                                print("It has a short range of 20 ft and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                print(
                                    "Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 "
                                    "instead.")
                                equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Spear"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Spear")
                                    break
                                else:
                                    continue
            print("Please choose Three Cantrips from the following list:")
            for index, item in enumerate(cleric_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the cantrip you want to add: "))
                    if cantrip_choice in range(1, len(cleric_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(cleric_cantrip_spell_list[cantrip_choice])
                        cleric_cantrip_spell_list.remove(cleric_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(cleric_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the second cantrip you want to add: "))
                    if cantrip_choice in range(1, len(cleric_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(cleric_cantrip_spell_list[cantrip_choice])
                        cleric_cantrip_spell_list.remove(cleric_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(cleric_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the third cantrip you want to add: "))
                    if cantrip_choice in range(1, len(cleric_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(cleric_cantrip_spell_list[cantrip_choice])
                        cleric_cantrip_spell_list.remove(cleric_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            x = wis_mod + 1
            print("You are able to prepare ", x, " First level spells")
            if x < 2:
                print("Please choose a spell from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 2:
                print("Please choose two spells from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 3:
                print("Please choose three spells from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 4:
                print("Please choose four spells from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 5:
                print("Please choose five spells from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fifth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 6:
                print("Please choose five spells from the following list:")
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fifth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(cleric_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the sixth spell you want to add: "))
                        if spell_choice in range(1, len(cleric_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(cleric_spell_list_1[spell_choice])
                            cleric_spell_list_1.remove(cleric_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
        else:
            print("Invalid Input")
            continue
        break
    # Cleric Class Gen End
    # Druid Class Gen Start
    elif class_input == "4":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Druid level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)")
        print("Weapons: Simple melee weapons")
        print("Tools: Herbalism kit")
        print("Saving Throws: Intelligence, Wisdom")
        print("Skills: Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, "
              "and Survival")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a wooden shield or (b) any simple weapon")
        print("(a) a scimitar or (b) any simple melee weapon")
        print("Leather armor and a druidic focus")
        print("========================")
        class_choice = input("Are you sure you want to be a Druid? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Druid"
            hit_points = 8 + con_mod
            STwis += 2
            STwis_box = True
            STint += 2
            STint_box = True
            featurelist.append("Spellcasing(Druid)")
            professionlist.append("Armor: Light")
            professionlist.append("Armor: Medium")
            professionlist.append("Armor: Shields")
            professionlist.append("Weapon: Simple")
            hitdie = "1d8"
            hitdietotal = "1d8"
            equipmentlist.append("Leather Armor")
            equipmentlist.append("Druidic Focus")
            print("Please choose two of the following skills: ")
            for index, item in enumerate(druid_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = druid_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        druid_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(druid_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = druid_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            druid_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please choose your first piece of equipment: ")
            print("1. Wooden Shield")
            print("2. Any simple weapon")
            while True:
                try:
                    equipment_choice_one_input = int(input("Enter your choice: "))
                    if equipment_choice_one_input == 1:
                        equipmentlist.append("Wooden Shield")
                        break
                    elif equipment_choice_one_input == 2:
                        print("Please choose a simple weapon: ")
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("Simple Weapon Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the "
                                        "same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage "
                                        "is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 "
                                        "instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue

                        break
                    else:
                        print("Invalid Input")
                        continue
                except ValueError:
                    print("Invalid Input")
                    continue
            print("Please choose your second piece of equipment: ")
            print("1. Scimitar")
            print("2. Any simple melee weapon")
            while True:
                try:
                    equipment_choice_one_input = int(input("Enter your choice: "))
                    if equipment_choice_one_input == 1:
                        print("The Scimitar does 1d6 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name = "Scimitar"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Scimitar")
                            break
                        else:
                            continue
                    elif equipment_choice_one_input == 2:
                        print("Please choose a simple weapon: ")
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("Simple Weapon Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the "
                                        "same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage "
                                        "is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when "
                                        "fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a "
                                        "ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for "
                                        "that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 "
                                        "instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                        break
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                break
            print("Please choose Two Cantrips from the following list:")
            for index, item in enumerate(druid_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the cantrip you want to add: "))
                    if cantrip_choice in range(1, len(druid_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(druid_cantrip_spell_list[cantrip_choice])
                        druid_cantrip_spell_list.remove(druid_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(druid_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the second cantrip you want to add: "))
                    if cantrip_choice in range(1, len(druid_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(druid_cantrip_spell_list[cantrip_choice])
                        druid_cantrip_spell_list.remove(druid_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            x = wis_mod + 1
            print("You are able to prepare ", x, " First level spells")
            if x < 2:
                print("Please choose a spell from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 2:
                print("Please choose two spells from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 3:
                print("Please choose three spells from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 4:
                print("Please choose four spells from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 5:
                print("Please choose five spells from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fifth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
            elif x == 6:
                print("Please choose five spells from the following list:")
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the first spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the second spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the third spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fourth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the fifth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                for index, item in enumerate(druid_spell_list_1, start=1):
                    print(index, item)
                while True:
                    try:
                        spell_choice = int(input("Please enter the number of the sixth spell you want to add: "))
                        if spell_choice in range(1, len(druid_spell_list_1) + 1):
                            spell_choice -= 1
                            first_level_spell_list.append(druid_spell_list_1[spell_choice])
                            druid_spell_list_1.remove(druid_spell_list_1[spell_choice])
                            break
                        else:
                            print("Please enter a valid number")
                            continue
                    except ValueError:
                        print("Please enter a valid number")
                        continue

            break
        else:
            print("Invalid Input")
            continue
    # Druid Class Gen End
    # Fighter Class Gen Start
    elif class_input == "5":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d10 per Fighter level")
        print("Your Hit Points at 1st Level is: 10 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d10 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light armor, Medium armor, Heavy Armor, shields")
        print("Weapons: Simple and Martial weapons")
        print("Tools: None")
        print("Saving Throws: Strength, Constitution")
        print("Skills: Choose two skills from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, "
              "Perception, and Survival")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) chain mail or (b) leather armor, longbow, and 20 arrows")
        print("(a) a martial weapon and a shield or (b) two martial weapons")
        print("(a) a light crossbow and 20 bolts or (b) two handaxes")
        print("========================")
        class_choice = input("Are you sure you want to be a Fighter? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Fighter"
            hit_points = 10 + con_mod
            STstr += 2
            STstr_box = True
            STcon += 2
            STcon_box = True
            featurelist.append("Second Wind")
            professionlist.append("Armor: Light")
            professionlist.append("Armor: Medium")
            professionlist.append("Armor: Heavy")
            professionlist.append("Armor: Shields")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Martial")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            hitdie = "1d10"
            hitdietotal = "1d10"
            print("Please choose two skills from the following list:")
            for index, item in enumerate(fighter_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = fighter_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        fighter_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(fighter_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = fighter_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            fighter_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("You must choose a Fighting Style as part of your Class. Please choose from the following: ")
            print("1. Archery")
            print("2. Defense")
            print("3. Dueling")
            print("4. Great Weapon Fighting")
            print("5. Protection")
            print("6. Two-Weapon Fighting")
            while True:
                try:
                    style_choice = int(input("Please enter the number of the style you want to choose: "))
                    if style_choice in range(1, 7):
                        if style_choice == 1:
                            print("You gain a +2 bonus to attack rolls you make with ranged weapons.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice -= 1
                                        featurelist.append("Combat Style: Archery")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                        elif style_choice == 2:
                            print("While you are wearing armor, you gain a +1 bonus to AC.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice -= 1
                                        featurelist.append("Combat Style: Defense")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                        elif style_choice == 3:
                            print("When you are wielding a melee weapon in one hand and no other weapons,\n you gain a "
                                  "+2 bonus to damage rolls with that weapon.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice -= 1
                                        featurelist.append("Combat Style: Dueling")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                        elif style_choice == 4:
                            print("When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon "
                                  "that you are wielding with two hands,\n you can reroll the die and must use the new "
                                  "roll, even if the new roll is a 1 or a 2. \nThe weapon must have the two-handed or "
                                  "versatile property for you to gain this benefit.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice -= 1
                                        featurelist.append("Combat Style: Great Weapon Fighting")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                        elif style_choice == 5:
                            print("When a creature you can see attacks a target other than you that is within 5 feet "
                                  "of you, you can use your reaction to impose disadvantage on the attack roll. \nYou "
                                  "must be wielding a shield.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice -= 1
                                        featurelist.append("Combat Style: Protection")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                        elif style_choice == 6:
                            print("When you engage in two-weapon fighting, you can add your ability modifier to the "
                                  "damage of the second attack.")
                            print("Are you sure you want to choose this style? Yes or No?: ")
                            while True:
                                try:
                                    style_choice_input = input("Please enter Yes or No: ")
                                    if style_choice_input.lower() in ["y", "yes"]:
                                        style_choice_input -= 1
                                        featurelist.append("Combat Style: Two-Weapon Fighting")
                                        break
                                    else:
                                        print("Invalid Input")
                                        continue
                                except ValueError:
                                    print("Invalid Input")
                                    continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
                break
            print("Please choose your first piece of equipment: ")
            print("1. Chainmail")
            print("2. leather armor, longbow, and 20 arrows")
            while True:
                try:
                    equipment_choice_one_input = int(input("Enter your choice: "))
                    if equipment_choice_one_input == 1:
                        print("Chainmail has a Armor Class of 13")
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_one_input = input("Please enter Yes or No: ")
                                if equipment_choice_one_input.lower() in ["y", "yes"]:
                                    equipmentlist.append("Chainmail")
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                    elif equipment_choice_one_input == 2:
                        print("Leather armor has a Armor Class of 11")
                        print("A Longbow has a range of 150 feet and a damage die of 1d8")
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_one_input = input("Please enter Yes or No: ")
                                if equipment_choice_one_input.lower() in ["y", "yes"]:
                                    equipmentlist.append("Leather Armor")
                                    equipmentlist.append("Longbow")
                                    equipmentlist.append("20 Arrows")
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
                break
            print("Please choose your second piece of equipment: ")
            print("1. A martial weapon and a shield")
            print("2. Two martial weapons")
            while True:
                try:
                    equipment_choice_two_input = int(input("Enter your choice: "))
                    if equipment_choice_two_input == 1:
                        print("Please choose your martial weapon: ")
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when \n"
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print(
                                        "It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                        "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid option")
                                continue
                        print("A shield has a Armor Class of 2")
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_two_input = input("Please enter Yes or No: ")
                                if equipment_choice_two_input.lower() in ["y", "yes"]:
                                    equipmentlist.append("Shield")
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                    elif equipment_choice_two_input == 2:
                        print("Please choose your First martial weapon: ")
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when \n"
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print(
                                        "It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                        "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        print("Please choose your Second martial weapon: ")
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when \n"
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print(
                                        "It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                        "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_two_input = input("Please enter Yes or No: ")
                                if equipment_choice_two_input.lower() in ["y", "yes"]:
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
                break
            print("Please choose your third piece of equipment: ")
            print("1. A Light Crossbow with 20 bolts")
            print("2. Two Handaxes")
            while True:
                try:
                    equipment_choice_one_input = int(input("Enter your choice: "))
                    if equipment_choice_one_input == 1:
                        print("A Light Crossbow has a range of 80 ft and deals 1d8 Piercing Damage.")
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_one_input = input("Please enter Yes or No: ")
                                if equipment_choice_one_input.lower() in ["y", "yes"]:
                                    equipmentlist.append("Light Crossbow")
                                    equipmentlist.append("20 Bolts")
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                    elif equipment_choice_one_input == 2:
                        print("The Handaxe does 1d6 Slashing Damage.")
                        print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use "
                            "when "
                            "fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                            "make a "
                            "ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier "
                            "for "
                            "that "
                            "attack roll and damage roll that you would use for a melee attack with the "
                            "weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a "
                            "dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the "
                            "finesse "
                            "property.")
                        print("Are you sure you want to choose this equipment? Yes or No?: ")
                        while True:
                            try:
                                equipment_choice_one_input = input("Please enter Yes or No: ")
                                if equipment_choice_one_input.lower() in ["y", "yes"]:
                                    equipmentlist.append("Two Handaxes")
                                    break
                                else:
                                    print("Invalid Input")
                                    continue
                            except ValueError:
                                print("Invalid Input")
                                continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
                break
        break
    # Fighter Gen End
    # Monk Gen Start
    elif class_input == "6":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Monk level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: None")
        print("Weapons: Simple weapons and Shortswords")
        print("Tools: Choose One type of Artisan's tools or one musical instrument")
        print("Saving Throws: Strength, Dexterity")
        print("Skills: Choose two skills from Acrobatics, Athletics, History, Insight, Religion, and Stealth")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a shortsword or (b) any simple weapon")
        print("10 darts")
        print("========================")
        print("[FEATURES]")
        print("Unarmored Defense: While you are not wearing any armor, your Armor Class equals 10 + your Dexterity "
              "modifier + your Wisdom modifier.")
        print(
            "Martial Arts: At 1st level, your practice of martial arts gives you mastery of combat styles that use "
            "\nunarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don’t have "
            "\n the two- handed or heavy property. You gain the following benefits while you are unarmed or wielding "
            "\nonly monk weapons and you aren’t wearing armor or wielding a shield: ")
        print("You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and "
              "monk weapons.")
        print("You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon.")
        print("When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one "
              "\nunarmed strike as a bonus action. For example, if you take the Attack action and attack with a "
              "\nquarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven’t already "
              "\ntaken a bonus action this turn.")
        print("========================")
        class_choice = input("Are you sure you want to be a Monk? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Monk"
            hit_points = 8 + con_mod
            STstr += 2
            STstr_box = True
            STdex += 2
            STdex_box = True
            featurelist.append("Unarmored Defense")
            featurelist.append("Martial Arts")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Shortsword")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            hitdie = "1d8"
            hitdietotal = "1d8"
            print("Please enter a Tool or Instrument to be proficient with: ")
            monk_tool_choice = input("Enter your choice: ")
            monk_tool_choice = ("Tool: " + monk_tool_choice)
            professionlist.append(monk_tool_choice)
            print("Please choose two skills from the following list:")
            for index, item in enumerate(monk_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = monk_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        monk_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(monk_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = monk_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            monk_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please choose what equipment you want: ")
            print("1. A short sword")
            print("2. Any simple weapon")
            while True:
                equipment_choice_input = input("Enter your choice: ")
                if equipment_choice_input == "1":
                    print("The Shortsword has a damage die of 1d6 and a damage type of piercing")
                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                    if equip_choice.lower() in ["y", "yes"]:
                        weapon_name = "Shortsword"
                        weapon_range = "None"
                        equipmentlist.append("Shortsword")
                        break
                    else:
                        continue
                elif equipment_choice_input == "2":
                    print("Please choose a simple weapon: ")
                    for index, item in enumerate(simple_weapon_list, start=1):
                        print(index, item)
                    while True:
                        start_equip_one = int(input("Simple Weapon Choice: "))
                        start_equip_one = simple_weapon_list[start_equip_one - 1]
                        if start_equip_one in simple_weapon_list:
                            if start_equip_one == "Club":
                                print("The Club does 1d4 Bludgeoning Damage.")
                                print("It has a Range of Zero")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Club"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Club")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Dagger":
                                print("The Dagger does 1d4 Piercing Damage.")
                                print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                                    "Strength or Dexterity modifier for the attack and damage rolls. You must use the "
                                    "same "
                                    "modifier for both rolls.")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Dagger"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Dagger")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Greatclub":
                                print("The Greatclub does 1d8 Bludgeoning Damage.")
                                print("It has a Range of Zero.")
                                print("It has the special properties: ")
                                print("Two-Handed: This weapon requires two hands when you attack with it.")
                                equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Greatclub"
                                    wpn2_damage = "1d8"
                                    equipmentlist.append("Greatclub")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Handaxe":
                                print("The Handaxe does 1d6 Slashing Damage.")
                                print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Handaxe"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Handaxe")
                                    equipmentlist.append("Handaxe")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Javelin":
                                print("The Javelin does 1d6 Piercing Damage.")
                                print("It has a short range of 30 ft, and a long range of 120 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Javelin"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Javelin")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Light hammer":
                                print("The Light hammer does 1d4 Bludgeoning Damage.")
                                print("It has a short range of 20 ft, and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Light hammer"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Light hammer")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Mace":
                                print("The Mace does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Mace"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Mace")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Quarterstaff":
                                print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Versatile: This weapon can be used with two hands, if you do so, then the damage "
                                    "is 1d8 "
                                    "instead")
                                equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Quarterstaff"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Quarterstaff")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Sickle":
                                print("The Sickle does 1d4 Slashing Damage.")
                                print("It has a range of Zero.")
                                print("It has the special properties: ")
                                print(
                                    "Light: A light weapon is small and easy to handle, making it ideal for use when "
                                    "fighting "
                                    "with two weapons.")
                                equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Sickle"
                                    wpn2_damage = "1d4"
                                    equipmentlist.append("Sickle")
                                    break
                                else:
                                    continue
                            elif start_equip_one == "Spear":
                                print("The Spear does 1d6 Piercing Damage.")
                                print("It has a short range of 20 ft and a long range of 60 ft.")
                                print("It has the special properties: ")
                                print(
                                    "Thrown: If a weapon has the thrown property, you can throw the weapon to make a "
                                    "ranged "
                                    "attack. If the weapon is a melee weapon, you use the same ability modifier for "
                                    "that "
                                    "attack roll and damage roll that you would use for a melee attack with the "
                                    "weapon. For "
                                    "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                    "dagger, "
                                    "you can use either your Strength or your Dexterity, since the dagger has the "
                                    "finesse "
                                    "property.")
                                print(
                                    "Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 "
                                    "instead.")
                                equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                if equip_choice.lower() in ["y", "yes"]:
                                    wpn_name_2 = "Spear"
                                    wpn2_damage = "1d6"
                                    equipmentlist.append("Spear")
                                    break
                                else:
                                    continue
                break
        break
    elif class_input == "7":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Paladin level")
        print("Your Hit Points at 1st Level is: 10 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d10 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light Armor, Medium Armor,Heavy Armor, Shields")
        print("Weapons: Simple Weapons and Martial Weapons")
        print("Tools: None")
        print("Saving Throws: Wisdom, Charisma")
        print("Skills: Choose two skills from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a martial weapon and a shield or (b) two martial weapons")
        print("(a) five javelins or (b) any simple melee weapon")
        print("Chain mail and a holy symbol")
        print("========================")
        print("[FEATURES]")
        print("Divine Sense:")
        print("The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like "
              "\nheavenly music in your ears. As an action, you can open your awareness to detect such forces. Until "
              "\nthe end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of "
              "\nyou that is not behind total cover. You know the type (celestial, fiend, or undead) of any being "
              "\nwhose presence you sense, but not its identity. Within the same radius, you also detect the presence "
              "of any "
              "\nplace or object that has been consecrated or desecrated, as with the hallow spell. You can use this "
              "\nfeature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, "
              "\nyou regain all expended uses.")
        print("Lay on Hands:")
        print("Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a "
              "\nlong rest. With that pool, you can restore a total number of hit points equal to your paladin level × "
              "5. \nAs an action, you can touch a creature and draw power from the pool to restore a number of hit "
              "\npoints to that creature, up to the maximum amount remaining in your pool. Alternatively, "
              "\nyou can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize "
              "\none poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single "
              "\nuse of Lay on Hands, expending hit points separately for each one. This feature has no effect on "
              "\nundead and constructs.")
        print("========================")
        class_choice = input("Are you sure you want to be a Paladin? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Paladin"
            hit_points = 10 + con_mod
            STwis += 2
            STwis_box = True
            STcha += 2
            STcha_box = True
            featurelist.append("Divine Sense")
            featurelist.append("Lay on Hands")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Martial")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            equipmentlist.append("Chain Mail")
            equipmentlist.append("Holy Symbol")
            hitdie = "1d10"
            hitdietotal = "1d10"
            print("Please choose two skills from the following list:")
            for index, item in enumerate(paladin_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = paladin_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        paladin_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(paladin_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = paladin_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please Choose your first piece of equipment: ")
            print("1. A Martial Weapon and a Shield")
            print("2. Two Martial Weapons")
            while True:
                try:
                    equipment_choice_input = int(input("Enter your choice: "))
                    if equipment_choice_input == 1:
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        print("Please Choose a weapon from the above list")
                        while True:
                            start_equip_one = int(input("Martial Weapon Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                          "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid option")
                                continue
                        equipmentlist.append("Shield")
                        break
                    elif equipment_choice_input == 2:
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        print("Please choose your First Martial Weapon from the list above.")
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                          "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid option")
                                continue
                        for index, item in enumerate(martial_weapon_list, start=1):
                            print(index, item)
                        print("Please choose your Second Martial Weapon from the list above.")
                        while True:
                            start_equip_one = int(input("Second Equipment Choice: "))
                            start_equip_one = martial_weapon_list[start_equip_one - 1]
                            if start_equip_one in martial_weapon_list:
                                if start_equip_one == "Battleaxe":
                                    print(
                                        "The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the "
                                        "special "
                                        "trait 'Versitile', which means you can use it with both hands, if you do, "
                                        "then the damage is 1d10 Slashing Damage.")
                                    equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Battleaxe"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Flail")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Glaive":
                                    print("The Glaive does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Glaive"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Glaive")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greataxe":
                                    print("The Greataxe does 1d12 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greataxe"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greataxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatsword":
                                    print("The Greatsword does 2d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Greatsword"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Greatsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Halberd":
                                    print("The Halberd does 1d10 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Halberd"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Halberd")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Lance":
                                    print("The Lance does 1d12 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print(
                                        "Special: You have disadvantage when you use a lance to attack a target "
                                        "within 5 feet of "
                                        "you. Also, a lance requires two hands to wield when you aren’t mounted.")
                                    equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Lance"
                                        wpn1_damage = "1d12"
                                        equipmentlist.append("Lance")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Longsword":
                                    print("The Longsword does 1d8 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead.")
                                    equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Longsword"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Longsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Maul":
                                    print("The Maul does 2d6 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Maul"
                                        wpn1_damage = "2d6"
                                        equipmentlist.append("Maul")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Morningstar":
                                    print("The Morningstar does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Morningstar"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Morningstar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Pike":
                                    print("The Pike does 1d10 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Heavy: Small creatures have a disadvantage on attack rolls")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Pike"
                                        wpn1_damage = "1d10"
                                        equipmentlist.append("Pike")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Rapier":
                                    print("The Rapier does 1d8 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Rapier"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Rapier")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Scimitar":
                                    print("The Scimitar does 1d6 Slashing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Scimitar"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Scimitar")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Shortsword":
                                    print("The Shortsword does 1d6 Piercing Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Shortsword"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Shortsword")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Trident":
                                    print("The Trident does 1d6 Piercing Damage.")
                                    print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged "
                                          "attacks.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d8 instead")
                                    equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Trident"
                                        wpn1_damage = "1d6"
                                        equipmentlist.append("Trident")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "War pick":
                                    print("The War pick does 1d8 Piercing Damage.")
                                    print("It has a Range of zero")
                                    equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "War pick"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("War pick")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Warhammer":
                                    print("The Warhammer does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands. If you do, the damage is "
                                        "1d10 instead")
                                    equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Warhammer"
                                        wpn1_damage = "1d8"
                                        equipmentlist.append("Warhammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Whip":
                                    print("The Whip does 1d4 Slashing Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Reach: This weapon adds 5 feet to your reach when you attack with it, "
                                        "as well as when "
                                        "determining your reach for opportunity attacks with it.")
                                    equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Whip"
                                        wpn1_damage = "1d4"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid option")
                                continue

                    else:
                        print("Not a valid option")
                        continue
                except ValueError:
                    print("Not a valid option")
                    continue
                break
            print("Please Choose your second piece of equipment")
            print("1. Five Javelins")
            print("2. A Simple Weapon")
            while True:
                try:
                    equipment_choice_input = int(input("Please choose an option: "))
                    if equipment_choice_input == 1:
                        print("The Five Javelins do 1d8 Piercing Damage.")
                        print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged attacks.")
                        print("It has the special properties: ")
                        print(
                            "\nThrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "\nattack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "\nattack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "\nexample, if you throw a handaxe, you use your Strength, but if you throw a dagger, you "
                            "\ncan use either your Strength or your Dexterity, since the dagger has the finesse "
                            "\nproperty.")
                        print(
                            "Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead")
                        equip_choice = input("Are you sure you want the Five Javelins? Yes or No?\nEnter your Choice: ")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Five Javelins")
                        else:
                            continue
                        break
                    elif equipment_choice_input == 2:
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("Equipment Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid choice")
                                continue
                    else:
                        print("Not a valid choice")
                        continue
                except ValueError:
                    print("Not a valid choice")
                    continue
                break
        else:
            print("Invalid Input")
            continue
        break
    elif class_input == "8":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d10 per Ranger level")
        print("Your Hit Points at 1st Level is: 10 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d10 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light, Medium, Shields")
        print("Weapons: Simple and Martial")
        print("Tools: None")
        print("Saving Throws: Strength and Dexterity")
        print("Choose three skills: Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, "
              "and Survival")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) scale mail or (b) leather armor")
        print("(a) two shortswords or (b) two simple melee weapons")
        print("A Longbow and a quiver of 20 arrows")
        print("========================")
        print("[FEATURES]")
        print("Favored Enemy: ")
        print("Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking "
              "\nto a certain type of enemy. Choose a type of favored enemy: aberrations, beasts, celestials, "
              "\nconstructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. "
              "\nAlternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies. You "
              "\nhave advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence "
              "\nchecks to recall information about them. When you gain this feature, you also learn one language of "
              "\nyour choice that is spoken by your favored enemies, if they speak one at all. You choose one "
              "\nadditional favored enemy, as well as an associated language, at 6th and 14th level. As you gain "
              "\nlevels, your choices should reflect the types of monsters you have encountered on your adventures.")
        print("\n")
        print("Natural Explorer: ")
        print("You are particularly familiar with one type of natural environment and are adept at traveling and "
              "\nsurviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, "
              "\ngrassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored "
              "\nterrain, your proficiency bonus is doubled if you are using a skill that you’re proficient in. While "
              "\ntraveling for an hour or more in your favored terrain, you gain the following benefits: \nDifficult "
              "terrain doesn’t slow your group’s travel. \nYour group can’t become lost except by magical means. "
              "\nEven "
              "when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), "
              "you remain alert to danger. \nIf you are traveling alone, you can move stealthily at a normal pace. "
              "When "
              "you forage, you find twice as much food as you normally would. \nWhile tracking other creatures, "
              "you also learn their exact number, their sizes, and how long ago they passed through the area.")
        print("========================")
        class_choice = input("Are you sure you want to be a Ranger? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Ranger"
            hit_points = 10 + con_mod
            STstr += 2
            STstr_box = True
            STdex += 2
            STdex_box = True
            featurelist.append("Favored Enemy")
            featurelist.append("Natural Explorer")
            professionlist.append("Armor: Light")
            professionlist.append("Armor: Medium")
            professionlist.append("Armor: Shields")
            professionlist.append("Weapon: Simple")
            professionlist.append("Weapon: Martial")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            hitdie = "1d10"
            hitdietotal = "1d10"
            print("Please choose three skills from the following list:")
            for index, item in enumerate(ranger_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = ranger_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        ranger_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(ranger_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = ranger_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(ranger_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = ranger_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            ranger_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please Choose your first piece of equipment: ")
            print("1. Scale Mail")
            print("2. Leather Armor")
            while True:
                try:
                    equipment_choice_input = int(input("Enter your choice: "))
                    if equipment_choice_input == 1:
                        print("Scale mail gives you 13 AC")
                        equip_choice = input("Are you sure you want the Scale Mail? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Scale Mail")
                            break
                        else:
                            continue
                    elif equipment_choice_input == 2:
                        print("Leather armor gives you 11 AC")
                        equip_choice = input("Are you sure you want the Leather Armor? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Leather Armor")
                            break
                        else:
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please Choose your second piece of equipment: ")
            print("1. Two Shortswords")
            print("2. Two simple melee weapons")
            while True:
                try:
                    equipment_choice_input = int(input("Enter your choice: "))
                    if equipment_choice_input == 1:
                        print("The Shortsword does 1d6 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Shortsword")
                            equipmentlist.append("Shortsword")
                        else:
                            continue
                    elif equipment_choice_input == 2:
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        print("Please choose your first weapon from the list above: ")
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid choice")
                                continue
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        print("Please choose your second weapon from the list above: ")
                        while True:
                            start_equip_one = int(input("First Equipment Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid choice")
                                continue
                except ValueError:
                    print("Not a valid choice")
                    continue
                break
    elif class_input == "9":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Rogue level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light")
        print("Weapons: Simple weapons, Hand crossbows, Longswords, Rapiers, Shortswords")
        print("Tools: Thieves’ tools")
        print("Saving Throws: Dexterity, Intelligence")
        print("Choose four skills: Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, "
              "Perception, Performance, Persuasion, Sleight of Hand, and Stealth")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a rapier or (b) a shortsword")
        print("(a) a shortbow and quiver of 20 arrows or (b) a shortsword")
        print("Leather armor, two daggers, and thieves’ tools")
        print("========================")
        print("[FEATURES]")
        print("Expertise: ")
        print("At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your "
              "proficiency with thieves’ tools. Your proficiency bonus is doubled for any ability check you make that "
              "uses either of the chosen proficiencies.")
        print("\n")
        print("Sneak Attack: ")
        print("Beginning at 1st level, you know how to strike subtly and exploit a foe’s distraction. Once per turn, "
              "\nyou can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on "
              "the "
              "\nattack roll. The attack must use a finesse or a ranged weapon. You don’t need advantage on the "
              "attack "
              "\nroll if another enemy of the target is within 5 feet of it, that enemy isn’t incapacitated, and you "
              "\ndon’t have disadvantage on the attack roll.")
        print("\n")
        print("Thieves’ Cant: ")
        print("During your rogue training you learned thieves’ cant, a secret mix of dialect, jargon, and code that "
              "\nallows you to hide messages in seemingly normal conversation. Only another creature that knows "
              "\nthieves’ cant understands such messages. It takes four times longer to convey such a message than it "
              "\ndoes to speak the same idea plainly. In addition, you understand a set of secret signs and symbols "
              "\nused to convey short, simple messages, such as whether an area is dangerous or the territory of a "
              "\nthieves’ guild, whether loot is nearby, or whether the people in an area are easy marks or will "
              "\nprovide a safe house for thieves on the run.")
        print("========================")
        class_choice = input("Are you sure you want to be a Rogue? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Rogue"
            hit_points = 8 + con_mod
            STdex += 2
            STdex_box = True
            STint += 2
            STint_box = True
            featurelist.append("Rage")
            professionlist.append("Armor: Light")
            professionlist.append("Weapon: Simple")
            professionlist.append("Tools: Thieves’ tools")
            professionlist.append("Weapon: Hand crossbows")
            professionlist.append("Weapon: Longswords")
            professionlist.append("Weapon: Rapiers")
            professionlist.append("Weapon: Shortswords")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            cantrip_list.append("")
            hitdie = "1d8"
            hitdietotal = "1d8"
            print("Please choose Four skills from the following list:")
            for index, item in enumerate(rogue_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = rogue_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        rogue_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(rogue_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = rogue_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(rogue_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = rogue_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(rogue_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = rogue_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            rogue_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please choose your piece of equipment: ")
            print("1. A Rapier")
            print("2. A Shortsword")
            while True:
                try:
                    equipment_choice_input = int(input("Enter your choice: "))
                    if equipment_choice_input == 1:
                        print("The Rapier does 1d8 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Rapier")
                            break
                    elif equipment_choice_input == 2:
                        print("The Shortsword does 1d6 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Shortsword")
                            break
                    else:
                        continue
                except ValueError:
                    print("Invalid Input")
                    continue
                break
            print("Please choose your second piece of equipment: ")
            print("1. A Shortbow and 20 arrows")
            print("2. A Shortsword")
            while True:
                try:
                    equipment_choice_input = int(input("Enter your choice: "))
                    if equipment_choice_input == 1:
                        print("The Shortbow does 1d6 Piercing Damage and has a range of 80ft")
                        equip_choice = input("Are you sure you want the Shortbow? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Shortbow")
                            equipmentlist.append("20 Arrows")
                            break
                        else:
                            continue
                    elif equipment_choice_input == 2:
                        print("The Shortsword does 1d6 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Shortsword")
                            break
                    else:
                        continue
                except ValueError:
                    print("Invalid Input")
                    continue
                break
    elif class_input == "10":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d6 per Sorcerer level")
        print("Your Hit Points at 1st Level is: 6 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d6 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: None")
        print("Weapons: Daggers, Darts, Slings, Quarterstaffs, Light Crossbows")
        print("Tools: None")
        print("Saving Throws: Constitution, Charisma")
        print("Choose two skills: Arcana, History, Insight, Intimidation, Persuasion, Religion")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a light crossbow and 20 bolts or (b) any simple weapon")
        print("A component pouch and an arcane focus")
        print("Two daggers")
        print("========================")
        print("[FEATURES]")
        print("Draconic Resilience: As magic flows through your body, it causes physical traits of your dragon "
              "\nancestors to emerge. At 1st level, your hit point maximum increases by 1 and increases by 1 again "
              "\nwhenever you gain a level in this class. Additionally, parts of your skin are covered by a thin sheen "
              "\nof dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier.")
        print("========================")
        class_choice = input("Are you sure you want to be a Sorcerer? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Sorcerer"
            hit_points = 6 + con_mod + 1
            STcon += 2
            STcon_box = True
            STcha += 2
            STcha_box = True
            featurelist.append("Draconic Resilience")
            professionlist.append("Weapon: Daggers")
            professionlist.append("Weapon: Darts")
            professionlist.append("Weapon: Slings")
            professionlist.append("Weapon: Quarterstaffs")
            professionlist.append("Weapon: Light Crossbows")
            equipmentlist.append("Component Pouch")
            equipmentlist.append("Arcane Focus")
            equipmentlist.append("Two Daggers")
            hitdie = "1d6"
            hitdietotal = "1d6"
            print("Please choose two skills from the following list:")
            for index, item in enumerate(sorcerer_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = sorcerer_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        sorcerer_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(sorcerer_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = sorcerer_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            sorcerer_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
                except ValueError:
                    print("Invalid Input")
                    continue
            print("Please choose your first piece of equipment: ")
            print("1. A light crossbow with 20 bolts")
            print("2. A simple weapon")
            while True:
                try:
                    equipment_choice_one = int(input("Enter your choice: "))
                    if equipment_choice_one == 1:
                        print("A Light crossbow does 1d8 damage and has a range of 80 ft")
                        equip_choice = input("Are you sure you want the Light Crossbow? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Light Crossbow")
                            break
                        else:
                            continue
                    elif equipment_choice_one == 2:
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("Second Equipment Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, then the "
                                        "damage is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid choice")
                                continue
                    else:
                        print("Not a valid choice")
                        continue
                except ValueError:
                    print("Not a valid choice")
                    continue
                break
            print("Please choose Four Cantrips from the following list:")
            for index, item in enumerate(sorcerer_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the cantrip you want to add: "))
                    if cantrip_choice in range(1, len(sorcerer_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(sorcerer_cantrip_spell_list[cantrip_choice])
                        sorcerer_cantrip_spell_list.remove(sorcerer_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(sorcerer_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the second cantrip you want to add: "))
                    if cantrip_choice in range(1, len(sorcerer_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(sorcerer_cantrip_spell_list[cantrip_choice])
                        sorcerer_cantrip_spell_list.remove(sorcerer_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(sorcerer_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the third cantrip you want to add: "))
                    if cantrip_choice in range(1, len(sorcerer_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(sorcerer_cantrip_spell_list[cantrip_choice])
                        sorcerer_cantrip_spell_list.remove(sorcerer_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(sorcerer_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the foruth cantrip you want to add: "))
                    if cantrip_choice in range(1, len(sorcerer_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(sorcerer_cantrip_spell_list[cantrip_choice])
                        sorcerer_cantrip_spell_list.remove(sorcerer_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            print("Please choose two spells from the following list:")
            for index, item in enumerate(sorcerer_spell_list_1, start=1):
                print(index, item)
            while True:
                try:
                    spell_choice = int(input("Please enter the number of the spell you want to add: "))
                    if spell_choice in range(1, len(sorcerer_spell_list_1) + 1):
                        spell_choice -= 1
                        first_level_spell_list.append(sorcerer_spell_list_1[spell_choice])
                        sorcerer_spell_list_1.remove(sorcerer_spell_list_1[spell_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(sorcerer_spell_list_1, start=1):
                print(index, item)
            while True:
                try:
                    spell_choice = int(input("Please enter the number of the spell you want to add: "))
                    if spell_choice in range(1, len(sorcerer_spell_list_1) + 1):
                        spell_choice -= 1
                        first_level_spell_list.append(sorcerer_spell_list_1[spell_choice])
                        sorcerer_spell_list_1.remove(sorcerer_spell_list_1[spell_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
    elif class_input == "11":
        print("[HIT POINTS]")
        print("Your Hit Dice is 1d8 per Warlock level")
        print("Your Hit Points at 1st Level is: 8 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d8 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: Light")
        print("Weapons: Simple Weapons")
        print("Tools: None")
        print("Saving Throws: Wisdom, Charisma ")
        print("Skills: Choose two from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion")
        print("========================")
        print("[EQUIPMENT]")
        print("(a) a light crossbow and 20 bolts or (b) any simple weapon ")
        print("a component pouch and an arcane focus")
        print("Leather armor, any simple weapon, and two daggers")
        print("========================")
        print("[FEATURES]")
        print("Pact: Fiend")
        print("Dark One's Blessing: Starting at 1st level, when you reduce a hostile creature to 0 hit points, "
              "\nyou gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1).")
        print("========================")
        class_choice = input("Are you sure you want to be a Warlock? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "Warlock"
            hit_points = 8 + con_mod
            STwis += 2
            STwis_box = True
            STcha += 2
            STcha_box = True
            featurelist.append("Pact: Fiend")
            featurelist.append("Dark One's Blessing")
            professionlist.append("Armor: Light")
            professionlist.append("Weapon: Simple")
            equipmentlist.append("Arcane Focus")
            equipmentlist.append("Component Pouch")
            equipmentlist.append("Leather Armor")
            equipmentlist.append("Two Daggers")
            hitdie = "1d8"
            hitdietotal = "1d8"
            print("Please choose two skills from the following list:")
            for index, item in enumerate(warlock_skill_list, start=1):
                print(index, item)
            while True:
                skill_choice_he_input = int(input("Enter what skill you want first: "))
                skill_choice_three = warlock_skill_list[skill_choice_he_input - 1]
                if skill_choice_three in skill_list:
                    if skill_choice_three == "Acrobatics":
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Animal Handling":
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Arcana":
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Athletics":
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Deception":
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "History":
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Insight":
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Intimidation":
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Investigation":
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Medicine":
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Nature":
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Perception":
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Performance":
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Persuasion":
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Religion":
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Sleight of Hand":
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Stealth":
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    elif skill_choice_three == "Survival":
                        survival += 2
                        survival_box = True
                        skill_list.remove(skill_choice_three)
                        warlock_skill_list.remove(skill_choice_three)
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(warlock_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = warlock_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            warlock_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
            print("Please Choose your first piece of equipment: ")
            print("1. Light crossbow and 20 bolts")
            print("2. Any Simple Weapon")
            while True:
                try:
                    equipment_choice_one = int(input("Enter your choice: "))
                    if equipment_choice_one == 1:
                        print("The Light crossbow does 1d8 pirceing damage")
                        equip_choice = input("Are you sure you want the Light Crossbow? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            equipmentlist.append("Light Crossbow")
                            break
                        else:
                            continue
                    elif equipment_choice_one == 2:
                        for index, item in enumerate(simple_weapon_list, start=1):
                            print(index, item)
                        while True:
                            start_equip_one = int(input("Second Equipment Choice: "))
                            start_equip_one = simple_weapon_list[start_equip_one - 1]
                            if start_equip_one in simple_weapon_list:
                                if start_equip_one == "Club":
                                    print("The Club does 1d4 Bludgeoning Damage.")
                                    print("It has a Range of Zero")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Club? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Club"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Club")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Dagger":
                                    print("The Dagger does 1d4 Piercing Damage.")
                                    print("It has a Range of 20 ft for short range. 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Finesse: When making an attack with a finesse weapon, you use your choice of "
                                        "your "
                                        "Strength or Dexterity modifier for the attack and damage rolls. You must use "
                                        "the same "
                                        "modifier for both rolls.")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Dagger"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Dagger")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Greatclub":
                                    print("The Greatclub does 1d8 Bludgeoning Damage.")
                                    print("It has a Range of Zero.")
                                    print("It has the special properties: ")
                                    print("Two-Handed: This weapon requires two hands when you attack with it.")
                                    equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Greatclub"
                                        wpn2_damage = "1d8"
                                        equipmentlist.append("Greatclub")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Handaxe":
                                    print("The Handaxe does 1d6 Slashing Damage.")
                                    print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Handaxe"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Handaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Javelin":
                                    print("The Javelin does 1d6 Piercing Damage.")
                                    print("It has a short range of 30 ft, and a long range of 120 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Javelin"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Javelin")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Light hammer":
                                    print("The Light hammer does 1d4 Bludgeoning Damage.")
                                    print("It has a short range of 20 ft, and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Light hammer"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Light hammer")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Mace":
                                    print("The Mace does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Mace"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Mace")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Quarterstaff":
                                    print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Versatile: This weapon can be used with two hands, if you do so, "
                                        "then the damage is 1d8 "
                                        "instead")
                                    equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Quarterstaff"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Quarterstaff")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Sickle":
                                    print("The Sickle does 1d4 Slashing Damage.")
                                    print("It has a range of Zero.")
                                    print("It has the special properties: ")
                                    print(
                                        "Light: A light weapon is small and easy to handle, making it ideal for use "
                                        "when fighting "
                                        "with two weapons.")
                                    equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Sickle"
                                        wpn2_damage = "1d4"
                                        equipmentlist.append("Sickle")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Spear":
                                    print("The Spear does 1d6 Piercing Damage.")
                                    print("It has a short range of 20 ft and a long range of 60 ft.")
                                    print("It has the special properties: ")
                                    print(
                                        "Thrown: If a weapon has the thrown property, you can throw the weapon to "
                                        "make a ranged "
                                        "attack. If the weapon is a melee weapon, you use the same ability modifier "
                                        "for that "
                                        "attack roll and damage roll that you would use for a melee attack with the "
                                        "weapon. For "
                                        "example, if you throw a handaxe, you use your Strength, but if you throw a "
                                        "dagger, "
                                        "you can use either your Strength or your Dexterity, since the dagger has the "
                                        "finesse "
                                        "property.")
                                    print(
                                        "Versatile: This weapon can be used with both hands. If you do, the damage is "
                                        "1d8 instead.")
                                    equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name_2 = "Spear"
                                        wpn2_damage = "1d6"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid choice")
                                continue
                    else:
                        print("Not a valid choice")
                        continue
                except ValueError:
                    print("Not a valid choice")
                    continue
                break
            print("Please Choose your Second piece of equipment: ")
            for index, item in enumerate(simple_weapon_list, start=1):
                print(index, item)
            while True:
                start_equip_one = int(input("Second Equipment Choice: "))
                start_equip_one = simple_weapon_list[start_equip_one - 1]
                if start_equip_one in simple_weapon_list:
                    if start_equip_one == "Club":
                        print("The Club does 1d4 Bludgeoning Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Club? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Club"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Club")
                            break
                        else:
                            continue
                    elif start_equip_one == "Dagger":
                        print("The Dagger does 1d4 Piercing Damage.")
                        print("It has a Range of 20 ft for short range. 60 ft for long range.")
                        print("It has the special properties: ")
                        print(
                            "Finesse: When making an attack with a finesse weapon, you use your choice of your "
                            "Strength or Dexterity modifier for the attack and damage rolls. You must use the same "
                            "modifier for both rolls.")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Dagger"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Dagger")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greatclub":
                        print("The Greatclub does 1d8 Bludgeoning Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Greatclub"
                            wpn2_damage = "1d8"
                            equipmentlist.append("Greatclub")
                            break
                        else:
                            continue
                    elif start_equip_one == "Handaxe":
                        print("The Handaxe does 1d6 Slashing Damage.")
                        print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Handaxe"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Handaxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Javelin":
                        print("The Javelin does 1d6 Piercing Damage.")
                        print("It has a short range of 30 ft, and a long range of 120 ft.")
                        print("It has the special properties: ")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Javelin"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Javelin")
                            break
                        else:
                            continue
                    elif start_equip_one == "Light hammer":
                        print("The Light hammer does 1d4 Bludgeoning Damage.")
                        print("It has a short range of 20 ft, and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Light hammer"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Light hammer")
                            break
                        else:
                            continue
                    elif start_equip_one == "Mace":
                        print("The Mace does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Mace"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Mace")
                            break
                        else:
                            continue
                    elif start_equip_one == "Quarterstaff":
                        print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Versatile: This weapon can be used with two hands, if you do so, then the damage is 1d8 "
                            "instead")
                        equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Quarterstaff"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Quarterstaff")
                            break
                        else:
                            continue
                    elif start_equip_one == "Sickle":
                        print("The Sickle does 1d4 Slashing Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print(
                            "Light: A light weapon is small and easy to handle, making it ideal for use when fighting "
                            "with two weapons.")
                        equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Sickle"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Sickle")
                            break
                        else:
                            continue
                    elif start_equip_one == "Spear":
                        print("The Spear does 1d6 Piercing Damage.")
                        print("It has a short range of 20 ft and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print(
                            "Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged "
                            "attack. If the weapon is a melee weapon, you use the same ability modifier for that "
                            "attack roll and damage roll that you would use for a melee attack with the weapon. For "
                            "example, if you throw a handaxe, you use your Strength, but if you throw a dagger, "
                            "you can use either your Strength or your Dexterity, since the dagger has the finesse "
                            "property.")
                        print(
                            "Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 instead.")
                        equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                        if equip_choice.lower() in ["y", "yes"]:
                            wpn_name_2 = "Spear"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Spear")
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    print("Not a valid choice")
                    continue
            break
            print("Please choose Two Cantrips from the following list:")
            for index, item in enumerate(warlock_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the cantrip you want to add: "))
                    if cantrip_choice in range(1, len(warlock_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(warlock_cantrip_spell_list[cantrip_choice])
                        warlock_cantrip_spell_list.remove(warlock_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(warlock_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the second cantrip you want to add: "))
                    if cantrip_choice in range(1, len(warlock_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(warlock_cantrip_spell_list[cantrip_choice])
                        warlock_cantrip_spell_list.remove(warlock_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            print("Please choose two spells from the following list:")
            for index, item in enumerate(warlock_spell_list_1, start=1):
                print(index, item)
            while True:
                try:
                    spell_choice = int(input("Please enter the number of the spell you want to add: "))
                    if spell_choice in range(1, len(warlock_spell_list_1) + 1):
                        spell_choice -= 1
                        first_level_spell_list.append(warlock_spell_list_1[spell_choice])
                        warlock_spell_list_1.remove(warlock_spell_list_1[spell_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(warlock_spell_list_1, start=1):
                print(index, item)
            while True:
                try:
                    spell_choice = int(input("Please enter the number of the spell you want to add: "))
                    if spell_choice in range(1, len(warlock_spell_list_1) + 1):
                        spell_choice -= 1
                        first_level_spell_list.append(warlock_spell_list_1[spell_choice])
                        warlock_spell_list_1.remove(warlock_spell_list_1[spell_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
    else:
        print("Invalid Input")
        continue
    break
# Work on adding skills to character sheet

print("==========================================================")
# Collect Background and Character info
print(
    "Hello Adventurer! Now that you have selected your Race and Class, It is time to flesh out the rest of your "
    "Character with a few questions.")
while True:
    print("What is", charactername, "'s Age? You can give an exact number or just say Young, Middleaged, or Old.")
    age = input("Age: ")
    print("Okay, so about how tall is", charactername, "?")
    height = input("Height: ")
    print("Alright, and how much do they weigh?")
    weight = input("Weight: ")
    print(charactername, "'s skin is what color?")
    skin_color = input("Skin Color: ")
    print("So how about their eye color?")
    eye_color = input("Eye Color: ")
    print("and their Hair color?")
    hair_color = input("Hair Color: ")
    print("Are you okay with the following choices?")
    print("Age:", age)
    print("Height:", height)
    print("Weight:", weight)
    print("Skin Color:", skin_color)
    print("Eye color:", eye_color)
    print("Hair color:", hair_color)
    confirm_choices = input("Yes or No?\n")
    if confirm_choices.lower() in ["y", "yes"]:
        break
    elif confirm_choices.lower() in ["n", "no"]:
        continue
    else:
        print("Please choose Yes or No.")
        continue
print("Alright, now that we know what your character looks like, lets flesh out WHO they are.")
personality_traits = input("Please describe your Character in one sentence.\nEnter sentence choice: ")
ideals = input("Please describe your Character's ideal. This can be anything your Character aspires to be or obtain."
               "\nEnter your Ideal: ")
bonds = input("Please describe your Character's bond. This can be some kind of personal quest or objective your "
              "Character is trying to complete.\nEnter your Bond: ")
flaws = input("Please describe your Character's flaw. This is something negative about your character that THEY know "
              "about and are trying to overcome.\nEnter your Flaw: ")
print("Please describe your Character's alignment. Your choices are :")
print("==========================================================================================================")
print("Lawful Good - Acts with compassion and always with honor and a sense of duty.")
print("==========================================================================================================")
print("Neutral Good - Acts altruistically, without regard for or against lawful precepts such as rules or tradition.")
print("==========================================================================================================")
print("Chaotic Good - Does what is necessary to bring about change for the better.")
print("==========================================================================================================")
print("Lawful Neutral - A lawful neutral character typically believes strongly in lawful concepts such")
print("as honor, order, rules, and tradition, but often follows a personal code.")
print("==========================================================================================================")
print("True Neutral - Tends not to feel strongly towards any alignment, or actively seeks their balance.")
print("==========================================================================================================")
print("Chaotic Neutral - A chaotic neutral character is an individualist who follows their own heart")
print("==========================================================================================================")
print("Lawful Evil - A lawful evil character sees a well-ordered system as being easier to exploit than")
print("to necessarily follow.")
print("==========================================================================================================")
print("Neutral Evil - A neutral evil character is typically selfish and has no qualms about turning on")
print("allies-of-the-moment, and usually makes allies primarily to further their own goals.")
print("============================================================================================================")
print("Chaotic Evil - A chaotic evil character tends to have no respect for rules, other people's")
print("lives, or anything but their own desires, which are typically selfish and cruel.")
alignment = input("Enter your Alignment: ")
experience = "0"
background = input(
    "Please enter what your character was BEFORE they became an adventurer, This can be anything from a humble Miner "
    "to a holy Priest, or even a homeless Vagabond. The choice is yours!\nEnter Background: ")
print("Okay, so you were a", background,
      ". From the following list, choose two skills you feel most closely relate to your background.")
for index, item in enumerate(skill_list, start=1):
    print(index, item)
while True:
    skill_choice_three_input = int(input("Enter what skill you want first: "))
    skill_choice_three = skill_list[skill_choice_three_input - 1]
    if skill_choice_three in skill_list:
        if skill_choice_three == "Acrobatics":
            acrobatics += 2
            acrobatics_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Animal Handling":
            animal_handling += 2
            animal_handling_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Arcana":
            arcana += 2
            arcana_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Athletics":
            athletics += 2
            athletics_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Deception":
            deception += 2
            deception_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "History":
            history += 2
            history_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Insight":
            insight += 2
            insight_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Intimidation":
            intimidation += 2
            intimidation_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Investigation":
            investigation += 2
            investigation_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Medicine":
            medicine += 2
            medicine_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Nature":
            nature += 2
            nature_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Perception":
            perception += 2
            perception_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Performance":
            performance += 2
            performance_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Persuasion":
            persuasion += 2
            persuasion_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Religion":
            religion += 2
            religion_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Sleight of Hand":
            slight_of_hand += 2
            slight_of_hand_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Stealth":
            stealth += 2
            stealth_box = True
            skill_list.remove(skill_choice_three)
            break
        elif skill_choice_three == "Survival":
            survival += 2
            survival_box = True
            skill_list.remove(skill_choice_three)
            break
        else:
            print("Invalid input")
            continue
    else:
        print("Invalid Input")
        continue
for index, item in enumerate(skill_list, start=1):
    print(index, item)
while True:
    skill_choice_four_input = int(input("Enter what skill you want for your second: "))
    skill_choice_four = skill_list[skill_choice_four_input - 1]
    if skill_choice_four == skill_choice_three:
        print("You can not choose the came skill twice.")
        continue
    elif skill_choice_four in skill_list:
        if skill_choice_four == "Acrobatics":
            acrobatics += 2
            acrobatics_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Animal Handling":
            animal_handling += 2
            animal_handling_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Arcana":
            arcana += 2
            arcana_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Athletics":
            athletics += 2
            athletics_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Deception":
            deception += 2
            deception_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "History":
            history += 2
            history_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Insight":
            insight += 2
            insight_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Intimidation":
            intimidation += 2
            intimidation_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Investigation":
            investigation += 2
            investigation_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Medicine":
            medicine += 2
            medicine_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Nature":
            nature += 2
            nature_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Perception":
            perception += 2
            perception_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Performance":
            performance += 2
            performance_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Persuasion":
            persuasion += 2
            persuasion_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Religion":
            religion += 2
            religion_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Sleight of Hand":
            slight_of_hand += 2
            slight_of_hand_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Stealth":
            stealth += 2
            stealth_box = True
            skill_list.remove(skill_choice_four)
            break
        elif skill_choice_four == "Survival":
            survival += 2
            survival_box = True
            skill_list.remove(skill_choice_four)
            break
        else:
            print("Invalid input")
            continue
    else:
        print("Invalid Input")
        continue
# RunPDFconverter - This code section deals with transfering the character data to a PDF

template_pdf = pdfrw.PdfReader(pdf_template)  # create a pdfrw object from our template.pdf
# template_pdf  # uncomment to see all the data captured from this PDF.

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

data_dict = {
    'ClassLevel': dndclass,
    'PlayerName': playername,
    'CharacterName': charactername,
    'Race ': race,
    'HPMax': hit_points,
    'Speed': speed,
    'STR': strength,
    'STRmod': str_mod,
    'DEX': dexterity,
    'DEXmod ': dex_mod,
    'CON': constitution,
    'CONmod': con_mod,
    'INT': intelligence,
    'INTmod': int_mod,
    'WIS': wisdom,
    'WISmod': wis_mod,
    'CHA': charisma,
    'CHamod': cha_mod,
    'PersonalityTraits ': personality_traits,
    'Features and Traits': ',\n '.join(featurelist),
    'ProficienciesLang': ',\n '.join(professionlist),
    'HD': hitdie,
    'HDTotal': hitdietotal,
    'ProfBonus': "+2",
    'Initiative': dex_mod,
    'ST Strength': STstr,
    'Check Box 11': STstr_box,
    'ST Dexterity': STdex,
    'Check Box 18': STdex_box,
    'ST Constitution': STcon,
    'Check Box 19': STcon_box,
    'ST Intelligence': STint,
    'Check Box 20': STint_box,
    'ST Wisdom': STwis,
    'Check Box 21': STwis_box,
    'ST Charisma': STcha,
    'Check Box 22': STcha_box,
    'Acrobatics': acrobatics,
    'Check Box 23': acrobatics_box,
    'Athletics': athletics,
    'Check Box 24': animal_handling_box,
    'Animal': animal_handling,
    'Check Box 25': arcana_box,
    'Deception ': deception,
    'Check Box 26': athletics_box,
    'History ': history,
    'Check Box 27': deception_box,
    'Insight': insight,
    'Check Box 28': history_box,
    'Intimidation': intimidation,
    'Check Box 29': insight_box,
    'Investigation ': investigation,
    'Check Box 30': intimidation_box,
    'SleightofHand': slight_of_hand,
    'Check Box 31': investigation_box,
    'Survival': survival,
    'Check Box 32': medicine_box,
    'Arcana': arcana,
    'Check Box 33': nature_box,
    'Perception ': perception,
    'Check Box 34': perception_box,
    'Nature': nature,
    'Check Box 35': performance_box,
    'Performance': performance,
    'Check Box 36': persuasion_box,
    'Persuasion': persuasion,
    'Check Box 37': religion_box,
    'Medicine': medicine,
    'Check Box 38': slight_of_hand_box,
    'Religion': religion,
    'Check Box 39': stealth_box,
    'Stealth ': stealth,
    'Check Box 40': survival_box,
    'Background': background,
    'Alignment': alignment,
    'Experience': experience,
    'Ideals': ideals,
    'Bonds': bonds,
    'Flaws': flaws,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Eyes': eye_color,
    'Skin': skin_color,
    'Hair': hair_color,
    'Wpn Name': wpn_name,
    'Wpn1 Damage': wpn1_damage,
    'Wpn Name 2': wpn_name_2,
    'Wpn2 Damage ': wpn2_damage,
    'Equipment': ', '.join(equipmentlist),
    'Spells 1014': cantrip_list[0],
    'Spells 1016': cantrip_list[1],

    'Feat+Traits': "PlaceHolder"
}


def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) is str:
                            annotation.update(pdfrw.PdfDict(AP=data_dict[key], V=data_dict[key]))
                        elif type(data_dict[key]) is bool:
                            if data_dict[key] is True:
                                annotation.update(pdfrw.PdfDict(V=pdfrw.PdfName('Yes')))
                                annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('Yes')))
                            elif data_dict[key] is False:
                                annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('')))
                        else:
                            annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
                            annotation.update(pdfrw.PdfDict(AP=''))
                    '''
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                        AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
                            '''
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


fill_pdf(pdf_template, pdf_output, data_dict)

print("Done!")
