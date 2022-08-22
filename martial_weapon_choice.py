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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/S"
                                        equipmentlist.append("Battleaxe")
                                        break
                                    else:
                                        continue
                                elif start_equip_one == "Flail":
                                    print("The Flail does 1d8 Bludgeoning Damage.\nIt has a Range of Zero.")
                                    equip_choice = input("Are you sure you want the Flail? Yes or No\n")
                                    if equip_choice.lower() in ["y", "yes"]:
                                        wpn_name = "Flail"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/B"
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
                                        wpn1_attack_bonus = 2 + str_mod
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d12/S"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d12/S"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d10/S"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d12/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/S"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "2d6/B"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d10/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/S"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/B"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d4/S"
                                        equipmentlist.append("Whip")
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Not a valid option")
                                continue