def Div(value):
    if(value % 5 == 0):
        print("True")

    else:
        print("False") 

def main():
    print("Enter a number")
    num = int(input())

    result = Div(num)

if __name__ == "__main__":
    main()               