import psutil
import sys

def processDisplay(pname):
    border ="*" * 60
    print(border)
    print("Information of currently running processes ")
    print(border)

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == pname:
                info = proc.as_dict(attrs=['pid','name','username'])
                print(info)
        except Exception:
            print("Exception occured")

def main():
    name=sys.argv[1]
    processDisplay(name)

if __name__ == "__main__":
    main()
