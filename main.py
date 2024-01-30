from room import Room
from item import Item
from player import Player

# create the rooms for the game
field = Room('Field', 'A barren field stretches out before you.',
             'A game trail appears to lead north.', {'north': 'log'})
log = Room('Log', 'A hollowed out log blocks the path in front of you.',
           'From here you can go north or south.', {
               'south': 'field',
               'crawl': 'fire_tower'
           })
fire_tower = Room(
    'Fire Tower',
    'A rusty firetower errupts from the treeline. The chain in front of the stairs is not much of a deterrant to adventurers.',
    '', {
        "south": "log",
        "up": "fire_tower_top"
    })
fire_tower_top = Room("Top of Fire Tower",
                      "You clear the final steps of the ladder and see the lush forest from above. A tiny flock of birds cross the horizon while a butterfly floats toward you. To the east you can see a crumbling structure in a clearing. A particularly dense section of forest gives you a bad feeling but you manage to shake it off while drinking in the magnificant vista.",
                      "You can only go back down the stairs.",
                      {"down": "fire_tower"})

flash_light = Item("Flash Light", "An old timey lantern.")
chain = Item("Chain", "An expensive looking necklace with a furby pendant. Practically useless.")

field.items = [flash_light]
log.items = [chain]

player1 = Player(input("What is your name: "))

# set the current room to the starting room
current_room = field

# main game loop
while True:
    # print the current room's name and description
    if not current_room.visited:
        print(f"\n{current_room.description}")
        if current_room.has_items():
            print("There is a(n)...")
            current_room.display_items()

    else:
        print(f"\n[{current_room.name}]\n")
        # for item in current_room.items:
        #   print(f"{item.name}")

    current_room.was_visited()

    # get the player's input
    # TODO: search through user input to find key verbs/nouns
    command = input("\nWhat do you want to do? ").lower()

    # process the player's input
    if command == "quit":
        print("\nThanks for playing!")
        break
    elif command == "controls" or command == "c":
        print(
            "\nTo move from place to place use 'north', 'south', 'east', 'west'. You may also be  able to move 'up' or 'down'. Some items can be picked up and used."
        )
    elif command == "look" or command == "l":
        current_room.display_items()
        # for item in current_room.items:
        #   print(f"{item.name}: {item.description}")
    elif command == "take" or command == "t":
        # taking out first item in current room inventory
        # TODO: TAKE SPECIFIC ITEM OUT OF ROOM
        # not sure why it only takes one item
        player1.add_inventory(current_room.items, current_room)



    elif command == "inventory" or command == "i":
        player1.display_inventory()
    else:
        next_room = current_room.move(command)
        if next_room is not None:
            # eval changes string to an object, because dictionary just has strings
            current_room = eval(next_room)
        else:
            print("\nInvalid command.")

# from room import Room

# field = Room("field", "A barren field stretches out before you")
# bombshelter = Room("bomb shelter", "A steel door opens from the ground")

# field.exits = bombshelter
# print(field.exits.name)
