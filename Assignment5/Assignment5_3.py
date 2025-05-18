def eligible(age):
    if (age >= 18):
        print("You are eligible to vote")

    else:
        print("You are not eligible to vote")

def main():
   ages = int(input("Enter your age "))
   eligible(ages)

   
if __name__ == "__main__":
    main()