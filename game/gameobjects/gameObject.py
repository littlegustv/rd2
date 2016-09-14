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

  def singularize(self, word):
    # shady shady shady -> need better way for handling exceptions!!
    singles = {"has": "have", "is": "are"}
    if not word:
      return ""
    elif word == "POSSESSIVE":
      return "r"
    elif word in singles.keys():
      return " {}".format(singles[word])
    else:
      return " {}".format(word)

  def pluralize(self, word):
    #shady - find a better place for this
    plurals = {"have": "has", "are": "is"}
    if not word:
      return ""
    elif word == "POSSESSIVE":
      return "'s"
    elif word in plurals.keys():
      return " {}".format(plurals[word])
    else:
      return " {}s".format(word)

  def can_see(self, object):
    return True#random.randint(0,100) < 65

  def render(self, message, objects, words, auto_output=True):
    output_buffer = []
    for i in range(0, len(objects)):
      if self == objects[i]:
        output_buffer.append("you{}".format(self.singularize(words[i])))
      else:
        if self.can_see(objects[i]):
          name = objects[i].name
        else:
          name = "someone"
        output_buffer.append("{}{}".format(name, self.pluralize(words[i])))
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