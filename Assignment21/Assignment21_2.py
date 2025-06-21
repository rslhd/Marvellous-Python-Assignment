import psutil
import os
import time
import schedule
import sys

def createLog(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")
    
    FileName = os.path.join(folderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")

    border = "-" * 60
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tLog file is created at : " + time.ctime()+"\n")
    fobj.write(border)

    data = processScan()

    for value in data:
        fobj.write("%s \n\n" %value)

    fobj.write(border)

    fobj.close()

def processScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    dirName = sys.argv[1] 
    schedule.every(1).minutes.do(createLog, dirName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
