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

# Constants for timing
SECONDS_TO_WAIT = 35    # Interval to check for upgrades
PLAY_TIME = 600 * 5     # Total playtime in seconds


class CookieClicker:
    """
    Selenium bot to automate Cookie clicking game
    Bot clicks on cookie and purchases available upgrades
    """
    def __init__(self):
        """
        Initializes web driver and necessary options
        """
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.timeout = time.time() + SECONDS_TO_WAIT
        self.finish_time = time.time() + PLAY_TIME

    def find_big_cookie(self):
        """
        Navigates to cookie game, maximizes window, handles initial setup of accepting cookies and selecting language
        """
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.driver.maximize_window()
        # Consent to personal data to be processed
        data_consent_button = self.driver.find_element(By.CLASS_NAME, "fc-button")
        data_consent_button.click()
        # select english as language
        english_button = self.wait.until(ec.presence_of_element_located((By.ID, "langSelect-EN")))
        english_button.click()

    def build_cookie_empire(self):
        """
        Continuously click cookie and each interval purchase available upgrades
        """
        while True:
            # Locate cookie element and click
            cookie = self.driver.find_element(By.ID, "bigCookie")
            cookie.click()

            current_time = time.time()  # Retrieve current time in seconds
            if current_time > self.finish_time:     # Stop game when playtime exceeded
                break
            elif current_time > self.timeout:
                # Look for affordable upgrades after each interval
                products = self.driver.find_elements(By.CLASS_NAME, "product")
                unlocked_enabled_products = [product for product in products if
                                             "unlocked enabled" in product.get_attribute("class")]

                # Find last upgrade which is most expensive
                if len(unlocked_enabled_products) > 0:
                    # Reset timer by adding interval time to current time in seconds
                    self.timeout = time.time() + SECONDS_TO_WAIT
                    unlocked_enabled_products[-1].click()

            # try:
            #     # Attempt to print cookies being produced per second
            #     cookies_per_second = self.driver.find_element(By.ID, "cookiesPerSecond")
            #     print(f"Producing Cookies {cookies_per_second.text}")
            #
            # except StaleElementReferenceException:
            #     # Handle stale element error by retrying
            #     cookies_per_second = self.driver.find_element(By.ID, "cookiesPerSecond")
            #     print(f"Producing Cookies {cookies_per_second.text}")


# Initialize instance of cookie clicker bot
cookie_clicker_bot = CookieClicker()
time.sleep(5)   # Wait for page to load
cookie_clicker_bot.find_big_cookie()    # Call method to navigate to cookie game and perform set up
time.sleep(5)
cookie_clicker_bot.build_cookie_empire()    # Call method to start game
