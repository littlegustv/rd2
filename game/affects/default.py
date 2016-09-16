from gameobjects.affect import Affect
from util.status import Status

class OnFire(Affect):
  def __init__(self, game, duration=10):
    super(OnFire, self).__init__(game, duration)
    self.modifiers = Status(self, {"health": 0, "maxhealth": 0, "damage": 10})

  def macroRound_update(self, game):
    if self.parent:
      self.parent.modifyStat('health', -5)
      self.parent.parent.render('{}.', [[self.parent, 'burn']])

  def end(self):
    super(OnFire, self).end()
    self.parent.parent.render('{} burning.', [[self.parent, 'stop']])