from BankAccount import BankAccount


class User:
    def __init__(self, name,last_name, email, age):
        self.name = name
        self.last_name=last_name
        self.email = email
        self.age=age
        self.account = BankAccount(int_rate=5,balance=100)
    def make_deposit(self,amount):
        self.account.deposit(100)
        self.account.balance += amount
        print(self.account.balance)
        return self
    def make_withdrawal(self,amount):
        self.account.withdraw(100)
        if self.account.balance < amount:
            self.balance -= 5
            print( f"Insufficient funds: Charging a $5 fee")
            return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
user_tre=User("Trequell","Belle","tre@aol.com",25)
user_tre.make_deposit(215)
user_tre.display_user_balance()
user_tre.make_withdrawal(104)
user_tre.display_user_balance()
