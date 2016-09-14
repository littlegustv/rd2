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

  # render is for output that needs to be processed before it is sent
  def render(self, message, objects, words):
    for obj in self.objects:
      obj.render(message, objects, words)

  def setExit(self, direction, room, oneway=False):
    self.exits[direction] = room
    if not oneway:
      room.exits[inverseDirection[direction]] = self