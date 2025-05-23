
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i 
    return result

def main():
  num = int(input("Enter a number to find its factorial: "))
  ret = factorial(num)
  print("Factorial is ",ret)

if __name__ == "__main__":
   main()