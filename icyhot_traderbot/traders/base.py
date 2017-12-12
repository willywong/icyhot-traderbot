
class NoopTrader:
  client = None
  tracker = None

  def __init__(self, client, tracker):
    self.client = client
    self.tracker = tracker

  def tick(self, tick_stats):
    pass

class AlwaysBuyTrader:
  client = None
  tracker = None

  def __init__(self, client, tracker):
    self.client = client
    self.tracker = tracker

  def tick(self, tick_stats):
    last_price = tick_stats["last_price"] 
    self.tracker.buy(last_price, 0.01)

class SillyTrader(NoopTrader):
  prev_price = None

  def tick(self, tick_stats):
    last_price = tick_stats["last_price"] 
    if self.prev_price != None and last_price < (0.99 * self.prev_price):
      self.tracker.buy(last_price, 0.01)
    self.prev_price = last_price

