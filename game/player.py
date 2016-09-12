from gameObject import GameObject
from debug import debug

class Player(GameObject):
  def __init__(self, game, connection):
    super(Player, self).__init__(game)
    self.connection = connection
    self.connection.setPlayer(self)
    self.input_queue = []
    self.output_queue = []
    self.lag = 0

  def microLoop_update(self, game):
    super(Player, self).microLoop_update(game)
    
    # render output buffer to connection
    if len(self.output_queue) > 0:
      self.connection.sendOutput("\n".join(self.output_queue))
      self.output_queue = []

    # handle command from input buffer
    if len(self.input_queue) > 0 and self.lag <= 0:
      self.handle(self.input_queue.pop())

  def input(self, message):
    self.input_queue.append(message)

  def output(self, message):
    self.output_queue.append(message)

  def handle(self, message):
    self.output("You say '{}'".format(message.strip()))