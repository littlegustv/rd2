from mobile import Mobile
from gameobject import GameObject
from debug import debug
from util.search import findInList

inverseDirection = {"north": "south", "south": "north", "east": "west", "west": "east" }

class Room(GameObject):

  def __init__(self, game):
    super(Room, self).__init__(game)
    self.exits = {
      "north": None,
      "south": None,
      "east": None,
      "west": None
    }
    self.game.rooms.append(self)

  def input(self, message):
    for obj in self.objects:
      obj.input(message)

  def output(self, message):
    for obj in self.objects:
      obj.output(message)

  # render is for output that needs to be processed before it is sent
  def render(self, message, args):
    for obj in self.objects:
      obj.render(message, args)

  def setExit(self, direction, room, oneway=False):
    self.exits[direction] = room
    if not oneway:
      room.exits[inverseDirection[direction]] = self

  def getMobileInRoomByName(self, name, looker=None):
    mobiles = [obj for obj in self.objects if isinstance(obj, Mobile) and looker.canSee(obj)]

    return findInList(mobiles, name)