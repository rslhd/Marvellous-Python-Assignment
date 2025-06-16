import sys

def main():
    if len(sys.argv ) < 2 :
        print("Enter the inputs in command line")
        exit
    
    fileName = sys.argv[1]
    searchName = sys.argv[2]
    
    fobj1 = open(fileName,"r")
    data = fobj1.read()

    frequency = data.count(searchName)

    print("The string ",searchName,"appears",frequency,"times in ",fileName)

    fobj1.close()

if __name__ == "__main__" :
    main()