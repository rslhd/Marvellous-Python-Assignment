def main ():
    fileName = "data.txt"

    fobj = open(fileName,"r") 

    display = fobj.read()

    print("Contents of file  ",display)
    
    fobj.close()

if __name__ == "__main__":
    main()