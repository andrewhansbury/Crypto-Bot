from binance.enums import *
from binance.client import Client

import config


client = Client(config.api_key, config.api_secret)

print("*Connected to Binance*")
info = client.get_account()


account = info['accountType']
# balances = info['balances']

# print(account)
# for i in info:
#     print(i)
futures = client.futures_account()
print(futures['totalWalletBalance'])


# FIND MAX AND MIN LEVRAGE OF COIN

def maxLeverage(pair):
    result = client.futures_leverage_bracket()
    for x in result:
        if 'BTCUSDT' in x['symbol']:
            print(x)
            print('\n')


print(maxLeverage('ETHUSDT'))


def place_trade(trade):
    pass
