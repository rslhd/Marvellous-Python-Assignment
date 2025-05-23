def large(no1,no2,no3,no4,no5):
   largest = no1
   if(no2 > largest):
    largest = no2
   if(no3 > largest):
    largest = no3
   if(no4 > largest):
    largest = no4
   if(no5 > largest):
    largest = no5
   print("The largest number is", largest)

def main():
 # Ask the user to enter 5 numbers
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   num3 = int(input("Enter third number: "))
   num4 = int(input("Enter fourth number: "))
   num5 = int(input("Enter fifth number: "))

   ret = large(num1, num2 , num3 , num4 , num5)

if __name__ == "__main__":
   main()