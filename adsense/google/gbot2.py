import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# Read proxies from the proxies.txt file
with open('proxies2.txt', 'r') as file:
    proxies = [line.strip() for line in file.readlines()]

# Google search query
query = "updatedmail kenya"
search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")

# Main loop to run the script multiple times
for i in range(100):  # Change this number to the desired number of iterations
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
    # options.add_argument("--headless")
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver
    
    try:
        # Perform the Google search
        driver.get(search_url)
        time.sleep(3)  # Wait for the search results to load

        # Find all the search result links
        search_results = driver.find_elements(By.CSS_SELECTOR, 'a')

        # Click on links containing "updatedmail.com"
        for link in search_results:
            href = link.get_attribute("href")
            if href and "updatedmail.co.ke" in href:
                driver.execute_script("arguments[0].click();", link)
                break  # Stop after clicking the first link
        else:
            print("No link containing 'updatedmail.com' found on the first page.")
            continue  # Move to the next iteration if no relevant link is found

        # Wait for the page to load
        time.sleep(3)

        # Open 10 URLs within the site
        for _ in range(10):
            # Find all the links within the site
            site_links = driver.find_elements(By.CSS_SELECTOR, 'a')
            # Filter out links with "updatedmail.com" in the href
            valid_links = [site_link.get_attribute("href") for site_link in site_links if site_link.get_attribute("href") and "updatedmail.co.ke" in site_link.get_attribute("href")]
            if not valid_links:
                print("No more valid links to open.")
                break  # No more valid links to open, break the loop
            # Randomly select a valid link and open it
            random_link = random.choice(valid_links)
            driver.execute_script(f"window.open('{random_link}', '_blank');")
            time.sleep(2)  # Wait for 2 seconds before opening the next URL

        # Random sleep time between 40 to 100 seconds
        random_sleep = random.randint(400, 500)
        time.sleep(random_sleep)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

    print(f"Iteration {i+1} completed.")

print("Script completed all iterations.")
