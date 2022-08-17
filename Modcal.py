def Modcal(mod) :
    if mod == 1 :
        mod = -5
    elif mod == 2 or mod == 3 :
        mod = -4
    elif mod == 4 or mod == 5 :
        mod = -3
    elif mod == 6 or mod == 7 :
        mod = -2
    elif mod == 8 or mod == 9 :
        mod = -1
    elif mod == 10 or mod == 11 :
        mod = 0
    elif mod == 12 or mod == 13 :
        mod = 1
    elif mod == 14 or mod == 15 :
        mod = 2
    elif mod == 16 or mod == 17 :
        mod = 3
    elif mod == 18 or mod == 19 :
        mod = 4
    elif mod == 20 or mod == 21 :
        mod = 5
    elif mod == 22 or mod == 23 :
        mod = 6
    elif mod == 24 or mod == 25 :
        mod = 7
    elif mod == 26 or mod == 27 :
        mod = 8
    elif mod == 28 or mod == 29 :
        mod = 9
    elif mod == 30 :
        mod = 10
    elif mod >= 31 :
        print("Invalid stat for mod calculation")
        mod = None
    return mod
        
