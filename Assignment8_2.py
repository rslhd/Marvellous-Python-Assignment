import threading

def sumEven(no):
    sum = 0 
    for i in range(2,no+2,2):
            sum = sum + i
    print(sum)

def sumOdd(no):
    sum = 0
    for i in range(1,no+1,2):
               sum = sum + i
    print(sum)

def main():
    T1 = threading.Thread(target = sumEven, args = (10,))
    T1.start()     
    T1.join()

    T2 = threading.Thread(target = sumOdd, args = (10,))
    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
   main()   