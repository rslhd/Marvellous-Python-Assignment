def main():
    fileName = "Number.txt"

    fobj = open(fileName,"w")
    print("Enter 10 numbers ")
    
    for i in range(10):
        print("Enter nunber",i+1," : ")
        num = int(input())
        fobj.write(str(num) +"\n")

    fobj.close()

if __name__ == "__main__":
    main()