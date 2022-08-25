class Character:

    def __init__(self, name):
        self.name = name
        self.race = None
        self.dndclass = None


class DNDClass:
    def __init__(self, name):
        self.name = name
        self.allowed_skills = []
        self.skill_points = 0
        self.pri_skills = []

    def select_pri_skills(self):
        self.pri_skills = []

        for x in range(self.skill_points):
            for i, skill in enumerate(self.allowed_skills, start=1):
                print(i, skill)
            add_skill_index = input(f'Please select skill {x + 1}: ')
            try:
                add_skill_index = int(add_skill_index) - 1
            except ValueError:
                print("This is not a valid number.")
                add_skill_index = -1
            while add_skill_index < 0 or add_skill_index > (len(self.allowed_skills) - 1):
                add_skill_index = input(f'That skill is not in the allowed skills. Please select skill {x + 1}: ')
                try:
                    add_skill_index = int(add_skill_index) - 1
                except ValueError:
                    print("This is not a valid number.")
                    add_skill_index = -1
            add_skill = self.allowed_skills.pop(add_skill_index)
            self.pri_skills.append(add_skill)
