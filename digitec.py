import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.digitec.ch/de/s1/product/apple-iphone-14-pro-1000-gb-deep-purple-610-sim-esim-48-mpx-5g-smartphone-21996997"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("strong", class_ = "sc-1aeovxo-1")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)

if __name__ == '__main__':
    scrape()