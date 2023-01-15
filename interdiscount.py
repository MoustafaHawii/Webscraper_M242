import requests
from bs4 import BeautifulSoup
import datetime 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def scrape():
    URL = "https://www.interdiscount.ch/de/mobiltelefon-tablet-smartwatch/mobiltelefon/mobiltelefone--c411000/apple-iphone-14-pro-max-5g-1000-gb-6-7-48-mp-dunkellila--p0009071726"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    price_element = result("div", class_ = "_3H04_H")
    price = price_element.text
    date_time = datetime.datetime.now()
    name = "interdiscount"

    print(price)
    print(date_time)
    print(name)

    c.execute('''INSERT INTO projects VALUES(?,?,?)''',(name, date_time,price))
    conn.commit()

if __name__ == '__main__':
    scrape()