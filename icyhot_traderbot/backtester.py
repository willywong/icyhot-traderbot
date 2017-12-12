import sys, os, time, datetime, dateutil.parser, importlib
import gdax
from configparser import ConfigParser
from .traders.base import AlwaysBuyTrader, SillyTrader

class TraderPerformanceTracker:
  """
  Minimal performance tracker
  """

  transactions = []
  client = None
  budget = 0.0
  wallet_btc = 0.0
  wallet_usd = 0.0

  def __init__(self, client, budget = 0.0):
    self.client = client
    self.budget = float(budget)
    self.wallet_usd = float(budget)
  
  def buy(self, price = 0.0, size=0.0, product_id = "BTC-USD"):
    if self.wallet_usd < price * size:
      print("Ignoring BUY request, not enough USD: needed " + str(price * size) + " only had " + str(self.wallet_usd))
      return
    print "BUY ", size, "at", price
    self.wallet_usd = self.wallet_usd - (price * size)
    self.wallet_btc = self.wallet_btc + size
    self.transactions.append({
      "type": "buy",
      "price": price,
      "size": size,
      "product_id": product_id
    })

  def sell(self, price = 0.0, size = 0.0, product_id = "BTC-USD"):
    if self.wallet_btc < size: 
      print("Ignoring SELL request, not enough BTC: needed " + str(size) + " only had " + str(self.wallet_btc))
      return
    self.wallet_btc = self.wallet_btc - size
    self.wallet_usd = self.wallet_usd + (price * size)
    self.transactions.append({
      "type": "sell",
      "price": price,
      "size": size,
      "product_id": product_id
    })

  def print_current_stats(self, last_price):
    # ticker = self.client.get_product_ticker("BTC-USD")
    print "Initial budget:", self.budget
    print "Ticker USD/BTC:", last_price
    print "BTC wallet:", self.wallet_btc
    btc_wallet_in_usd = (self.wallet_btc * last_price)
    print "BTC wallet in USD:", btc_wallet_in_usd
    print "USD wallet:", self.wallet_usd
    print "Wallet total in USD:", (self.wallet_usd + btc_wallet_in_usd)
    print "Total (realized and unrealized) gains (USD):", ((self.wallet_usd + btc_wallet_in_usd) - self.budget)
    print "Total (realized and unrealized) gains (%):", (((self.wallet_usd + btc_wallet_in_usd) - self.budget) * 100.0 / self.budget)
    print "Transactions:", str(self.transactions)

def main(argv):
  if len(argv) < 2:
    raise IOError("No config file provided. Usage: " + argv[0] + " CONFIG_FILE")

  config_file = os.path.expanduser(argv[1])
  config_parser = ConfigParser()
  config_parser.read([config_file])

  test_data_file = config_parser.get("BackTesting", "data-path")
  start_datetime = config_parser.get("BackTesting", "start-datetime")
  end_datetime = config_parser.get("BackTesting", "end-datetime")
  tick_period = int(config_parser.get("BackTesting", "tick-period"))
  budget = float(config_parser.get("BackTesting", "budget-usd"))
  
  trader_class = config_parser.get("BackTesting-Trader", "trader-class")
  try:
    TraderClass = getattr(importlib.import_module("icyhot_traderbot.traders"), trader_class)
  except AttributeError as w:
    TraderClass = getattr(importlib.import_module("icyhot_traderbot.traders.base"), trader_class)

  start_timestamp = (dateutil.parser.parse(start_datetime) - datetime.datetime(1970,1,1)).total_seconds() 
  end_timestamp = (dateutil.parser.parse(end_datetime) - datetime.datetime(1970,1,1)).total_seconds()

  tracker = TraderPerformanceTracker(client=None, budget=2000.0)
  trader = TraderClass(client=None, tracker=tracker)

  # in seconds
  tick_period = 5 
  prev_timestamp = None
  last_price = None

  with open(test_data_file, 'r') as data_f: 
    for line in data_f:
      # format is timestamp,price,quantity
      parts = line.split(",")
      timestamp = int(parts[0])
      price = float(parts[1])
      quantity = float(parts[2])

      if timestamp < start_timestamp:
	continue
      if timestamp > end_timestamp:
	break

      should_tick = False
      if prev_timestamp is None:
	should_tick = True
      elif timestamp >= (prev_timestamp + tick_period):
	should_tick = True

      if should_tick:
	tick_stats = {
	  "last_price": price
	}
	trader.tick(tick_stats)

      last_price = price

  tracker.print_current_stats(last_price)

if __name__ == "__main__":
  main(sys.argv)
