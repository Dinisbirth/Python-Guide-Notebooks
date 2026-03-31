## Slide 1

CT7121 Python Notebooks and Scripting
Week 3

## Slide 2

Collections
What are collections?
A collection variable is a variable at its most general level a variable that can store more than one thing – at the same time
We normally have some way of
indexing
i.e. finding the value we want within the variable – either a number, or sometimes some other identifier

## Slide 3

Collections
Collections are very commonly used across all programming languages.
In Python, there are 4 really common types of Collections that you will come across:
Lists
The simplest type of collection, flexible, can be altered, and ordered.
Tuple
These are collections of data that are ordered but cannot be changed after being declared.
Set
These are collections of data which are unordered and cannot be indexed.
Dictionaries
These are collections of data which are unordered, changeable and indexed via a key.

## Slide 4

Lists
Lists are collections of data that are ordered and can be changed.
In Python, Lists are written with square brackets
You can access individual elements of the collection by referring to the index number.
The index starts from
0.
So to access the 3
rd
item in the list…
And you can also access the list backwards using negative numbers

## Slide 5

Lists – Adding to the list
You can change the variable by setting the index of the list
You can add to the end of the list using the append() method built into the list object.
You can Insert a element to the list using the insert() method and providing an index.

## Slide 6

Lists – Removing from the list
You can remove a specific element from the list using the remove() method.
You can remove the last element in the list using the pop() method.
Pop() will also return the value it removed for you. This means you are able to see and do operations on the element it removed.
Or you can supply an index to pop() and remove a element from the list by index.
E.g. to remove the third item in the list:

## Slide 7

Lists – Index Slicing
You can use index slicing to select multiple elements of the list
To get the first two elements from a list I can use ‘0:2’ as the index:
Starts at index 0 and continues up to but not including index 2
You can leave out the beginning index and it will assume to begin from the start of the list.
It’s the same the other way around, if you leave the end index, it will continue to the end of the list.

## Slide 8

Lists – Other Utilities
You can sort a list alphabetically using the sort() method
You can reverse the list using the reverse() method
Lists do not need to be the same variable type for every element, e.g. you can have strings,
ints
, floats and bools all in the same list!

## Slide 9

Lists – in and not
You can use two operators with list values and string, “in” and “not”
These operators will return True or False

## Slide 10

Strings
We have been using strings a little bit in python since we very first started
But there’s a bit more to them than just using them to store characters, you can also use them to manipulate characters in a lot of different ways

## Slide 11

Sidenote: ASCII and UTF-8
Computers deal with numbers (stored in binary), not letters
So how do we deal with letters? We just use numbers to represent letters
In order to do this the most basic standard is
ASCII
– this is an 8 bit standard, that’s capable of representing all characters in the English alphabet
Nowadays we often use UTF standards instead, which are slightly more complex and can represent all possible characters due to a variable bit length (most common is UTF-8, which is similar to ASCII)
So when we see “c” for example, what is actually stored inside the computer is the number 99. Or when we see a “@” it is the character 64
Mostly this is transparent to the programmer, but it is worth having an understanding of

## Slide 12

Strings – quotation marks
Remember that we can (in Python) use either single or double quotes as we wish to represent a string
This allows us to use single quotes, if we wish our string to contain double quotes – or vice versa.

## Slide 13

Strings – escape characters
What about if we want to use both single and double quotes?
Then we have to delve into “escape characters”
These are special characters that are invisible – thinking back to that ascii table, you’ll remember that there are things included such as 8 being a backspace character. 9 is a horizontal tab, 10 is a linefeed and 13 is a carriage return
These are characters that rather than being printed, tell the program doing the printing to do something to the string

## Slide 14

Strings – escape characters
In Python, the escape character is a backslash
A backslash followed by an “n” will actually print a newline character rather than “\n”, a backslash followed by a “t” will print a tab character
This same syntax can also be used to print quotation marks, or backslashes themselves – so “\”” would print a “, “\’” would print a ‘, and “\\” would print an actual backslash
An alternative for some of this is to use “raw strings”

## Slide 15

Strings – raw strings
In Python, a raw string is a string in which escape characters will not be used
Instead the string will be read in ignoring backslashes (or rather treating them as part of the string)
This is useful if you need to type something like a path, that may have a lot of backspaces in

## Slide 16

Strings – triple quote strings
In Python, a triple quote string is a string that encompasses all the characters within it – newline characters and tabs etc included.
Text within a triple quote string does not need to be indented like the rest of python code
These are sometimes inserted into code as a way to achieve multiline comments

## Slide 17

String indexing
Each letter of a string can be accessed via indexing
Just like a list! In some ways you can think of strings as really being a list of characters.

## Slide 18

String indexing
Just like a list, we can slice in a variety of ways as well

## Slide 19

String indexing
Or use in and not in
As these are returning Booleans, we can also use them in if statements and other conditional logic

## Slide 20

String concatenation
As we have already seen in previous sessions, strings can be concatenated – added together, to combine into one string

## Slide 21

String f strings
But (and again, we’ve already seen this, but to cover it formally) we can use (since python 3.6) f strings to accomplish this easier.

## Slide 22

String functions
Strings also have a few useful tricks up their sleeves – first we’ll take a look at these four methods
upper() – returns a new string that’s all uppercase
lower() – returns a new string that’s all lowercase
isupper
() – returns True if the string is all uppercase
islower
() – returns False if the string is all lowercase

## Slide 23

String functions
Strings also have a few useful tricks up their sleeves – first we’ll take a look at these four methods
upper()
lower()
isupper
()
islower
()

## Slide 24

String functions
There are a whole bunch of other useful functions attached to strings (every string is
typed
as an object, which has these functions written as part of it – more about this when we do object orientation)
In a IDE or editor with auto-complete, you can probably look through these functions, and get an idea for what they do
Otherwise, you want to use this
reference

## Slide 25

Tutorial - Lists
Open Python (in a notebook or on the command line, as you prefer) and complete the following tasks
Create a list of Names and print them out
Remove one of the names from the list and print out the new list
Add two more names and print these out
Bonus:
Print the list of names out in reverse
Bonus2:
Print them from the inside out (i.e. the central list item, then the two outers, then the two outside of those…)

## Slide 26

Tutorial Bonus Challenges
Your starter list is: [5, 3, 9, 12, 14]
Write some code to find and return the largest value in a list
Write some code to find and return the lowest value in a list
Write some python code that will take this list and create a new list, with the same values organised highest to lowest – you may use any built in python functionality to achieve this
Your starter string is “The quick brown fox jumps over the lazy dog!”
Write some python code that will reverse this string
Write some python code that will extract the second and third words from this string
Write some python code that will leave the words in the same order, but reverse the characters in each word
I.e. output should be: “
ehT
kciuq
nworb
xof
spmuj
revo
eht
yzal
!god”
