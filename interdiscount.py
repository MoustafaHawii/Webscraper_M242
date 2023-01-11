import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.interdiscount.ch/de/mobiltelefon-tablet-smartwatch/mobiltelefon/mobiltelefone--c411000/apple-iphone-14-pro-max-5g-1000-gb-6-7-48-mp-dunkellila--p0009071726"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("div", class_ = "_3H04_H")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)
    print("interdiscount")

if __name__ == '__main__':
    scrape()