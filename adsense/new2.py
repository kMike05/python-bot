import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = [
 '66.29.129.56:48642','67.213.210.118:59008','38.91.107.229:47167','23.105.170.35:62049','66.29.128.244:64940','67.213.212.38:52044','66.29.128.245:28045','66.29.128.245:31314','67.213.210.175:20018','67.213.212.50:28041','46.105.44.29:20181','162.0.220.220:20118','212.83.143.211:22618','212.83.143.223:46453','162.210.197.69:39772','162.210.192.171:23380','67.213.212.36:55751','174.138.176.74:11616','209.159.153.19:32037','174.138.176.74:36820','38.91.107.229:28002','162.0.220.218:61382','212.83.143.223:42119','23.105.170.33:61298','67.213.210.61:28335','67.213.212.56:63323','66.29.128.246:47382','212.83.143.223:15664','23.105.170.30:28123','162.0.220.215:15020','66.29.128.243:31734','67.213.212.57:28249','162.19.7.61:43119','66.23.233.210:38163','67.213.212.51:11840','66.29.129.53:46684'

]

urls = [
   'https://kilimobiashara.co.ke/p/can-a-novel-alzheimer-s-biomarker-aid-in-diagnosing-the-disease-prior-to-the-manifestation-of-symptoms',
    'https://kilimobiashara.co.ke/p/ex-citi-banker-claims-she-was-fired-for-refusing-to-falsify-data-for-a-regulator',
    'https://kilimobiashara.co.ke/p/discoveries-shed-light-on-the-reasons-behind-age-related-decrease-in-mobility',
    'https://kilimobiashara.co.ke/p/explore-the-growing-trend-of-smaller-homes-and-shop-for-tiny-houses-online-to-see-their-prices',
    'https://kilimobiashara.co.ke/p/greek-shipping-experiences-a-decline-in-bank-lending-alongside-a-rise-in-sale-and-leaseback-transactions',
    'https://kilimobiashara.co.ke/p/red-lobster-s-bankruptcy-troubles-beyond-endless-shrimp',
    'https://kilimobiashara.co.ke/p/i-invested-my-house-deposit-in-preserving-my-fertility-through-egg-freezing',
    'https://kilimobiashara.co.ke/p/fincantieri-inaugurates-new-saudi-subsidiary-to-expand-its-presence-and-operations-in-the-region',
    'https://kilimobiashara.co.ke/p/pandemic-worsens-depression-more-in-teen-boys-than-girls',
    'https://kilimobiashara.co.ke/p/a-danish-court-has-dismissed-a-claim-that-a-patient-s-rights-were-violated-by-not-being-provided-with-vegan-food',
    'https://kilimobiashara.co.ke/p/neuroscience-suggests-that-just-6-to-10-minutes-a-day-of-specific-activities-can-enhance-intelligence-boost-focus-and-even-increase-brain-size',
    'https://kilimobiashara.co.ke/p/the-united-states-plans-to-take-legal-action-against-live-nation-the-parent-company-of-ticketmaster',
    'https://kilimobiashara.co.ke/p/rejuvenating-mitochondria-may-help-combat-toxic-proteins-in-alzheimer-s-disease',
    'https://kilimobiashara.co.ke/p/here-s-the-lowdown-on-the-post-office-scandal-understanding-the-horizon-debacle',
    'https://kilimobiashara.co.ke/p/an-actress-from-after-life-shares-how-creating-music-has-served-as-a-source-of-healing-for-her',
    'https://kilimobiashara.co.ke/p/zhejiang-seaport-and-evergreen-are-collaborating-on-eco-friendly-refueling-initiatives',
    'https://kilimobiashara.co.ke/p/mortgage-rates-have-fallen-for-the-third-consecutive-week-dropping-below-7',
    'https://kilimobiashara.co.ke/p/several-major-european-ports-are-collaborating-on-a-project-aimed-at-enhancing-climate-resilience-in-their-infrastructure',
    'https://kilimobiashara.co.ke/p/a-former-us-marine-pilot-arrested-in-australia-allegedly-collaborated-with-a-chinese-hacker-according-to-his-lawyer',
    'https://kilimobiashara.co.ke/p/doctors-oppose-proposed-public-masking-ban',
    'https://kilimobiashara.co.ke/p/trump-media-s-320-million-net-loss-caused-a-13-decrease-in-share-prices',
    'https://kilimobiashara.co.ke/p/a-former-dp-world-executive-has-been-appointed-to-lead-ssa-marine-s-container-terminal-business',
    'https://kilimobiashara.co.ke/p/trump-media-valued-at-7-billion-had-sales-of-less-than-1-million-in-q1',
    'https://kilimobiashara.co.ke/p/reduced-resilience-in-young-people-linked-to-increased-psoriasis-risk-later',
    'https://kilimobiashara.co.ke/p/researchers-have-decoded-how-immune-cells-recognize-cancer-s-accelerated-metabolism',
    'https://kilimobiashara.co.ke/p/does-olive-oil-consumption-correlate-with-reduced-risk-of-death-related-to-dementia',
    'https://kilimobiashara.co.ke/p/the-shipping-industry-is-apprehensive-about-the-burdensome-implications-of-new-cybersecurity-regulations-introduced-by-the-united-states',
    'https://kilimobiashara.co.ke/p/what-do-assisted-dying-assisted-suicide-and-euthanasia-mean-and-what-are-the-legal-implications',
    'https://kilimobiashara.co.ke/p/china-accuses-the-us-of-weaponizing-trade-through-the-imposition-of-new-tariffs',
    'https://kilimobiashara.co.ke/p/usa-and-world-inflation',
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
        time_to_sleep = random.uniform(120, 240)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f'Proxy {proxy} used and stayed open for {time_to_sleep / 60} minutes')
finally:
    driver.quit()