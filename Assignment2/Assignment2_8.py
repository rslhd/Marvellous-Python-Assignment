def displayPattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, " ", end="")
        print()

def main():
    number = int(input("Enter a number: "))
    displayPattern(number)

if __name__ == "__main__":
    main()