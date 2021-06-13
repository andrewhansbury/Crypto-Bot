from typing import List
from binance.enums import *
from binance.client import Client
import time

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

def maxLeverage(symbol):
    start_time = time.time()
    assert isinstance(symbol, str)
    symbol = symbol.upper()
    result = client.futures_leverage_bracket()
    for x in result:
        if symbol == x['symbol']:
            print("--- %s seconds ---" % (time.time() - start_time))
            return x['brackets'][0]['initialLeverage']
    return "Not Found"


print(maxLeverage('DOGEUSDT'))
x = {'symbol': 'DOGEUSDT', 'leverage': 45}
print(client.futures_change_leverage(
    **x))
client.futures_coin_change_leverage(**x)


#client.futures_change_margin_type(symbol='DOGEUSDT', marginType='CROSSED')
x = {'symbol': 'DOGEUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 100.0}

client.futures_create_order(**x)


def place_trade(trade):
    pass
