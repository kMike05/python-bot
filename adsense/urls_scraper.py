import requests
from bs4 import BeautifulSoup
import re

def is_post_url(url):
    # Assuming post URLs are longer than custom pages and have a specific structure
    return len(url) > 30 and re.search(r'/\d{4}/\d{2}/', url)

def scrape_urls(base_url):
    visited_urls = set()
    post_urls = set()

    def scrape_page(url):
        if url in visited_urls:
            return
        visited_urls.add(url)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all anchor tags
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith('/'):
                href = base_url + href
            elif not href.startswith('http'):
                continue

            if base_url in href and href not in visited_urls:
                if is_post_url(href):
                    post_urls.add(href)
                scrape_page(href)

    scrape_page(base_url)
    return post_urls

if __name__ == "__main__":
    base_url = "https:/wiredwhirl.com"
    post_urls = scrape_urls(base_url)
    
    # Print the collected post URLs
    for url in post_urls:
        print(url)
