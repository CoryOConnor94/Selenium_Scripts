from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime

class CineworldScraper:

    def __init__(self, url="https://www.cineworld.ie"):
        """ Initialize driver, necessary options and lists to store scraped values"""
        self.options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.movie_names = []
        self.movie_times = []
        self.url = url
        self.today = datetime.today().strftime('%Y-%m-%d')

    def set_chrome_options(self):
        """Set chrome options for Selenium"""
        self.options.add_argument("disable-infobars")
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-dev-shm-usage")
        self.options.add_argument("no-sandbox")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-blink-features=AutomationControlled")

    def start_driver(self):
        """Start webdriver"""
        self.set_chrome_options()
        self.driver.get(self.url)
        self.accept_cookies()

    def accept_cookies(self):
        """Accept cookies if popup appears"""
        try:
            cookies_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'onetrust-accept')]")))
            cookies_button.click()
        except NoSuchElementException:
            print('No cookies popup found, continuing...')

    def go_to_whats_on(self):
        """Navigates to what's on page"""
        whats_on = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@id, 'menu-item-whatson')]")))
        whats_on.click()

    def get_movies(self):
        """ Retrieves movie names and what's on today and upcoming movie dates"""
        # Wait for movie containers to load
        movie_containers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row.qb-movie")))
        # Loop through each movie container
        for container in movie_containers:
            # Extract the movie name from the container
            movie_name = container.find_element(By.CSS_SELECTOR, "h3.qb-movie-name").text
            self.movie_names.append(movie_name)
            # Extract all movie times within the same container
            time_elements = container.find_elements(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")
            movie_time = [time.text for time in time_elements]  # Get the text for each time
            self.movie_times.append(movie_time)

    def save_to_csv(self):
        """Saves scraped data to csv file"""
        film_df = pd.DataFrame({'Film': self.movie_names, 'Film Time': self.movie_times})
        film_df.to_csv(f'cineworld_listings_{self.today}', index=False)
        self.close_driver()

    def close_driver(self):
        """Closes the browser"""
        self.driver.quit()


def main():
    """Main flow of program"""
    cineworld_scraper = CineworldScraper()
    cineworld_scraper.start_driver()
    cineworld_scraper.go_to_whats_on()
    cineworld_scraper.get_movies()
    cineworld_scraper.save_to_csv()

if __name__=='__main__':
    main()
