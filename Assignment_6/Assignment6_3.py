def table(n):
    for i in range(1,11):
        tab = n * i
        print(n,"x",i ,"=",tab)
    
def main():
    ret = int(input("Enter a number"))
    table(ret)       

if __name__ == "__main__":
    main()   