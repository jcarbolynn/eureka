class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []
    self.health = 100.0

  def add_inventory(self, item, current_room):
    '''adds item to player inventory, pops from room inventory'''
    self.inventory.append(item)
    current_room.remove_item(item)
    print(f"{item.name} was taken")

  def remove_inventory(self, item, current_room):
    '''adds item to player inventory, pops from room inventory'''
    self.inventory.remove(item)
    current_room.add_item(item)
    print(f"Placed {item.name} in {current_room.name}")

  def display_inventory(self):
    for item in self.inventory:
      print(f"{item.name}")
