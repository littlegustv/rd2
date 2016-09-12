from debug import debug
import uuid

class GameObject(object):
  def __init__(self, game):
    self.game = game
    self.name = 'Default GameObject'
    self.uuid = uuid.uuid1()
    self.input_queue = []
    self.output_queue = []
    self.lag = 0
    self.connection = None

    debug('New GameObject created. Name: [{}] UUID [{}].'.format(self.name, self.uuid))

  def microLoop_update(self, game):
    if self.connection:
      # render output buffer to connection
      if len(self.output_queue) > 0:
        self.connection.sendOutput("\n".join(self.output_queue))
        self.output_queue = []

      # handle command from input buffer
      if len(self.input_queue) > 0 and self.lag <= 0:
        self.handle(self.input_queue.pop())

  def macroRound_update(self, game):
    pass
    #debug('UUID [{}] macroRound_update.'.format(self.uuid))

  def input(self, message):
    self.input_queue.append(message)

  def output(self, message):
    self.output_queue.append(message)

  def handle(self, message):
    self.output("You say '{}'".format(message.strip()))

  def attachConnection(self, connection):
    self.connection = connection
    self.connection.attachGameObject(self)
