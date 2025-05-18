def minimumNum(number):
    minimum = number[0]

    for number in number:
        if(number < minimum):
            minimum = number
    return minimum

def main():
    n = int(input("Enter number of elements : "))
    numbers = []

    for i in range(n):
      num = int(input(f"Enter element {i+1}: "))
      numbers.append(num)  

    minimumNumbers = minimumNum(numbers)
    print("The minimum number is " , minimumNumbers) 

if __name__ == "__main__":
    main()                