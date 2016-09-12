from debug import debug

def do_say(args, player, game):
	# Say to everyone in the game
	if len(args) == 0:
		player.output('Say what?')
		return

	message = (' ').join(args)
	player.output('You say \'{0}\'.'.format(message))

	others = [object for object in game.objects if object is not player]

	for other in others:
		other.output('{0} says \'{1}\'.'.format(player.name, message))
