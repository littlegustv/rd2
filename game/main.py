import sys, os

from debug import debug
from game import Game
from gameObject import GameObject
from redis_settings import r
from connection import Connection

# Create game
try:
	game = Game()
except (KeyError, NameError) as err:
	debug('Error creating game: {}.'.format(err))
	sys.exit(1)
debug('Game created.')

# Start game
game.start()
debug('Game started.')

# Subscribe to redis channel
pubsub = r.pubsub()
pubsub.subscribe('register')

debug('Listening.')

while True:
	for item in pubsub.listen():
		if type(item['data']) is long:
			continue

		conn = Connection(item['data'])
		game.registerConnection(conn)