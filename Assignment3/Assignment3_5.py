from MarvellousNum import ChkPrime

def listPrime():
    numbers = []
    n = int(input("Enter how many numbers: "))

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    total = 0
    for num in numbers:
        if ChkPrime(num):
            total += num

    return total

def main():
    result = listPrime()
    print("Sum of all prime numbers is:", result)

if __name__ == "__main__":
    main()