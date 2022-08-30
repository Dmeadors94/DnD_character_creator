import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Enemy:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.power = power + Dice(20).roll()
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power - enemy.armor_class
        print("{} attacks {}".format(self.name, enemy.name))
        print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Character:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.power = power + Dice(20).roll()
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power - enemy.armor_class
        print("{} attacks {}".format(self.name, enemy.name))
        print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


hero = Character("Hero", 10, 5, 5)
goblin = Enemy("Goblin", 6, 2, 5)

hero.print_status()
goblin.print_status()

while True:
    if goblin.health >= 0:
        hero.attack(goblin)
    else:
        print("The goblin is dead.")
        break
    if hero.health >= 0:
        goblin.attack(hero)
    else:
        print("The hero is dead.")
        break

if goblin.alive():
    print("The goblin has escaped!")
else:
    print("The goblin is dead.")
