class Demo:
    vari = "Value"
    def __init__(self,a,b):
      self.no1 = a
      self.no2 = b

    def fun(self):
        print("Number is ", self.no1)

    def gun(self):
       print("Number is ", self.no2)

def main():
   obj1 = Demo(2,8)
   obj2 = Demo(3, 0)

   obj1.fun()
   obj2.fun()
   obj1.gun()
   obj2.gun()

if __name__ == "__main__":
   main()
