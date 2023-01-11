import requests
from bs4 import BeautifulSoup
import datetime 

def scrape():
    URL = "https://www.melectronics.ch/de/p/794694800000/apple-iphone-14-pro-1tb-deep-purple"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("span", class_ = "HoaWkyNbwTJiluR0wpcQF")
    date_time = datetime.datetime.now()

    print(prise_element.text)
    print(date_time)
    print("melectronic")

if __name__ == '__main__':
    scrape()