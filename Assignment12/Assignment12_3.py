class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input("Enter a number "))    
        self.value2 = int(input("Enter a number ")) 

    def addition(self):
           return self.value1 + self.value2

    def subtraction(self):
        return self.value1 - self.value2

    def multiplication(self):
        return self.value1 * self.value2

    def division(self):
        return self.value1 / self.value2
    
def main():
    obj = Arithmetic()   
    obj.accept() 

    ret = obj.addition()
    print("Addition of two number is ",ret)

    ret = obj.subtraction()
    print("Subtraction of two number is ",ret)

    ret = obj.multiplication()
    print("Multiplication of two number is ",ret)

    ret = obj.division()
    print("Division of two number is ",ret)
          
if __name__ == "__main__":
    main()