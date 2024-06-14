import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxies = [

'38.91.107.2:23011',
'108.181.132.118:47512',
'162.210.197.69:30988',
'162.210.192.171:35332',
'162.210.192.171:61850',
'174.138.176.77:17845',
'67.213.212.48:39346',
'23.105.170.33:61237',
'162.210.192.171:39286',
'108.181.133.59:60631',
'174.138.176.78:34892',
'162.210.197.69:31369',
'212.83.137.30:24344',
'67.213.212.40:64575',
'141.94.238.246:49389',
'162.210.192.171:60496',
'162.210.192.171:38255',
'174.138.176.75:34485',
'108.181.132.117:52855'


]

urls = [
    'https://www.google.com/search?q=https://wiredwhirl.com/alaskas-license-renewal-process/',
    'https://www.google.com/search?q=https://wiredwhirl.com/florida-drivers-license-renewal/',
    'https://www.google.com/search?q=https://wiredwhirl.com/connecticut-driver-license-renewal/',
    'https://www.google.com/search?q=https://wiredwhirl.com/weight-of-gasoline/',
    'https://www.google.com/search?q=https://wiredwhirl.com/colorado-driver-license-renewal/',
    'https://www.google.com/search?q=https://wiredwhirl.com/td-bank-routing-numbers/',
    'https://www.google.com/search?q=https://wiredwhirl.com/delaware-drivers-license-renewal/',
    'https://www.google.com/search?q=https://wiredwhirl.com/alabama-driver-license-renewal/'
]

# Initialize the Chrome driver with options
def create_driver(proxy=None):
    options = Options()
    options.add_argument('--new-window')
    if proxy:
        options.add_argument('--proxy-server=%s' % proxy)
    return webdriver.Chrome(options=options)

def scroll_page(driver, scroll_duration=30):
    end_time = time.time() + scroll_duration
    while time.time() < end_time:
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)  # Sleep for a second before scrolling again

try:
    for proxy in proxies:
        print(f'Using proxy: {proxy}')
        
        driver = create_driver(proxy)
        
        # Open each URL in its own tab simultaneously
        for url in urls:
            driver.execute_script("window.open('{}', '_blank');".format(url))
            print(f"Opened {url} with proxy {proxy}")
        
        # Switch to each tab and perform operations
        for tab_idx in range(len(urls)):
            driver.switch_to.window(driver.window_handles[tab_idx])
            
            try:
                # Wait until the search results are loaded
                search_result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.g a"))
                )
                first_result_url = search_result.get_attribute("href")
                driver.get(first_result_url)  # Open the extracted URL in the same tab
                print(f"Opened {first_result_url} in tab {tab_idx + 1} with proxy {proxy}")

                # Scroll the page for 30 seconds
                scroll_page(driver, scroll_duration=30)
                print(f"Scrolled {first_result_url} for 30 seconds in tab {tab_idx + 1} with proxy {proxy}")
                
            except Exception as e:
                print(f"Failed to open search result in tab {tab_idx + 1}: {e}")
        
        # Randomize the time between 2 and 4 minutes
        time_to_sleep = random.uniform(30, 50)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f'Proxy {proxy} used and stayed open for {time_to_sleep / 60} minutes')

finally:
    driver.quit()
