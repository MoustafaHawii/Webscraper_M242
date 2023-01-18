import requests
from bs4 import BeautifulSoup
import datetime 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def scrape():
    URL = "https://www.melectronics.ch/de/p/794694800000/apple-iphone-14-pro-1tb-deep-purple"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    price_element = result("span", class_ = "HoaWkyNbwTJiluR0wpcQF")
    price = price_element.text
    date_time = datetime.datetime.now()
    name = "melectronic"

    price1 = price.replace("CHF", "")
    price2 = price1.replace(".–", "")
    price3 = price2.replace("'", "")

    price3 = float(price3)

    print(price3)
    print(date_time)
    print(name)

    c.execute('''INSERT INTO projects VALUES(?,?,?)''',(name, date_time,price3))
    conn.commit()

if __name__ == '__main__':
    scrape()