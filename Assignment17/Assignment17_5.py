import schedule
import time

def timeC():
    filename = "Marvellous.txt" 
    fobj = open(filename,"a")
    fobj.write(time.ctime()+"\n")
    
def main():
    schedule.every(5).minutes.do(timeC)

    print("Application is in waiting state ")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()