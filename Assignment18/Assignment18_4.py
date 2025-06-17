
import sys

def main():
    if len(sys.argv ) < 2 :
        print("Enter new file names that need to be compared")
        exit
    
    targetFileName = sys.argv[1]
    sourceFileName = sys.argv[2]
    
    fobj1 = open(targetFileName,"r")
    data1 = fobj1.read()

    fobj2 = open(sourceFileName,"r")
    data2 = fobj2.read()

    if data1 == data2 :
        print("Success")
    
    else :
        print("Not same data")

    fobj2.close()
    fobj1.close()



if __name__ == "__main__" :
    main()
