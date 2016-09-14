import unittest
from game import Game
from gameobjects.gameObject import GameObject
from gameobjects.room import Room

class TestOutputRendering(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.game = Game()
    cls.room = Room(cls.game)
    cls.mobile = GameObject(cls.game)
    cls.target = GameObject(cls.game)
    cls.bystander = GameObject(cls.game)
    cls.room.objects = [cls.mobile, cls.target, cls.bystander]
    cls.mobile.parent = cls.room
    cls.target.parent = cls.room
    cls.bystander.parent = cls.room

  def test_start(self):
    self.assertEqual(self.mobile.name, 'Default')

  def test_look(self):
    self.assertEqual(self.mobile.render('{} around.', [self.mobile], ['look'], False), 'You look around.')
    self.assertEqual(self.bystander.render('{} around.', [self.mobile], ['look'], False), '{} looks around.'.format(self.mobile.name))

  def test_say(self):
    self.assertEqual(self.mobile.render("{} 'hello!'", [self.mobile], ['say'], False), "You say 'hello!'")
    self.assertEqual(self.bystander.render("{} 'hello!'", [self.mobile], ['say'], False), "{} says 'hello!'".format(self.mobile.name))

  def test_tell(self):
    self.assertEqual(self.mobile.render("{} {} 'hello!'", [self.mobile, self.target], ['tell', None], False), "You tell {} 'hello!'".format(self.target.name))
    self.assertEqual(self.target.render("{} {} 'hello!'", [self.mobile, self.target], ['tell', None], False), "{} tells you 'hello!'".format(self.mobile.name))

  def test_answer(self):
    self.assertEqual(self.mobile.render("{} 'hello!'", [self.mobile], ['answer'], False), "You answer 'hello!'")
    self.assertEqual(self.bystander.render("{} 'hello!'", [self.mobile], ['answer'], False), "{} answers 'hello!'".format(self.mobile.name))

  def test_bash(self):
    self.assertEqual(self.mobile.render("{} {} sprawling with a powerful bash!", [self.mobile, self.target], ['send', None], False), "You send {} sprawling with a powerful bash!".format(self.target.name))
    self.assertEqual(self.target.render("{} {} sprawling with a powerful bash!", [self.mobile, self.target], ['send', None], False), "{} sends you sprawling with a powerful bash!".format(self.mobile.name))
    self.assertEqual(self.bystander.render("{} {} sprawling with a powerful bash!", [self.mobile, self.target], ['send', None], False), "{} sends {} sprawling with a powerful bash!".format(self.mobile.name, self.target.name))

  def test_combat_line(self):
    self.assertEqual(self.mobile.render("{} clumsy pierce misses {}!", [self.mobile, self.target], ['POSSESSIVE', None], False), "Your clumsy pierce misses {}!".format(self.target.name))
    self.assertEqual(self.target.render("{} clumsy pierce misses {}!", [self.mobile, self.target], ['POSSESSIVE', None], False), "{}'s clumsy pierce misses you!".format(self.mobile.name))
    self.assertEqual(self.bystander.render("{} clumsy pierce misses {}!", [self.mobile, self.target], ['POSSESSIVE', None], False), "{}'s clumsy pierce misses {}!".format(self.mobile.name, self.target.name))

def test_bounty(self):
    self.assertEqual(self.mobile.render("{} a bounty on {} head, raising the total to 500 gold.", [self.mobile, self.target], ['place', 'POSSESSIVE'], False), "You place a bounty on {}'s head, raising the total to 500 gold.".format(self.target.name))
    self.assertEqual(self.target.render("{} a bounty on {} head, raising the total to 500 gold.", [self.mobile, self.target], ['place', 'POSSESSIVE'], False), "{} places a bounty on your head, raising the total to 500 gold.".format(self.mobile.name))
    self.assertEqual(self.bystander.render("{} a bounty on {} head, raising the total to 500 gold.", [self.mobile, self.target], ['place', 'POSSESSIVE'], False), "{} places a bounty on {}'s head, raising the total to 500 gold.".format(self.mobile.name, self.target.name))

if __name__ == '__main__':
    unittest.main()