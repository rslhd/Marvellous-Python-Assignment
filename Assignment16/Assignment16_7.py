def main():
    fobj = open("mark.txt","w")
    fobj.write("Parth 90\n")
    fobj.write("Gitu 90\n")
    fobj.write("Lokesh 95\n")
    fobj.write("Usha 91.9\n")

    fobj = open("mark.txt","r")
    lines = fobj.readlines()
    
    print("Students with marks greater than 75 ")

    for i in lines:
        data = i.split()
        if float(data[1])>= 75:
            print(data[0],"=>",data[1])

    fobj.close()

if __name__ == "__main__":
    main()