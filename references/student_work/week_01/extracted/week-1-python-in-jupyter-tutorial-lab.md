# Notebook Summary



## Markdown Cells

# **Section 1: Getting Started with Jupyter Notebooks**

# About me

I enjoy going to the **gym**, learning **new things**, and spending quality time with my **family**.

# **Section 2: Variables and Data Types**

**Define one variable for each of the following data types: int, float, str, and bool. 
Print each variable and its type using print() and type().**

**Create two integer variables and perform addition, subtraction, multiplication, and division.**

**Create two string variables and demonstrate concatenation.**

**Create two boolean variables and demonstrate logical AND, OR, and NOT operations**

# **Section 3: Data Structures**

**Create a list containing numbers from 1 to 10.    
Add an element to the end of the list and insert an element at the third position.   
Slice the list to get the first 5 elements.**

**Create a tuple with at least four elements and try changing one of them (observe what 
happens, as tuples are immutable). 
Create a dictionary representing a book, including its title, author, publication year, and 
genre. 
Add a new key-value pair representing the number of pages in the book.**

# **Section 4: Functions**

**Write a func on max_of_two that takes two numbers as arguments and returns the larger of 
them.**

**Create a variable outside of a function and try to access it inside the function. 
Create a variable inside a function and try to access it outside the function.**

# **Section 5: Writing Explanatory Text in Jupyter**

**Create a new Markdown cell in your Jupyter Notebook. 
Write a brief paragraph about your favorite data structure (lists, tuples, or dictionaries). Use 
at least two different Markdown formating styles (like bold, italic, or bullet points).**

_i like to ride a bike_ and as well to play football with my **friends**.
> 1. car
> 2. bike
> 3. pasta

**Write the quadratic formula using LaTeX in a Markdown cell.
Include an equation of your choice (it can be from physics, mathematics, etc.) and explain
the equantion your own words.
These exercises should provide a comprehensive hands-on experience with the basics of
Python and Jupyter Notebook. As you work through these exercises, remember that
experimenting and practicing are key to deepening your understanding of programming
concepts.**





## Code Cells

"Dinis Nascimento"

my_int = 25
my_float = 4
my_str = "Dinis Nascimento"
my_bool = "true"

print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_str, type(my_str))
print(my_bool, type(my_bool))

a = 10 
b = 15

print ("addition:", a + b)
print ("subtraction:", a - b) 
print ("division:" , a / b) 
print ("multiplication:", a * b)

a = "dinis"
b = "Nascimento"

print ("concatenation:", a + "" + b)

x = True
y = False

print ("X AND Y:", x and y)
print ("X or Y:", x or y)
print ("not x :", not x)
print ("not Y:", not y)

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.append (11)

numbers.insert (2, 25)

first_five = numbers[:5]

print("Full list after modifications:", numbers)
print ("five first numbers:",first_five)

my_tuple = (10,20,30,40)

print ("original tuple:", my_tuple)

try:
my_tuple[1] = 99
except TypeError as e:
print("Error:", e)

book = {"title" : "Raul forte",  
"author" : "jonh trabuco"  
,"publication year": "2001"  
, "genre" : "fiction"  }

print("Original dictionary:", book)

book["pages"] = 350

print("Updated dictionary:", book)

def max_of_two(a, b):
if a > b:
return a
else:
return b

print("Max of 10 and 20:", max_of_two(10, 20))

def sum_list(numbers):
total = 0
for num in numbers:
total += num
return total


print("Max of 10 and 20:", max_of_two(10, 20))
print("Sum of [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))
