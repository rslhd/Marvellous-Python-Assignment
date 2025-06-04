class Circle:
    Pi = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
   
    def accept(self):
        self.radius = float(input("Enter radius "))
    
    def calArea(self):
        ans = 0.0
        self.area = Circle.Pi * self.radius * self.radius   

    def calCircumference(self):
          ans = 0.0
          self.circumference = 2 * Circle.Pi * self.radius
    
    def display(self):
         print("Radius is " , self.radius)
         print("Area of circle is ", self.area)
         print("Circumference of the circle is ", self.circumference)

def main():
     obj = Circle()

     obj.accept()
     obj.calArea()    
     obj.calCircumference()   
     obj.display()   

if __name__ == "__main__":
     main()     
