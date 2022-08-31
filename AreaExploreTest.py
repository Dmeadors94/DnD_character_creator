rooms = {"Field": "A barren field with a single tree", "House": "A nice house with a front door"}

items = {"Key": "A key to a locked door", "Sword": "A sword to defeat the dragon"}


def opposite_direction(direction):
    if direction == "north":
        return "south"
    elif direction == "south":
        return "north"
    elif direction == "east":
        return "west"
    elif direction == "west":
        return "east"
    else:
        return "error"


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def connect_to(self, other_room, direction):
        self.connections[direction] = other_room
        other_room.connections[opposite_direction(direction)] = self

    def go(self, direction):
        return self.connections[direction]

    def get_details(self):
        print(self.name)
        print("Exits: " + ", ".join(self.connections.keys()))
        print(self.description)

    def get_exits(self):
        return self.connections.keys()


class Player:
    def __init__(self):
        self.current_room = None
        self.inventory = []

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory


field = Room("Field", rooms["Field"])
house = Room("House", rooms["House"])
house.items.append(items["Key"])
field.connect_to(house, "south")
print(field.get_details())
print(house.get_details())
mychar = Player
mychar.current_room = field
direction_choice = input("Which direction do you want to go?\nEnter your Choice: ")
mychar.current_room = mychar.current_room.go(direction_choice)
print(mychar.current_room.get_details())
