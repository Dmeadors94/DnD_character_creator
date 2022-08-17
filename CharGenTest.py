import random
import dice

def CharGen() : 
    race = None
    dndclass = None
    hit_points = None
    AC = None
    gold = None
    equipment = None
    traits = None
    skills = None
    spells = None

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
                break
            else : continue
        
        
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
            print("========================")
            print("Are you sure you want to be a Barbarian? Yes or No?: ")
            class_choice = input(":")
            if class_choice.lower() in ["y" , "yes"] :
                dndclass = "Barbarian"
                break
            else : pass
        else: continue
            

