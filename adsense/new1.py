import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Read proxies from the proxies.txt file
with open('proxies.txt', 'r') as file:
    proxies = [line.strip().split("|")[0] for line in file.readlines()]

# List of URLs to open
urls = [
    "https://updatedmail.co.ke/tag/betty-kyallo/",
"https://updatedmail.co.ke/tag/tanzaniacelebrities/",
"https://updatedmail.co.ke/category/technology/",
"https://updatedmail.co.ke/category/entertainment/",
"https://updatedmail.co.ke/2022/10/27/meet-13-young-kenyan-entrepreneurs-who-made-their-first-million-in-their-20s/",
"https://updatedmail.co.ke/tag/kylian-mbappe/",
"https://updatedmail.co.ke/2024/05/04/too-soon-to-leave-yet-hes-gone-mma-giant-francis-ngannou-mourns-his-15-month-old-son-kobe/",
"https://updatedmail.co.ke/tag/jose-chameleone/",
"https://updatedmail.co.ke/2024/05/07/eric-omondi-urges-christina-shusho-to-release-zakayo-video-a-gospel-anthem-with-political-undertones/",
"https://updatedmail.co.ke/tag/raila-odinga/",
"https://updatedmail.co.ke/tag/arsenal-win/",
"https://updatedmail.co.ke/2024/05/06/kenyan-living-in-saudi-arabia-set-to-be-executed-after-being-found-guilty-of-doing-this/",
"https://updatedmail.co.ke/2024/05/06/hii-ni-mbaya-kenyans-react-after-two-red-cross-workers-were-spotted-doing-this-on-a-rescue-mission/",
"https://updatedmail.co.ke/tag/oulanyahs-body-arrives/",
"https://updatedmail.co.ke/tag/kenya-kwanza/",
"https://updatedmail.co.ke/tag/liverpool/",
"https://updatedmail.co.ke/tag/russian-war/",
"https://updatedmail.co.ke/2023/05/23/tribute-to-kenyas-legend-journalist-swale-mdoe/",
"https://updatedmail.co.ke/tag/worldcupqualifier/",
"https://updatedmail.co.ke/jouma480gmail-com/",
"https://updatedmail.co.ke/2022/10/27/remember-the-former-ntv-presenter-here-is-what-to-him-after-he-was-fired-after-working-for-18-years-for-ntv/",
"https://updatedmail.co.ke/tag/entebbe-oulanyah-burial/",
"https://updatedmail.co.ke/author/john-ouma/",
"https://updatedmail.co.ke/tag/arsenal-news/",
"https://updatedmail.co.ke/tag/neymar/",
"https://updatedmail.co.ke/page/2/",
"https://updatedmail.co.ke/tag/putin/",
"https://updatedmail.co.ke/2022/12/07/vera-sidika-finally-addresses-romours-that-she-is-pregnant-with-second-child/",
"https://updatedmail.co.ke/2022/05/20/sasha-mbote-opens-up-how-a-photo-with-raila-ruined-her-her-life/",
"https://updatedmail.co.ke/tag/real-madrid/",
"https://updatedmail.co.ke/page/20/",
"https://updatedmail.co.ke/category/tie-life-style/",
"https://updatedmail.co.ke/tag/rongrende/",
"https://updatedmail.co.ke/tag/pallaso/",
"https://updatedmail.co.ke/tag/oulanyahs/",
"https://updatedmail.co.ke/tag/ugandan-celebrity-news/",
"https://updatedmail.co.ke/category/politics/",
"https://updatedmail.co.ke/disclaimer/",
"https://updatedmail.co.ke/2023/01/26/meet-former-ntv-and-ktn-news-anchor-lindah-oguttu-now-works-in-mjengo-photos/",
"https://updatedmail.co.ke/tag/dp-ruto/",
"https://updatedmail.co.ke/category/uncategorized/",
"https://updatedmail.co.ke/2024/05/04/mwanzo-mpya-stevo-simple-boy-forced-to-open-new-social-media-accounts-after-his-previous-management-refused-to-give-him-access-to-his-accounts/",
"https://updatedmail.co.ke/tag/bobiwine/",
"https://updatedmail.co.ke/2024/05/05/christina-shushos-ex-husband-hits-back-it-hurts-butnew-level-new-devil-new-glory/",
"https://updatedmail.co.ke/category/tie-world/",
"https://updatedmail.co.ke/tag/sakaja/",
"https://updatedmail.co.ke/tag/cristiano-ronaldo-manchester-united/",
"https://updatedmail.co.ke/category/lifestyle/",
"https://updatedmail.co.ke/tag/dp/",
"https://updatedmail.co.ke/tag/ralf-randnick-manchester-united/",
"https://updatedmail.co.ke/2024/05/04/a-heartfelt-celebration-lilian-mulis-birthday-honored-by-her-beloved-mysteryman/",
"https://updatedmail.co.ke/tag/ukrainevsrussiawar/",
"https://updatedmail.co.ke/tag/uda/",
"https://updatedmail.co.ke/tag/man-united/",
"https://updatedmail.co.ke/tag/one-kenya-alliance/",
"https://updatedmail.co.ke/tag/gossip/",
"https://updatedmail.co.ke/2023/07/02/12739/",
"https://updatedmail.co.ke/tag/worldwar3/",
"https://updatedmail.co.ke/category/lifestyle-society/",
"https://updatedmail.co.ke/tag/diamond/",
"https://updatedmail.co.ke/privacy-policy/",
"https://updatedmail.co.ke/tag/uon/",
"https://updatedmail.co.ke/2024/05/05/akothe-celebrates-after-king-roso-gifted-her-ksh-1-5-million-in-tiktok-live/",
"https://updatedmail.co.ke/2022/03/08/halima-namakula-hanson-baliruno-accused-of-making-off-with-shs7m-belonging-to-events-promoter/",
"https://updatedmail.co.ke/page/622/",
"https://updatedmail.co.ke/tag/arsenal-fc/",
"https://updatedmail.co.ke/tag/william-ruto/",
"https://updatedmail.co.ke/2022/07/04/bahati-finally-opens-up-on-diana-maruas-pregnancy/",
"https://updatedmail.co.ke/about-us/",
"https://updatedmail.co.ke/tag/liverpool-fc-news/",
"https://updatedmail.co.ke/page/3/",
"https://updatedmail.co.ke/2024/05/07/ringtone-apoko-kenyas-controversial-gospel-artist-on-the-search-for-a-prayerful-lady-who-can-devote-up-to-seven-hours-a-day-to-pray-and-procreate-7-children/",
"https://updatedmail.co.ke/tiehome/",
"https://updatedmail.co.ke/",
"https://updatedmail.co.ke/2024/05/06/god-is-punishing-kenya-with-floods-pastor-ezekiel-odero-comes-out-clean-about-the-current-floods/",
"https://updatedmail.co.ke/page/10/",
"https://updatedmail.co.ke/2022/03/08/huyu-hataki-mtu-afanye-kazi-yake-nana-exposes-boyfriend-madiba-after-he-did-this-to-her-in-mombasa/",
"https://updatedmail.co.ke/tag/ukraine-war/",
"https://updatedmail.co.ke/tag/bobi-wine/",
"https://updatedmail.co.ke/category/entertainment/updatedmail-sports/",
"https://updatedmail.co.ke/2022/12/06/lisemwalo-lipo-karen-nyamu-finally-responds-to-pregnancy-rumors/",
"https://updatedmail.co.ke/tag/russian-forces/",
"https://updatedmail.co.ke/tag/azimio-la-umoja/",
"https://updatedmail.co.ke/tag/people-power/",
"https://updatedmail.co.ke/2022/02/07/edouard-mendy-is-on-top-of-the-world-right-now/",
"https://updatedmail.co.ke/tag/raila-university-of-leipzig/",
"https://updatedmail.co.ke/author/joh/",
"https://updatedmail.co.ke/tag/champions-league/",
"https://updatedmail.co.ke/contact-us/",
"https://updatedmail.co.ke/category/tie-business/",
"https://updatedmail.co.ke/tag/ralf-rangnick/",
]

