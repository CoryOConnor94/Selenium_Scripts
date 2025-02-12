from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd

class AudibleScraper:

    def __init__(self, url='https://www.audible.co.uk/adblbestsellers?ref_pageloadid=KvV8e1j22JuFptQw&pf_rd_p=dca427de-0b1b-4161-9f47-9abd6b23bcb1&pf_rd_r=NWTVA4HZT861CWMW8XEN&plink=Oi6jfb0EcT0qlzmA&pageLoadId=qCROzhejGpO1oVoa&creativeId=209a9396-a0bd-443c-93ab-d608f0c4ed36&ref=a_newreleas_t1_navTop_pl0cg1c0r0'):
        """ Initialize driver, necessary options and lists to store scraped values"""
        self.options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = url
        self.current_page = 1
        self.book_titles = []
        self.book_authors = []
        self.book_lengths = []

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

    def accept_cookies(self):
        """Accepts cookies if popup appears"""
        try:
            cookies_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'truste-button3')]")))
            cookies_button.click()
        except NoSuchElementException:
            print('No cookies popup found, continuing...')

    def get_pagination(self):
        """Finds total number of pages"""
        try:
            pagination = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'pagingElements')]")))
            pages = pagination.find_elements(By.TAG_NAME, 'li')
            return int(pages[-2].text.strip())  # Second last item is the last page (last item is the next page button)
        except (NoSuchElementException, IndexError, ValueError):
            print('Pagination not found or unreadable, defaulting to 1 page')
            return 1

    def scrape_page(self):
        """Scrapes current pages titles, authors, and lengths"""
        try:
            book_container = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
            products = book_container.find_elements(By.XPATH, ".//li[contains(@class, 'productListItem')]")

            for product in products:
                self.book_titles.append(product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text)
                self.book_authors.append(product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text)
                self.book_lengths.append(product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text)
        except Exception as e:
            print('Error scraping page data:', e)

    def go_to_next_page(self):
        """Clicks next page button"""
        try:
            next_page_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'nextButton')]")))
            next_page_button.click()
            return True
        except NoSuchElementException:
            print('No more pages to navigate')
            return False

    def scrape_all_pages(self):
        """Loops through all pages to scraping book data"""
        self.start_driver()
        self.accept_cookies()
        total_pages = self.get_pagination()

        current_page = 1
        while current_page <= total_pages:
            print(f'Scraping page {current_page}/{total_pages}')
            self.scrape_page()
            if not self.go_to_next_page():
                break
            current_page += 1

    def save_to_csv(self, filename='audible_best_sellers.csv'):
        """Save scraped data to csv file"""
        book_df = pd.DataFrame({'Title': self.book_titles, 'Author': self.book_authors, 'Length': self.book_lengths})
        book_df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')

    def close_driver(self):
        """Closes the browser"""
        self.driver.quit()


def main():
    """Main flow of program"""
    audible_scraper = AudibleScraper()
    audible_scraper.scrape_all_pages()
    audible_scraper.save_to_csv()
    audible_scraper.close_driver()

if __name__ == '__main__':
    main()
