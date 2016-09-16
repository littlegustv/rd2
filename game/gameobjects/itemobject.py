from gameobject import GameObject
from debug import debug
from util.status import Status
import random

# inventory is a gameobject that does not pass its Item's modifiers on to its parent
class Inventory(GameObject):
  def getModifier(self, stat):
    return 0

# equipment is just the opposite!
class Equipment(GameObject):
  def getModifier(self, stat):
    s = 0
    for obj in self.objects:
      s += obj.getModifier(stat)
    return s

class Item(GameObject):
  def __init__(self, game):
    super(Item, self).__init__(game)
    self.blindName = 'something'
    self.modifiers = Status(self, {"health": 0, "maxhealth": random.randint(0,50), "damage": random.randint(0,10) })
    debug('Item created.')

  def getName(self, looker=None):
    name = super(Item, self).getName(looker)
    if name != self.blindName:
      return self.article(name)
    else:
      return name