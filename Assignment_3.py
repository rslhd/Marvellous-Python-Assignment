def Add(no1 ,no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():
    print("Enter a number")
    value1 = int(input())

    print("Enter another number")
    value2 = int(input())

    result = Add(value1 , value2)

    print("Addition of two numbers is ",result)

if __name__ == "__main__":
    main()