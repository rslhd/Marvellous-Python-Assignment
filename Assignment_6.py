def inte(value):
    if(value > 0):
        print("Number is positive")

    elif(value < 0):
        print("Number is negative")
    
    else:
      print("Number is zero")

def main():
    print("Enter a number")
    num = int(input())

    result = inte(num)

if __name__ == "__main__":
    main()
