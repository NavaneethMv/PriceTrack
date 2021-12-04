from os import link
from bs4 import BeautifulSoup
import requests

HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'}

def scrape(LINK):
    try:
        source = requests.get(LINK, headers=HEADERS).text
        soup = BeautifulSoup(source, "lxml")
        title = soup.find("span", id="productTitle").get_text().strip()
        try:
            price = soup.find("span", id="priceblock_dealprice").get_text()
        except Exception:
            price = soup.find("span", id="priceblock_ourprice").get_text()
        return title, price
    except Exception:
        return "Error finding the title","Error finding price"
    
