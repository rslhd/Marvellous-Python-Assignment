import sys

def main():
    if len(sys.argv ) != 2 :
        print("Enter new file name as command argument")
        exit
    
    targetFileName = sys.argv[1]
    sourceFileName = "Demo.txt"
    
    fobj1 = open(targetFileName,"w")

    fobj2 = open(sourceFileName,"r")
    data = fobj2.read()

    fobj1.write(data)

    fobj2.close()
    fobj1.close()



if __name__ == "__main__" :
    main()