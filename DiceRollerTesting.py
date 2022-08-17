from random import randint


#print(dice_value)
def roll() :
    while True:
        try:
            dice_value = input("Enter dice to roll: ")
            dice_value = dice_value.split("d")
            dice_value = list(map(int, dice_value))
            dice_amount = dice_value [0]
            dice_type = dice_value [1]
            if dice_amount >= 0 and dice_type >= 0 :
                rolling = []
                counter = int(dice_value[0])
                while counter >= 1  :
                    diceroll = randint(1,int(dice_value[1]))
                    rolling.append(diceroll)
                    counter -= 1
                return rolling
            else : print("Bad input, please input a dice value with proper value. Ex: 4d6")
        except Exception:
            print("Bad input, please input a dice value with proper value. Ex: 4d6")
            continue
        break

