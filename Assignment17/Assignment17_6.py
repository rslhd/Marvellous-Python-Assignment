import schedule
import time

def lunchTime():
    print("Lunch Time")

def wrapUpTime():
    print("Wrap Up Work")


def main():
    schedule.every().day.at("13:00").do(lunchTime)

    schedule.every().day.at("18:00").do(wrapUpTime)

    print("Application is in waiting state ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()