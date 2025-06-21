import psutil
import os
import time
import sys
import smtplib
from email.message import EmailMessage

def sendmail(fpath):

    fobj = open(fpath,"rb")
    data = fobj.read()

    msg = EmailMessage()
    msg.add_attachment(data ,maintype = "file",subtype = "log",filename = fpath)

    msg['Subject'] = "log file of current processes"
    msg['From'] = "kalokheyashshree@gmail.com"
    msg['To'] = "ganeshenter1476@rediffmail.com"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kalokheyashshree@gmail.com", "Hello this is Marvellous Automation")
    s.send_message(msg)
    s.quit()

def createLog(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    filename = os.path.join(folderName,"marvellous%s.log" %(timestamp))

    fobj = open(filename,"w")

    border="-" * 60

    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystems process log\n")
    fobj.write("\n\t\tLog file is created at "+time.ctime()+"\n")
    fobj.write(border)

    data = processScan()
    for value in data:
        fobj.write("%s \n" %value)

    fobj.write(border)

    fobj.close()

    return filename

def processScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["name","pid","username"])
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    dirname = sys.argv[1]
    path =  createLog(dirname)
    sendmail(path)

if __name__ == "__main__":
    main()
