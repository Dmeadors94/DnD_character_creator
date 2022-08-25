for y in dict.keys(skill_dict):
                    if y == add_skill:
                        print(f'{skill_dict[y]}')
                        choice_skill = input("Do you want to be proficent in this skill? Yes or No: ")
                        if choice_skill.lower() in ["y", "yes"]:
                            self.allowed_skills.remove(add_skill)
                            self.pri_skills.append(add_skill)