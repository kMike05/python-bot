import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = ['67.213.210.118:44087']

urls = [
    'https://google.com'
]

options = Options()

# To open each URL in a different tab, set the following option:
options.add_argument("--new-window")

driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver

try:
    for proxy in proxies:
        options.add_argument('--proxy-server=%s' % proxy)
    
    for url in urls:
        driver.execute_script("window.open('{}', '_blank');".format(url))
        print(f"Opened {url}")

    time.sleep(2)  # Give some time for all tabs to load

    # Auto-scroll in each tab
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # Sleep for 1 second after scrolling

    # Sleep to keep the window open
    time.sleep(120)  # Stay in the window for 5 minutes (300 seconds)
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    driver.quit()