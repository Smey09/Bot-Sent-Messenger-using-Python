from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from time import sleep

import FacebookAccountInfo

class MessenBot:
    messageDict = dict()
    
    def __init__(self, username, pw) -> None:
        self.usrName = username
        self.pw = pw
        self.driver = webdriver.Chrome(options=self.ChromeOptionSetup())        
        
    def StartOperation(self):
        try:
            self.driver.get("https://web.facebook.com/")
            self._wait('//input[@name="email"]')
            self.driver.find_element(By.NAME, "email").send_keys(self.usrName)
            self.driver.find_element(By.NAME, "pass").send_keys(self.pw)
            self.driver.find_element(By.NAME, "login").click()
            for chat in self.messageDict:
                self._openMessengerChatSearch(chat)
                for message in self.messageDict[chat]:
                    self._sendMessage(message[0], message[1])
            sleep(5)
        except Exception as ec:
            print(f'Exception Occurred: {str(ec)}')

    def ChromeOptionSetup(self) -> Options:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-notifications')
        return self.chrome_options


    def SendMessageTo(self, user, message, message_amount = 1):
        if user not in self.messageDict:
            self.messageDict[user] = []
        self.messageDict[user].append([message, message_amount])


    def _openMessengerChatSearch(self, chatName):
        messenger_btn_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/span/span/div/div[1]'
        self._wait(messenger_btn_xpath)
        self.driver.find_element(By.XPATH, messenger_btn_xpath).click()

        messenger_search_xpath = '//input[@aria-label="Search Messenger"]'
        self._wait(messenger_search_xpath)
        self.driver.find_element(By.XPATH, messenger_search_xpath).send_keys(chatName)
        
        messenger_chat_xpath = f'//a[@role="presentation" and .//*[text()="{chatName}"]]'
        self._wait(messenger_chat_xpath)
        self.driver.find_element(By.XPATH, messenger_chat_xpath).click()
    
    def _sendMessage(self, message, amount=1):
        message_box_xpath = '//div[@aria-label=\'Message\']'
        self._wait(message_box_xpath)
        for i in range(amount):
            sleep(0.5)
            self.driver.find_element(By.XPATH, message_box_xpath).send_keys(message)
            self.driver.find_element(By.XPATH, message_box_xpath).send_keys(Keys.ENTER)

    def _wait(self, xpath : str):
        WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        sleep(2)

def function():
    bot1 = MessenBot(FacebookAccountInfo.username, FacebookAccountInfo.password)
    bot1.SendMessageTo('Your friend Name On facebook', 'Text that you want to sent',1)
    bot1.SendMessageTo('Smey', 'test', 2)

    bot1.StartOperation()
function()

