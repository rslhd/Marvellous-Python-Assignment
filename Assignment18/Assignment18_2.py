import os 

def main():
    fileName = input("Enter the file name to check ")

    ret = os.path.exists(fileName)

    if ret == True :
        print ("File exists")
        fobj = open(fileName,"r")
        
        data = fobj.read()

        print("Data from file is ",data)

        fobj.close()
            
    else :
        print("File does not exist") 

if __name__ == "__main__":
    main()