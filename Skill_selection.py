print("Please choose two skills from the following list:")
            for index, item in enumerate(paladin_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want first: "))
                    skill_choice_three = paladin_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except ValueError:
                    print("Invalid Input")
                    continue
                except IndexError:
                    print("Invalid Input")
                    continue
            for index, item in enumerate(paladin_skill_list, start=1):
                print(index, item)
            while True:
                try:
                    skill_choice_he_input = int(input("Enter what skill you want second: "))
                    skill_choice_three = paladin_skill_list[skill_choice_he_input - 1]
                    if skill_choice_three in skill_list:
                        if skill_choice_three == "Acrobatics":
                            acrobatics += 2
                            acrobatics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Animal Handling":
                            animal_handling += 2
                            animal_handling_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Arcana":
                            arcana += 2
                            arcana_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Athletics":
                            athletics += 2
                            athletics_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Deception":
                            deception += 2
                            deception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "History":
                            history += 2
                            history_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Insight":
                            insight += 2
                            insight_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Intimidation":
                            intimidation += 2
                            intimidation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Investigation":
                            investigation += 2
                            investigation_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Medicine":
                            medicine += 2
                            medicine_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Nature":
                            nature += 2
                            nature_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Perception":
                            perception += 2
                            perception_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Performance":
                            performance += 2
                            performance_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Persuasion":
                            persuasion += 2
                            persuasion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Religion":
                            religion += 2
                            religion_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Sleight of Hand":
                            slight_of_hand += 2
                            slight_of_hand_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Stealth":
                            stealth += 2
                            stealth_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        elif skill_choice_three == "Survival":
                            survival += 2
                            survival_box = True
                            skill_list.remove(skill_choice_three)
                            paladin_skill_list.remove(skill_choice_three)
                            break
                        else:
                            print("Invalid input")
                            continue
                    else:
                        print("Invalid Input")
                        continue
                except IndexError:
                    print("Invalid Input")
                    continue
                except ValueError:
                    print("Invalid Input")
                    continue