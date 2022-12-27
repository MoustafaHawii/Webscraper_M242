import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.mobilezone.ch/de/mobilgeraete/handys/apple/iphone-14-pro-5g/deep-purple/1-tb/100010898"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("span", class_ = "mz-m-product-buy-box__wrapper__buy-box-inner__price-label")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)

if __name__ == '__main__':
    scrape()