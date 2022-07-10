# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output
#5 is num the variable output has a value bracket the loop will send each number from i in the for loop in a decrementing fasion from 5
#return output will printthe final solution outcome for output andwhat was sent to the bracket
print(countdown(5))

def wow(num):
    bracket=[]
    for i in range(num,-1,-1):
        bracket.append(i)
    return bracket
print(wow(5))
# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list):
    print(list[0])
    return list[1]
#list is the parameter and it is being invoked at the bottom with two arguements in a bracket and its indexes are called on to print 1 and return 2
print(print_and_return([1,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    return list[0] + len(list)
#return the first index 1 plus length of list 5 = 6 is the return given a parameter and invoked with a arguement of a list
print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

#the order of what will be printed or show up in the console is based of what is invoked first it will go throught the array untill finished and the do the other arguement. since the first array goes through for loop and there is a comparison/a invoke that has to do with both.
#5 is taken then 3 and eventually 4 anything number that was higher then 2 in 0index which never changed because numbers that are higher are removed.
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
#the function has two parameters thar are  invoked forst invoke is in a for loop starting at 0 going to 4 and is being takin to the variable output by .append each loop untill finish and then returned the output=[]and is in the console in a list form similar to the next invoked arguements. 