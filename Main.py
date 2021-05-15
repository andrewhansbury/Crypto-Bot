from discordwebscraper import *
import Trades
import bnbot
import time

new_trade = False


def main():
    connect()
    saveToFile()
    while True:
        driver.refresh()

        time.sleep(1)


if __name__ == "__main__":
    main()
