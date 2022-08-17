import pdfrw
import random
import dice
import Modcal
import os
#============================================
#TO-DO LIST
#Find a way to make PDFRW tick check boxes properly
#Make Features list print one per line
#Explain tool profs
#============================================
#Define all variables needed for StatGen
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
#Define all variables needed for CharGen
race = None
dndclass = None
hit_points = None
AC = None
gold = None
equipment = None
traits = None
skills = None
skill_list = ["Acrobatics","Animal Handling","Arcana","Athletics","Deception","History","Insight","Intimidation","Investigation","Medicine","Nature","Perception","Performance","Persuasion","Religion","Sleight of Hand","Stealth","Survival"]
spells = None
#Define all variables needed for PDFconverter
pdf_template = "template.pdf"
pdf_output = "output.pdf"
playername = input("What is your Player Name?: ")
charactername = input("What is your Character's Name?: ")
featurelist = []
professionlist = []
#Run StatGen
def startstats():
        diceRolls = []
        for d6Roll in range(4):
            x = random.randint(1,6)
            diceRolls.append(x)
        del diceRolls[diceRolls.index(min(diceRolls))] #deletes the lowest number
        Stat = sum(diceRolls) #totals the remaining 3 numbers
        return Stat
while True :
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
    print("Your stats are: ",stats)
    print("Please assign the stats to the following stats:")
    print("Strength: Your physcial power")
    print("Dexterity: Your agility and swiftness")
    print("Consitution: Your endurance")
    print("Intelligence: Your reasoning and memory")
    print("Wisdom: Your percetion and insight")
    print("Charisma: Your force of personality")
    reroll_choice = input("Do you want to re-roll your stats? Yes or No: ")
    if reroll_choice.lower() in ["y" , "yes"] :
        continue
    elif reroll_choice.lower() in ["n" , "no"] :
            break
    else :
            print("Please choose Yes or No.")
            continue
while True :
    strength = input("Out of your stats, which one should be Strength?\n")
    try :
        strength = int(strength)
        if strength == stats[0] or strength == stats[1] or strength == stats[2] or strength == stats[3] or strength == stats[4] or strength == stats[5] :
            stats.remove(int(strength))
            str_mod = Modcal.Modcal(strength)
            print("Your Strength Modifier is: ",str_mod)
            print("Your remaining stats are: ",stats)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter one of your stats")
    continue
while True :
    dexterity = input("Out of your stats, which one should be Dexterity?\n")
    try :
        dexterity = int(dexterity)
        if dexterity == stats[0] or dexterity == stats[1] or dexterity == stats[2] or dexterity == stats[3] or dexterity == stats[4] :
            stats.remove(int(dexterity))
            dex_mod = Modcal.Modcal(dexterity)
            print("Your Dexterity Modifier is: ",dex_mod)
            print("Your remaining stats are: ",stats)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter one of your stats")
    continue
while True : 
    constitution = input("Out of your stats, which one should be Constitution?\n")
    try :
        constitution = int(constitution)
        if constitution == stats[0] or constitution == stats[1] or constitution == stats[2] or constitution == stats[3] :
            stats.remove(int(constitution))
            con_mod = Modcal.Modcal(constitution)
            print("Your Constitution Modifier is: ",con_mod)
            print("Your remaining stats are: ",stats)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter one of your stats")
    continue
while True : 
    intelligence = input("Out of your stats, which one should be Intelligence?\n")
    try :
        intelligence = int(intelligence)
        if intelligence == stats[0] or intelligence == stats[1] or intelligence == stats[2] :
            stats.remove(int(intelligence))
            int_mod = Modcal.Modcal(intelligence)
            print("Your Intelligence Modifier is: ",int_mod)
            print("Your remaining stats are: ",stats)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter one of your stats")
    continue
while True : 
    wisdom = input("Out of your stats, which one should be Wisdom?\n")
    try :
        wisdom = int(wisdom)
        if wisdom == stats[0] or wisdom == stats[1] :
            stats.remove(int(wisdom))
            wis_mod = Modcal.Modcal(wisdom)
            print("Your Wisdom Modifier is: ",wis_mod)
            print("Your remaining stat is: ",stats)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter one of your stats")
