# Selenium Bot Automation Repository

## Overview
This repository contains multiple bot automation scripts for various platforms, including Cookie Clicking game, Instagram, Twitter, LinkedIn, and Cineworld. Each bot is designed to automate specific tasks using Selenium and other necessary tools.

## Bots Included

### Cookie Clicker Bot
**Description:**
This Python bot automates the Cookie Clicker game using Selenium. It continuously clicks the big cookie and purchases available upgrades to maximize cookies per second. The bot runs for a specified duration and attempts to optimize purchases based on available resources.

**Features:**
- Automatically clicks the big cookie.
- Purchases the most expensive available upgrade at set intervals.
- Handles initial game setup, including language selection and data consent.
- Dynamically increases the interval for checking upgrades.
- Implements exception handling for stale elements.

**Requirements:**
Ensure you have the following installed:

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically installed by `webdriver_manager`)

Install the required dependencies using:
```sh
pip install selenium webdriver-manager
```

**Usage:**
Run the script using:
```sh
python cookie_clicker_bot.py
```

**Configuration:**
Modify these constants in the script to change behavior:
```python
SECONDS_TO_WAIT = 25  # Time interval to check for upgrades
PLAY_TIME = 600 * 5   # Total playtime in seconds
```

**Troubleshooting:**
- **StaleElementReferenceException**: The script includes retry logic to handle this issue.
- **WebDriver Not Found**: Ensure Chrome is installed and up to date.
- **Game Not Loading**: Check if the Cookie Clicker website is accessible.

---

### Instagram Bot
**Description:**
This Python bot automates the process of following Instagram users using Selenium. It logs into an Instagram account, navigates to a target profile, and follows their followers. The bot is designed to streamline engagement and audience growth 

**Requirements:**
- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically installed by `webdriver_manager`)

Install the required dependencies using:
```sh
pip install selenium webdriver-manager
```

**Usage:**

Set up environment variables for security:
```sh
export USERNAME='your_instagram_username'
export PASSWORD='your_instagram_password'
```
Run script using:
``` sh
python instagram_follower_bot.py
```

**Configuration:**
Modify this constants to specify target instagram account
```python
TARGET_ACCOUNT = ""
```
---

### Twitter Bot
**Description:**
This Python bot automates internet speed testing and tweets complaints if the speed is below the promised rate. It uses Selenium to interact with Speedtest.net and Twitter.

**Features:**
- Tests internet speed using Speedtest.net.
- Logs into Twitter automatically.
- Tweets a complaint to the ISP if speeds are lower than expected
  
**Requirements:**
- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically installed by `webdriver_manager`)
  
**Usage:**
Set up environment variables for security:
```sh
export USERNAME='your_twitter_username'
export PASSWORD='your_twitter_password'
```
Run script using:
``` sh
python internet_speed_twitter_bot.py
``` 

**Configuration:**
Modify these constants to specify expected upload and download speeds
```python
PROMISED_UP_SPEED = ''
PROMISED_DOWN_SPEED = ''
```
---

### LinkedIn Bot
**Description:**
This Python bot automates job searches on LinkedIn using Selenium. It logs into a LinkedIn account, navigates to Python developer job listings, and saves available job postings for later review.

**Features:**
- Logs into a LinkedIn account automatically.
- Navigates to Python developer job listings.
- Scrolls through job postings and saves them.
- Handles login credentials securely.
  
**Requirements:**
- Python 3.x
- Google Chrome browser
- ChromeDriver (automatically installed by webdriver_manager)

Install the required dependencies using:
```sh
pip install selenium webdriver-manager
```

**Usage:**
Set up environment variables for security:
```sh
export USERNAME='your_linkedin_username'
export PASSWORD='your_linkedin_password'
```
Run script using:
```sh
python linkedin_job_applier.py
```

**Configuration:**
Modify URL to target specific job listings
```python
URL = ""
```

---

### Cineworld Scraping Bot
**Description:**
This Python bot scrapes movie listings and showtimes from Cineworld's website. It automates the retrieval of movie names and available screening times using Selenium

**Features:**
- Navigates to the Cineworld website.
- Retrieves movie titles and their available showtimes.
- Stores the collected data in a pandas DataFrame for easy access and manipulation.

**Requirements:**
- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically installed by webdriver_manager)
- Required Python libraries:
  Install dependencies using:
  ```sh
  pip install selenium webdriver-manager pandas
  ```
  
**Usage:**
```sh
python cineworld_scraper.py
```

**Configuration:**
Modify URL to target specific webpage
```python
url = ""
```

---

### Audible Scraping Bot
**Description:**
This Python bot  extracts best-selling audiobook data from Audible. It uses Selenium to automate the extraction of book titles, authors, and lengths, saving the data into a CSV file

**Features:**
- Navigates to the Audible website.
- Extracts title, author, and length of audiobooks.
- Handles pagination to scrape multiple pages.
- Saves data to csv file
- Includes error handling for missing elements

**Requirements:**
- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically installed by webdriver_manager)
- Required Python libraries:
  Install dependencies using:
  ```sh
  pip install selenium webdriver-manager pandas
  ```
  
**Usage:**
```sh
python audible_scraper.py
```

**Configuration:**
Modify URL to target specific page
```python
url = ""
```

---
## License
This project is open-source and available under the MIT License.

