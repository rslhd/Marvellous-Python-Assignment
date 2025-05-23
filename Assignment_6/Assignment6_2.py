def even(n):
    return n % 2 == 0

def sum(no):
    total = 0
    for i in range(1, no + 1):
        if even(i):
            total += i
    return total

def main():
    result = sum(100)
    print("Sum of all even numbers till 100 is:", result)

if __name__ == "__main__":
    main()    