while True : 
    charisma = input("Out of your stats, which one should be Charisma?\n")
    try :
        charisma = int(charisma)
        if charisma == stats[0] :
            stats.remove(int(charisma))
            cha_mod = Modcal.Modcal(charisma)
            print("Your Charisma Modifier is: ",cha_mod)
            break
        else : print("Please enter one of your stats")
        continue
    except : print("Please enter on of your stats")

print("Your final stats are: ")
print("Strength: ",strength)
print("Dexterity: ",dexterity)
print("Constitution: ",constitution)
print("Intelligence: ",intelligence)
print("Wisdom: ",wisdom)
print("Charisma: ",charisma)
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
#Run CharGen
while True :
    print("Please select a race from the following list: ")
    print("1.Human")
    print("2.Dwarf")
    #print("3.Elf")
    #print("4.Half-Elf")
    #print("5.Half-Orc")
    #print("6.Halfing")
    #print("7.Gnome")
    #print("8.Dragonborn")
    #print("9.Tiefling")

    race_input = input("Race Choice: ")

    if race_input == "1" :
        print("Ability Score Increase: Your ability scores each increase by 1.")
        print("========================")
        print("Age: Humans reach adulthood in their late teens and live less than a century.")
        print("========================")
        print("Alignment: Humans tend toward no particular alignment. The best and the worst are found among them.")
        print("========================")
        print("Size: Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Languages: You can speak, read, and write Common and one extra language of your choice.")
        print("Humans typically learn the languages of other peoples they deal with, including obscure dialects.")
        print("They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.")
        race_choice = input("Do you want to be a Human? Yes or No?: ")
        if race_choice.lower() in ["y" , "yes"] :
            race = "Human"
            strength += 1
            str_mod = Modcal.Modcal(strength)
            dexterity += 1
            dex_mod = Modcal.Modcal(dexterity)
            constitution += 1
            con_mod = Modcal.Modcal(constitution)
            intelligence += 1
            con_mod = Modcal.Modcal(intelligence)
            wisdom += 1
            wis_mod = Modcal.Modcal(wisdom)
            charisma += 1
            cha_mod = Modcal.Modcal(charisma)
            speed = "30ft"
            professionlist.append("Language: Common")
            lang_choice = input("Please enter ANY language:\nLanguage Choice: ")
            lang_choice = "Language: " + lang_choice
            professionlist.append(lang_choice)
            break
        else : continue
    
        
    elif race_input == "2" :
        print("Ability Score Increase: Your Constitution score increases by 2.")
        print("========================")
        print("Age: Dwarves mature at the same rate as humans, but they’re considered young until they reach the age of 50. On average, they live about 350 years.")
        print("========================")
        print("Alignment: Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.")
        print("========================")
        print("Size: Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.")
        print("========================")
        print("Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.")
        print("========================")
        print("Dwarven Combat Training: You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.")
        print("========================")
        print("Tool Proficiency: You gain proficiency with the artisan’s tools of your choice: smith’s tools, brewer’s supplies, or mason’s tools.")
        print("========================")
        print("Stonecunning: Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.")
        race_choice = input("Do you want to be a Dwarf? Yes or No?: ")
        if race_choice.lower() in ["y" , "yes"] :
            race = "Dwarf"
            constitution += 2
            con_mod = Modcal.Modcal(constitution)
            STcon = con_mod
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
            tool_choice = input("Please choose one:\n1.Smith's Tools\n2.Brewer's Supplies\n3.Mason's Tools\nTool Choice: ")
            while True :
                    if tool_choice == "1" :
                        professionlist.append("Tool: Smith's Tools")
                        break
                    elif tool_choice == "2" :
                        professionlist.append("Tool: Brewer's Supplies")
                        break
                    elif tool_choice == "3" :
                        professionlist.append("Tool: Mason's Tools")
                        break
                    else : continue
            
            break
        else : continue
    
#Define Skills
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
#Start Class Choice
while True :
    print("Please select a class from the following list: ")
    print("1.Barbarian")
    #print("2.Bard")
    #print("3.Cleric")
    #print("4.Druid")
    #print("5.Fighter")
    #print("6.Monk")
    #print("7.Paladin")
    #print("8.Ranger")
    #print("9.Rouge")
    #print("10.Sorcerer")
    #print("11.Warlock")
    #print("12.Wizard")

    class_input = input("Class Choice: ")

    if class_input == "1" :
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
        class_choice = input("Are you sure you want to be a Barbarian? Yes or No?: ")
        if class_choice.lower() in ["y" , "yes"] :
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
            hitdie = "1d12"
            hitdietotal = "1d12"
            break
        else : pass
    else: continue
#Work on adding skills to character sheet

print("Choose two skills:\n1.Animal Handling\n2.Athletics\n3.Intimidation\n4.Nature\n5.Perception\n6.Survival")

while True :
    skill_choice_one = input("Choose first skill: ")

    if skill_choice_one == "1" :
        animal_handling += 2
        skill_list.remove("Animal Handling")
        break
    elif skill_choice_one == "2" :
        athletics += 2
        skill_list.remove("Athletics")
        break
    elif skill_choice_one == "3" :
        intimidation += 2
        skill_list.remove("Intimidation")
        break
    elif skill_choice_one == "4" :
        nature += 2
        skill_list.remove("Nature")
        break
    elif skill_choice_one == "5" :
        perception += 2
        skill_list.remove("Perception")
        break
    elif skill_choice_one == "6" :
        survival += 2
        skill_list.remove("Survival")
        break
    else :
        print("Please select a valid skill.")
        continue
while True :
    skill_choice_two = input("Choose second skill: ")

    if skill_choice_two == skill_choice_one :
        print("You can not choose the same skill twice.")
        continue
    elif skill_choice_two == "1" :
        animal_handling += 2
        skill_list.remove("Animal Handling")
        break
    elif skill_choice_two == "2" :
        athletics += 2
        skill_list.remove("Athletics")
        break
    elif skill_choice_two == "3" :
        intimidation += 2
        skill_list.remove("Intimidation")
        break
    elif skill_choice_two == "4" :
        nature += 2
        skill_list.remove("Nature")
        break
    elif skill_choice_two == "5" :
        perception += 2
        skill_list.remove("Perception")
        break
    elif skill_choice_two == "6" :
        survival += 2
        skill_list.remove("Survival")
        break
    else :
        print("Please select a valid skill.")
        continue
    
        
#Collect Background and Character info
print("Hello Adventurer! Now that you have selected your Race and Class, It is time to flesh out the rest of your Character with a few questions.")
while True :
        print("What is",charactername,"'s Age? You can give an exact number or just say Young, Middleaged, or Old.")
        age = input("Age: ")
        print("Okay, so about how tall is",charactername,"?")
        height = input("Height: ")
        print("Alright, and how much do they weigh?")
        weight = input("Weight: ")
        print(charactername,"'s skin is what color?")
        skin_color = input("Skin Color: ")
        print("So how about their eye color?")
        eye_color = input("Eye Color: ")
        print("and their Hair color?")
        hair_color = input("Hair Color: ")
        print("Are you okay with the following choices?")
        print("Age:" ,age)
        print("Height:",height)
        print("Weight:",weight)
        print("Skin Color:",skin_color)
        print("Eye color:",eye_color)
        print("Hair color:",hair_color)
        confirm_choices = input("Yes or No?\n")
        if confirm_choices.lower() in ["y" , "yes"] :
                break
        elif confirm_choices.lower() in ["n" , "no"] :
                continue
        else :
                print("Please choose Yes or No.")
                continue
print("Alright, now that we know what your character looks like, lets flesh out WHO they are.")
background = input("Please enter what your character was BEFORE they became an adventurer, This can be anything from a humble Miner to a holy Priest, or even a homeless Vagabond. The choice is yours!\nEnter Background: ")
print("Okay, so you were a",background,". From the following list, choose two skills you feel most closely relate to your background.")
for index, item in enumerate(skill_list, start=1):
    print(index, item)
while True :
        skill_choice_three_input = int(input("Enter what skill you want first: "))
        skill_choice_three = skill_list[skill_choice_three_input - 1]
        if skill_choice_three == skill_list[0] or skill_choice_three == skill_list[1] or skill_choice_three == skill_list[2] or skill_choice_three == skill_list[3] or skill_choice_three == skill_list[4] or skill_choice_three == skill_list[5] or skill_choice_three == skill_list[6] or skill_choice_three == skill_list[7] or skill_choice_three == skill_list[8] or skill_choice_three == skill_list[9] or skill_choice_three == skill_list[10] or skill_choice_three == skill_list[11] or skill_choice_three == skill_list[12] or skill_choice_three == skill_list[13] or skill_choice_three == skill_list[14] or skill_choice_three == skill_list[15] :
                if skill_choice_three == "Acrobatics" :
                        acrobatics += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Animal Handling" :
                        animal_handling += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Arcana" :
                        arcana += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Atheltics" :
                        athletics += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Deception" :
                        deception += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "History" :
                        history += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Insight" :
                        insight += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Intimidation" :
                        intimidation += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Investigation" :
                        investigation += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Medicine" :
                        medicine += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Nature" :
                        nature += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Perception" :
                        perception += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Performance" :
                        performance += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Persuasion" :
                        persuasion += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Religion" :
                        religion += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Sleight of Hand" :
                        slight_of_hand += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Stealth" :
                        stealth += 2
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Survival" :
                        survival += 2
                        skill_list.remove(skill_choice_three)
                        break
                else :
                        print("Invalid input")
                        continue
        else :
                print("Invalid Input")
                continue
for index, item in enumerate(skill_list, start=1):
    print(index, item)
while True :
        skill_choice_four_input = int(input("Enter what skill you want for your second: "))
        skill_choice_four = skill_list[skill_choice_four_input - 1]
        if skill_choice_four == skill_choice_three :
                print("You can not choose the came skill twice.")
                continue
        elif skill_choice_four == skill_list[0] or skill_choice_four == skill_list[1] or skill_choice_four == skill_list[2] or skill_choice_four == skill_list[3] or skill_choice_four == skill_list[4] or skill_choice_four == skill_list[5] or skill_choice_four == skill_list[6] or skill_choice_four == skill_list[7] or skill_choice_four == skill_list[8] or skill_choice_four == skill_list[9] or skill_choice_four == skill_list[10] or skill_choice_four == skill_list[11] or skill_choice_four == skill_list[12] or skill_choice_four == skill_list[13] or skill_choice_four == skill_list[14] or skill_choice_four == skill_list[15] :
                if skill_choice_four == "Acrobatics" :
                        acrobatics += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Animal Handling" :
                        animal_handling += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Arcana" :
                        arcana += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Atheltics" :
                        athletics += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Deception" :
                        deception += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "History" :
                        history += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Insight" :
                        insight += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Intimidation" :
                        intimidation += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Investigation" :
                        investigation += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Medicine" :
                        medicine += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Nature" :
                        nature += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Perception" :
                        perception += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Performance" :
                        performance += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Persuasion" :
                        persuasion += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Religion" :
                        religion += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Sleight of Hand" :
                        slight_of_hand += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Stealth" :
                        stealth += 2
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Survival" :
                        survival += 2
                        skill_list.remove(skill_choice_four)
                        break
                else :
                        print("Invalid input")
                        continue
        else :
                print("Invalid Input")
                continue

#RunPDFconverter - This code section deals with transfering the character data to a PDF

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
    'PersonalityTraits ': "PlaceHolder",
    'Features and Traits': ', '.join(featurelist),
    'ProficienciesLang': ', '.join(professionlist),
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
    'Athletics': athletics,
    'Animal': animal_handling,
    'Deception ': deception,
    'History ': history,
    'Insight': insight,
    'Intimidation': intimidation,
    'Investigation ': investigation,
    'SleightofHand': slight_of_hand,
    'Survival': survival,
    'Arcana': arcana,
    'Perception ': perception,
    'Nature': nature,
    'Performance': performance,
    'Persuasion': persuasion,
    'Medicine': medicine,
    'Religion': religion,
    'Stealth ': stealth,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Eyes': eye_color,
    'Skin': skin_color,
    'Hair': hair_color,
    
    'Feat+Traits': "Dorf\ndarkvision\n"
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
