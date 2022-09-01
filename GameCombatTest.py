import random

monsters = {
    "Goblin": {"health": 10, "power": 2, "armor_class": 0},
    "Orc": {"health": 15, "power": 3, "armor_class": 13},
    "Troll": {"health": 30, "power": 6, "armor_class": 15},
    "Ogre": {"health": 50, "power": 9, "armor_class": 16},
    "Dragon": {"health": 75, "power": 12, "armor_class": 18},
}


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Enemy:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.attack_hit_chance = power
        self.attack_damage = power
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.attack_hit_chance + Dice(20).roll() >= enemy.armor_class:
            battle_damage = self.attack_damage + Dice(6).roll()
            enemy.health -= battle_damage
            print("{} attacks {} and does {} damage".format(self.name, enemy.name, battle_damage))
            print("{} has {} health remaining".format(enemy.name, enemy.health))
        else:
            print("{} attacks {} and misses!".format(self.name, enemy.name))
            print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.attack_damage))


class Character:

    def __init__(self, name, health, power, armor_class):
        self.name = name
        self.health = health
        self.attack_hit_chance = power
        self.attack_damage = power
        self.armor_class = armor_class

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.attack_hit_chance + Dice(20).roll() >= enemy.armor_class:
            battle_damage = self.attack_damage + Dice(6).roll()
            enemy.health -= battle_damage
            print("{} attacks {} and does {} damage".format(self.name, enemy.name, battle_damage))
            print("{} has {} health remaining".format(enemy.name, enemy.health))
        else:
            print("{} attacks {} and misses!".format(self.name, enemy.name))
            print("{} has {} health remaining".format(enemy.name, enemy.health))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.attack_damage))


random_mob = (random.choice(list(monsters.items())))
hero = Character("Hero", 50, 10, 13)
monster = Enemy(random_mob[0], random_mob[1]["health"], random_mob[1]["power"], random_mob[1]["armor_class"])

hero.print_status()
monster.print_status()

while True:
    if monster.health >= 1 and hero.health >= 1:
        hero.attack(monster)
    else:
        break
    if hero.health >= 1 and monster.health >= 1:
        monster.attack(hero)
    else:
        break

if monster.alive():
    print("The monster has escaped!")
else:
    print("The monster is dead.")

if hero.alive():
    print("The hero has escaped!")
else:
    print("The hero is dead.")
