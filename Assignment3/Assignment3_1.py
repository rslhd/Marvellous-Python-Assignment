def sumNumbers(numbers):
    
    total = 0
    for number in numbers:
        total += number
    return total

def main():

    n = int(input("Enter the number of elements: "))
    numbers = []
    
    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    result = sumNumbers(numbers)
    print("Sum of the numbers:", result)

if __name__ == "__main__":
    main()    