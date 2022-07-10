"""
object  oriented programming
reflects real world entities more closely
build systems that are easily extended or changed
S Single responsiblity principle
O   open closed principle
L liskov substitution principle
I INterface segregation principle
D Dependenct inversion principle
OBJECTS  ENCAPSULATION MESSAGES ABSTRACTION POLYMORPHISM INHERITANCE
O object an concept thing in your software solution
has astate or data in the form of variables
has a behavior or operations in the form of functions
A 
I 
E 
E 
P 
A Class can be reused  a data type 
"""
#when ever we declare a variable we are creating a instance of a classex x = [1,2,3] x is a instance of a list an instance is simply aobject that follows the pattern defined by its class
"""
# class User:
#    attributes:
#         first_name
#         last_name
#         age
#Methods: birthday(  increases age)
#say_greeting( says hello)
"""
class User:
    def __init__(self):
        self.first_name ="ada"
        self.last_name="will"
        self.age=42
print("hello")
user_ada = User()
print(user_ada.first_name)
user2_=User()
print(user2_.age)

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")
adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
adrien.greeting()
# prints Hello, my name is Adrien
cool_person.greeting()
# prints Hello, my name is Sadie
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward
#ENCAPSULATION
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")
#INHERITANCE
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
    super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
    super().brew_now(beans)
    print("Frothy!!!")
#POLYMORPHISM
class CappuccinoM( CoffeeM ):
def __init__(self,name):
super().__init__(name)
self.milk = "whole"
def make_cappuccino(self,beans):
super().brew_now(beans)
print("Frothy!!!")
def clean(self):
print("Cleaning the froth!")
#ABSTRACTION
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self, beans):
        self.cafe.brew_now(beans)


class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum


