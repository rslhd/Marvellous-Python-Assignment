def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if(number > maximum):
            maximum = number
    return maximum

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    maximum_number = find_maximum(numbers)

    print("The maximum number is:", maximum_number)

if __name__ == "__main__":
    main()        
