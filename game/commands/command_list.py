from debug import debug

def do_where(args, player, game):
  output_buffer = ["Players near you:"]
  for m in [mobile for mobile in game.mobiles if mobile.connection]:
    output_buffer.append("{}: {}".format(m.getName(looker=player), m.parent.getName(looker=player)))
  player.output("\n".join(output_buffer))

def do_who(args, player, game):
  output_buffer = ["Players Online:"]
  for m in [mobile for mobile in game.mobiles if mobile.connection]:
    output_buffer.append("{}".format(m.getName(looker=player)))
  player.output("\n".join(output_buffer))

def do_say(args, player, game):
  if len(args) == 0:
    player.output('Say what?')
    return

  message = (' ').join(args)

  if player.parent:
    player.parent.render("{} '" + message + "'", [[player, 'say']])

def do_yell(args, player, game):
  if len(args) == 0:
    player.output('What exactly is so important?')
    return

  message = (' ').join(args)

  for room in game.rooms:
    room.render("{} '" + message + "'", [[player, 'yell']])

def do_look(args, player, game):
  if player.room:
    exits = [ k for k, v in player.room.exits.iteritems() if v ]
    exits_string =  "There are exits to the {}.".format(", ".join(exits)) if len(exits) > 0 else "There are no exits."
    objects_string = "\n".join(["{} is here.".format(obj.name) for obj in player.room.objects if obj is not player])
    player.output('You are in the {}.\n{}\n{}'.format(player.room.name, exits_string, objects_string))

    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} looks around.'.format(player.name))

def do_name(args, player, game):
  if len(args) == 0:
    player.output('Your name is {}.'.format(player.name))
  else:
    player.name = args[0]
    player.output('Your name is now {}.'.format(player.name))

def do_south(args, player, game):
  do_move("south", player, game)

def do_north(args, player, game):
  do_move("north", player, game)

def do_west(args, player, game):
  do_move("west", player, game)

def do_east(args, player, game):
  do_move("east", player, game)

def do_move(direction, player, game):
  debug(direction, 'test')
  if not player.room:
    player.output("You'd have to be in a room to move anywhere!")
  elif not player.room.exits[direction]:
    player.output("There is no exit in that direction.")
  else:
    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} leaves {}.'.format(player.getName(looker=mobile), direction))

    player.room.objects.remove(player)
    player.room = player.room.exits[direction]
    player.room.objects.append(player)

    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} has arrived.'.format(player.getName(looker=mobile)))

    do_look([], player, game)