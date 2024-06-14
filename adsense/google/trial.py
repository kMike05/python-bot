import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = [
 
'37.221.193.221:16912',
'67.213.212.39:28927',
'162.210.197.69:35443',
'67.213.212.55:10514',
'162.210.197.69:53040',
'38.91.107.2:46382',
'66.29.129.54:28025',
'162.210.192.171:10453',
'174.138.176.77:47774',
'23.105.170.35:53646',
'162.210.197.69:53629',
'37.221.193.221:11498'



]

urls = [
'https://updatedmail.co.ke/2024/06/13/the-reality-of-fair-weather-relationships-a-cautionary-tale/',
'https://updatedmail.co.ke/2024/06/13/makeup-artist-shares-story-of-how-a-client-turned-her-into-a-chef/',
'https://updatedmail.co.ke/2024/06/13/american-woman-cries-out-after-nigerian-husband-disappears-two-months-after-arriving-in-the-u-s/',
'https://updatedmail.co.ke/2024/06/13/tiktoker-by-soundkraft-gody-tennor-tipsy-gee-and-kappy-hits-10-million-views-propelling-arbantone-into-the-global-spotlight/',
'https://updatedmail.co.ke/2024/06/12/son-of-u-s-president-hunter-biden-convicted-of-illegally-buying-a-gun-after-hiding-his-drug-use/',
'https://updatedmail.co.ke/2024/06/12/guinness-beverage-company-to-exit-nigerian-market/',
'https://updatedmail.co.ke/2024/06/12/south-african-man-suffers-trauma-after-hiv-misdiagnosis-and-arv-treatment/',
'https://updatedmail.co.ke/2024/06/12/woman-commits-suicide-after-confession-of-sleeping-with-dogs-resurfaces-online/',
'https://updatedmail.co.ke/2024/06/12/five-signs-the-person-youre-dating-is-perfect-for-you/',
'https://updatedmail.co.ke/2024/06/12/oprah-winfrey-hospitalized-for-stomach-issue-that-left-her-with-stuff-coming-out-of-both-ends-according-to-gamonthsyle-king-five-after-mogul-admitted-to-using-weight-loss-drugs/',
'https://updatedmail.co.ke/2024/06/12/new-rules-for-bringing-dogs-into-the-us-starting-in-august-see-list/',
'https://updatedmail.co.ke/2024/06/12/breaking-news-malawi-vice-president-saulos-chilima-and-nine-others-confirmed-dead-in-a-plane-crash/',
'https://updatedmail.co.ke/2024/06/11/you-came-here-to-distribute-oversized-plastic-shoes-to-our-kids-charlene-rutos-charity-work-under-fire-from-kitui-mps/',
'https://updatedmail.co.ke/2024/06/11/53-year-old-nigerian-woman-gives-birth-to-quadruplets-a-miracle-of-modern-medicine/',
'https://updatedmail.co.ke/2024/06/11/nigerian-lady-interrupts-wedding-convoy-accuses-groom-of-abandoning-her-after-3-children/',
'https://updatedmail.co.ke/2024/06/11/my-husband-impregnated-all-our-four-housemaids-and-because-of-that-i-wanted-to-walk-out-of-our-marriage-before-this-man-rescued-our-marriage-a-woman-narrates-how-dr-mugwenu-helped-her-husband-sto/'

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
        time_to_sleep = random.uniform(400, 500)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f'Proxy {proxy} used and stayed open for {time_to_sleep / 60} minutes closed trial py')
finally:
    driver.quit()
