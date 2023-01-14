import requests
from bs4 import BeautifulSoup
import datetime 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def scrape():
    URL = "https://store.dq-solutions.ch/de/apple-iphone-14-pro-1-tb-dunkellila-2022-ci0535?m=1665"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find

    prise_element = result("span", class_ = "finalPrice")
    prise = prise_element.text 
    date_time = datetime.datetime.now()
    name = "dqSolution"

    print(prise)
    print(date_time)
    print(name)

    c.execute('''INSERT INTO projects VALUES(?,?,?)''',(name, date_time,prise))
    conn.commit()

if __name__ == '__main__':
    scrape()