#from discordwebscraper import main
#from discordwebscraper import main
from typing import List
from binance.enums import *
from binance.client import Client
import time
import config
import math


client = Client(config.api_key, config.api_secret)
print("*Connected to Binance*")
print(client.ping())


def get_last_price(symbol):
    #price_info = client.futures_orderbook_ticker(symbol=symbol)['askPrice']
    price_string = client.futures_symbol_ticker(symbol=symbol)['price']
    #price = price_string[0:price_string.index('.')]
    return float(price_string)


def get_precision(symbol):
    symbols_precision = {}
    info = client.futures_exchange_info()
    for item in info['symbols']:
        symbols_precision[item['symbol']] = item['quantityPrecision']

    return symbols_precision[symbol]


def futures_balance():
    # balances = info['balances']
    info = client.get_account()
    account = info['accountType']
    futures = client.futures_account()
    return futures['totalWalletBalance']


# FIND MAX AND MIN LEVRAGE OF COIN
# maxLeverage('DOGEUSDT') returns -> 50
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


def position_size(symbol, percent_risk, leverage):
    account_balance = int(futures_balance()[0:futures_balance().index('.')])
    usdt_size = account_balance * percent_risk/100

    return usdt_size / get_last_price(symbol) * leverage


def place_trade(trade):
    #client.futures_change_leverage(symbol='BTCUSDT', leverage=25)

    #client.futures_change_margin_type(symbol='DOGEUSDT', marginType='CROSSED')
    #x = {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'LIMIT', 'quantity': .001}

    # client.futures_create_order(**x)
    # Set symbol
    assert isinstance(trade, dict)
    symbol = trade['coin'].upper() + "USDT"

    # Set side
    side = None
    if trade['type'] == 'long':
        side = 'BUY'
    elif trade['type'] == 'short':
        side = 'SELL'

    # Set quantity
    # gets string of balance until decimal point (31.234 -> 31)
    quantity_str = str(position_size(symbol, 10, maxLeverage(symbol)))
    precision = get_precision(symbol)
    quantity = quantity_str[0:quantity_str.index('.')+precision+1]

    # Set Price Buffer
    price = get_last_price(symbol)
    print(price)
    price_length = len(str(price))
    buffered_price = price * 1.0007
    buffered_price = str(buffered_price)[0:price_length]
    print(buffered_price)

    type = 'market'
    try:
        client.futures_change_leverage(
            symbol=symbol, leverage=maxLeverage(symbol))
        if type == 'limit':
            client.futures_create_order(symbol=symbol, side=side, type='LIMIT',
                                        quantity=quantity, price=buffered_price, timeInForce='GTC')
        elif type == 'market':
            client.futures_create_order(symbol=symbol, side=side, type='MARKET',
                                        quantity=quantity,)

    except:
        print("ERROR COULD NOT PLACE TRADE")


if __name__ == "__main__":
    pass

    # print(type(futures_balance()))
