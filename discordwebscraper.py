# TEST BRANCH | Faster testing because it pulls messages from text file instead of Discord

import string
from typing import List
from selenium import webdriver
import string
import pickle
import codecs
import os
os.system('cls')


DRIVER_PATH = 'chromedriver.exe'
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)


def login():

    email_input = driver.find_element_by_xpath(
        "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input")
    email_input.send_keys("andrew.hansbury@gmail.com")

    pass_input = driver.find_element_by_xpath(
        "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input")

    pass_input.send_keys("Andr1234")

    submit_button = driver.find_element_by_xpath(
        "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]")

    submit_button.click()
    print("Logged In! \n")


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


def saveToFile():
    messages = []
    driver.implicitly_wait(10)
    sent = driver.find_elements_by_class_name(
        "message-2qnXI6")
    for message in sent:
        messages.append((message.text.lower()))

    with open('Messages.txt', 'wb') as file:
        pickle.dump(messages, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()


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
    for message in trade_list:
        message = message[message.index("coin"):]
        print(message)
        print()


def main():

    # driver.get(
    #    'https://discord.com/login?redirect_to=%2Fchannels%2F646144563802800139%2F834441984314834944')
    #print("Connected to Discord! \n")
    # login()
    # saveToFile()()
    with open('Messages.txt', 'rb') as file:
        trade_array = pickle.load(file)
    getTrade(trade_array)


if __name__ == "__main__":
    main()
