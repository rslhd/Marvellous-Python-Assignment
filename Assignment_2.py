def ChkNum(no1):
    if(no1/2 == 0):
        print("Number is even")

    else:
        print("Number is odd")    

def main():
    print("Enter a number")
    value = int(input())

    result = ChkNum(value)

if __name__ == "__main__":
    main()