# import os
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
TARGET_ACCOUNT = "rhodesian___ridgeback"


class InstaFollower:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        """Logs into instagram account"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        accept_cookies = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._a9--")))
        accept_cookies.click()
        time.sleep(5)
        username_form = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']"
                                                                                  "/div/div[1]/div/label/input")))
        username_form.send_keys(USERNAME)
        password_form = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']"
                                                                                  "/div/div[2]/div/label/input")))
        password_form.send_keys(PASSWORD)
        login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]")))
        login_button.click()
        time.sleep(5)
        dont_save_creds_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x1i10hfl")))
        dont_save_creds_button.send_keys(Keys.ENTER)
        time.sleep(5)
        dont_turn_on_notifications_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_a9--")))
        dont_turn_on_notifications_button.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        """Goes to given instagram account and finds their followers"""
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(5)

        followers = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div"
                                                                              "/div/div/div[1]/div[1]/div[2]/div[2]"
                                                                              "/section/main/div/header/section/ul"
                                                                              "/li[2]/a")))
        followers.send_keys(Keys.ENTER)
        time.sleep(5)

    def follow(self):
        """Follows targets accounts followers"""
        for i in range(5):
            try:
                list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
                for follower in list_of_followers:
                    if follower.text == "Follow":
                        follower.click()
                        time.sleep(2)

            except Exception as e:
                print(e)


def main():
    """Main flow of program"""
    insta_follower = InstaFollower()
    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()


if __name__ == "__main__":
    main()
