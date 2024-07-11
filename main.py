from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Load credentials
with open('credentials.txt', 'r') as file:
    email, password = [line.strip() for line in file.readlines()]

# Load keywords
with open('keywords.txt', 'r') as file:
    keywords = file.read().splitlines()

# Load ChromeDriver path
with open('chromedriverpath.txt', 'r') as file:
    chromedriver_path = file.readline().strip()

# Setup Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the WebDriver using the ChromeDriver path from the text file
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

def login_youtube(email, password):
    driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube')
    time.sleep(2)
    driver.find_element(By.NAME, 'identifier').send_keys(email)
    driver.find_element(By.NAME, 'identifier').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

def report_comment(comment_element):
    try:
        # Click on the options menu of the comment
        comment_element.find_element(By.CSS_SELECTOR, "div[aria-label='More actions']").click()
        time.sleep(1)
        # Click the 'Report' option
        driver.find_element(By.XPATH, "//yt-formatted-string[text()='Report']").click()
        time.sleep(1)
        # Select 'Unwanted commercial content or spam'
        driver.find_element(By.XPATH, "//yt-formatted-string[text()='Unwanted commercial content or spam']").click()
        time.sleep(1)
        # Confirm report
        driver.find_element(By.CSS_SELECTOR, "div[aria-label='Report']").click()
        time.sleep(1)
    except Exception as e:
        print(f"Error reporting comment: {e}")

def check_and_report_comments(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        comments = driver.find_elements(By.ID, 'content-text')
        for comment in comments:
            if any(keyword in comment.text.lower() for keyword in keywords):
                report_comment(comment)
                time.sleep(2)  # Give it a short break after reporting

        # Scroll down to load more comments
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(5)  # Wait for more comments to load
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break  # Break the loop if no more comments are loaded
        last_height = new_height

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    login_youtube(email, password)
    check_and_report_comments(video_url)

    driver.quit()
