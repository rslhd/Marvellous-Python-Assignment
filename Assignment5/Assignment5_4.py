def large(no1, no2, no3):
    if(no1 > no2):
        if(no1 > no3):
          print("Largest number is ", no1)
        else:
          print("Largest number is ", no3)

    else:
        if(no2 > no3):
           print("Largest number is ", no2) 
        else:
           print("Largest number is ", no3)

def main():
    num1 = int(input("Enter one number "))
    num2 = int(input("Enter next number "))
    num3 = int(input("Enter next number "))
    large(num1, num2, num3)                    

if __name__ == "__main__":
    main()   