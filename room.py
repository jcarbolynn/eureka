class Room:
    def __init__(self, name, description, paths, exits):
        self.name = name
        self.description = description
        self.path_description = paths
        self.visited = False
        self.exits = exits
        self.items = []

    # def __str__(self):
    #   return f"{self.description}"
    def display_items(self):
        for item in self.items:
            print(f"{item.name}: {item.description}")

    def has_items(self):
        if self.items:
            return True

    def was_visited(self):
        self.visited = True

    def move(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    # def move(self, direction):
    #   if direction in self.exits:
    #     next_room_name = self.exits[direction]
    #     next_room = eval(next_room_name)
    #     print(f"You move to {next_room.name}.")
    #     print(next_room.description)
    #     print("You can go:")
    #     for exit_direction, exit_name in next_room.exits.items():
    #         print(f"- {exit_direction.capitalize()} to {eval(exit_name).name}")
    #     return next_room
    #   else:
    #     print("You can't go that way.")
    #     return None

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} placed in {self.name}")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"{item} added to PLAYER's INVENTORY")

# class Room:
#   def __init__(self, name, description):
#     self.name = name
#     self.description = description
#     self.visited = False
#     self.exits = { }
#     self.contents = []
