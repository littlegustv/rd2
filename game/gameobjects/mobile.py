import random

from gameobject import GameObject
from itemObject import Inventory, Equipment
from debug import debug
from combat.damage import damageDecorators

class Mobile(GameObject):
  def __init__(self, game):
    super(Mobile, self).__init__(game)
    # since it's a mobile, add it to the game's list of mobiles
    self.game.mobiles.append(self)

    self.inventory = Inventory(game)
    self.equipment = Equipment(game)

    self.objects.append(self.inventory)
    self.objects.append(self.equipment)

    self.blindName = 'someone'

    self.fighting = None

    self.commandHandler.registerModule('combat')

    self.attacksPerRound = 2
    self.damageNoun = 'grep'

  def macroRound_update(self, game):
    super(Mobile, self).macroRound_update(game)

    if self.fighting is not None:
      self.doCombatRound()

  def startCombatWith(self, target):
    if target.fighting is None:
      target.fighting = self

    self.fighting = target
    debug('{0} starts combat with {1}.'.format(self.name, target.name))

  def removeFromCombat(self):
    self.fighting = None

    for mob in [obj for obj in self.room.objects if isinstance(obj, Mobile)]:
      if mob.fighting == self:
        mob.fighting = None

  def doCombatRound(self):
    debug('Combat round. [name={0}]'.format(self.name))

    for i in xrange(self.attacksPerRound):
      self.doCombatHit()

  def doCombatHit(self):
    debug('Combat hit. [name={0}]'.format(self.name))

    damage = random.randint(0, 1)
    
    self.doDamage(damage=damage, target=self.fighting, noun=self.damageNoun)

  def doDamage(self, damage, target, noun):
    debug('Combat damage. [name={0}]'.format(self.name))
    decorator = damageDecorators[damage]

    self.output('Your {0} {1} {2} {3}.'.format(
      decorator[0], 
      noun, 
      decorator[1], 
      target.getName(looker=self)))

    target.output('{0}\'s {1} {2} {3} you.'.format(
      self.getName(looker=target),
      decorator[0], 
      noun, 
      decorator[1]))

    for mob in self.getOtherObjectsInRoom(exceptions=[target]):
      mob.output('{0}\'s {1} {2} {3} {4}.'.format(
        self.getName(looker=target),
        decorator[0], 
        noun, 
        decorator[1], 
        target.getName(looker=self)))