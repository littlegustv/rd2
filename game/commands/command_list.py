import random

from debug import debug

def do_burn(args, player, game):
  from affects.default import OnFire
  fire = OnFire(game)
  player.objects.append(fire)
  fire.parent = player
  player.parent.render('{} to burn', [[player, 'start']])

def do_equipment(args, player, game):
  player.output("You are wearing:")
  for item in player.equipment.objects:
    player.output(item.getName(player))

def do_remove(args, player, game):
  if len(args) == 0:
    player.output('Remove what?')
    return

  items = player.equipment.objects

  for item in items:
    if item.name.lower().startswith(args[0].lower()):
      player.equipment.objects.remove(item)
      player.inventory.objects.append(item)
      player.parent.render('{} using {}', [[player, 'stop'], [item, None]])
      return

  # not found
  player.output("You aren't wearing that.")


def do_wear(args, player, game):
  if len(args) == 0:
    player.output('Wear what?')
    return

  items = player.inventory.objects

  for item in items:
    if item.name.lower().startswith(args[0].lower()):
      player.equipment.objects.append(item)
      player.inventory.objects.remove(item)
      player.parent.render('{} using {}', [[player, 'start'], [item, None]])
      return

  # not found
  player.output("You don't have that.")


def do_inventory(args, player, game):
  player.output("You are carrying:")
  for item in player.inventory.objects:
    player.output(item.getName(looker=player))
  
def do_drop(args, player, game):
  if len(args) == 0:
    player.output('Drop what?')
    return

  items = player.inventory.objects

  for item in items:
    if item.name.lower().startswith(args[0].lower()):
      player.inventory.objects.remove(item)
      player.parent.objects.append(item)
      player.parent.render('{} {}', [[player, 'drop'], [item, None]])
      return

  # not found
  player.output("You don't have that.")


def do_get(args, player, game):
  if len(args) == 0:
    player.output('Get what?')
    return

  #shady -> using __class__.__name__ to check if something can be gotten -> improve later?
  items = [item for item in player.parent.objects if item.__class__.__name__ == 'Item']

  for item in items:
    if item.name.lower().startswith(args[0].lower()):
      player.inventory.objects.append(item)
      player.parent.objects.remove(item)
      player.parent.render('{} {}', [[player, 'get'], [item, None]])
      return

  # not found
  player.output("You don't see that here.")


# shady demo command to let me see a single stat ('damage')
def do_stats(args, player, game):
  player.output("Stats:")

  for key in player.stats.keys():
    player.output("{}: {}".format(key.capitalize(), player.getStat(key)))
  
def do_where(args, player, game):
  player.output("Players near you:")
  for m in [mobile for mobile in game.mobiles if mobile.connection]:
    player.output("{}: {}".format(m.getName(looker=player), m.parent.getName(looker=player)))
  
def do_who(args, player, game):
  player.output("Players Online:")
  for m in [mobile for mobile in game.mobiles if mobile.connection]:
    player.output("{}".format(m.getName(looker=player)))
  
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

    player.output('You are in the {}.'.format(player.room.name))
    for obj_string in ["{} is here.".format(obj.getName(player)) for obj in player.room.objects if obj is not player]:
      player.output(obj_string)
    player.output("There are exits to the {}.".format(", ".join(exits)) if len(exits) > 0 else "There are no exits.")

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

    # compromise!
    player.parent = player.room

    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} has arrived.'.format(player.getName(looker=mobile)))

    do_look([], player, game)

def do_bite(args, player, game):
  if player.fighting is not None:
    player.doDamage(random.randint(30,100), player.fighting, 'bite')
    return

  if len(args) == 0:
    player.output('Kill whom?')
    return

  target = args[0]
  targetMobile = player.room.getMobileInRoomByName(target, looker=player)

  if targetMobile is None:
    player.output('They aren\'t here.')
    return

  if targetMobile == player:
    player.output('Suicide is a mortal sin.')
    return

  do_yell(['Help! I am being attacked by {0}!'.format(player.getName(looker=targetMobile)),], targetMobile, game)
  player.doDamage(random.randint(30,100), targetMobile, 'bite')

def do_kill(args, player, game):
  if player.fighting is not None:
    player.output('You are already fighting!')
    return

  if len(args) == 0:
    player.output('Kill whom?')
    return

  target = args[0]
  targetMobile = player.room.getMobileInRoomByName(target, looker=player)

  if targetMobile is None:
    player.output('They aren\'t here.')
    return

  if targetMobile == player:
    player.output('Suicide is a mortal sin.')
    return

  do_yell(['Help! I am being attacked by {0}!'.format(player.getName(looker=targetMobile)),], targetMobile, game)
  player.startCombatWith(targetMobile)
  player.doCombatRound()

def do_flee(args, player, game):
  if player.fighting is None:
    player.output('You aren\'t fighting anyone.')
    return

  available_exits = []
  for direction, exit in player.parent.exits.iteritems():
    if exit != None:
      available_exits.append(direction)

  if len(available_exits) <= 0:
    player.output('There is no way out!')

  if random.randint(0,9) > 4:
    player.output('You can\'t escape!')

    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} tries to flee, but fails!'.format(player.getName(looker=mobile)))
  else:
    player.removeFromCombat()

    player.output('You flee from combat!')

    for mobile in player.getOtherObjectsInRoom():
      mobile.output('{} has fled!'.format(player.getName(looker=mobile)))

    do_move(random.choice(available_exits), player, game)