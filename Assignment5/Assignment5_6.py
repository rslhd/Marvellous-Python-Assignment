def Tem(cel):
    fahr = (cel * 9/5) + 32
    print("Conversion is " , fahr) 

def main():
        Celi = int(input("Enter temperature in Celsius: "))
        Tem(Celi)

if __name__ == "__main__":
    main()