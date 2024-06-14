import requests
from bs4 import BeautifulSoup

def get_google_suggestions(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://www.google.com/search?q={query}&hl=en"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    suggestions = []
    for suggestion in soup.find_all('div', {'class': 'BNeawe deIvCb AP7Wnd'}):
        suggestions.append(suggestion.get_text())

    return suggestions

# Example usage
query = "kilimobiashara.co.ke"
suggestions = get_google_suggestions(query)
print("Google Search Suggestions:")
for suggestion in suggestions:
    print(suggestion)
