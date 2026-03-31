## Slide 1

CT7201 Python Notebooks and Scripting
Week 5

## Slide 2

Simple input in Python
If we want to get some input from the user whilst our code is running, we can use the “input” function –
On the command line this pauses our program, and requests some input from the user
Within Jupyter this pops up a input box – and pauses execution until we’ve typed in some input and pressed enter

## Slide 3

While loops
We’ve already seen “for” loops in Python, another kind of loop we can use is a “while” loop – this is a loop that continues to loop the whole time a condition is true
Be wary using this – it’s possible to lock python into an endless loop if you accidentally use a condition that will never be True, which will lock it up until you restart forcibly

## Slide 4

Combining while and input
There are two reasons we might want to combine while loops and input
In order to include input validation – i.e. to check that the user has input something close to what we want
In order to collect multiple inputs

## Slide 5

Input Validation
We can initially get an input from a user, then include a while statement that checks whether the input is valid
If the input isn’t valid, it will continually ask for new inputs, until a valid input is obtained

## Slide 6

Multiple Inputs

## Slide 7

Object Oriented Programming
So far, we’ve been doing what could be referred to as “procedure oriented” programming, or as is more commonly said “procedural” programming.
This means we’re organising our programming in terms of execution running from top to bottom, and functions that run within that.
This approach to programming can be used for almost anything – but when you start to work with larger and larger programs you’ll start to get something we refer to as “spaghetti code”.

## Slide 8

So how do we prevent spaghettification?
We start to think in terms of “objects”!
Object oriented code means that we wrap up bits of our program into combinations of data and functionality.
We say “This data, is linked with these functions, and therefore we can link them together so that we can treat them as one
object
.
And we’ve used this approach loads already – because
everything
in python is an object – even integers are actually a combination of some data (the number the integer stores) and some functions that can work with that data.
Strings are objects, that’s how we get all of our string functions, and lists are objects… everything is an object.

## Slide 9

Okay…
We can create our own objects, which gives us “parcels” of data and functionality that we can pass around as needed.
The simplest possible class looks like this:

## Slide 10

Classes
When we create a class, we are defining something that an object in python
can
be, rather than creating a copy of it. We have to later create a copy of it (an
instance
) and we can have multiple instances of each class, with their own distinct variables (or
state
).
But that class can’t do very much.. (anything).
If we want it to do stuff, we have to add some functions to it
The first thing we’re going to add is an __init__ function

## Slide 11

A quick word about underscores
In most other languages, methods (functions within a class) and fields (variables within a class), will be able to be private, protected, or public
In these languages, this controls whether the methods and fields are available from outside the class itself or not – contrary to what you may expect, the normal is that they are not accessible from outside the class, and that you have a strict defined interface of public elements that allow interaction with the class.

## Slide 12

Enter.. Python
In Python, we don’t have any controls like this – effectively everything is public – everything is available from outside the class. We do have a convention though, which is used throughout python.
This is that methods or fields which are surrounded by a single underscore, are
not
intended for use outside of the class
Methods and fields which are surrounded by double underscores are
really not
intended for use outside of the class
But anything is still fair game in the interests of being pythonic (simple, and sensible).

## Slide 13

So, the __init__ function
Is not intended for access outside the class, and is automatically run whenever we create a new instance of the class.
It is intended for setup – so for example if your class was going to manage access to a database it may setup the connection, or if your class is going to manage access to a file, it will open the file up ready

## Slide 14

The init method

## Slide 15

What’s the self parameter?
It’s a parameter which every method inside of a class in python must have – it refers to the current instance of the class
We can create and set variables on our class instance, by creating them on the self object, as you can see in that example with .name and .age
We can also create variables in a different way as demonstrated in the next slide.

## Slide 16

Class Variables
Class variables can be declared like this – within the class body.
These variables belong to the class – rather than to any particular instance of the class, and are accessible from every instance with the same value.
They are accessed using the class name.
In other languages – these are roughly equivalent to “static” variables.

## Slide 17

Tutorial
Try to re-implement your tutorial from last week (a solution to store information about a series of individuals), using classes to store that information, and using a list to contain those classes
Bonus:
See if you can expand this small program, to allow the user to add, or remove people, print out a list of people, and exit when the user decides too
