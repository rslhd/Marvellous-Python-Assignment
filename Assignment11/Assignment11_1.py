def num(no):
    if (no > 0):
        num(no - 1)
        print(no)   

def main():
   num(8)

if __name__ == "__main__":
    main()
