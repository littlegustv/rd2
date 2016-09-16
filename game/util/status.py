from debug import debug

# status is NOT a gameobject, it is not updated; it simply contains any 'stats' that an object might have

# it is used in TWO cases for a game_object
#
#   -> to define the stat attributes of the object itself (gameobject.stats)
#
#   -> to define the stat modifications that the object has on its parent (gameobject.modifiers)

class Status(object):

  def __init__(self, object, config={}):

    #shady -> is this needed?
    self.object = object

    # these default values are for mobiles
    self.damage = 10
    self.health = 100
    self.maxhealth = 100

    # allows for stats to be customized on create
    if config:
      for key, value in config.iteritems():
        if hasattr(self, key):
          setattr(self, key, value)

    debug("New Stat object created for object {}".format(object.name))

  def keys(self):
    return ["damage", "health", "maxhealth"]
