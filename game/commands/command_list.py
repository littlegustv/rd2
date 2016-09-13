from debug import debug

def do_say(args, player, game):
  # Say to everyone in the game
  if len(args) == 0:
    player.output('Say what?')
    return

  message = (' ').join(args)
  player.output('You say \'{0}\'.'.format(message))

  if player.parent:
    player.parent.output('{0} says \'{1}\'.'.format(player.name, message))

def do_look(args, player, game):
  if player.parent:
    exits = [ k for k, v in player.parent.exits.iteritems() if v ]
    exits_string =  "There are exits to the {}.".format(", ".join(exits)) if len(exits) > 0 else "There are no exits."
    objects_string = "\n".join(["{} is here.".format(object.name) for object in player.parent.objects])
    player.output('You are in the {}.\n{}\n{}'.format(player.parent.name, exits_string, objects_string))
    player.parent.output('{} looks around.'.format(player.name))

def do_name(args, player, game):
  if len(args) == 0:
    player.output('Your name is {}.'.format(player.name))
  else:
    player.name = args[0]
    player.output('Your name is {}.'.format(player.name))

def do_south(args, player, game):
  do_move("south", player, game)

def do_north(args, player, game):
  do_move("north", player, game)

def do_west(args, player, game):
  do_move("west", player, game)

def do_east(args, player, game):
  do_move("east", player, game)

def do_move(direction, player, game):
  if not player.parent:
    player.output("You'd have to be in a room to move anywhere!")
  elif not player.parent.exits[direction]:
    player.output("There is no exit in that direction.")
  else:
    player.parent.output('{} leaves {}'.format(player.name, direction))
    player.parent.objects.remove(player)
    player.parent = player.parent.exits[direction]
    player.parent.objects.append(player)
    player.parent.output('{} has arrived.'.format(player.name))
    player.input('look')