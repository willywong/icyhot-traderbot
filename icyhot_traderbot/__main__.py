import sys, os, time
import gdax
from configparser import ConfigParser

def main(argv):
  if len(argv) < 2:
    raise IOError("No config file provided. Usage: " + argv[0] + " CONFIG_FILE")

  config_file = os.path.expanduser(argv[1])
  config_parser = ConfigParser()
  config_parser.read([config_file])

  key = config_parser.get("GDAXKeys", "key")
  secret = config_parser.get("GDAXKeys", "secret")
  passphrase = config_parser.get("GDAXKeys", "passphrase")

  auth_client = gdax.AuthenticatedClient(key, secret, passphrase, api_url="https://api.gdax.com")
  print auth_client.get_accounts()
  print auth_client.get_product_24hr_stats("BTC-USD")
  prev_price = -1
  while True:
    ticker = auth_client.get_product_ticker("BTC-USD")
    print(ticker)
    current_price = ticker["price"]
    if prev_price > 0 and current_price < 0.95 * prev_price: 
      print "BUY BUY BUY at", current_price
    prev_price = current_price
    time.sleep(120)

if __name__ == "__main__":
  main(sys.argv)
