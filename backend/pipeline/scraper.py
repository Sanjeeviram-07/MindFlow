import requests
from bs4 import BeautifulSoup

def scrape_content(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs[:10]:
        text += p.get_text()

    return text