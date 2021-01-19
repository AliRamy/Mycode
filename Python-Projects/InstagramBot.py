from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, usrename, password, anotherusername, message):
        self.username = usrename
        self.password = password
        self.anotherusername = anotherusername
        self.message = message
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email = bot.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = bot.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login = bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        login.send_keys(Keys.ENTER)

    def makechat(self):
        bot = self.bot
        time.sleep(10)
        direct = bot.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
        direct.click()
        time.sleep(10)
        sendmessage = bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
        sendmessage.send_keys(Keys.ENTER)
        time.sleep(10)
        username = bot.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')
        username.send_keys(self.anotherusername)
        time.sleep(10)
        check = bot.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button')
        check.click()
        time.sleep(10)
        chat = bot.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')
        chat.click()
        time.sleep(10)
        boxtext = bot.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        boxtext.send_keys(self.message)
        boxtext.send_keys(Keys.ENTER)
        time.sleep(10)
        bot.quit()


message = input('Input Your Message:\n')
email = input('Input The Acount You Want To Send Message To:\n')
ali = InstagramBot('bottosayhello', 'AliRamy12345@#$', email, message)
ali.login()
ali.makechat()
