from selenium import webdriver
import discord
import time
import codecs

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


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


# change this to a more accurate name tho tbh
def getTrade():
    messages = []
    driver.implicitly_wait(10)
    sent = driver.find_elements_by_class_name(
        "message-2qnXI6")
    with codecs.open('Messages.txt', 'w', "utf-8-sig") as file:
        for message in sent:
            file.write(message.text)

    file.close()
    # with open('Messages.txt', 'w') as file:
    #     for message in messages:
    #         file.write(message)
    # file.close()


def main():

    driver.get(
        'https://discord.com/login?redirect_to=%2Fchannels%2F646144563802800139%2F834441984314834944')
    login()
    getTrade()


if __name__ == "__main__":
    main()
