## Slide 1

CT7201 Python Notebooks and Scripting
Week 1

## Slide 2

What is a computer?
This may seem an obvious question – normally a box, with a keyboard attached, and a screen
Or sometimes a laptop
What may be less obvious is that almost every modern device is a computer – microwaves, televisions, mobile phones, smart watches, games consoles, fridges, washing machines
Often whether or not they are designated as “smart” they have a computer of some sort at their core

## Slide 3

So what
is
a computer?
Generally speaking, we have a “CPU (Central Processing Unit)
We have two kinds of memory
Long term storage or “hard drives”
Short term storage or “RAM (Random Access memory)”
We have some I/O (Input/Output) such as:
Network port (Ethernet or WiFi)
USB (Universal Serial Bus) ports
Monitor ports (DisplayPort, HDMI, DVI (Digital Video Interface), or VGA (Vertical Graphics Array) usually)

## Slide 4

What is Python?
Python is a programming language for Computers
It is a
high-level
,
interpreted
, language
It is named Python as a tribute to the UK comedic duo “Monty Python”, and was initially developed by a dutch developer named “Guido Van-Rossum”, although it has been
open-source
for many years now and has many contributors
It is one of the most popular programming languages around today (by some measures the most popular) and it is by far and away the most common language for Data Science and Artificial Intelligence work

## Slide 5

High level?
Python is a high level language, other high level languages you may have heard of are R, C, C#, C++, Java, Perl..
Low level languages exist also, these are sometimes called “Machine Languages” – they are composed of binary numbers which together form codes that instruct the CPU what to do
Computers
only
run low-level languages
So what use are the high-level languages?
We also have a low-level language program, which can take a high level language program, and translate it into an appropriate low-level language

## Slide 6

Why the split?
A CPU cannot complete complex instructions, it can only complete very simple instructions such as “Load X from memory, add X and Y, increment Y” etc.
It can, however, do billions of these instructions per second
More complex instructions (expressed in high level languages) can be translated into many of these low level instructions
So a computer does not do complex things, it does very very simple things, very very fast
It’s a lot easier to write complex instructions than write a few billion lines of simple maths

## Slide 7

Translation?
So this is where the
interpreted
part comes from
In Python the “
translator
” is an “
interpreter
” because it steps through python code, interpreting each line into machine code one at a time
Other approaches are
compiled
, where all the code is written, saved, and then translated into a final machine-code file as one finalised unit of code
Or
just in time
compilation, where the code is loaded, and compiled into machine code
just
before the CPU needs those instructions

## Slide 8

How does this affect speed?
Usually, compiled languages are fastest due to their low overheads and heavy optimisation of the code being possible – as it doesn’t matter how long the one-time step of compilation takes in this scenario
Just in time compiled languages are usually a little slower, although theoretically there’s no reason they need to be.
Interpreted languages are usually the slowest, as there is significant overhead in the interpretation of the language, and normally they are very high level languages – i.e. their instructions are complex and end up translating into a lot of lower level instructions

## Slide 9

So why Python?
If this is the case, why has Python become so popular for machine learning and data science?
Python can be used interactively – due to its interpreted nature you can type code, see any output, and then type some more code – allowing an interactive coding process which is much more challenging with a just-in-time or compiled language
Python is easy to learn – it may not always seem it if you’re new to it, but compared to other programming languages it has simple syntax and is quite close to English
Python can still achieve speed – by calling compiled pre-written code where performance is important, and offering flexibility
elsewher

## Slide 10

Okay – so how do we use Python?
To code Python we need a python interpreter
And something to write our code in – we could just use notepad
But something like Visual Studio code or Jupyter notebooks give us a nicer environment to code in
It has auto-complete, and syntax highlighting to help us with our coding

## Slide 11

Jupyter Notebooks
Please follow the live coding session to achieve the following:
Get visual studio code working with
Jupyter
notebooks plugin
Code a very first Python program “Hello World”
Use some variables to store things
Create and call some
“Functions”

## Slide 12

What do we learn in those exercises?
Python is
whitespace significant
this means that spaces and tabs in Python can mean something – and must be in the right places
In practice, this mostly only applies to the very first sections of whitespace on each line

## Slide 13

What does it mean?
In most programming languages “
code blocks
” are denoted by brackets
Programmers however still use indentation to represent this visually – it makes debugging and reading code hugely easer
In Python we dispense with the brackets, and make the indentation compulsory
The difference can be seen clearly on the following slide

## Slide 14

Indented vs Unindented

## Slide 15

Variables in Python
A variable can store things for your program to use later
These things stored in memory have a
type
The
type
tells you what you can do with that particular variable
These are some of the most common types:
Integers (whole numbers)
Floats (Floating point numbers, i.e. numbers with a decimal point)
Booleans (True/False values)
Strings (Characters, i.e. words, names, etc)

## Slide 16

Integers
Often referred to as “ints”
These are signed whole numbers (i.e. positive or negative)
In Python integers can store increasing numbers until the computer runs out of memory – in stark contrast to most other languages, where different types of int can store differing values

## Slide 17

Floats
Floating point numbers, i.e. numbers with decimal points in them
e.g. 4.2, 100.23, 0.54
Only approximately accurate! So don’t use these for anything where exact accuracy matters (money etc)

## Slide 18

Strings
Strings store an array of characters (this will make more sense later)
i.e. a name “William” or a word “Hello”
In Python, strings can be defined with either double-quotation marks “ or single quotation marks ‘
If your outer string is written with single quotation marks – it can contain double quotation marks, and vice versa

## Slide 19

Literal strings and newlines
In programming, with strings, everything that text can do has to be represented by characters
Some of these characters are visible, some are not
Generally speaking invisible characters are represented with a “sescape character”, a \ followed by a character that tells python which invisible character you want
i.e. \t is a tab, \n is a newline
An alternative is to use a literal string – these are contained by triple quotation marks (single or double) and pass through everything in them

## Slide 20

F strings
As of python 3.6 we have a handy way to insert other variables into a string to be printed out
If we prepend a ‘f’ to the string (put it on the front) we can then within the string include variables and python expressions within curly braces

## Slide 21

Boolean
Booleans store either “True” or “False”
They are an efficient way to store a value which is true or false, and also represent the type behind the built in Python keywords “True” and “False”

## Slide 22

Variable Naming
Variables need to have a name – so you can access them from within your code
There are a few rules about how they may be named
A variable name may only contain letters (A-Z and a-z), numbers (0-9) and underscores ( _ )
A variable name may not start with a number
Variable names are case sensitive, i.e.
MY_VARIABLE and my_variable are
different
variable names, as are My_variable and my_variablE – and all four are different from each other

## Slide 23

Scope
Scope is linked to variables, a variables scope is the places it exists in
When you create a variable in a function in Python, it exists locally within that function only
When you create it outside of a function it is “global”
So a variable created in a function is available inside that function only – not in the outer scope. A variable created in the global scope can be accessed – with some additional syntax – throughout
the program

## Slide 24

Tutorial
Follow along with the live-coding exercise, setting up Python, and exploring some of the different ways you can code in python
Take your hello world program from before, and change it to read “Hello” and then your name
Now try to change this so that you can build different sentences variables that are set as your
program runs
