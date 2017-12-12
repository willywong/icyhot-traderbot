# icyhot-traderbot

Clone it: 

```
git clone https://github.com/mahaekoh/icyhot-traderbot
```

Install it:

```
python icyhot-traderbot/setup.py install
```

## Running the backtester

### Download some data: 

You can download and extract historical price CSV files from http://api.bitcoincharts.com/v1/csv/

### Update the config: 

The file config/backtester.cfg if provided for you to modify. 

```
[BackTesting]
# updated data files can be retrieved and extracted from http://api.bitcoincharts.com/v1/csv/
data-path: /Users/mahaekoh/Downloads/coinbaseUSD.csv
start-datetime: 2017-10-01T00:00:00
end-datetime: 2017-11-01T00:00:00
tick-period: 5
budget-usd: 2000

[BackTesting-Trader]
trader-class: SillyTrader
# trader-class: AlwaysBuyTrader
```

#### Configure the tester

* `data-path`: You must update the data-path to point towards your local copy of the dataset you selected. 
* `start-datetime`: Start timestamp to begin backtesting
* `end-datetime`: End timestamp to end backtesting
* `tick-period`: Traders receive a periodic tick and make decisions on every tick. This parameter sets the tick period in seconds.
* `budget-usd`: The starting budget in USD

#### Configure the trader

* `trader-class`: Name of trader module to load. Currently built-in are: NoopTrader, AlwaysBuyTrader, and SillyTrader

### Test the trader

```
python -m icyhot_traderbot.backtester config/backtester.cfg
```

## Running the API tester

Create a key config:

```
[GDAXKeys]
key: 8541070b9this0is0my0gdax0keybcef
secret: TEbOG2SEQ3EmySecretsAreVerySecureYouSeeQu7xUIBt7ZSreiqufdshbjfnqiurD/oxWtldqYZaE7nQdEQ==
passphrase: 92j48pass1g
```

Run it:

```
python -m icyhot_traderbot config/YOUR_KEY_CONFIG.cfg
```
