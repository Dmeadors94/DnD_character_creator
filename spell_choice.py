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