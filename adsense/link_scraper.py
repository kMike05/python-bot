import requests
from bs4 import BeautifulSoup
import re

def get_internal_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        internal_links = set()

        # Find all anchor tags
        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            if href.startswith('/') or href.startswith(url):
                internal_links.add(href)

        return internal_links
    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return set()

def filter_urls(urls):
    filtered_urls = set()
    for url in urls:
        if not re.match(r'^/(tag|category|page|author|author|tag|category)/.*', url):
            filtered_urls.add(url)
    return filtered_urls

def save_urls_to_file(urls, filename):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(f'"{url}",\n')

def main():
    base_url = 'https://updatedmail.co.ke/'
    internal_links = get_internal_links(base_url)
    filtered_links = filter_urls(internal_links)
    save_urls_to_file(filtered_links, 'kilimobiashara_urls.txt')

if __name__ == "__main__":
    main()
