class Trades:

    last_trade = None

    def __init__(self, coin, type, entry, leverage, sl, tp):
        self.coin = coin
        self.type = type
        self.entry = entry
        self.leverage = leverage
        self.sl = sl
        self.tp = tp
        last_trade = self
