# Notebook Summary



## Markdown Cells

# Exercises Week 2

**If we list all the natural numbers below 10 that are multiples of 3 or 5, we get four numbers. When we sum these numbers, what is the result? Write a python program to help you calculate these.**

**Using the code given to you and described throughout the lecture, and googling any resources you wish
Expand upon our program to gain the sum of all multiples of 3 or 5 below 1000
Having completed that task successfully, use the same knowledge to attempt the following tasks:
Find the sum of all multiples of 3, 4 or 8 below 100,000
Find the sum of all multiples of 3, 5 or 9 below 100,000**



## Code Cells

natural_number = list(range(1,11))
print(natural_number)

def sum_of_multiple(x):
total = 0
for n in range(1, x):
if n % 3 == 0 or n % 5 == 0:
total += n
return total

print(sum_of_multiple(10))

def sum_of_multiples(x):
total = 0
for n in range(1, x):            # use x here instead of limit
if n % 3 == 0 or n % 5 == 0:
total += n
return total

print(sum_of_multiples(10))

def sum_of_multiply ():
total=0
for i in range(0,10):
if i%3 ==0 or i%5 ==0:
total = total + i
return total


print ("sum_of_multiply:",sum_of_multiply())

def sum_multiples(x,y,z):
total = 0
for n in range(1,x):
if (n % 3 == 0 or n % 4 == 0 or n % 8 == 0) or (n % 3 == 0 or n % 5 == 0 or n % 9 == 0):
total += n
return total
print("sum_multiples :",sum_multiples(1000000,[3,4,8]))
print("sum_multiples :",sum_multiples(1000000,[3,5,9]))

def sum_multiples(y):
total = 0
for n in range(1, y):
if n % 3 == 0 or n % 5 == 0 or n % 9 == 0:
total += n
return total 

print("sum_multiples :",sum_multiples(1000000))

students = {
"studens_name":("dinis",
"Maria",  
"Tiago"),  
"student_id":(10,   
32,    
40),  
"module":"abc"
}
print(students)



def multiply(a,b):
c=a*b
print(c)
return c
multiply(a,b)
result = multiply 


def multiply(a,b):
c=a*b
print(c)
multiply(3,4)

def multiply(a,b):
c=a*b
print(c)
return c
print(a)
print(b)
