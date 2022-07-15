from BankAccount import BankAccount#this is importing bankaccount class to user


class User:#class is user
    def __init__(self, name,last_name, email, age):#constructor is creating what a user looks like
        self.name = name
        self.last_name=last_name
        self.email = email
        self.age=age
        self.account = BankAccount(int_rate=5,balance=100)#this is creating a instance in bankaccount within the users class
        
        #METHODS OF THE CLASS
    def make_deposit(self,amount):
        self.account.balance += amount
        print(self.account.balance)
        return self#REMEMBER TO RETURN SELF IF YOU WANT TO CHAIN AT THE END OF EACH METHOD
    def make_withdrawal(self,amount):
        if self.account.balance < amount:
            self.account.balance -= 5
            print( f"Insufficient funds: Charging a $5 fee")
        else:
            self.account.balance -= amount
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
#creating a instance of a user and assigning to a object 
user_tre=User("Trequell","Belle","tre@aol.com",25)
#chaining the methods together
user_tre.make_deposit(215).display_user_balance().make_withdrawal(404).display_user_balance()