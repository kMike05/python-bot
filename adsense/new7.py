import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Read proxies from the proxies.txt file
with open('proxies.txt', 'r') as file:
    proxies = [line.strip() for line in file.readlines()]

# URLs to open
urls = [
    "https://kilimobiashara.co.ke/p/can-a-novel-alzheimer-s-biomarker-aid-in-diagnosing-the-disease-prior-to-the-manifestation-of-symptoms",
"https://kilimobiashara.co.ke/p/ex-citi-banker-claims-she-was-fired-for-refusing-to-falsify-data-for-a-regulator",
"https://kilimobiashara.co.ke/p/discoveries-shed-light-on-the-reasons-behind-age-related-decrease-in-mobility",
"https://kilimobiashara.co.ke/p/explore-the-growing-trend-of-smaller-homes-and-shop-for-tiny-houses-online-to-see-their-prices",
"https://kilimobiashara.co.ke/p/greek-shipping-experiences-a-decline-in-bank-lending-alongside-a-rise-in-sale-and-leaseback-transactions",
"https://kilimobiashara.co.ke/p/red-lobster-s-bankruptcy-troubles-beyond-endless-shrimp",
"https://kilimobiashara.co.ke/p/i-invested-my-house-deposit-in-preserving-my-fertility-through-egg-freezing",
"https://kilimobiashara.co.ke/p/fincantieri-inaugurates-new-saudi-subsidiary-to-expand-its-presence-and-operations-in-the-region",
"https://kilimobiashara.co.ke/p/pandemic-worsens-depression-more-in-teen-boys-than-girls",
"https://kilimobiashara.co.ke/p/a-danish-court-has-dismissed-a-claim-that-a-patient-s-rights-were-violated-by-not-being-provided-with-vegan-food",
"https://kilimobiashara.co.ke/p/neuroscience-suggests-that-just-6-to-10-minutes-a-day-of-specific-activities-can-enhance-intelligence-boost-focus-and-even-increase-brain-size",
"https://kilimobiashara.co.ke/p/the-united-states-plans-to-take-legal-action-against-live-nation-the-parent-company-of-ticketmaster",
"https://kilimobiashara.co.ke/p/rejuvenating-mitochondria-may-help-combat-toxic-proteins-in-alzheimer-s-disease",
"https://kilimobiashara.co.ke/p/here-s-the-lowdown-on-the-post-office-scandal-understanding-the-horizon-debacle",
"https://kilimobiashara.co.ke/p/an-actress-from-after-life-shares-how-creating-music-has-served-as-a-source-of-healing-for-her",
"https://kilimobiashara.co.ke/p/zhejiang-seaport-and-evergreen-are-collaborating-on-eco-friendly-refueling-initiatives",
"https://kilimobiashara.co.ke/p/mortgage-rates-have-fallen-for-the-third-consecutive-week-dropping-below-7",
"https://kilimobiashara.co.ke/p/several-major-european-ports-are-collaborating-on-a-project-aimed-at-enhancing-climate-resilience-in-their-infrastructure",
"https://kilimobiashara.co.ke/p/a-former-us-marine-pilot-arrested-in-australia-allegedly-collaborated-with-a-chinese-hacker-according-to-his-lawyer",
"https://kilimobiashara.co.ke/p/doctors-oppose-proposed-public-masking-ban",
"https://kilimobiashara.co.ke/p/trump-media-s-320-million-net-loss-caused-a-13-decrease-in-share-prices",
"https://kilimobiashara.co.ke/p/a-former-dp-world-executive-has-been-appointed-to-lead-ssa-marine-s-container-terminal-business",
"https://kilimobiashara.co.ke/p/trump-media-valued-at-7-billion-had-sales-of-less-than-1-million-in-q1",
"https://kilimobiashara.co.ke/p/reduced-resilience-in-young-people-linked-to-increased-psoriasis-risk-later",
"https://kilimobiashara.co.ke/p/researchers-have-decoded-how-immune-cells-recognize-cancer-s-accelerated-metabolism",
"https://kilimobiashara.co.ke/p/does-olive-oil-consumption-correlate-with-reduced-risk-of-death-related-to-dementia",
"https://kilimobiashara.co.ke/p/the-shipping-industry-is-apprehensive-about-the-burdensome-implications-of-new-cybersecurity-regulations-introduced-by-the-united-states",
"https://kilimobiashara.co.ke/p/what-do-assisted-dying-assisted-suicide-and-euthanasia-mean-and-what-are-the-legal-implications",
"https://kilimobiashara.co.ke/p/china-accuses-the-us-of-weaponizing-trade-through-the-imposition-of-new-tariffs",
"https://kilimobiashara.co.ke/p/usa-and-world-inflation",
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

# Main loop to run the script multiple times
for i in range(10000):
    if not proxies:
        print("No more proxies available.")
        break

    # Randomly select and remove a proxy from the list
    proxy = random.choice(proxies)
    proxies.remove(proxy)

    # Print the proxy being used
    print(f"Using proxy: {proxy}")

    # Generate a random user agent
    user_agent = UserAgent().random

    # Set the proxy and user agent options for the browser
    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver

    try:
        # Randomly shuffle the URLs and select a random number between 8 and 10
        random.shuffle(urls)
        num_urls_to_open = random.randint(8, 12)
        selected_urls = urls[:num_urls_to_open]

        # Open the selected URLs in separate tabs
        for url in selected_urls:
            driver.execute_script("window.open('{}', '_blank');".format(url))
            time.sleep(2)  # Wait for 2 seconds before opening the next URL

        # Get all the tabs
        tabs = driver.window_handles

        for tab in tabs:
            driver.switch_to.window(tab)

            # Gradually scroll to the bottom of the page
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollBy(0, 200);")
                time.sleep(1)  # Wait for 1 second before scrolling again
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

        # Random sleep time between 2 to 5 minutes
        random_sleep = random.randint(120, 200)
        time.sleep(random_sleep)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

    print(f"Iteration {i+1} completed.")

print("Script completed all iterations.")
