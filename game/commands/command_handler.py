from command_module import CommandModule
from debug import debug


class CommandHandler(object):
  def __init__(self):
    self.modules = []

  def tryCommand(self, message, player, game):
    try:
      command = message.split()[0]
    except IndexError:
      # Empty message
      return

    try:
      args = message.split()[1:]
    except IndexError:
      # No args
      args = []

		allCommands = {}

			# Build giant dictionary
		for module in self.modules:
			allCommands.update(module.commands)

			commandFunction = self.getCommand(command, allCommands)
			if commandFunction is not None:
				commandFunction(args, player, game)
				break
		else:
			player.output('Huh?')

	def getCommand(self, command, allCommands):
		for key in sorted(allCommands):
			if key.startswith(command.lower()):
				return allCommands[key]

	def registerModule(self, name):
		if name in [module.name for module in self.modules]:
			debug('Tried to register duplicate CommandModule. [name={}]'.format(name), 'warning')
		else:
			newModule = CommandModule(name)
			if newModule is None:
				debug('Failed to register CommandModule. [name={}]'.format(name), 'error')
			else:
				self.modules.append(newModule)