# Initialize UserAgent for generating random user agents
ua = UserAgent()

# Function to smooth scroll
def smooth_scroll(driver, scroll_pause_time=0.1, scroll_step=50):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for y in range(0, last_height, scroll_step):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(scroll_pause_time)
    driver.execute_script(f"window.scrollTo(0, {last_height});")

# Main loop to run the script multiple times
for i in range(10000):
    if not proxies:
        print("No more proxies available.")
        break

    # Randomly select a proxy
    proxy = random.choice(proxies)

    # Generate a random user agent
    user_agent = ua.random

    # Set the proxy and user agent options for the browser
    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)  # Using inbuilt Selenium ChromeDriver

    try:
        # Open all URLs in separate tabs
        for url in urls:
            driver.execute_script("window.open('{}', '_blank');".format(url))
            time.sleep(2)  # Wait for 2 seconds before opening the next URL

        # Switch to each tab and perform the scrolling
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            time.sleep(5)  # Give some time for the page to load

            # Auto-scroll in the tab
            smooth_scroll(driver, scroll_pause_time=0.1, scroll_step=50)
            time.sleep(5)  # Sleep for 5 seconds after scrolling

        # Random sleep time between 2 to 5 minutes
        random_sleep = random.randint(150, 300)
        time.sleep(random_sleep)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

    print(f"Iteration {i} completed.")

    # Optionally, re-add the proxy to the list if it didn't fail
    proxies.append(proxy)
