from debug import debug

# status is NOT a gameobject, it is not updated; it simply contains any 'stats' that an object might have

# it is used in TWO cases for a game_object
#
#   -> to define the stat attributes of the object itself (gameobject.stats)
#
#   -> to define the stat modifications that the object has on its parent (gameobject.modifiers)

class Status(object):

  def __init__(self, object):

    #shady -> is this needed?
    self.object = object

    self.damage = 10
    self.health = 100
    debug("New Stat object created for object {}".format(object.name))

  def keys(self):
    return ["damage", "health"]
