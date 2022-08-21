print("[HIT POINTS]")
        print("Your Hit Dice is 1d12 per class level")
        print("Your Hit Points at 1st Level is: 12 + your Constitution modifier")
        print("Your Hit points at Higher Levels is: 1d12 + Constitution modifier per level")
        print("========================")
        print("[PROFICIENCIES]")
        print("Armor: ")
        print("Weapons: ")
        print("Tools: ")
        print("Saving Throws: ")
        print("Choose two skills: ")
        print("========================")
        print("[EQUIPMENT]")
        print("========================")
        print("[FEATURES]")
        print("========================")
        class_choice = input("Are you sure you want to be a class? Yes or No?: ")
        if class_choice.lower() in ["y", "yes"]:
            dndclass = "class"
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