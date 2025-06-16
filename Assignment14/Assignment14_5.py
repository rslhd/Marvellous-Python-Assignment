class bankaccount:
    def __init__(self,a,b,c):
        self.name = a
        self.accountNumber = b
        self.balance = c

    def deposit(self):
        print("amount to deposit: ")
        depAmount=int(input())
        self.balance = self.balance + depAmount

    def withdraw(self):
        print("amount to withdraw: ")
        widAmount=int(input())
        self.balance = self.balance - widAmount

    def display(self):
        print("Name ",self.name)
        print("Account number: ",self.accountNumber)
        print("Balance: ",self.balance)
    
def main():
    obj1 = bankaccount("Gitu",90,2000)
    obj1.display()
    obj1.deposit()
    obj1.withdraw()
    obj1.display()

if __name__ == "__main__":
    main()