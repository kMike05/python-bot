import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker
import browser_cookie3
import socks
import socket
import os
import shutil
import tempfile
import psutil

# Ensure Chrome is closed
def close_chrome():
    for process in psutil.process_iter():
        if process.name() == "chrome.exe":
            process.kill()

# Generate cookies
def get_cookies_for_proxy(proxy_ip):
    try:
        close_chrome()  # Ensure Chrome is closed
        original_cookie_path = os.path.expanduser(
            r'~\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies'
        )
        temp_cookie_path = tempfile.NamedTemporaryFile(delete=False).name
        shutil.copyfile(original_cookie_path, temp_cookie_path)
        cj = browser_cookie3.chrome(cookie_file=temp_cookie_path)
        return cj
    except PermissionError as e:
        print(f"PermissionError: {e}")
        return None

proxy_ip = "your_proxy_ip"
cookies = get_cookies_for_proxy(proxy_ip)

# Configure SOCKS5 proxy
def set_socks_proxy(proxy_ip, proxy_port):
    socks.set_default_proxy(socks.SOCKS5, proxy_ip, int(proxy_port))
    socket.socket = socks.socksocket

# Read the list of proxies from the file
with open("proxies.txt", "r") as f:
    proxies = f.readlines()

proxies = [proxy.strip() for proxy in proxies]

# Configure Chrome options
chrome_options = Options()
fake = Faker()

# Define the path to chromedriver
chromedriver_path = 'chromedriver.exe'
service = Service(chromedriver_path)

# Define the search query and target URL
query = "kilimobiashara site:kilimobiashara.co.ke"
search_url = "https://www.google.com/search?q=" + query.replace("kilimobiashara", "+")

# Loop through each proxy in the list
for proxy in proxies:
    proxy_ip, proxy_port = proxy.split(":")
    
    # Set the SOCKS5 proxy
    set_socks_proxy(proxy_ip, proxy_port)
    
    # Check the validity of the proxy
    try:
        requests.get("https://www.google.com", timeout=3)
    except:
        print(f"Skipping proxy {proxy} (not working)")
        continue
    
    # Generate fake user agent and cookies
    user_agent = fake.user_agent()
    cookies = get_cookies_for_proxy(proxy_ip)
    
    chrome_options.add_argument(f'--proxy-server=socks5://{proxy_ip}:{proxy_port}')
    chrome_options.add_argument(f'user-agent={user_agent}')
    
    chrome = None
    try:
        chrome = webdriver.Chrome(service=service, options=chrome_options)
        
        # Open Google and perform the search
        chrome.get(search_url)
        
        time.sleep(3)
        
        # Add cookies to the browser
        if cookies:
            for cookie in cookies:
                chrome.add_cookie({
                    'name': cookie.name,
                    'value': cookie.value,
                    'domain': cookie.domain
                })
        
        # Refresh the page to apply cookies
        chrome.refresh()
        
        # Find the search results links with "kilimobiashara.co.ke" in the URL
        links = chrome.find_elements(By.CSS_SELECTOR, 'a[href*="kilimobiashara.co.ke"]')
        
        # Open each relevant link in a new tab
        for link in links:
            url = link.get_attribute("href")
            chrome.execute_script(f"window.open('{url}', '_blank')")
            time.sleep(6)
        
        # Scroll down the page to mimic normal behavior
        scroll_pause_time = 2
        last_height = chrome.execute_script("return document.body.scrollHeight")
        
        while True:
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = chrome.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Open all links on the page in new tabs
        page_links = chrome.find_elements(By.CSS_SELECTOR, 'a')
        for link in page_links:
            href = link.get_attribute("href")
            if href:
                chrome.execute_script(f"window.open('{href}', '_blank')")
                time.sleep(3)
    
    except Exception as e:
        print(f"Error with proxy {proxy}: {e}")
    
    finally:
        if chrome:
            chrome.quit()
