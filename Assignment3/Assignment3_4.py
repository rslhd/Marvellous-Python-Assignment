def calculateFrequency(numbers, target):
    return numbers.count(target)

def main():

    N = int(input("Enter how many numbers you want to input: "))
    numbers = []


    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)


    searchNum = int(input("Enter the number to find its frequency: "))

    freq = calculateFrequency(numbers, searchNum)
    print(f"The frequency of {searchNum} is: {freq}")


if __name__ == "__main__":
    main()