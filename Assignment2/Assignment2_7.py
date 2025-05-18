def displayPattern(n):
    for i in range(n):
        for i in range(1, n + 1):
            print(i , " ", end="")
        print()

def main():
    number = int(input("Enter a number: "))
    displayPattern(number)

if __name__ == "__main__":
    main()
