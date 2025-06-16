def main():
    fobj = open("names.txt","w")
    fobj.write("Gitu\n")
    fobj.write("Jay\n")
    fobj.write("Mina\n")
    fobj.write("\n")

    nfobj = open("stu.txt","w")

    fobj = open("name.txt","r")
    lines = fobj.readlines()
    
    for i in lines:
        lines = i.split()
        if lines != []:
            nfobj.write(i)

if __name__=="__main__":
    main()