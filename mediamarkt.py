import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.mediamarkt.ch/de/product/_apple-iphone-14-pro-2151070.html"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    price_element = result("span", class_ = "product-attributes__item-text")
    date_time = datetime.datetime.now()

    print(price_element.text)
    print(date_time)
    print("mediamarkt")

if __name__ == '__main__':
    scrape()
