class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []
    self.health = 10.0

  def add_inventory(self, items, current_room):
    '''adds item to player inventory, pops from room inventory'''
    for item in items:
      if not item.fixed:
        # self.inventory = self.inventory.append(current_room.items.pop(item))
        print(f"{item.name} is {item.fixed}")
        self.inventory.append(item)
        current_room.items.remove(item)
        print(f"{item.name} was taken")

  #  WHY IS IT NOT GOING THROUGH FOR LOOP AGAIN

  def display_inventory(self):
    for item in self.inventory:
      print(f"{item.name}")
