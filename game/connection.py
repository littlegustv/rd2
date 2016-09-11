import threading

from debug import debug
from redis_settings import r

class Connection(object):
	def __init__(self, id):
		self.id = id
		self.outputChannel = 'from server {}'.format(id)

		self.pubsub = r.pubsub()
		self.game = None  #shady

		self.pubsub.subscribe('from client {}'.format(id))
		self.waitForRedis()

	def processInput(self, input):
		# For now, just send a message back saying that you received it
		message = 'You say: {}'.format(input)
		self.sendOutput(message)

		# And send the message to everyone else chatroom style
		message = '{} says: {}'.format(self.id, input)
		self.broadcastToOthers(message)

	def sendOutput(self, message):
		r.publish(self.outputChannel, message)

	def _waitForRedis(self):
		debug('Starting Connection Redis thread.')
		while True:
			for item in self.pubsub.listen():
				if type(item['data']) is long:
					continue

				self.processInput(item['data'])

	def waitForRedis(self):
		threading.Thread(target=self._waitForRedis).start()

	def broadcastToOthers(self, message):  #shady
		if self.game is not None:
			self.game.broadcastToAllExcept(message, [self,])