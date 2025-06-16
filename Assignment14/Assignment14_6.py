class calculator():

    def __init__(self):
        self.value1 = int(input("enter value1: "))
        self.value2 = int(input("enter value2: "))
    
    def addition(self):
        print("Addition: ", self.value1 + self.value2)

    def subtraction(self):
        print("Subtraction: ", self.value1 - self.value2)

    def multiplication(self):
        print("Multiplication: ", self.value1 * self.value2)

    def division(self):
        print("Division: ", self.value1 / self.value2)
        
def main():
    obj1 = calculator()

    obj1.addition()
    obj1.subtraction()
    obj1.multiplication()
    obj1.division()
    
if __name__ == "__main__":
    main()