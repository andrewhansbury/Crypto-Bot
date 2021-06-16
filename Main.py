from discordwebscraper import *
import Trades
import bnbot
import time


new_trade = False

# probably should add way to keep files in memory
# instead of constantly opening and writing to file


def main():
    start_time = time.time()
    connect()
    read_and_save()
    list_of_trades = file_to_trades()
    last_trade = list_of_trades[-1]
    while True:

        driver.refresh()
        read_and_save()
        list_of_trades = file_to_trades()
        try:
            updated_last_trade = list_of_trades[-1]
        except:
            updated_last_trade = None

        if last_trade == updated_last_trade:
            print("No new trade")
            print(updated_last_trade)
            print("--- %s seconds ---" % (time.time() - start_time))

        elif updated_last_trade == None:
            print("Caught ERROR")

        else:
            # bnbot.place_trade()
            print("\nNew Trade!\n")
            print("Previous Trade: " + str(last_trade))
            print("New Trade:      " + str(updated_last_trade))

            last_trade = updated_last_trade

        time.sleep(.5)


if __name__ == "__main__":
    main()
