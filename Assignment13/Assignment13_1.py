class Bookstore:
    NoOfBooks = 0
    def __init__(self,a, b):
        self.Name = a
        self.Author = b
        Bookstore.NoOfBooks += 1
    
    def accept(self):
       self.Name = input("Enter name of book")
       self.Author = input("Enter author of book")

    def display(self):
        print("The name of the book is", self.Name)
        print("The author of the book", self.Author)
        print("The number of books is", Bookstore.NoOfBooks)    

def main():
    obj1 = Bookstore("Linux system of programing", "Robert Love")
    obj1.display()

    obj2 = Bookstore("Linux system of programing", "Robert Love")
    obj2.display()
  
if __name__ == "__main__":
    main()  
