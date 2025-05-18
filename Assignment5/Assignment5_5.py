def chkEO(number):
    if(number % 2 == 0):
        print("The number is even.")

    else:
        print("The number is odd.")

def main():
        num = int(input("Enter an integer: "))
        chkEO(num)
    
if __name__ == "__main__":
    main()