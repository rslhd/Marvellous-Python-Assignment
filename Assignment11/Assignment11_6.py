def nat(no):
    if(no <= 1):
        return no
    return no  + nat(no - 1)
    
def main():
    ret = nat(5)
    print(ret)

if __name__ == "__main__":
    main()        