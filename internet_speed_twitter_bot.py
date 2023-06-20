import os
import time
from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

PROMISED_UP_SPEED = 10
PROMISED_DOWN_SPEED = 150


class InternetSpeedTwitterBot:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.up_speed = ""
        self.down_speed = ""

    def get_internet_speed(self):
        """Tests internet speed using speedtest.net"""
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        accept_policy = self.wait.until((EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))))
        accept_policy.click()
        test_internet_speed = self.wait.until((EC.presence_of_element_located((By.CLASS_NAME, "start-text"))))
        test_internet_speed.click()
        time.sleep(40)
        self.down_speed = self.wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, ".download-speed")))).text
        self.up_speed = self.wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, ".upload-speed")))).text

    def complain_on_twitter(self):
        """Tweets complaints to ISP if speed is below SLA"""
        complaint = f"@VirginMedia I paid for Download speeds of {PROMISED_DOWN_SPEED}Mbps " \
                    f"and Upload speeds of {PROMISED_UP_SPEED}Mbps," \
                    f"Instead I have Download speeds of {self.down_speed}Mbps and upload speed of {self.up_speed}Mbps,"
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()

        log_in = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div/div[1]/div/div/"
                                                                           "div/div/div[2]/div/div/div[1]"
                                                                           "/a/div/span/span")))
        log_in.click()
        username_form = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div"
                                                                                  "/div/div/div[2]/div[2]/div/div/"
                                                                                  "div[2]/div[2]/div/div/div/div[5]"
                                                                                  "/label/div/div[2]/div/input")))
        username_form.send_keys(USERNAME)
        username_form.send_keys(Keys.ENTER)

        password_form = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div"
                                                                                  "/div/div/div[2]/div[2]/div/div"
                                                                                  "/div[2]/div[2]/div[1]/div/div/"
                                                                                  "div[3]/div/label/div/"
                                                                                  "div[2]/div[1]/input")))
        password_form.send_keys(PASSWORD)
        enter_password = self.wait.until((EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div"
                                                                                    "/div/div/div/div[2]/div[2]/div/div"
                                                                                    "/div[2]/div[2]/div[2]/div/div[1]"
                                                                                    "/div/div/div/div/span/span"))))
        enter_password.click()
        self.driver.implicitly_wait(20)

        make_tweet = self.wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, "br[data-text='true'"))))
        make_tweet.send_keys(complaint)

        send_tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]"
                                                                               "/main/div/div/div/div/div/div[3]"
                                                                               "/div/div[2]/div[1]/div/div/div/div[2]"
                                                                               "/div[3]/div/div/div[2]/div[3]"
                                                                               "/div/span/span")))
        send_tweet.click()


def main():
    """Main flow of program"""
    twitter_bot = InternetSpeedTwitterBot()
    twitter_bot.get_internet_speed()
    twitter_bot.complain_on_twitter()


if __name__ == "__main__":
    main()
