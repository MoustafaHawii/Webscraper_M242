import requests
from bs4 import BeautifulSoup
import datetime 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def scrape():
    URL = "https://www.digitec.ch/de/s1/product/apple-iphone-14-pro-1000-gb-deep-purple-610-sim-esim-48-mpx-5g-smartphone-21996997"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    price_element = result("strong", class_ = "sc-1aeovxo-1")
    price = price_element.text
    date_time = datetime.datetime.now()
    name = "digitec"

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