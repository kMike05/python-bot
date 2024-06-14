import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = [
 
'192.185.176.196:58709',
'96.91.130.130:13555',
'64.20.153.79:14859',
'71.67.14.116:34822',
'204.232.98.8:57102',
'209.33.200.86:51506',
'199.119.159.243:49110',
'108.17.53.177:27092',
'67.55.177.7:29493',
'45.76.21.140:52029',
'72.52.178.71:49282',
'47.21.40.26:29090',
'68.69.235.128:29043',
'67.224.119.2:42077',
'162.193.208.227:52372',
'50.74.11.110:46508',
'94.72.113.108:64200',
'23.115.210.116:29086',
'65.123.5.135:13144',
'166.153.219.184:54230',
'192.185.81.186:13414',
'184.179.105.126:46061',
'192.81.112.86:64666',
'50.184.105.177:58055',
'108.17.53.178:14894',
'166.113.61.163:34858',
'24.120.113.134:37622',
'63.158.178.195:24474',
'38.141.1.60:61045',
'50.240.246.249:14900',
'99.47.129.212:30547',
'23.114.75.89:53489',
'199.19.112.162:30508',
'207.244.246.52:46692',
'8.30.102.195:48600',
'96.10.118.44:20921',
'216.51.234.62:13497',
'174.76.18.170:15227',
'172.105.154.191:28153',
'8.29.16.122:55169',
'64.237.80.122:58656',
'72.26.5.167:24728',
'64.20.129.11:17324',
'96.82.165.254:37099',
'24.112.77.67:15817',
'24.248.211.56:27960',
'166.169.125.207:53342',
'137.118.93.204:36990',
'72.19.38.218:16501',
'207.32.236.179:30118'

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
        time_to_sleep = random.uniform(500, 700)  # Random time between 2 and 4 minutes
        time.sleep(time_to_sleep)
        
        print(f'Proxy {proxy} used and stayed open for {time_to_sleep / 60} minutes')
finally:
    driver.quit()