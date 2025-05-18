def digits(num):
    count = 0
    if num == 0:
        count = 1
    else:
        while num != 0:
            num = num // 10
            count += 1
    return count

def main():
    number = int(input("Enter a number: "))
    result = digits(number)
    print("Number of digits is:", result)

if __name__ == "__main__":
    main()
