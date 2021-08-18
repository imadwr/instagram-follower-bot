from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os

CHROME_DRIVER_PATH = "/Development/chromedriver.exe"

ACCOUNT = "python.hub"

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    # Login to instagram
    def login(self):
        print("logging in instagram")
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    # Find the followers of the target account
    def find_followers(self):
        print("finding followers")
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(ACCOUNT)
        sleep(3)
        account_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        account_button.click()
        sleep(3)
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        sleep(3)
        followers_div = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_div)
            sleep(2)

    # Follow all the followers
    def follow(self):
        print("following")
        all_follow_buttons = self.driver.find_elements_by_css_selector(".PZuss li button")
        for button in all_follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_follower = InstaFollower()

insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()

insta_follower.driver.quit()