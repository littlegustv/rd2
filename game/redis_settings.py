import redis, os, sys

from debug import debug

# Set up redis config
try:
	config = {
		'host': os.environ['RD_REDIS_HOST'],
		'port': os.environ['RD_REDIS_PORT'],
		'db': 0
	}
except KeyError as err:
	debug('Error setting up redis config: {}.'.format(err))
	sys.exit(1)
debug('Redis config complete.')

r = redis.StrictRedis(**config)
