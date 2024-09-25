from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the WebDriver you downloaded (e.g., ChromeDriver)
driver_path = "chromedriver.exe"

# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# URL of the website you want to scrape
url = ""

# Open the URL
driver.get(url)

# Wait for the dynamic content to load (adjust wait time as necessary)
try:
    # Use WebDriverWait to wait until a specific element is present (e.g., h3.qb-movie-name)
    movie_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3.qb-movie-name"))
    )

    # Extract the movie names
    for movie in movie_elements:
        print(movie.text)

finally:
    # Close the browser
    driver.quit()
