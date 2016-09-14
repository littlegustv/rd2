from debug import debug
from commands.command_handler import CommandHandler

class GameObject(object):
  def __init__(self, game):
    self.game = game
    self.name = 'Default'

    self.uid = game.currentId
    game.currentId += 1

    self.objects = []
    self.parent = None

    self.room = None

    self.input_queue = []
    self.output_queue = []
    self.lag = 0
    self.connection = None

    self.commandHandler = CommandHandler()
    self.commandHandler.registerModule('test')

    debug('New GameObject created. [name={0},id={1}].'.format(self.name, self.uid))

  def microLoop_update(self, game):
    if self.connection:
      # render output buffer to connection
      if len(self.output_queue) > 0:
        joinedMessage = '\r\n'.join(self.output_queue)
        self.connection.sendOutput("{}\r\n".format(joinedMessage))
        self.output_queue = []

      # handle command from input buffer
      if len(self.input_queue) > 0 and self.lag <= 0:
        self.handle(self.input_queue.pop())

  def macroRound_update(self, game):
    pass
    #debug('UUID [{}] macroRound_update.'.format(self.uid))

  def input(self, message):
    self.input_queue.append(message)

  def output(self, message):
    self.output_queue.append(message)

  def handle(self, message):
    self.commandHandler.tryCommand(message, self, self.game)
    # self.output("You say '{}'".format(message.strip()))

  def attachConnection(self, connection):
    self.connection = connection

  def getOtherObjectsInRoom(self):
    return [obj for obj in self.game.objects if self.room == obj.room and obj is not self]