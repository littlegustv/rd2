import random
from debug import debug
from gameobjects.room import Room

class SimpleProcedural():
  def generate_rooms(self):
    adjectives = ["Boreal", "Twilight", "Frozen", "Fiery", "Blasted", "Raging", "Blazing"]
    nouns = ["Forest", "Plains", "Heath", "Tundra", "Town Square", "Church", "River", "Desert"]
    directions = ["north", "south", "east", "west"]
    for i in range(0, 6):
      room = Room(self)
      room.name = "{} {}".format(random.choice(adjectives), random.choice(nouns))
      debug('Room {} created [uid={}]'.format(room.name, room.uid))

      if len(self.rooms) > 0:
        room.setExit(random.choice(directions), self.rooms[i-1])

      self.rooms.append(room)
      self.objects.append(room)