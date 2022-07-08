num1 = 42 #integer 
num2 = 2.3#decimal/float
boolean = True# boolean
string = 'Hello World'# string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#dictionary
fruit = ('blueberry', 'strawberry', 'banana')#tuples
print(type(fruit))#type string
print(pizza_toppings[1])#index sausage
pizza_toppings.append('Mushrooms')#['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushrooms']
print(person['name'])
person['name'] = 'George'#string function person parameter name arguement george
person['eye_color'] = 'blue'#string function person parameter eye_color arguement blue single line
print(fruit[2])#variable index in a tuples banana 

if num1 > 45:#conditional
    print("It's greater")
else:#conditional
    print("It's lower")

if len(string) < 5:#conditional len= length of string less than 5
    print("It's a short word!")
elif len(string) > 15:#conditional
    print("It's a long word!")
else:#conditional
    print("Just right!")

for x in range(5):# for loop
    print(x)#conditional
for x in range(2,5):#for loop
    print(x)
for x in range(2,10,3):#for loop
    print(x)
x = 0
while(x < 5):#while loop
    print(x)
    x += 1#increment by 1

pizza_toppings.pop()#remove  element from end of array
pizza_toppings.pop(1)#remove specific index in array

print(person)
person.pop('eye_color')#
print(person)

for topping in pizza_toppings: #single line
    if topping == 'Pepperoni':#single line
        continue# continues throught out if
    print('After 1st if statement')
    if topping == 'Olives':
        break# codition stops code above stops

def print_hello_ten_times():#function   parameter
    for num in range(10):#loop ten times printing hello*10
        print('Hello')

print_hello_ten_times()#called function

def print_hello_x_times(x):#parameter
    for num in range(x):#0-4 range is 4
        print('Hello')#called function

print_hello_x_times(4)#gave a arguement 

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):#range 14 hello *14
        print('Hello')

print_hello_x_or_ten_times()#empty nothing prints
print_hello_x_or_ten_times(4)#arguement 


"""
Bonus section
"""
num3 = 72
print(num3)
fruit = ('cranberry','blueberry', 'strawberry', 'banana')
print(fruit[0])


# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1