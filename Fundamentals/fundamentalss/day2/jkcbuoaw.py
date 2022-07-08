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
