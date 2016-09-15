from debug import debug
import random
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

    self.blindName = 'someobject'

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

  def inflect(self, word):
    synonyms = {
      "r": "'s",
      "are": "is",
      "have": "has",
      "were": "was"
    }
    if word == None or len(word) <= 0:
      return ""
    elif word in synonyms.keys():
      if word == "r":
        return "{}".format(synonyms[word])
      else:
        return " {}".format(synonyms[word])
    else:
      return " {}s".format(word)

  def render(self, message, arguments, auto_output=True):
    output_buffer = []
    for arg in arguments:
      if self == arg[0]:
        arg[1] = "" if arg[1] == None else arg[1]
        if arg[1] == 'r' or arg[1] == "":
          output_buffer.append("you{}".format(arg[1]))
        else:
          output_buffer.append("you {}".format(arg[1]))
      else:
        if self.can_see(arg[0]):
          name = arg[0].name
        else:
          name = "someone"
        output_buffer.append("{}{}".format(name, self.inflect(arg[1])))
    result = message.format(*output_buffer)
    result = result[0].capitalize() + result[1:]
    if auto_output:
      self.output(result)
    else:
      return result

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

  def getName(self, looker=None):
    if looker is not None and looker.canSee(self):
      return self.name
    else:
      return self.blindName

  def canSee(self, target):
    return False #test
    return random.randint(0, 100) > 35