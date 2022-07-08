class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print( f"Insufficient funds: Charging a $5 fee")
            return self
        self.balance -= amount
        print(self.balance)
        return self
        
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        
        return self

mybank_account = BankAccount(5,100)  

mybank_account.deposit(100).deposit(10000).deposit(2).withdraw(300).withdraw(400).deposit(1).display_account_info().yield_interest().display_account_info()

mybank_account2 = BankAccount(2,100)  
mybank_account2.deposit(50).deposit(0).withdraw(25).withdraw(1).withdraw(2).withdraw(1).display_account_info()



