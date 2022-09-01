rooms = {"Field": "A barren field with a single tree", "House": "A nice house with a front door",
         "Forest": "A lush forest with many trees", "Cave": "A dark cave with no light",
         "Water Well": "A old abandoned well with a chain hanging down into the darkness.",
         "Living Room": "A dusty old Living Room. The room is littered with cobwebs."}

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
        self.locked = False

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

    def look(self):
        self.current_room.get_details()
        for item in self.current_room.items:
            print(item)
        for item in self.inventory:
            print(item)


field = Room("Field", rooms["Field"])
house = Room("House", rooms["House"])
cave = Room("Cave", rooms["Cave"])
forest = Room("Forest", rooms["Forest"])
water_well = Room("Water Well", rooms["Water Well"])
living_room = Room("Living Room", rooms["Living Room"])
house.items.append(items["Key"])
field.connect_to(house, "south")
field.connect_to(cave, "east")
field.connect_to(forest, "west")
field.connect_to(water_well, "north")
house.connect_to(living_room, "south")
living_room.locked = True
mychar = Player()
mychar.current_room = field
while True:
    print("Please choose a command. Type 'help' for a list of commands.")
    command = input("> ")
    if command == "help":
        print("""
        You can move around the map by typing the direction you want to go.
        You can also type 'look' to see what is around you.
        You can also type 'inventory' to see what you have in your inventory.
        you can also type 'pickup' to pick up an item.
        You can also type 'quit' to quit the game.
        """)
    elif command == "quit":
        break
    elif command == "look":
        mychar.look()
    elif command == "inventory":
        print(mychar.get_inventory())
    elif command == "pickup" and mychar.current_room.items:
        print("You picked up a " + mychar.current_room.items[0])
        mychar.pickup(mychar.current_room.items.pop())
        if "A key to a locked door" in mychar.get_inventory():
            living_room.locked = False
    elif command in mychar.current_room.get_exits():
        mychar.current_room = mychar.current_room.go(command)
        if mychar.current_room.locked is True:
            print("The way is locked.")
            mychar.current_room = mychar.current_room.go(opposite_direction(command))
        elif mychar.current_room.monster is True:
            print("A monster has appeared!")
            mychar.current_room.monster = False
        else:
            print("You are now in a " + mychar.current_room.name)
    else:
        print("Command not recognised.")
