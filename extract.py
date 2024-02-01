import requests
from bs4 import BeautifulSoup

def extract_all_hrefs_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        anchor_tags = soup.find_all('a')
        
        href_contents = [tag.get('href') for tag in anchor_tags]
        return href_contents
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
# Example usage
url = 'https://wemabank.freshdesk.com/support/solutions/folders/67000452558'
results = extract_all_hrefs_from_url(url)

if results:
    for result in results:
        print(result)
else:
    print("Failed to extract href contents from the URL.")
