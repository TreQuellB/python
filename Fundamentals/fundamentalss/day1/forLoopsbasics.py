#1 Basic - Print all integers from 0 to 150.
#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for i in range(0,151 ):
    print(i)

for i in range(5,1005,5):
    print(i)

for i in range(1,101):
    if(i%10==0):
        print("Coding Dojo")
    elif(i%5==0):
        print("Coding")
    else:
        print(i)

y=0
for i in range(1,500001,2):
    # if(i%2!=0):
        y+=i
        # print(i)
print(y)


for i in range(2018,0,-4):
    print(i)


lowNum =2
highNum =9
mult =3
for i in range(lowNum,highNum+1):
    if(i%mult==0):
        print(i)
# trying to print 3 6 and 9  i=2 % mult=3 and it increases to 9 but does not print 9 so i add 1 to highnum and it becomes 10 which means i can print 9.