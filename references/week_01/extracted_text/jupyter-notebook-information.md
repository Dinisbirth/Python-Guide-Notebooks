# Notebook Summary



## Markdown Cells

# 1. Variables

# 2. Integer, Float, String, Boolean

# 3. Collection: List, Set, Tuple

# 4. Dictionary

# 5. Functions : Arguments , Return.



## Code Cells

#Variable = a reusable container for storing a value 
#           a variable behaves as if it were the value it contains 
#age = 25
#print(age)
#print(f"you are {age} years old") # most common way of do it 
#print("you are ",age, "years old")

# INTEGER #   never is "2.5 or 2.1" numeros que sao inteiros sem virgulas 

#age = 25    #never is "2.5 or 2.1" 
#players = 2   
#quantity = 3
#(f"I'm {age} years old, i have {players} proffisional players and we have {quantity} leagues")

# FLOAT # number that have decimal number # sao valoores com virlgulas

#gps = 3.2
#distance = 2.5
#price = 5.66
#print(f"The version {gps} of the gps, we have {distance} to make and it will coost us {price} £")

# STRING #series of text # coisas que sao iqueas a uma messagem or text 

#name = "Dinis"
#food = "pizza"
#animal = "lion"

#print(f"My name is {name} my favorite food is {food} and my favorite animal is {animal}")

# BOOLEAN #it's true or false # so pode ser duas respostas 

#online = True
#for_sale = False 
#running = True
#print(f"Are you online? {online}, Are you for sale? {for_sale}, is this program still running? {running}")

#if running:
#print("The game is still on")
#else:
#print("the game is over")

# COLLECTION : single "variable" used to store multiple values:
# LIST = [] ordered and changeble. Duplicates ok.

fruits =["apple","orange","banana", "coconut"]
# print(dir(fruits)) #atributes of different methods that we can use in the collection 
#print(fruits) #discription of each fuctions and atributes
# print(len(fruits)) #para ver quantos elementos estao na lista
# print( "apple" in fruits) #find if the item is in the list

#fruits[0] = "pineapple" # we can change names or items iside of the list
#print(fruits[0])
#print(fruits[:4])
#fruits.append("pineapple") # to add element to the end of the list.
#fruits.remove("apple") # to remove something from the list
#fruits.insert(0,"pineapple") #insert in the beguining 
#fruits.sort() # order alfabetica
#fruits.reverse() #reverse based on the order that we put in beguining
#fruits.clear() #deletes all the items from the list
# print(fruits.index("banana")) # gives the number of the item situated in the list (would be number 3)
#for fruit in fruits:
#print(fruits)

# SET = {} unordered and immutable,but add/Remove ok. No duplicates.

#fruits ={"apple","orange","banana", "coconut"}
#print(fruits)


# TUPLE = () ordered and unchangeable. Duplicates ok. Faster.
#fruits = ("apple","orange","banana", "coconut")
#print(fruits)

# DICTIONARY = a collection of {key:value} pairs.
#              ordered and changeable. No duplicates.
#capitals = {"Portugal": "Lisbon",
"England": "London",
"France": "Paris",
"Spain" : "Madrid"}

#print(capitals.get("Spain")) #to have a specific capital stating the country

# capitals.update({"germany": "Berlin"}) # to add other country and capital to the dictionary or change 
# capitals.pop ("spain") # removes the key
# keys = capitals.keys() # will return all the kys method in our dictionary
# keys = capitals.keys() # to get all the kys in a format of a list 
# for key in capitals.keys(): 

# values = capitals.values() # to get all the value in a format of a list
#for value in capitals.values():

# items = capitals.items() #to add together the key : value in a list way 
# for key, value in capitals.items():
# print(f"{key}:{value}")

# FUCTION = a block of reusable code
#           place() after the function name to invoke it 
# def happy_birthday(): # o define a fuction with one unique name
# print("happy birthay to you!") 
#happy_birthday() # this is to call the fuction 

# Arguments 
# happy_birthday("bro") # any data that you put on the middle is none as arguments you can send a values or variable direct to a functions
#def happy_birthday(name, age): # you need to asign a name to data on the fuction, temporary data in the fuction "name" 
#  print(f"happy birthay to {name}!")
#   print(f"you are {age} years old")
#happy_birthday("bro", 21) # we have 2 arguments here so on the fuction we need to call for 2 to match the number of arguments  
#happy_birthday("Dinis", 25) 
#happy_birthday("Hasini", 30)

# New function

#def display_invoice(username, amount, due_date):
#   print(f"Hello {username}")
#  print( f"The Amount that you need to pay is {amount}£ and the Date is {due_date}")
#display_invoice("Dinis", 2.33, "13/10/2025")

# RETURN = Statemnet used to end a fuction
#          and send a result back to the caller, its a automation way to make the fuction give us a return value, and sorted it on the function variable
#exercise 1
#def add(x, y):
#  z = x + y
#   return z
#def subtract(x, y):
#  z = x - y
#   return z
#def multiple(x, y):
#   z = x * y
#    return z
#def divide(x, y):
#    z = x / y
#    return z
#print(add(1,2))
#print(subtract(1,2))
#print(multiple(1,2))
#print(divide(1,2))

# exercise 2 
# fuction for name and surname with letra maiuscula no inicio 
# def create_name(first, last):
#    first = first.capitalize()
#    last = last.capitalize()
#   return first + " " + last
#full_name = create_name("dinis","nascimento")

#print(full_name)

name = "dinis"
print(name)
