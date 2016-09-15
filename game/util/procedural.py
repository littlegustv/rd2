import random
from debug import debug
from gameobjects.room import Room, inverseDirection
from gameobjects.itemobject import Item

class SimpleProcedural():
  def generate_rooms(self):
    adjectives = ["Boreal", "Twilight", "Frozen", "Fiery", "Blasted", "Raging", "Blazing"]
    nouns = ["Forest", "Plains", "Heath", "Tundra", "Town Square", "Church", "River", "Desert"]
    for i in range(0, 6):
      room = Room(self)
      room.name = "{} {}".format(random.choice(adjectives), random.choice(nouns))
      debug('Room {} created [uid={}]'.format(room.name, room.uid))

      if len(self.rooms) > 0:
        oldRoom = self.rooms[i-1]
        exits = oldRoom.exits.keys()
        unusedExits = [exit for exit in exits if oldRoom.exits[exit] is None]
        newExit = random.choice(unusedExits)
        room.setExit(inverseDirection[newExit], oldRoom)

      for i in range(0, random.randint(0,4)):
        item = Item(self)
        room.objects.append(item)