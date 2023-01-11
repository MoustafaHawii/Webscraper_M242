import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.computerli.ch/products/6656289"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("span", class_ = "price")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)
    print("computerli")

if __name__ == '__main__':
    scrape()