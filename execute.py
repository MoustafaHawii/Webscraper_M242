import schedule 
import time
from main import main_def as main_def

def job():
    print("funktioniert")
    main_def()

#schedule.every().day.at("13:53").do(job)
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    #time.sleep(60)
