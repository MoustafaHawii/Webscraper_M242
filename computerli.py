import requests
from bs4 import BeautifulSoup
import datetime 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def scrape():
    URL = "https://www.computerli.ch/products/6656289"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    price_element = result("span", class_ = "price")
    price = price_element.text
    date_time = datetime.datetime.now()
    name = "computerli"

    print(price)
    print(date_time)
    print(name)

    c.execute('''INSERT INTO projects VALUES(?,?,?)''',(name, date_time,price))
    conn.commit()

if __name__ == '__main__':
    scrape()