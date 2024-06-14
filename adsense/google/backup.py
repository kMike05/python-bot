import undetected_chromedriver as uc
import time
import http.cookiejar as cookiejar
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# List of URLs to open
urls = [
    'https://kilimobiashara.co.ke/p/can-a-novel-alzheimer-s-biomarker-aid-in-diagnosing-the-disease-prior-to-the-manifestation-of-symptoms',
    'https://kilimobiashara.co.ke/p/ex-citi-banker-claims-she-was-fired-for-refusing-to-falsify-data-for-a-regulator',
    'https://kilimobiashara.co.ke/p/discoveries-shed-light-on-the-reasons-behind-age-related-decrease-in-mobility',
    'https://kilimobiashara.co.ke/p/explore-the-growing-trend-of-smaller-homes-and-shop-for-tiny-houses-online-to-see-their-prices',
    'https://kilimobiashara.co.ke/p/greek-shipping-experiences-a-decline-in-bank-lending-alongside-a-rise-in-sale-and-leaseback-transactions',
    'https://kilimobiashara.co.ke/p/red-lobster-s-bankruptcy-troubles-beyond-endless-shrimp'
]

# List of proxies
proxies = [
  '66.29.128.245:27751',
'37.221.193.221:18782',
'37.221.193.221:34649',
'37.221.193.221:13221',
'67.213.212.55:27580',
'108.181.132.115:43872',
'67.213.212.54:12305',
'209.159.153.20:43874'
]

# Path to save/load cookies
cookie_file = 'cookies.txt'

def save_cookies(driver, filename):
    with open(filename, 'w') as file:
        for cookie in driver.get_cookies():
            file.write(f"{cookie['name']}={cookie['value']}; ")

def load_cookies(driver, filename):
    with open(filename, 'r') as file:
        cookies = file.read().strip().split('; ')
        for cookie in cookies:
            name, value = cookie.split('=')
            driver.add_cookie({'name': name, 'value': value, 'path': '/', 'domain': '.kilimobiashara.co.ke'})

def create_driver(proxy):
    # Initialize the undetected Chrome WebDriver with proxy settings
    options = uc.ChromeOptions()
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument(f'--proxy-server=http://{proxy}')  # Set the proxy server

    # Create the WebDriver instance with the given options
    driver = uc.Chrome(options=options)
    return driver

# Save cookies using one proxy to ensure they are loaded later
driver = create_driver(proxies[0])
driver.get(urls[0])
time.sleep(5)  # Wait for the page to load and cookies to be set
save_cookies(driver, cookie_file)
driver.quit()

# Open all URLs in a single window for each proxy
for proxy in proxies:
    print(f"Using proxy: {proxy}")
    driver = create_driver(proxy)
    
    # Open the first URL in the main window
    driver.get(urls[0])
    time.sleep(5)  # Wait for the page to load

    # Load cookies
    load_cookies(driver, cookie_file)

    # Open all URLs in new tabs
    for url in urls[1:]:
        driver.execute_script(f"window.open('{url}', '_blank');")

    # Wait for 120 seconds before closing the browser
    print(f"Waiting for 120 seconds. You can interact with the browser during this time.")
    time.sleep(240)
    driver.quit()
    print(f"Closed browser for proxy: {proxy}")
