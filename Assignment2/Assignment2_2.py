def displayPattern(n):
    for i in range(n):
        print("*" * n)

def main():
    number = int(input("Enter a number: "))
    displayPattern(number)

if __name__ == "__main__":
    main()
