import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxies = [


'162.210.197.69:49879',
'162.0.220.216:34146',
'67.213.212.52:18671',
'23.105.170.32:49811',
'67.213.212.52:47728',
'67.213.212.47:63289',
'162.0.220.217:12587',
'67.213.212.54:58208',
'67.213.212.54:20962',
'23.105.170.35:37628',
'212.83.143.211:10417',
'108.181.132.117:37399',
'67.213.212.38:34700',
'67.213.212.38:32097',
'174.138.176.76:37103',
'67.213.210.118:39896',
'174.138.176.78:49968',
'66.29.128.243:54195',
'67.213.212.38:36037',
'67.213.212.57:33935',
'23.105.170.30:60482',
'37.221.193.221:17665'


]

urls = [
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/13/makeup-artist-shares-story-of-how-a-client-turned-her-into-a-chef/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/13/american-woman-cries-out-after-nigerian-husband-disappears-two-months-after-arriving-in-the-u-s/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/13/tiktoker-by-soundkraft-gody-tennor-tipsy-gee-and-kappy-hits-10-million-views-propelling-arbantone-into-the-global-spotlight/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/son-of-u-s-president-hunter-biden-convicted-of-illegally-buying-a-gun-after-hiding-his-drug-use/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/guinness-beverage-company-to-exit-nigerian-market/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/south-african-man-suffers-trauma-after-hiv-misdiagnosis-and-arv-treatment/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/woman-commits-suicide-after-confession-of-sleeping-with-dogs-resurfaces-online/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/five-signs-the-person-youre-dating-is-perfect-for-you/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/oprah-winfrey-hospitalized-for-stomach-issue-that-left-her-with-stuff-coming-out-of-both-ends-according-to-gamonthsyle-king-five-after-mogul-admitted-to-using-weight-loss-drugs/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/new-rules-for-bringing-dogs-into-the-us-starting-in-august-see-list/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/12/breaking-news-malawi-vice-president-saulos-chilima-and-nine-others-confirmed-dead-in-a-plane-crash/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/11/you-came-here-to-distribute-oversized-plastic-shoes-to-our-kids-charlene-rutos-charity-work-under-fire-from-kitui-mps/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/11/53-year-old-nigerian-woman-gives-birth-to-quadruplets-a-miracle-of-modern-medicine/',
'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/11/nigerian-lady-interrupts-wedding-convoy-accuses-groom-of-abandoning-her-after-3-children/',
    'https://www.google.com/search?q=https://updatedmail.co.ke/2024/06/11/my-husband-impregnated-all-our-four-housemaids-and-because-of-that-i-wanted-to-walk-out-of-our-marriage-before-this-man-rescued-our-marriage-a-woman-narrates-how-dr-mugwenu-helped-her-husband-sto/',

   
]

# Initialize the Chrome driver with options
def create_driver(proxy=None):
    options = Options()
    options.add_argument('--new-window')
    if proxy:
        options.add_argument('--proxy-server=%s' % proxy)
    return webdriver.Chrome(options=options)

def scroll_page(driver, scroll_duration=20):
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
                search_result = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.g a"))
                )
                first_result_url = search_result.get_attribute("href")
                driver.get(first_result_url)  # Open the extracted URL in the same tab
                print(f"Opened {first_result_url} in tab {tab_idx + 1} with proxy {proxy}")

                # Scroll the page for 30 seconds
                scroll_page(driver, scroll_duration=20)
                print(f"Scrolled {first_result_url} for 30 seconds in tab {tab_idx + 1} with proxy {proxy}")
                
            except Exception as e:
                print(f"Failed to open search result in tab {tab_idx + 1}: {e}")
        
        # Randomize the time between 2 and 4 minutes
        time_to_sleep = random.uniform(30, 50)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f'Proxy {proxy} used and stayed open for {time_to_sleep / 60} minutes closed wired.py')

finally:
    driver.quit()
