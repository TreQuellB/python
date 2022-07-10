number = 10
if number > 0:
    print(f" number{number} is positive")
elif number < 0:
    print(f"hey yall {number} ah ooooo")
else:
    print(f" number{number} is negative")

print(type([]))
number = 1
number_two = 2
number_three = 3
numbers = [1, 2, 3, 4, 5, 6, -1, 0, [1,2,3,4,5]]
print(numbers[6])
#list in a list can be targeted by targeting the index of list then targetting the number in the index index number
print(numbers[8][0])
#cant get index out of range will give back a error
#list methods
numbers = [1,2,3]
numbers.remove(1)#remove 2
numbers.reverse()#[3,1]
numbers.append(1245)#[3,1,1245] adds the number to list
del numbers[0]#would delete what ever is in index 0
del numbers[0:3]#would delete from index 0 to 3 index 1 and 2 would be deleted
numbers.clear()#was cleared so false when trying to find 3 in line 26
print(numbers)
print(len(numbers))#tells how many values in list which would be 0
print(3 in numbers)
#SETS
numberList=[1,1]
numberSet = {1,1}#does not allow duplicates will only print  1 one time
print(numberList)
print(numberSet.remove(1))

lettera={"a","b"}
letterb={"a","c", "d"}
union = lettera | letterb
intersection = lettera & letterb
difference = letterb - lettera
print(f"Defference{difference}")#finds the difference in the list and prints them which ever list is first for comparison
print(f"Union = {union}")
print(f"Intersection = {intersection}")#intersection finds what ever is a duplicate and prints in set{a}would be here
print(lettera | letterb)
#DICTIONARIES KEYS AND VALUES
person = {
    "name":"jamal",
    "age":20,
    "hair":"black"
}
print(person["age"])
print(person["hair"])
print(person["name"])
print(person.keys())#shows keys in list
print(person.values())#show values in list
person["age"]=30#update age to 30
print(person)
#LOOPS
names = ["ahmed","tre",
    "mike", "robert"]
#FOR LOOP
for name in (names):
    print(names)

person = {
    "name":"jamal",
    "age":20,
    "hair":"black"
}
for key in person:
    print(f"key:{key}value:{person[key]}")

result = 0
numbers = [1,2,3,4]
for number in numbers:
    result += number
print(f"Results ={result}")
#WHILE LOOP BREAK AND CONTINUE
number = 30
while number < 20:
    print(number)
    number +=1
else:
    print("okay")


number = 30
while number < 20:
    number +=1
    if number < 5:
        break
    print(number)
    
number = 30
while number < 20:
    number +=1
    if number < 5:
        continue
    print(number)

def greet (name):
    print(f"hey{name}")
greet("vlskv")
greet("vlskv")

def greet():
    print("oo")
greet()

def what(age):
    if age >=16:
        return True
    else:
        return False
whaat = what(10)
print(whaat)

def convertGender(gender="unknown"):
    if gender.upper()=="M":
        return "male"
    elif gender.upper() == "F":
        return "female"
    else:
        return f"gender{gender} is unknown"
print(convertGender("m"))
print(convertGender("f"))
print(convertGender("hello"))
print(convertGender("M"))
print(convertGender("F"))
#IMPORT
# import math
# print(math.isqrt(25))
# from math import isqrt#squre route import that was already made by some one or yourself
#import a fileor the file you created use name to target
from datetime import datetime
import calculator
print(calculator.divide(1,2))
print(calculator.plus(1,2))
print(calculator.subtract(1,2))
print(calculator.times(1,2))
print(calculator.remainder(1,2))
from calculator import divide#other way to do it
print(divide(2,2))
#CLASSES A BLUEPRINT FOR CREATING ANYTHING YOU CAN THINK OF THE BLUEPRINT TO CREATE OBJECTS
#WITH CLASSES WE REPRESENT THE ATTRIBUTE
class Phone:
    def __init__(self, brand, price):
        self.brand =brand#properties
        self.price=price

    def call(self, phone_number):
        print(f"{self.brand} is calling{phone_number}")
iphone = Phone("Iphone 7+",300)
samsung = Phone("Samsung s20 ",1400)
print(iphone.brand)
print(iphone.price)
print(samsung.brand)
print(samsung.price)
iphone.call("777")
#WORKING WITH DATES
import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())
print(datetime.datetime.now().time())

from datetime import datetime
from datetime import date
print(datetime.now())
print(date.today())
print(datetime.now().day)
#FORMATTING DATES

