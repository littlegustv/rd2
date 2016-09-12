import threading

from debug import debug
from redis_settings import r

class Connection(object):
  def __init__(self, id):
    self.id = id
    self.outputChannel = 'from server {}'.format(id)

    self.pubsub = r.pubsub()
    self.game = None  #shady

    self.gameObject = None

    self.pubsub.subscribe('from client {}'.format(id))
    self.waitForRedis()

  def processInput(self, input):
    if self.gameObject:
      self.gameObject.input(input)

  def attachGameObject(self, obj):
    self.gameObject = obj

  def sendOutput(self, message):
    r.publish(self.outputChannel, message)

  def _waitForRedis(self):
    while True:
      for item in self.pubsub.listen():
        if type(item['data']) is long:
          continue

        self.processInput(item['data'])

  def waitForRedis(self):
    debug('Starting connection Redis thread.')
    t = threading.Thread(target=self._waitForRedis)
    t.setDaemon(True)
    t.start()