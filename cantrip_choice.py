print("Please choose Two Cantrips from the following list:")
            for index, item in enumerate(druid_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the cantrip you want to add: "))
                    if cantrip_choice in range(1, len(druid_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(druid_cantrip_spell_list[cantrip_choice])
                        druid_cantrip_spell_list.remove(druid_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue
            for index, item in enumerate(druid_cantrip_spell_list, start=1):
                print(index, item)
            while True:
                try:
                    cantrip_choice = int(input("Please enter the number of the second cantrip you want to add: "))
                    if cantrip_choice in range(1, len(druid_cantrip_spell_list) + 1):
                        cantrip_choice -= 1
                        cantrip_list.append(druid_cantrip_spell_list[cantrip_choice])
                        druid_cantrip_spell_list.remove(druid_cantrip_spell_list[cantrip_choice])
                        break
                    else:
                        print("Please enter a valid number")
                        continue
                except ValueError:
                    print("Please enter a valid number")
                    continue