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
			self.commands['who'] = command_list.do_who
			self.commands['stats'] = command_list.do_stats
			self.commands['get'] = command_list.do_get
			self.commands['drop'] = command_list.do_drop
			self.commands['inventory'] = command_list.do_inventory
			self.commands['wear'] = command_list.do_wear
			self.commands['remove'] = command_list.do_remove
			self.commands['equipment'] = command_list.do_equipment

		if self.name == 'combat':
			self.commands['bite'] = command_list.do_bite
			self.commands['kill'] = command_list.do_kill
			self.commands['flee'] = command_list.do_flee
			self.commands['burn'] = command_list.do_burn