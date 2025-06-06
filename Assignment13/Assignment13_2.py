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


"""class BankAccount:
    # Class variable for Rate of Interest (ROI)
    roi = 10.5

    # Constructor to initialize instance variables from user input
    def __init__(self):
        self.name = input("Enter account holder name: ")
        self.amount = float(input("Enter initial account balance: "))

    # Method to deposit amount into account
    def deposit(self):
        deposit_amount = float(input(f"Enter amount to deposit in {self.name}'s account: "))
        self.amount += deposit_amount
        print(f"Deposited {deposit_amount}. New balance: {self.amount}")

    # Method to withdraw amount from account
    def withdraw(self):
        withdraw_amount = float(input(f"Enter amount to withdraw from {self.name}'s account: "))
        if withdraw_amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= withdraw_amount
            print(f"Withdrew {withdraw_amount}. New balance: {self.amount}")

    # Method to calculate interest
    def cal_interest(self):
        interest = self.amount * BankAccount.roi / 100
        print(f"Interest for {self.name}'s account at ROI {BankAccount.roi}% is: {interest}")
        return interest

    # Method to display account details
    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: {self.amount}")

# Create multiple objects and demonstrate methods
account1 = BankAccount()
account2 = BankAccount()

# For Account 1
print("\n--- Operations for Account 1 ---")
account1.deposit()
account1.withdraw()
account1.cal_interest()
account1.display() 

# For Account 2
print("\n--- Operations for Account 2 ---")
account2.deposit()
account2.withdraw()
account2.cal_interest()
account2.display() """
