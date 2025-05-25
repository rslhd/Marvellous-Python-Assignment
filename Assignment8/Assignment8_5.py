import threading

def numO(no):
    for i in range(1,no+1,1):
        print(i)

def numR(no):
    for i in range(no,0,-1):
        print(i)

def main():
   T1 = threading.Thread(target = numO ,args = (50,))
   T1.start()
   T1.join()
   
   T2 = threading.Thread(target = numR, args = (50,))
   T2.start()
   T2.join()

if __name__ == "__main__":
    main()            