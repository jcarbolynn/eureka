class Animal:
  def __init__(self, name, description, health):
    self.name = name
    self.description = description
    self.health = health

  def display_health(self):
    print(f"{self.name}'s health is: {self.health}")

  # multiplier always 0-1
  def pet(self, multiplier):
    self.health = self.health
    self.health = self.health + self.health*multiplier

  def attack(self, health, player_object, multiplier):
    # change player health
    # player_object.SET HEALTH = player_object.health - player_object.health * multiplier
    pass
