from gameobject import GameObject

class Affect(GameObject):

  def __init__(self, game, duration=None):
    super(Affect, self).__init__(game)
    self.duration = duration

  def microLoop_update(self, game):
    if self.duration != None:
      self.duration -= game.microLoop_timer
      if self.duration <= 0:
        self.end()
  
  def end(self):
    if self.parent:
      self.parent.objects.remove(self)
    self.game.objects.remove(self)