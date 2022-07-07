class User:
    def __init__(self):
        self.last_name="Hov"
        self.first_name="Tre"
        self.age=30

print(1)
user_tre = User()
print(user_tre.first_name)

# declare a class and give it name Shoe
class Shoe:		
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True

skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type) # Classic Sk8-Hi
print(dress_shoe.type)	# Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats

class Body:
    def __init__(self):
        self.shirts="blue shirts"
        self.pants="red pants " + str(4)
        self.hat="black"

the_shirts=Body()
print(the_shirts.shirts)
the_pants=Body()
print(the_pants.pants)
the_hat=Body()
print(the_hat.hat)

the_shirts.shirts="red shirts"
print(the_shirts.shirts)

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

class Group:
    def __init__(self,name,food):
        self.name = name
        self.food = food
    def hello(self):
        print(f"hey hows it going {self.name}")

johnny = Group("johnny","hamburga")
johnny.hello()


class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
# Create two shoe instances
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
        
# The skater shoes go on sale by 20% reduced price:
skate_shoe.price = skater_shoe.price * (1 - 0.2)
        
# The dress shoes go on sale by 10% reduction:
dress_shoe.price = dress_shoe.price * (1 - 0.1)
        
# The skater shoes go on sale AGAIN by another 10%:
skate_shoe.price = skater_shoe.price * (1 - 0.1)

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

class Hat:
    def __init__(self,size,smell,color,look):
        self.size = size
        self.smell = smell
        self.color = color
        self.price = price

smell_s = Hat(55,"bad","brown",54)

smell_s.size = smel_s.size * (1 - 0.03)

