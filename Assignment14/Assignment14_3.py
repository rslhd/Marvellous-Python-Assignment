class Book:
    def __init__(self,a):
        self.__price = a

    def getPrice(self):
        return self.__price

    def setPrice(self):
        NewPrice = int(input("Enter new price : "))
        self.__price = NewPrice

    def display(self):
        print("Book Price : ",self.__price)

def main():
    book1 = Book(350)
    book1.GetPrice()
    book1.display()

    book1.SetPrice()
    book1.display()

if __name__ == "__main__":
    main()