"""
Data types
boolean string numbers undefined null JS
"""
"""
PY data types
directly name variable no let var conste
standard is first_name = then set value
boolean numbers strings none
"""
flag =True
flag2 =False#first letter upper case
grade = 9.45#decimal
age = 20#integer
first_name = "alex"
last_name= 'will'
#console.log (variable name)JS
print(flag)
print(grade)
#use terminal to execute
#windows user python name of folder and file you are in
print(last_name + "age")
print(last_name +" " + str(age))#age has a value of int 20 which will be printed as a string so it can print
print(f"hello there my name is{first_name} {last_name}. And i am {age}years old")
#when a function dosent get a value i t will print none
print(type(age))
#prints what the value is in the variable age holds a integer
print(type(flag))
print(type(first_name))#string
print(int(grade))#float is now a number
print(int(grade),grade)#changing floats to numbers and then back to float
grade = int(grade)#float into number
print(len(first_name))#give a number how ever many letters in this case
print(len(first_name),len(last_name))
#COMPOSITE TYPE arrays are list not called array in python
"""

"""
grades=[1,23,3,4]
print(grades)#list  prints
print(len(grades))#length of list
print(grades[0])#print the index in the list
#ADD to the list
grades.append(10)
print(grades)#will print list along with 10 added to end
grades_copy = grades#this is a reference becomes grades list
grades_copy = grades[:]#will copy the list grades if original grades change the grades_copy will not
#object in  JS are dictionaries in python
student ={
    "first_name":"Alex",
    "last_name":"hope",
    "age":23,
    "passed":True
}
print(student["first_name"])
l_n ="last_name"
print(student[l_n])
student["people"]="alot"#will add to list dictionary end of list
print(student)
#TUPLE LIST IMMUTABLE YOU CAN NOT MODIFY THE LIST ONCE SET A VALUE
course = ("Python","4 weeks","spencer Raunch")
print(course)
course =("pablo")#will not be added to list
course[0]="web fundamentals"
print(course[0])
# .append will not work
#CONDITIONALS STATEMENTS IF ELIF ELSE <>=<=> and or!= !
num=20 
if num> 15:
    print("f{num}is  15.")#tab
    print("something")
elif num ==15:
    print(f"{num}is exactly 15")
else:
    print(f"{num}is lesser or equal than 15")
print("this will always print ")
#order of executions is () */% + - not < > <= >= == and += -= or =
#LOOPS, FUNCTIONS, DEBUGGING WITH PRINT
for i in range(5):
    print(i)#0 -4 is what will print
for i in range(0,5):
    print(i)
    for i in range(0,100,3):#multiples of three counting from 0 going to 100 incrementing by 3
        print(i)
for i in range(99,0,-3):#decreasing from 99 by three going to 0
    print(i)
for i in range(0,100):
    if i ==46:
        continue#will continue after looping to 46 but if loop is printing you will not see 46 in terminal
    if i ==50:
        break#when loop hits 50 will break out of loop 
    print(i)
stuff=["milk","ice cream","chicken"]
for i in range(len(stuff)):
    print(f"({i})stuff at {stuff[i]}")#will print loop number then target the variable at its value in loop in order
list_num =1
for stuffs in stuff:
    print(f"{list_num}){stuff}")#listnum number value is printed each loop the indecies in stuff is printed all along with the string
    list_num+=1#adds one to listnum everytime it loops
#indexes are indecies plural of index is indecies
student ={
    "name":"awsome guy",
    "dbz":"Ubb"
}
for key in student:
    print(f"{key}yeah thats right{student[key]}")#how to do string and add the parameter/variable in the arguement/value to target them or a function that can target them key is the first thing in a dict
    
for apple in student:
    print(f"{apple} :{student[apple]}")
if "name" in student:
    print("student has a name")
else:
    print("who")

#WHILE LOOPS
num=1
while num <10:
    print(num)
    num+=1
#a while loop is for if you dont know how long it will run
#FUNCTIONS
def add(num1,num2):
    x = num1 +num2#
    print(x)#will give 5
    return x
add(2,3)#invoke gave arguements no print nothing will happen
print(add(2,3))#will be 5
#return is what you want the function to replace its self with when done
#so you can print before return and get solution and return the solution return x with the variable that would have a value that has changed or not changed but the main thing you have to do is invoke the the function that in this casee has two arguements and aparameter that is in the function there can be parameter with out a arguement and just invoke function
#you have to put return at the end of function or everything below it will not be valid return is saying im done
def add_three(num1,num2=3):#gave num2 its arguement already
    return num1 + num2
print(add_three(5))#num1 has its arguement 3 + 5 =8
print(add_three(1,8))#putting a number here at num2 will over right it
print(add_three(num2=8,num1=5))
#DEBUGGING
def multiply(num_list,num):
    for i in range(len(num_list)): #range length of numlist is 5
        x=num_list[i]#x becomes numlist 0 -4printed going to 5
        x *= num#0 x5 0
        num_list[i] = x
        print(num_list)
    return num_list
a=[2,4,10,16]#going through the list returning the number after multiplying it by 5 and moving on to the next number and multiply it and return it it to terminal
b=multiply(a,10)
print(b)
