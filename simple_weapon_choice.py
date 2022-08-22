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
                                        wpn_name = "Club"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d4/B"
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
                                        wpn_name = "Dagger"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d4/P"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d8/B"
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
                                        wpn_name = "Handaxe"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/S"
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
                                        wpn_name = "Javelin"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/P"
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
                                        wpn_name = "Light hammer"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d4/B"
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
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/B"
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
                                        wpn_name = "Quarterstaff"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/B"
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
                                        wpn_name = "Sickle"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d4/S"
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
                                        wpn_name = "Spear"
                                        wpn1_attack_bonus = 2 + str_mod
                                        wpn1_damage = "1d6/P"
                                        equipmentlist.append("Spear")
                                        break
                                    else:
                                        continue
                                else:
                                    print("That is not a valid choice.")
                                    continue
                            else:
                                print("That is not a valid choice.")
                                continue