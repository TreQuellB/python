# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello Tre! ", 3  )	# with a comma
print("Hello Tre! " + 2 )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello" , 3  )	# with a comma
print("Hello"+ 42  )	# with a +	-- this one should give us an error! 
print("Hello"+ str(42)  )	# with a +
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2) ) # with .format() 
print( f"i love to eat sushi and pizza" ) # with an f string
