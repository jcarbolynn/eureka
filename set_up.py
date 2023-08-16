from room import Room
from item import Item
from animal import Animal

class Set_Up:
  def __init__(self):
    # create the rooms for the game
    self.field = Room('Field', 'A barren field stretches out before you.',
                 'A game trail appears to lead north.', {'north': 'log'})
    self.log = Room('Log', 'A hollowed out log blocks the path in front of you.',
               'From here you can go north or south.', {'south': 'field','crawl': 'fire_tower'})
    self.fire_tower = Room('Fire Tower','A rusty firetower errupts from the treeline. The chain in front of the stairs is not much of a deterrant to adventurers.','', {"south": "log","up": "fire_tower_top"})
    self.fire_tower_top = Room("Top of Fire Tower", "You clear the final steps of the ladder and see the lush forest from above. A tiny flock of birds cross the horizon while a butterfly floats toward you. To the east you can see a crumbling structure in a clearing. A particularly dense section of forest gives you a bad feeling but you manage to shake it off while drinking in the magnificant vista.","You can only go back down the stairs.",{"down": "fire_tower"})
    
    self.light = Item("Light", "An old timey lantern.")
    self.chain = Item("Chain", "An expensive looking necklace with a furby pendant. Practically useless.")
    
    self.field.items = [self.light, self.chain]
    self.log.items = [self.chain]
    
    self.cat = Animal("cat", "fat cat with a primordial pouch", 45)
    
    self.field.animals = [self.cat]
