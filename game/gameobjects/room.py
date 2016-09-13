from gameObject import GameObject
from debug import debug
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

  def input(self, message):
    for obj in self.objects:
      obj.input(message)

  def output(self, message):
    for obj in self.objects:
      obj.output(message)

  def setExit(self, direction, room, oneway=False):
    self.exits[direction] = room
    if not oneway:
      room.exits[inverseDirection[direction]] = self