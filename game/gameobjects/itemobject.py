from gameobject import GameObject
from debug import debug

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
    debug('Item created.')

  def getName(self, looker=None):
    name = super(Item, self).getName(looker)
    if name != self.blindName:
      return self.article(name)
    else:
      return name