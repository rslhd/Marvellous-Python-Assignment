Fact = 1
def fact(no):
    if(no >= 1):
        global Fact
        Fact = Fact * no
        no = no - 1
        fact(no)
        return Fact
    
def main():
    ret = fact(5)
    print(ret)

if __name__ == "__main__":
    main()       