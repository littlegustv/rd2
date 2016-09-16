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
    self.damageNoun = random.choice(['grep', 'entangle', 'strangle', 'blast'])
    
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

  def doDie(self):
    self.removeFromCombat()
    for m in self.game.mobiles:
      m.render('{} dead!', [[self, 'are']])
    self.stats.health = self.stats.maxhealth #shady, use accessor methods?

  def doCombatRound(self):
    debug('Combat round. [name={0}]'.format(self.name))

    for i in xrange(self.attacksPerRound):
      self.doCombatHit()

  def doCombatHit(self):
    debug('Combat hit. [name={0}]'.format(self.name))

    damage = random.randint(0, self.getStat('damage'))
    
    self.doDamage(damage=damage, target=self.fighting, noun=self.damageNoun)

  def doDamage(self, damage, target, noun):
    if not target:
      return

    debug('Combat damage. [name={0}]'.format(self.name))
    decorator = damageDecorators[damage % len(damageDecorators)]  # so we don't go out of bounds!

    # combat re-initiated on any damage dealt
    self.startCombatWith(target)

    target.modifyStat("health", -damage)

    self.output('Your {0} {1} {2} {3}{4}.'.format(
      decorator[2], 
      noun, 
      decorator[1], 
      target.getName(looker=self),
      decorator[3]
    ))

    target.output('{0}\'s {1} {2} {3} you{4}. {5}'.format(
      self.getName(looker=target),
      decorator[2], 
      noun, 
      decorator[1],
      decorator[3],
      target.getStat('health')
    ))

    for mob in self.getOtherObjectsInRoom(exceptions=[target]):
      mob.output('{0}\'s {1} {2} {3} {4}{5].'.format(
        self.getName(looker=target),
        decorator[2], 
        noun, 
        decorator[1], 
        target.getName(looker=self)),
        decorator[3]
      )

    if target.getStat('health') <= 0:
      target.doDie()