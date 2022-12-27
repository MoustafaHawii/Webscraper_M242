import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://store.dq-solutions.ch/de/apple-iphone-14-pro-1-tb-dunkellila-2022-ci0535?m=1665"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("span", class_ = "finalPrice")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)

if __name__ == '__main__':
    scrape()