import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

SECONDS_TO_WAIT = 25
PLAY_TIME = 600 * 5


class CookieClicker:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.timeout = time.time() + SECONDS_TO_WAIT
        self.finish_time = time.time() + PLAY_TIME

    def find_big_cookie(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.driver.maximize_window()
        # Consent to personal data to be processed and select english as language
        data_consent_button = self.driver.find_element(By.CLASS_NAME, "fc-button")
        data_consent_button.click()

        english_button = self.wait.until(ec.presence_of_element_located((By.ID, "langSelect-EN")))
        english_button.click()

    def build_cookie_empire(self):
        while True:
            cookie = self.driver.find_element(By.ID, "bigCookie")
            cookie.click()

            current_time = time.time()
            if current_time > self.finish_time:
                break
            elif current_time > self.timeout:
                # Look for affordable upgrades
                products = self.driver.find_elements(By.CLASS_NAME, "product")
                unlocked_enabled_products = [product for product in products if
                                             "unlocked enabled" in product.get_attribute("class")]

                # Find last upgrade which is most expensive
                if len(unlocked_enabled_products) > 0:
                    self.timeout = time.time() + SECONDS_TO_WAIT
                    unlocked_enabled_products[-1].click()

            try:
                cookies_per_second = self.driver.find_element(By.ID, "cookiesPerSecond")
                #print(f"Cookies {cookies_per_second}")

            except StaleElementReferenceException:
                # Try again
                cookies_per_second = self.driver.find_element(By.ID, "cookiesPerSecond")
                print(f"Cookies {cookies_per_second}")


cookie_clicker_bot = CookieClicker()
time.sleep(5)
cookie_clicker_bot.find_big_cookie()
time.sleep(5)
cookie_clicker_bot.build_cookie_empire()

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# driver.get("https://orteil.dashnet.org/cookieclicker/")
# driver.maximize_window()
#
# # Consent to personal data to be processed and select english as language
# data_consent = driver.find_element(By.CLASS_NAME, "fc-button")
# data_consent.click()
# wait = WebDriverWait(driver, 10)
# english_button = wait.until(ec.presence_of_element_located((By.ID, "langSelect-EN")))
# english_button.click()
#
# cookie = wait.until(ec.presence_of_element_located((By.ID, "bigCookie")))
#
# timeout = time.time() + SECONDS_TO_WAIT
# finish_time = time.time() + PLAY_TIME
#
# while True:
#     cookie = driver.find_element(By.ID, "bigCookie")
#     cookie.click()
#
#     current_time = time.time()
#     if current_time > finish_time:
#         break
#     elif current_time > timeout:
#         # Look for affordable upgrades
#         products = driver.find_elements(By.CLASS_NAME, "product")
#         unlocked_enabled_products = [product for product in products if "unlocked enabled"
#         in product.get_attribute("class")]
#
#         # Find last upgrade which is most expensive
#         if len(unlocked_enabled_products) > 0:
#             unlocked_enabled_products[-1].click()
#         timeout = time.time() + SECONDS_TO_WAIT
#
#     try:
#         cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond")
#         print(f"Cookies {cookies_per_second}")
#
#     except StaleElementReferenceException:
#         # Try again
#         cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond")
#         print(f"Cookies {cookies_per_second}")
#
#


