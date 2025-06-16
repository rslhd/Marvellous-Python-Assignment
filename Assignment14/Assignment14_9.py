class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
            return self.price == other.price
        
    def display(self):
        print("Product Name  ", self.name,"Price",self.price)

def main ():
    obj1 = Product("Laptop", 50000)
    obj2 = Product("Book", 60)
    obj3 = Product("Bag", 300)

    obj1.display()
    obj2.display()
    obj3.display()

    print("Is p1 and p2 equal in price ?", obj1 == obj2)  
    print("Is p1 and p3 equal in price ?", obj1 == obj3)  

if __name__ == "__main__":
    main()