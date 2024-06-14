import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Read proxies from the proxies.txt file
with open('proxies.txt', 'r') as file:
    proxies = [line.strip() for line in file.readlines()]

# URLs to open
urls = [
    'https://google.com'
]

options = Options()
#options.add_argument("--headless")  # Optional: Run in headless mode

# Function to smooth scroll
def smooth_scroll(driver, scroll_pause_time=0.1, scroll_step=100):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for y in range(0, last_height, scroll_step):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(scroll_pause_time)
    driver.execute_script(f"window.scrollTo(0, {last_height});")

# Function to search Google and open results containing a specific term
def search_google_and_open_results(driver, search_term, keyword):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for search results to load

    links = driver.find_elements(By.XPATH, f"//a[contains(@href, '{keyword}')]")
    for link in links:
        href = link.get_attribute("href")
        driver.execute_script("window.open('{}', '_blank');".format(href))
        time.sleep(2)  # Give some time for the new tab to load

# Main loop to run the script multiple times
for i in range(10000):
    if not proxies:
        print("No more proxies available.")
        break

    # Randomly select and remove a proxy from the list
    proxy = random.choice(proxies)
    proxies.remove(proxy)
    options.add_argument('--proxy-server=%s' % proxy)
    
    driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver
    
    try:
        for url in urls:
            driver.get(url)
            print(f"Opened {url} with proxy {proxy}")

            # If Google is opened, perform the search
            if "google.com" in url:
                search_google_and_open_results(driver, "kilimobiashara.co.ke", "kilimobiashara.co.ke")

            time.sleep(2)  # Give some time for the page to load

            # Auto-scroll in the tab
            smooth_scroll(driver, scroll_pause_time=0.5, scroll_step=100)
            time.sleep(10)  # Sleep for 10 seconds after scrolling

        # Random sleep time between 2 to 5 minutes
        random_sleep = random.randint(120, 300)
        print(f"Sleeping for {random_sleep} seconds before the next iteration.")
        time.sleep(random_sleep)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

    print(f"Iteration {i+1} completed.")

print("Script completed all iterations.")
