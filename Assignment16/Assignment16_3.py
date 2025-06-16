def main():
    fileName = "data.txt"

    fobj = open(fileName,"r")
    data = fobj.read() 

    lineCount = len(data.splitlines())
    print("Number of lines are  ",lineCount)

    wordCount = len(data.split())
    print("Number of words are  ",wordCount)  

    characterCount = len(data)
    print("Number of characters are  ",characterCount)

    fobj.close()
    
if __name__ == "__main__":
    main()

    