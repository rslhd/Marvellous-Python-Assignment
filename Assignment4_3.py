def filterX(numbers):
    result = []
    for num in numbers:
        if 70 <= num <= 90:
            result.append(num)
    return result

def mapX(fNumbers):
    result = []
    for num in fNumbers:
        result.append(num + 10)
    return result

def reduceX(mNumbers):
    product = 1
    for i in mNumbers:
        product = product * mNumbers
    return product

def main():
    
    numbers = []
    n = int(input("How many numbers do you want to enter? "))
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    print("Original Numbers:", numbers)
    

    fNumbers = filterX(numbers)
    print("Filtered Numbers :", fNumbers)
    
    
    mNumbers = mapX(fNumbers)
    print("Mapped Numbers :", mNumbers)
    
    
    product = reduceX(mNumbers)
    print("Product of all numbers:", product)
    

if __name__ == "__main__":
    main()        
