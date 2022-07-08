from Fundamentals.oops.day1.BankAccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    def