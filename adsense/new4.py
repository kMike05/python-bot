import time
import random
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

# Read proxies from the proxies.txt file
with open('proxies_new4.txt', 'r') as file:
    proxies = [line.strip() for line in file.readlines()]

# URLs to open
urls = [
    "https://kilimobiashara.co.ke/p/significant-strides-have-been-achieved-in-member-state-discussions-regarding-revisions-to-the-international-health-regulations-ihr",
    "https://kilimobiashara.co.ke/p/early-diagnosis-and-treatment-of-asthma-and-copd-can-greatly-enhance-quality-of-life",
    "https://kilimobiashara.co.ke/p/amidst-red-sea-disruptions-container-lines-rake-in-a-5-4-billion-profit",
    "https://kilimobiashara.co.ke/p/research-reveals-that-over-20-of-canadians-face-challenges-in-accessing-primary-healthcare-services",
    "https://kilimobiashara.co.ke/p/norway-s-telenor-group-appoints-new-ceo",
    "https://kilimobiashara.co.ke/p/ohio-lawmakers-are-being-urged-to-include-biden-on-the-november-ballot",
    "https://kilimobiashara.co.ke/p/the-inflation-rate-drops-to-its-lowest-level-in-nearly-three-years",
    "https://kilimobiashara.co.ke/p/high-costs-and-side-effects-are-causing-many-people-to-stop-using-new-weight-loss-medications",
    "https://kilimobiashara.co.ke/p/still-undecided-about-college-apply-for-scholarships-or-even-to-schools-now",
    "https://kilimobiashara.co.ke/p/revealing-the-full-extent-of-potential-overcapacity-in-container-shipping",
    "https://kilimobiashara.co.ke/p/shipping-stakeholders-express-apprehension-regarding-stringent-new-cyber-security-regulations-imposed-by-the-us",
    "https://kilimobiashara.co.ke/p/the-uk-s-asylum-process-significantly-impacts-the-health-and-wellbeing-of-asylum-seekers",
    "https://kilimobiashara.co.ke/p/educating-barbers-to-recognize-mental-health-concerns",
    "https://kilimobiashara.co.ke/p/houthi-style-grey-zone-warfare-unnerves-the-global-business-community",
    "https://kilimobiashara.co.ke/p/learn-about-the-various-types-of-breast-cancer",
    "https://kilimobiashara.co.ke/p/the-ntsb-determined-that-a-defective-propeller-blade-led-to-the-power-loss-of-the-boxship",
    "https://kilimobiashara.co.ke/p/many-older-americans-often-fail-to-prepare-for-long-term-care-including-considerations-for-costs-location-and-the-emotional-impact",
    "https://kilimobiashara.co.ke/p/stroke-rates-are-increasing-particularly-among-young-people",
    "https://kilimobiashara.co.ke/p/bank-of-america-bullish-on-rupee-despite-election-volatility",
    "https://kilimobiashara.co.ke/p/oil-prices-decline-for-the-fourth-consecutive-session-due-to-concerns-over-us-inflation",
]

# Function to load cookies
def load_cookies(driver, cookies_file):
    try:
        with open(cookies_file, 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
    except FileNotFoundError:
        pass

# Function to save cookies
def save_cookies(driver, cookies_file):
    cookies = driver.get_cookies()
    with open(cookies_file, 'wb') as file:
        pickle.dump(cookies, file)

# Main loop to run the script multiple times
for i in range(10000):
    if not proxies:
        print("No more proxies available.")
        break

    # Randomly select and remove a proxy from the list
    proxy = random.choice(proxies)
    proxies.remove(proxy)

    # Generate a random user agent
    user_agent = UserAgent().random

    # Set the proxy and user agent options for the browser
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver

    try:
        # Load cookies for maintaining browsing history
        driver.get("https://kilimobiashara.co.ke")
        load_cookies(driver, 'cookies.pkl')
        driver.refresh()

        # Open the first 10 URLs in separate tabs
        for url in urls[:10]:
            driver.execute_script("window.open('{}', '_blank');".format(url))
            time.sleep(2)  # Wait for 2 seconds before opening the next URL

        # Save cookies after visiting the pages
        save_cookies(driver, 'cookies.pkl')

        # Random sleep time between 2 to 5 minutes
        random_sleep = random.randint(200, 400)
        time.sleep(random_sleep)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

    print(f"Iteration {i+1} completed.")

print("Script completed all iterations.")
