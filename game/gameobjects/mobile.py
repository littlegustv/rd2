from gameobject import GameObject

class Mobile(GameObject):
	def __init__(self, game):
		super(Mobile, self).__init__(game)

		self.blindName = 'someone'