import command_list


class CommandModule(object):
	def __init__(self, name):
		self.commands = {}
		self.name = name

		if self.name == 'test':
			self.commands['say'] = command_list.do_say

	def getCommand(self, command):
		for key, function in self.commands.iteritems():
			if command == key:
				return function
				break