import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = [
 
'67.213.212.38:61819',
'67.213.212.55:19946',
'108.181.133.59:10680',
'67.213.212.39:61454',
'162.210.197.69:28993',
'162.210.192.171:49982',
'108.181.132.116:39795',
'174.138.176.75:10660',
'37.221.193.221:13847',
'66.23.233.210:19618',
'67.213.210.61:38332',
'162.210.192.171:53946',
'162.210.197.69:53466',
'37.221.193.221:21443'




]

urls = [
'https://wiredwhirl.com/how-wide-is-55-inch-tv/',
'https://wiredwhirl.com/att-email-login-web-mobile-and-app-login-techniques/',
'https://wiredwhirl.com/netflix-login/',
'https://wiredwhirl.com/wells-fargo-routing-numbers/',
'https://wiredwhirl.com/how-much-does-uber-pay-an-in-depth-guide2024/',
'https://wiredwhirl.com/how-to-cancel-siriusxm-on-phone-and-online/',
'https://wiredwhirl.com/create-facebook-account/',
'https://wiredwhirl.com/california-drivers-license-renewal/',
'https://wiredwhirl.com/alabama-driver-license-renewal/'

]

# Initialize the Chrome driver
driver = webdriver.Chrome(options=Options())  # Using inbuilt Selenium ChromeDriver

try:
    for proxy in proxies:
        print(f'Using proxy: {proxy}')
        
        options = Options()
        options.add_argument('--new-window')
        options.add_argument('--proxy-server=%s' % proxy)
        
        driver.quit()  # Close the previous window before opening a new one
        driver = webdriver.Chrome(options=options)
        
        # Shuffle the URLs list and select the first 10
        random.shuffle(urls)
        selected_urls = urls[:10]
        
        for url in selected_urls:
            driver.execute_script("window.open('{}', '_blank');".format(url))
            print(f"Opened {url} with proxy {proxy}")
        
        # Randomize the time between 2 and 4 minutes
        time_to_sleep = random.uniform(180, 200)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f' closed wiredexpress.py')
finally:
    driver.quit()
