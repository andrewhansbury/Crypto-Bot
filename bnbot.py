#from discordwebscraper import main
from typing import List
from binance.enums import *
from binance.client import Client
import time
import config
import math


client = Client(config.api_key, config.api_secret)
print("*Connected to Binance*")


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
    print(quantity)
    client.futures_create_order(symbol=symbol, side=side, type='LIMIT',
                                quantity=quantity, price=get_last_price(symbol), timeInForce='GTC')
    try:
        client.futures_change_leverage(
            symbol=symbol, leverage=maxLeverage(symbol))
        client.futures_create_order(symbol=symbol, side=side, type='LIMIT',
                                    quantity=quantity, price=get_last_price(), timeInForce='GTC')

    except:
        print("ERROR COULD NOT PLACE TRADE")


if __name__ == "__main__":
    trade = {'coin': 'lit', 'type': 'long', 'entry': '3.31-3.42',
             'leverage': '20-50x', 'stop loss': '3.28', 'take profits': '** 3.49/3.55/3.79'}
    place_trade(trade)

    # print(type(futures_balance()))
