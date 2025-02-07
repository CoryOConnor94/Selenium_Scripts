# Selenium Bot Automation Repository

## Overview
This repository contains multiple bot automation scripts for various platforms, including Cookie Clicker, Instagram, Twitter, and LinkedIn. Each bot is designed to automate specific tasks using Selenium and other necessary tools.

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

- Python 3.x
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

**Features:**

**Requirements:**

**Usage:**

**Configuration:**

**Troubleshooting:**

---

### Twitter Bot
**Description:**

**Features:**

**Requirements:**

**Usage:**

**Configuration:**

**Troubleshooting:**

---

### LinkedIn Bot
**Description:**

**Features:**

**Requirements:**

**Usage:**

**Configuration:**

**Troubleshooting:**

## License
This project is open-source and available under the MIT License.

