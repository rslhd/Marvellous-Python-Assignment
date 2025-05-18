def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    
    if isPrime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

if __name__ == "__main__":
    main()
