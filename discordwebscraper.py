# TEST BRANCH | Faster testing because it pulls messages from text file instead of Discord
import os
import codecs
import pickle
from selenium import webdriver
from typing import List
import string
import time
start_time = time.time()
os.system('cls')


DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


def connect():
    driver.get(
        'https://discord.com/login?redirect_to=%2Fchannels%2F646144563802800139%2F834441984314834944')
    print("Connected to Discord! \n\n")


def login():
    try:
        email_input = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
        email_input.send_keys("andrew.hansbury@gmail.com")

        pass_input = driver.find_element_by_xpath(
            "//*[@id=\"app-mount\"]/div[2]/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")

        pass_input.send_keys("Andr1234")

        submit_button = driver.find_element_by_xpath(
            "//*[@id=\"app-mount\"]/div[2]/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")

        submit_button.click()
        print("Logged In! \n")
    except:
        pass


def saveToFile():
    messages = []
    driver.implicitly_wait(20)
    print("Logged In! \n\n")
    sent = driver.find_elements_by_class_name(
        "message-2qnXI6")
    for message in sent:
        messages.append((message.text.lower()))

    with open('Messages.txt', 'wb') as file:
        pickle.dump(messages, file, protocol=pickle.HIGHEST_PROTOCOL)

    file.close()
    return messages


# change this to a more accurate name tho tbh
def importTrades():
    messages = []
    driver.implicitly_wait(10)
    sent = driver.find_elements_by_class_name(
        "message-2qnXI6")
    with codecs.open('Messages.txt', 'w', "utf-8-sig") as file:
        for message in sent:
            messages.append((message.text.lower()))
            file.write(message.text)
    file.close()

    return messages


def getTrade(messages):
    trades = []
    #assert isinstance(trades, dict)
    assert isinstance(messages, List)
    # for message in messages:
    #     assert isinstance(message, str)
    #     if "coin:" in message:
    #         message = message[message.index("coin"):]
    #     else:
    #         messages.pop(message)
    # for message in messages:
    #     print(message)

    trade_list = [x for x in messages if "coin:" in x]
    # for message in trade_list:
    #     message = message[message.index("coin"):]
    #     print(message)
    #     print()
    return trade_list


def formatTrade(messages):
    # saves trades formatted as a pickled object onto the file saved_trades.txt
    saved_trades = []
    assert isinstance(messages, List)

    for message in messages:
        print(message)
        trade = {}
        assert isinstance(message, str)

        message = message.lower()
        if "coin" in message:
            str1 = message.split("coin:")[1].strip()
            coin = str1[0:str1.index('/')]
            trade['coin'] = coin
        if "short:" in message:
            str2 = message.split("short:")[1].strip()
            t_type = str2[0:str2.index('\n')]
            trade['type'] = t_type
        if "entry:" in message:
            str3 = message.split("entry:")[1].strip()
            entry = str3[0:str3.index('\n')]
            trade['entry'] = entry
        if "leverage:" in message:
            str4 = message.split("leverage:")[1].strip()
            leverage = str4[0:str4.index('\n')]
            trade['leverage'] = leverage
        if "stop loss:" in message:
            str5 = message.split("stop loss:")[1].strip()
            stop_loss = str5[0:str5.index('\n')]
            trade['stop loss'] = stop_loss
        if "take profits:" in message or "take profit" in message:
            try:
                str6 = message.split("take profits:")[1].strip()
            except:
                str6 = message.split("take profit:")[1].strip()
            take_profit = str6[0:str6.index('\n')]
            trade['take profits'] = take_profit
        saved_trades.append(trade)

    with open('saved_trades.txt', 'wb') as file:
        pickle.dump(saved_trades, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()
    print("Trades Saved to saved_trades.txt")


def loadTrades():
    # returns list of read
    all_trades = []
    with open('saved_trades.txt', 'rb') as file:
        all_trades = pickle.load(file)
    for trade in all_trades:
        print(trade)
    return all_trades


def main():
    connect()
    login()
    saveToFile()
    with open('Messages.txt', 'rb') as file:
        messages_array = pickle.load(file)
    tradelist = getTrade(messages_array)
    formatTrade(tradelist)
    loadTrades()


if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
