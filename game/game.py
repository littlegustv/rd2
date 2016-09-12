import time, os, threading, random
from debug import debug
from gameObject import GameObject


class Game(object):
  def __init__(self):
    self.currentId = 0

    self.objects = []
    self.connections = []

    self.microLoop_timer = float(os.environ['RD_MICROLOOP_TIMER'])
    self.macroRound_timer = float(os.environ['RD_MACROROUND_TIMER'])
    
    self.microLoop_counter = 0

  def start(self):
    self.microLoop_update()

  def microLoop_update(self):
    self.microLoop_counter += 1

    for obj in self.objects:
      obj.microLoop_update(self)

    if self.microLoop_counter >= ( self.macroRound_timer / self.microLoop_timer ) :
      self.macroLoop_update()
      self.microLoop_counter = 0

    timer = threading.Timer(self.microLoop_timer, self.microLoop_update).start()

  def macroLoop_update(self):

    if random.randint(0,2) == 0:
      self.broadcastAtmosphere()

    for obj in self.objects:
      obj.macroRound_update(self)

  def registerConnection(self, conn):
    if next((x for x in self.connections if x.id == conn.id), None) is None:
      obj = GameObject(self)

      obj.attachConnection(conn)
      conn.attachGameObject(obj)

      self.objects.append(obj)
      debug('Registered new connection. [id={0}]'.format(conn.id))
      return True
    else:
      debug('Rejected new connection (already exists): id [{}]'.format(conn.id))
      return False

  def broadcastAtmosphere(self):
    atmosphereOptions = [
      'Thunder rumbles ominously in the distance.',
      'The leaves around you rustle in the breeze.',
      'An owl hoots in the distance.'
    ]
    currentAtmosphere = random.choice(atmosphereOptions)
    debug(currentAtmosphere, 'test')
    # shady
    # just as a demo, sends currentAtmosphere to all objects
    for obj in self.objects:
      obj.output(currentAtmosphere)
