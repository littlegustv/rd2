from debug import debug
import uuid

class GameObject(object):
	def __init__(self):
		self.name = 'Default GameObject'
		self.uuid = uuid.uuid1()

		debug('New GameObject created. Name: [{}] UUID [{}].'.format(self.name, self.uuid))

	def microLoop_update(self, game):
		debug('UUID [{}] microLoop_update.'.format(self.uuid))

	def macroRound_update(self, game):
		debug('UUID [{}] macroRound_update.'.format(self.uuid))
