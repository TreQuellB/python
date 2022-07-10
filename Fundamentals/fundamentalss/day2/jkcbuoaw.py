int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
print(random.randint(2,5)) # provides a random number between 2 and 5

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]

nums12 = [3,4,5,6,66,6]
nums12.append(4)
print(nums12)

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

# len(sequence) returns the length (number of items) in a sequence.
# max(sequence) returns the highest value in a sequence.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence
my_list = [1, 'Zen', 5, 'hi']
print(len(my_list))
# output
# 3

# The following are some commonly used list methods:
# list.append(value) appends a value to the end of the list.
# list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
# list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
# list.reverse() reverses the order of the elements, in place.*
# list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*
my_list = [1,5,2,8,4]
my_list.pop()
my_list.reverse()
my_list.index(1)
my_list.append(45)
print(my_list)
# output:
# [1,5,2,8]

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
for x in range(10):
    print(x)
# output: 5, 2
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

name = 0
while name <= 10:
    print(3389283)
    name += 5

y = 3
while y > 0:
    print(y)
    y = y - 3
else:
    print("Final else statement")

for i in range(1,5000001,2):
    print(i)



for i in range(0,101,1):
    if i % 5==0:
        print("coding dojo")
    elif i % 10==0:
        print("Coding")
    else:
        print(i)


lowNum=3
highNum=9
mult=3
for i in range(lowNum,highNum,mult):
    print(i)

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()# output: good morning (repeated on 2 lines)
be_cheerful("tim")# output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")# output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)# output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")# output: good morning kb (repeated on 3 lines)
# want to repeat  * 2 print and skip a line /or n/
def meeting(name, repeat=2):
    print(f"hey how ya doin{name}\n" * repeat)
meeting("joe")

def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
[2, 4, 10, 16] 
2
[2, 4, 10, 16]
4
[2, 4, 10, 16]
10
[2, 4, 10, 16]
16
[2, 4, 10, 16]
[2, 4, 10, 16]

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# =5
def number_of_food_goupss():
    return 1
print(number_of_food_goupss())
#will return 5
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
def num():
    return 30000
print(num() + num22222())
#error other function not defined
# number_of_days_in_a_week_silicon_or_triangle_sides() is not defined error
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
def num2():
    return 21
    return 322244444444444
print(num2())
#will print first return only =5
# =5 only runs first return
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
def num3():
    return 3
    print(23)
    print(3333)
print(num3())
#reyurn will only print no other print method can work with return print and print would work
#3
# =10 & 5
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#print 5 but the the function does not have a parameter and x is invoking function that has nothing so the automatic response that prints in print for x is non
# 5 x is empty no parameter for name in function

#6
def add(b,c):
    print(b+c)
    return b,c
print(add(1,2) + add(2,3))
#added return to return a array/list/tuples it prints 3 and 5 before unknown error didnt know why tho return got rid of it tho
# a error but print 3 and 5

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#str turns numbers to strings so b="2"c="5"b+c="25"
# na

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#print 100 return 10 b=100 it is not less than 10
# print 100 and return 10?
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# 7 and 14 and 21 3rd problem is using the condition problem getting the answer then adding the two answer for final result/print
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prints 8 3 +5 return value show 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# print 500 300 500 500
#first one is 500 out of function in function 300 outside function 500 500 because of the variable outside the function b they take on the int 500
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# 500 500 300 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500 500 300 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# find the functions invoke and go in order top to bottom 1 3 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1  3 5 10

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
person["pokimon"] = "pikachu"
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)
if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")
my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc



