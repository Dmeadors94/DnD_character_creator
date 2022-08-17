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
martial_weapon_list = ["Battleaxe","Flail","Glaive","Greataxe","Greatsword","Halberd","Lance","Longsword","Maul","Morningstar","Pike","Rapier","Scimitar","Shortsword","Trident","War pick","Warhammer","Whip"]
simple_weapon_list = ["Club","Dagger","Greatclub","Handaxe","Javelin","Light hammer","Mace","Quarterstaff","Sickle","Spear"]
equipmentlist = []
traits = None
skills = None
skill_list = ["Acrobatics","Animal Handling","Arcana","Athletics","Deception","History","Insight","Intimidation","Investigation","Medicine","Nature","Perception","Performance","Persuasion","Religion","Sleight of Hand","Stealth","Survival"]
barb_skill_list = ["Animal Handling","Athletics","Intimidation","Nature","Perception","Survival"]
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
print("Your stats are: ",stats)
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
#Define Skills
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
#Run CharGen
while True :
    print("Please select a race from the following list: ")
    print("1.Human")
    print("2.Dwarf")
    print("3.Elf")
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
    elif race_input == "3" :
        print("Ability Score Increase: Your Dexterity score increases by 2.")
        print("========================")
        print("Age: Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.")
        print("========================")
        print("Alignment: Elves love freedom, variety, and self- expression, so they lean strongly toward the gentler aspects of chaos. They value and protect others’ freedom as well as their own, and they are more often good than not.")
        print("========================")
        print("Size: Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.")
        print("========================")
        print("Speed: Your base walking speed is 30 feet.")
        print("========================")
        print("Darkvision: Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("========================")
        print("Keen Senses: You have proficiency in the Perception skill.")
        print("========================")
        print("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.")
        print("========================")
        print("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        print("========================")
        print("Languages: You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poems are famous among other races. Many bards learn their language so they can add Elvish ballads to their repertoires.")
        race_choice = input("Do you want to be a Elf? Yes or No?: ")
        if race_choice.lower() in ["y" , "yes"] :
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
                        
        else : continue
    

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
            for index, item in enumerate(barb_skill_list, start=1):
                print(index, item)
            while True :
                    skill_choice_three_input = int(input("Enter what skill you want first: "))
                    skill_choice_three = barb_skill_list[skill_choice_three_input - 1]
                    if skill_choice_three in skill_list :
                            if skill_choice_three == "Acrobatics" :
                                    acrobatics += 2
                                    acrobatics_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Animal Handling" :
                                    animal_handling += 2
                                    animal_handling_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Arcana" :
                                    arcana += 2
                                    arcana_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Athletics" :
                                    athletics += 2
                                    athletics_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Deception" :
                                    deception += 2
                                    deception_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "History" :
                                    history += 2
                                    history_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Insight" :
                                    insight += 2
                                    insight_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Intimidation" :
                                    intimidation += 2
                                    intimidation_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Investigation" :
                                    investigation += 2
                                    investigation_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Medicine" :
                                    medicine += 2
                                    medicine_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Nature" :
                                    nature += 2
                                    nature_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Perception" :
                                    perception += 2
                                    perception_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Performance" :
                                    performance += 2
                                    performance_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Persuasion" :
                                    persuasion += 2
                                    persuasion_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Religion" :
                                    religion += 2
                                    religion_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Sleight of Hand" :
                                    slight_of_hand += 2
                                    slight_of_hand_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Stealth" :
                                    stealth += 2
                                    stealth_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            elif skill_choice_three == "Survival" :
                                    survival += 2
                                    survival_box = True
                                    skill_list.remove(skill_choice_three)
                                    break
                            else :
                                    print("Invalid input")
                                    continue
                    else :
                            print("Invalid Input")
                            continue
            for index, item in enumerate(barb_skill_list, start=1):
                print(index, item)
            while True :
                    skill_choice_four_input = int(input("Enter what skill you want for your second: "))
                    skill_choice_four = barb_skill_list[skill_choice_four_input - 1]
                    if skill_choice_four == skill_choice_three :
                            print("You can not choose the came skill twice.")
                            continue
                    elif skill_choice_four in skill_list :
                            if skill_choice_four == "Acrobatics" :
                                    acrobatics += 2
                                    acrobatics_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Animal Handling" :
                                    animal_handling += 2
                                    animal_handling_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Arcana" :
                                    arcana += 2
                                    arcana_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Athletics" :
                                    athletics += 2
                                    athletics_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Deception" :
                                    deception += 2
                                    deception_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "History" :
                                    history += 2
                                    history_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Insight" :
                                    insight += 2
                                    insight_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Intimidation" :
                                    intimidation += 2
                                    intimidation_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Investigation" :
                                    investigation += 2
                                    investigation_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Medicine" :
                                    medicine += 2
                                    medicine_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Nature" :
                                    nature += 2
                                    nature_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Perception" :
                                    perception += 2
                                    perception_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Performance" :
                                    performance += 2
                                    performance_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Persuasion" :
                                    persuasion += 2
                                    persuasion_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Religion" :
                                    religion += 2
                                    religion_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Sleight of Hand" :
                                    slight_of_hand += 2
                                    slight_of_hand_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Stealth" :
                                    stealth += 2
                                    stealth_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            elif skill_choice_four == "Survival" :
                                    survival += 2
                                    survival_box = True
                                    skill_list.remove(skill_choice_four)
                                    break
                            else :
                                    print("Invalid input")
                                    continue
                    else :
                            print("Invalid Input")
                            continue
            print("Please choose your starting equipment from the following: ")
            for index, item in enumerate(martial_weapon_list, start=1):
                print(index, item)
            while True :
                start_equip_one = int(input("First Equipment Choice: "))
                start_equip_one = martial_weapon_list[start_equip_one - 1]
                equipmentlist.append("Four Javelin")
                if start_equip_one in martial_weapon_list :
                    if start_equip_one == "Battleaxe" :
                        print("The Battleaxe does 1d8 Slashing Damage.\nIt has a Range of Zero.\nIt has the special trait 'Versitile', which means you can use it with both hands, if you do, then the damage is 1d10 Slashing Damage.")
                        equip_choice = input("Are you sure you want the Battleaxe? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Battleaxe"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Battleaxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Flail" :
                        print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                        equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Flail"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Flail")
                            break
                        else:
                            continue
                    elif start_equip_one == "Glaive" :
                        print("The Glaive does 1d10 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Glaive? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Glaive"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Glaive")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greataxe" :
                        print("The Greataxe does 1d12 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greataxe? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Greataxe"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Greataxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greatsword" :
                        print("The Greatsword does 2d6 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greatsword? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Greatsword"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Greatsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Halberd" :
                        print("The Halberd does 1d10 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Halberd? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Halberd"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Halberd")
                            break
                        else:
                            continue
                    elif start_equip_one == "Lance" :
                        print("The Lance does 1d12 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it.")
                        print("Special: You have disadvantage when you use a lance to attack a target within 5 feet of you. Also, a lance requires two hands to wield when you aren’t mounted.")
                        equip_choice = input("Are you sure you want the Lance? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Lance"
                            wpn1_damage = "1d12"
                            equipmentlist.append("Lance")
                            break
                        else:
                            continue
                    elif start_equip_one == "Longsword" :
                        print("The Longsword does 1d8 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead.")
                        equip_choice = input("Are you sure you want the Longsword? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Longsword"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Longsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Maul" :
                        print("The Maul does 2d6 Bludgeoning Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Maul? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Maul"
                            wpn1_damage = "2d6"
                            equipmentlist.append("Maul")
                            break
                        else:
                            continue
                    elif start_equip_one == "Morningstar" :
                        print("The Morningstar does 1d8 Piercing Damage.")
                        print("It has a Range of Zero.")
                        equip_choice = input("Are you sure you want the Morningstar? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Morningstar"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Morningstar")
                            break
                        else:
                            continue
                    elif start_equip_one == "Pike" :
                        print("The Pike does 1d10 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Heavy: Small creatures have a disadvantage on attack rolls")
                        print("Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it.")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Pike? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Pike"
                            wpn1_damage = "1d10"
                            equipmentlist.append("Pike")
                            break
                        else:
                            continue
                    elif start_equip_one == "Rapier" :
                        print("The Rapier does 1d8 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Finesse: When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.")
                        equip_choice = input("Are you sure you want the Rapier? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Rapier"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Rapier")
                            break
                        else:
                            continue
                    elif start_equip_one == "Scimitar" :
                        print("The Scimitar does 1d6 Slashing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Finesse: When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        equip_choice = input("Are you sure you want the Scimitar? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Scimitar"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Scimitar")
                            break
                        else:
                            continue
                    elif start_equip_one == "Shortsword" :
                        print("The Shortsword does 1d6 Piercing Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Finesse: When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        equip_choice = input("Are you sure you want the Shortsword? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Shortsword"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Shortsword")
                            break
                        else:
                            continue
                    elif start_equip_one == "Trident" :
                        print("The Trident does 1d6 Piercing Damage.")
                        print("It has a Range of 20 ft for short ranged attacks and 60 for long ranged attacks.")
                        print("It has the special properties: ")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        print("Versatile: This weapon can be used with two hands. If you do, the damage is 1d8 instead")
                        equip_choice = input("Are you sure you want the Trident? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Trident"
                            wpn1_damage = "1d6"
                            equipmentlist.append("Trident")
                            break
                        else:
                            continue
                    elif start_equip_one == "War pick" :
                        print("The War pick does 1d8 Piercing Damage.")
                        print("It has a Range of zero")
                        equip_choice = input("Are you sure you want the War pick? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "War pick"
                            wpn1_damage = "1d8"
                            equipmentlist.append("War pick")
                            break
                        else:
                            continue
                    elif start_equip_one == "Warhammer" :
                        print("The Warhammer does 1d8 Bludgeoning Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print("Versatile: This weapon can be used with two hands. If you do, the damage is 1d10 instead")
                        equip_choice = input("Are you sure you want the Warhammer? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Warhammer"
                            wpn1_damage = "1d8"
                            equipmentlist.append("Warhammer")
                            break
                        else:
                            continue
                    elif start_equip_one == "Whip" :
                        print("The Whip does 1d4 Slashing Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print("Finesse: When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.")
                        print("Reach: This weapon adds 5 feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it.")
                        equip_choice = input("Are you sure you want the Whip? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name = "Whip"
                            wpn1_damage = "1d4"
                            equipmentlist.append("Whip")
                            break
                        else:
                            continue
                    else:
                        continue
                else :
                    print("Not a valid option")
                    continue
            print("Please choose your second piece of starting equipment from the following, NOTE: If you choose 'Handaxe' you recive TWO of them.")
            for index, item in enumerate(simple_weapon_list, start=1):
                print(index, item)
            while True :
                start_equip_one = int(input("Second Equipment Choice: "))
                start_equip_one = simple_weapon_list[start_equip_one - 1]
                if start_equip_one in simple_weapon_list :
                    if start_equip_one == "Club" :
                        print("The Club does 1d4 Bludgeoning Damage.")
                        print("It has a Range of Zero")
                        print("It has the special properties: ")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        equip_choice = input("Are you sure you want the Club? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Club"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Club")
                            break
                        else:
                            continue
                    elif start_equip_one == "Dagger" :
                        print("The Dagger does 1d4 Piercing Damage.")
                        print("It has a Range of 20 ft for short range. 60 ft for long range.")
                        print("It has the special properties: ")
                        print("Finesse: When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls.")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        equip_choice = input("Are you sure you want the Dagger? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Dagger"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Dagger")
                            break
                        else:
                            continue
                    elif start_equip_one == "Greatclub" :
                        print("The Greatclub does 1d8 Bludgeoning Damage.")
                        print("It has a Range of Zero.")
                        print("It has the special properties: ")
                        print("Two-Handed: This weapon requires two hands when you attack with it.")
                        equip_choice = input("Are you sure you want the Greatclub? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Greatclub"
                            wpn2_damage = "1d8"
                            equipmentlist.append("Greatclub")
                            break
                        else:
                            continue
                    elif start_equip_one == "Handaxe" :
                        print("The Handaxe does 1d6 Slashing Damage.")
                        print("It has a Range of 20 ft for short range, and 60 ft for long range.")
                        print("It has the special properties: ")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        equip_choice = input("Are you sure you want the Handaxe? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Handaxe"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Handaxe")
                            equipmentlist.append("Handaxe")
                            break
                        else:
                            continue
                    elif start_equip_one == "Javelin" :
                        print("The Javelin does 1d6 Piercing Damage.")
                        print("It has a short range of 30 ft, and a long range of 120 ft.")
                        print("It has the special properties: ")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        equip_choice = input("Are you sure you want the Javelin? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Javelin"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Javelin")
                            break
                        else:
                            continue
                    elif start_equip_one == "Light hammer" :
                        print("The Light hammer does 1d4 Bludgeoning Damage.")
                        print("It has a short range of 20 ft, and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        equip_choice = input("Are you sure you want the Light hammer? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Light hammer"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Light hammer")
                            break
                        else:
                            continue
                    elif start_equip_one == "Mace" :
                        print("The Mace does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        equip_choice = input("Are you sure you want the Mace? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Mace"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Mace")
                            break
                        else:
                            continue
                    elif start_equip_one == "Quarterstaff" :
                        print("The Quarterstaff does 1d6 Bludgeoning Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print("Versatile: This weapon can be used with two hands, if you do so, then the damage is 1d8 instead")
                        equip_choice = input("Are you sure you want the Quarterstaff? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Quarterstaff"
                            wpn2_damage = "1d6"
                            equipmentlist.append("Quarterstaff")
                            break
                        else:
                            continue
                    elif start_equip_one == "Sickle" :
                        print("The Sickle does 1d4 Slashing Damage.")
                        print("It has a range of Zero.")
                        print("It has the special properties: ")
                        print("Light: A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.")
                        equip_choice = input("Are you sure you want the Sickle? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
                            wpn_name_2 = "Sickle"
                            wpn2_damage = "1d4"
                            equipmentlist.append("Sickle")
                            break
                        else:
                            continue
                    elif start_equip_one == "Spear" :
                        print("The Spear does 1d6 Piercing Damage.")
                        print("It has a short range of 20 ft and a long range of 60 ft.")
                        print("It has the special properties: ")
                        print("Thrown: If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property.")
                        print("Versatile: This weapon can be used with both hands. If you do, the damage is 1d8 instead.")
                        equip_choice = input("Are you sure you want the Spear? Yes or No\n")
                        if equip_choice.lower() in ["y" , "yes"] :
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
        else : pass
    else: continue
#Work on adding skills to character sheet

print("==========================================================")
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
        if skill_choice_three in skill_list :
                if skill_choice_three == "Acrobatics" :
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Animal Handling" :
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Arcana" :
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Athletics" :
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Deception" :
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "History" :
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Insight" :
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Intimidation" :
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Investigation" :
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Medicine" :
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Nature" :
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Perception" :
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Performance" :
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Persuasion" :
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Religion" :
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Sleight of Hand" :
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Stealth" :
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_three)
                        break
                elif skill_choice_three == "Survival" :
                        survival += 2
                        survival_box = True
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
        elif skill_choice_four in skill_list :
                if skill_choice_four == "Acrobatics" :
                        acrobatics += 2
                        acrobatics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Animal Handling" :
                        animal_handling += 2
                        animal_handling_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Arcana" :
                        arcana += 2
                        arcana_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Athletics" :
                        athletics += 2
                        athletics_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Deception" :
                        deception += 2
                        deception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "History" :
                        history += 2
                        history_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Insight" :
                        insight += 2
                        insight_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Intimidation" :
                        intimidation += 2
                        intimidation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Investigation" :
                        investigation += 2
                        investigation_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Medicine" :
                        medicine += 2
                        medicine_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Nature" :
                        nature += 2
                        nature_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Perception" :
                        perception += 2
                        perception_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Performance" :
                        performance += 2
                        performance_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Persuasion" :
                        persuasion += 2
                        persuasion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Religion" :
                        religion += 2
                        religion_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Sleight of Hand" :
                        slight_of_hand += 2
                        slight_of_hand_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Stealth" :
                        stealth += 2
                        stealth_box = True
                        skill_list.remove(skill_choice_four)
                        break
                elif skill_choice_four == "Survival" :
                        survival += 2
                        survival_box = True
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
