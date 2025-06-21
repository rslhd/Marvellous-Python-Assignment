import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

def calculateCheckSum(path, blocksize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def findDuplicate(directoryName ="Marvellous"):

    flag = os.path.isabs(directoryName)

    if(flag==False):
        directoryName=os.path.abspath(directoryName)

    flag = os.path.exists(directoryName)

    if(flag==False):
        print("the path is invalid")
        exit()

    flag = os.path.isdir(directoryName)

    if(flag==False):
        print("The path is valid but target is not a directory")
        exit()

    duplicate = {}

    for FolderName , SubFoldersNames , FileNames in os.walk(directoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = calculateCheckSum(fname)

            if(checksum in duplicate):
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum] = [fname]

    return duplicate

def deleteDuplicate(path = "Marvellous"):

    mydict = findDuplicate(path)

    result = list(filter(lambda x : len(x)>1 , mydict.values()))

    count = 0
    c = 0

    for value in result:
        for subvalue in value:
            count = count+1
            if (count > 1):
                print("File is deleted ",subvalue)
                os.remove(subvalue)   
                c = c +1         
        count = 0

    print("Total deleted files ",c)

def sendMail(fpath):

    fobj = open(fpath,"rb")
    data = fobj.read()

    msg = EmailMessage()
    msg.add_attachment(data ,maintype = "file",subtype = "log", filename = fpath)

    msg['Subject'] = "log file of current processes"
    msg['From'] = "kalokheyashshree@gmail.com"
    msg['To'] = "ganeshenter1476@reddiffmail.com"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kalokheyashshree@gmail.com", "Hello this is Marvellous Automation")
    s.send_message(msg)
    s.quit()

def main():
 
    border="-" * 60
    print(border)
    print("-----------------------Marvellous Automation----------------------")
    print(border)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("Scriptname.py nameofdirectory")
            print("Please provide valid absolute path")

    if(len(sys.argv) == 3):
            schedule.every(int(sys.argv[2])).minutes.do(deleteDuplicate)

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of command line argument")
        print("Use the given flags as ")
        print("--h  used to display the help")
        print("--u  used to display the usage")

    print(border)
    print("-----------------Thank you for using our script ------------------")
    print("----------------------Marvellous Infosystems----------------------")
    print(border)
    
if __name__ == "__main__":
    main()
