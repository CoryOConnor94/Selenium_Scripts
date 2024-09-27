from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

now = datetime.now()
formatted_date = f"{now.year}-{now.month}-{now.day}"

# Path to the WebDriver you downloaded (e.g., ChromeDriver)
driver_path = "chromedriver.exe"

# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# URL of the website you want to scrape
url = f"https://www.cineworld.ie/#/buy-tickets-by-cinema?in-cinema=0001&at={formatted_date}&view-mode=list"

# Open the URL
driver.get(url)

# Wait for the dynamic content to load
try:
    # Wait for movie containers to load (assuming each movie is inside a container like a div)
    movie_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row.qb-movie"))
        # Update this selector based on the actual container
    )

    # Initialize dictionary to store movie names and times
    movies_with_times = {}

    # Loop through each movie container
    for container in movie_containers:
        # Extract the movie name from the container
        movie_name = container.find_element(By.CSS_SELECTOR, "h3.qb-movie-name").text

        # Extract all movie times within the same container
        time_elements = container.find_elements(By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")
        movie_times = [time.text for time in time_elements]  # Get the text for each time

        # Store movie name and its list of times in the dictionary
        movies_with_times[movie_name] = movie_times

    # Print the result
    print(movies_with_times)

finally:
    # Close the browser
    driver.quit()
