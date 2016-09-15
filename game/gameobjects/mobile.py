from gameobject import GameObject
from itemObject import Inventory, Equipment
from debug import debug

class Mobile(GameObject):
  def __init__(self, game):
    super(Mobile, self).__init__(game)
    # since it's a mobile, add it to the game's list of mobiles
    self.game.mobiles.append(self)

    self.inventory = Inventory(game)
    self.equipment = Equipment(game)

    self.objects.append(self.inventory)
    self.objects.append(self.equipment)

    self.blindName = 'someone'
