from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd


class CineworldBot:

    def __init__(self, url="https://www.cineworld.ie"):
        """ Initialize driver, necessary options and lists to store scraped values"""
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        # Initialize lists to store movie names and times
        self.movie_names = []
        self.movie_times = []
        self.url = url

    def accept_cookies(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # Accept cookies
        cookies_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'onetrust-accept')]")))
        cookies_button.click()

    def go_to_whats_on(self):
        # Go to What's on page
        whats_on = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@id, 'menu-item-whatson')]")))
        whats_on.click()

    def get_movies(self):
        """ Retrieves movie names and what's on today and upcoming movie dates"""
        # Wait for movie containers to load (assuming each movie is inside a container like a div)
        movie_containers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row.qb-movie"))
            # Update this selector based on the actual container
        )

        # Loop through each movie container
        for container in movie_containers:
            # Extract the movie name from the container
            movie_name = container.find_element(By.CSS_SELECTOR, "h3.qb-movie-name").text
            self.movie_names.append(movie_name)
            # Extract all movie times within the same container
            time_elements = container.find_elements(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")
            movie_time = [time.text for time in time_elements]  # Get the text for each time
            self.movie_times.append(movie_time)

        # Convert to Dataframe
        film_df = pd.DataFrame({'Film': self.movie_names, 'Film Time': self.movie_times})
        print(film_df)
        self.driver.quit()


cineworld_bot = CineworldBot()
cineworld_bot.accept_cookies()
cineworld_bot.go_to_whats_on()
cineworld_bot.get_movies()
