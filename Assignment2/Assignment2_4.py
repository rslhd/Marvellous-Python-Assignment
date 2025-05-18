def sumFactors(num):
    total = 0
    for i in range(1, num + 1):
            total += i
    return total

def main():
    number = int(input("Enter a number: "))
    result = sumFactors(number)
    
    print("Sum of factors is:", result)

if __name__ == "__main__":
    main()
