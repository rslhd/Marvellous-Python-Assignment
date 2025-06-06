class BankAccount:
    ROI = 10.5
    def __init__ (self):
        self.Name = input("Enter your name ")
        self.Amount = float(input("Enter your amount "))

    def deposit(self):
        depoAmount = float(input("Enter the deposited amount ")) 
        self.Amount += depoAmount
        print("New deposited amount is ", self.Amount)

    def withdraw(self):
        getMoney = float(input("Enter the amount to be withdrawn ")) 
        self.Amount -= getMoney
        print("New amount is ", self.Amount)     

    def calInterest(self):
        inter = self.Amount * BankAccount.ROI / 100
        print("The calculated interest is ", inter)

    def display(self):
        print("The name is", self.Name) 
        print("Deposited amount is ", self.Amount) 

def main():
    obj1 = BankAccount()  
    obj1.deposit()   
    obj1.withdraw()    
    obj1.calInterest() 
    obj1.display() 

if __name__ == "__main__":
    main()    
