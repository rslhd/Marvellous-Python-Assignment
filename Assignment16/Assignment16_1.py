def main ():
    fileName = "Student.txt"

    fobj = open(fileName,"w")
    
    data = ("Gitu , Ari , Rithik , Nela, Nita")
    
    fobj.write(data)

    fobj.close()


if __name__ == "__main__":
    main()
