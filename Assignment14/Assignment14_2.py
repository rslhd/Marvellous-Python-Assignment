class Rectangle:
    def __init__(self,a,b):
        self.lenght = a
        self.breath = b
        
    def area(self):
        Area = self.lenght * self.breath
        print("The area of rectangle is ", Area)    

    def perimeter(self):
        Peri  = 2 * (self.lenght + self.breath)    
        print("The perimeter of the rectangle is ", Peri)

def main():
    obj1  = Rectangle(5,8)        
    obj1.area()
    obj1.perimeter()

if __name__ == "__main__":
    main()    