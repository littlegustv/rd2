import command_list


class CommandModule(object):
	def __init__(self, name):
		self.commands = {}
		self.name = name

		if self.name == 'test':
			self.commands['look'] = command_list.do_look
			self.commands['north'] = command_list.do_north
			self.commands['south'] = command_list.do_south
			self.commands['east'] = command_list.do_east
			self.commands['west'] = command_list.do_west
			self.commands['name'] = command_list.do_name
			self.commands['say'] = command_list.do_say

	def getCommand(self, command):
		for key, function in self.commands.iteritems():
			if key.startswith(command.lower()):
				return function
				break