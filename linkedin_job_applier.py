import os
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class LinkedInBot:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def linkedin_login(self):
        """Logs into LinkedIn account"""
        self.driver.get("https://www.linkedin.com/jobs/search/?=true&keywords=python%20developer&refresh=true")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        log_in = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")))
        log_in.click()
        username_form = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_form.send_keys(USERNAME)
        password_form = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_form.send_keys(PASSWORD)
        self.driver.implicitly_wait(10)
        password_form.send_keys(Keys.ENTER)

    def save_jobs(self):
        """Locates save job button and scrolls down page saving each job"""
        self.driver.implicitly_wait(10)
        save_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-save-button")))
        on = True
        while on:
            scroll_object = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.disabled')))
            scroll_object.send_keys(Keys.TAB)
            scroll_object.send_keys(Keys.END)
            self.driver.implicitly_wait(10)

            all_listings = self.driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list .disabled")
            for listing in all_listings:
                try:
                    self.driver.implicitly_wait(10)
                    save_button.click()
                    # driver.implicitly_wait(10)
                    scroll_object = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.disabled')))
                    scroll_object.send_keys(Keys.TAB)
                    scroll_object.send_keys(Keys.END)
                    # driver.implicitly_wait(10)

                except StaleElementReferenceException:
                    print("Not Found. Skipped")
            on = False


bot = LinkedInBot()
bot.linkedin_login()
bot.save_jobs()

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# driver.get("https://www.linkedin.com/jobs/search/?=true&keywords=python%20developer&refresh=true")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
# log_in = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")))
# log_in.click()
# username_form = wait.until(EC.presence_of_element_located((By.ID, "username")))
# username_form.send_keys(USERNAME)
# password_form = wait.until(EC.presence_of_element_located((By.ID, "password")))
# password_form.send_keys(PASSWORD)
# driver.implicitly_wait(10)
# password_form.send_keys(Keys.ENTER)
#
# save_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-save-button")))
# on = True
# while on:
#     scroll_object = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.disabled')))
#     scroll_object.send_keys(Keys.TAB)
#     scroll_object.send_keys(Keys.END)
#     driver.implicitly_wait(10)
#
#     all_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list .disabled")
#     for listing in all_listings:
#         try:
#             driver.implicitly_wait(10)
#             save_button.click()
#             #driver.implicitly_wait(10)
#             scroll_object = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.disabled')))
#             scroll_object.send_keys(Keys.TAB)
#             scroll_object.send_keys(Keys.END)
#             #driver.implicitly_wait(10)
#
#         except StaleElementReferenceException:
#             print("Not Found. Skipped")
#     on = False
