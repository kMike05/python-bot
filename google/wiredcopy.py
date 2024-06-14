import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxies = [


'67.213.210.175:10323',
'67.213.212.39:64518',
'212.83.137.30:46596',
'212.83.143.204:18755',
'38.91.107.2:38192',
'162.210.192.171:62565',
'162.210.192.171:40160',
'23.105.170.33:50873',
'209.159.153.20:23998',
'66.29.128.242:22280',
'174.138.176.75:22322',
'162.210.197.69:14582',
'209.159.153.21:33150',
'23.105.170.33:54661',
'23.105.170.34:60279',
'162.210.197.69:25024',
'162.210.192.171:29681'



]

urls = [
    'https://www.google.com/search?q=https://wiredwhirl.com/alaskas-license-renewal-process/',
    'https://www.google.com/search?q=https://wiredwhirl.com/florida-drivers-license-renewal/',
    'https://www.google.com/search?q=https://wiredwhirl.com/connecticut-driver-license-renewal/',
'https://www.google.com/search?q=https://wiredwhirl.com/att-email-login-web-mobile-and-app-login-techniques/',
'https://www.google.com/search?q=https://wiredwhirl.com/netflix-login/',
'https://www.google.com/search?q=https://wiredwhirl.com/wells-fargo-routing-numbers/',
'https://www.google.com/search?q=https://wiredwhirl.com/how-much-does-uber-pay-an-in-depth-guide2024/',
'https://www.google.com/search?q=https://wiredwhirl.com/how-to-cancel-siriusxm-on-phone-and-online/',
'https://www.google.com/search?q=https://wiredwhirl.com/create-facebook-account/',
'https://www.google.com/search?q=https://wiredwhirl.com/california-drivers-license-renewal/',
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
