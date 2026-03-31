## Slide 1

CT7201 Python Notebooks and Scripting
Week 2

## Slide 2

Functions
You have seen functions in some of our previous examples
A function is a chunk of code that we can call, potentially supplying some values (arguments) and which can return some values
In python the syntax for defining a function is:
“
pass
” is a keyword in Python,
meaning do nothing. Our
functions here have to have some
code, but it does not need to do
anything.

## Slide 3

Type Annotation
If you wish (and there are reasons you may want to if you start to work on larger programs) you can also annotate python functions with the types for their arguments
This allows your code editor to check that you have passed the correct types, and allows for type linter programs to scan your code ahead of time and warn of any possible type errors
Type annotations are not required however, and code will run perfectly fine without them

## Slide 4

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 5

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 6

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 7

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 8

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 9

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 10

Control Flow
We call a function by using that functions name, followed by a pair of brackets, that contain a list of the required arguments
When we call a function, we say that control has passed to that function
It retains control until it completes, or returns a value

## Slide 11

Operators
Operators are used to perform operations on or with variables
Python has maths operators:
+
-
*
/
%
**
//
Addition
Subtraction
Multiplication
Division
Modulus
Exponentiation
Floor Division (Divide, then round to nearest whole number)

## Slide 12

So we can use Python just like a calculator
By using print, numbers and operators

## Slide 13

Task 1
Using operators, variables and whatever python environment you please
Attempt to solve the following puzzle:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get four numbers. When we sum these numbers, what is the result? Write a python program to help you calculate these.

## Slide 14

You hopefully wrote something like this
We are only using the code we’ve learnt so far (f-strings were mentioned this morning, although they’re not absolutely necessary for this)
We have printed out all of the numbers below 10 divided by 3 and by 5
We can therefore notice the ones that are whole numbers, pick them out, and write another line to add them together

## Slide 15



## Slide 16

And there is!
Rather than typing out the code to do multiple divisions, we can get our program to do something we call a loop

## Slide 17

For loops in Python
A for loop is normally a loop that can, using a variable, count from one number to another, and run some code for each number counted
In python we would use the syntax
Keyword
for
, followed by a variable which will be used to count, followed by the keyword
in
followed by “range(lower-bound, upper-bond) and a colon
After this colon, an indented block with code to be executed through the loop

## Slide 18

For loops
As you can see on the right, a for loop using this syntax can very easily print out numbers 1-9
We can also perform operations with this number

## Slide 19

Like so
As can be seen on the right, we can easily print out the divisions for the number 3, without having to type nearly so many lines
We could also do the same thing for 5 – or we could create a function

## Slide 20

Like so…!
As can be seen below, we have a function with three parameters
And then call it twice, to achieve our goal

## Slide 21

Can we go further?
As you may have guessed, we can.
We do need to encounter another control statement in Python though.
The “if” statement
In Python this is the keyword “
if
” followed by a
condition
, followed by a colon
A condition is something that will evaluate to either “True” or “False” (a
boolean
value)
This is followed, similarly to
for
loops, by an indented block
In this case, the indented block is executed only if the statement evaluates to “True”, it is skipped if the statement evaluates to “False”

## Slide 22

Conditional statements?
We need more operators:
Equal
Not Equal
Greater than
Less than
Greater than or equal to
Less than or equal to
==
!=
>
<
>=
<=
And
Or
Not
“and”
“or”
“not”

## Slide 23

End result...
So here we have a program that will only print out the whole numbers
We are nearly there – can we eliminate the human element necessary to read these numbers and then add them?

## Slide 24

A program that does it all…
This gets us to here...

## Slide 25

A program that does it all…
This gets us to here...
The “
global
” keyword
here allows
us to access a variable at the
script level, from within
a function.

## Slide 26

Tutorial
Using the code given to you and described throughout the lecture, and googling any resources you wish
Expand upon our program to gain the sum of all multiples of 3 or 5 below 1000
Having completed that task successfully, use the same knowledge to attempt the following tasks:
Find the sum of all multiples of 3, 4 or 8 below 100,000
Find the sum of all multiples of 3, 5 or 9 below 100,000

## Slide 27

Tips!
Remember to break the problem down into small parts
Remember to use all of the python coding tools at your disposal
Don’t be afraid to look back through slides for reminders, or use google or internet search – I’m definitely not expecting you to memorise this stuff
Data scientists do not memorise every single possible combination of python commands – nobody does as there are simply too many
You learn the most common ones, the best approaches, and rely on documentation where necessary
So it is not “cheating” to look things up! It is good practice!
