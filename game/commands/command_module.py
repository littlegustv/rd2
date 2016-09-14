import command_list


class CommandModule(object):
	def __init__(self, name):
		self.commands = {}
		self.name = name

		self.factoryCreate()

	def factoryCreate(self):
		self.commands = {}

		if self.name == 'test':
			self.commands['look'] = command_list.do_look
			self.commands['north'] = command_list.do_north
			self.commands['south'] = command_list.do_south
			self.commands['east'] = command_list.do_east
			self.commands['west'] = command_list.do_west
			self.commands['n'] = command_list.do_north
			self.commands['s'] = command_list.do_south
			self.commands['e'] = command_list.do_east
			self.commands['w'] = command_list.do_west
			self.commands['name'] = command_list.do_name
			self.commands['say'] = command_list.do_say
			self.commands['yell'] = command_list.do_yell
			self.commands['where'] = command_list.do_where
			self.commands['who'] = command_list.do_wh0