import schedule
import datetime
import time

def checkmail():
   print("Checking email ", datetime.datetime.now())
   
def main():
    schedule.every(10).seconds.do(checkmail)
    
    print("Application is in waiting state ")
    while True:
      schedule.run_pending() 
      time.sleep(1)
      
if __name__ == "__main__":
    main()