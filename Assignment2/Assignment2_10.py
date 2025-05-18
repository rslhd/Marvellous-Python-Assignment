def sumDigits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total

def main():
    number = int(input("Enter a number: "))
    result = sumDigits(number)

    print("The sum of the digits is:", result)

if __name__ == "__main__":
    main()
