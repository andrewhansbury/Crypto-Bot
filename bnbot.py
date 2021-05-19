from binance.enums import *
from binance.client import Client

import config


client = Client(config.api_key, config.api_secret)

print("*Connected to Binance*")
info = client.get_account()


account = info['accountType']
#balances = info['balances']

# print(account)
# for i in info:
#     print(i)
futures = client.futures_account()
print(futures['totalWalletBalance'])

# for f in futures:
#     print(f)
x = client.futures_exchange_info()
print(x)
for i in x:
    print(i)


def place_trade(trade):
    pass
