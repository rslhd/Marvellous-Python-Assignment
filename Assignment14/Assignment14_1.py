class Employee :
    def __init__(self,a,b,c):
        self.Name = a
        self.Emp_ID = b
        self.Salary = c

    def display (self):
        print("Name : "+self.Name)
        print("ID : ",self.Emp_ID)
        print("Salary : ",self.Salary)

def main():
    obj1 = Employee("Rohit",800, 500000)
    obj1.display() 

if __name__ == "__main__":
    main()
