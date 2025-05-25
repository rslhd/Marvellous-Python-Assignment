import threading

def even(no):
    for i in range(2,no+1,2):
       print("Even numbers are ",i) 

def odd(no):
    for i in range(1,no+1,2):
       print("Odd numbers are ",i)

def main():
    T1 = threading.Thread(target = even, args = (11,))
    T1.start()     
    T1.join()

    T2 = threading.Thread(target = odd, args = (10,))
    T2.start()
    T2.join()

if __name__ == "__main__":
   main()   
