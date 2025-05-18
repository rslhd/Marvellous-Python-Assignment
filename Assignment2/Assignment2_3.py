def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def main():
    getNum = int(input("Enter a number "))
    doFact = factorial(getNum)

    print("Factorial is " , doFact)

if __name__ == "__main__":
    main()            

