import random

def StatGen() : 

    strength = None
    dexterity = None
    constitution = None
    intelligence = None
    wisdom = None
    charisma = None

    def startstats():
        diceRolls = []
        for d6Roll in range(4):
            x = random.randint(1,6)
            diceRolls.append(x)
        del diceRolls[diceRolls.index(min(diceRolls))] #deletes the lowest number
        Stat = sum(diceRolls) #totals the remaining 3 numbers
        return Stat
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
    while True :
        strength = input("Out of your stats, which one should be Strength?\n")
        try :
            strength = int(strength)
            if strength == stats[0] or strength == stats[1] or strength == stats[2] or strength == stats[3] or strength == stats[4] or strength == stats[5] :
                stats.remove(int(strength))
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

