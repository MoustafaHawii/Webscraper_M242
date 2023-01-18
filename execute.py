import schedule 
import time
from main import main_def as main_def

def job():
    print("works")
    main_def()

#schedule.every().day.at("00:00").do(job)
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    #time.sleep(60)
