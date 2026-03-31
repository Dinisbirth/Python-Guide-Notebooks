## Slide 1

CT7201 Python Notebooks and Scripting
Week 4

## Slide 2

Multidimensional lists in Python
Lists in python can contain any other valid variable type
Let me reiterate – they can contain
any
other valid variable type – which includes lists, dictionaries, and other collection types

## Slide 3

Multidimensional lists in Python
As you can imagine, this allows you to hold data in a huge variety of ways – out to as many dimensions as the memory in your computer will allow
This isn’t simply limited to lists, dictionaries, tuples, etc can all contain other collections as elements. This lets you build up highly complex representations of data from these types

## Slide 4

Dictionaries in Python
Dictionaries in Python as a type of
Collection
that works differently from a list – they are
mutable
collections of a bunch of values
A dictionary is typed out in python with curly braces: { }
A dictionary contains
Key, Value pairs
. These are elements that consist of an identifier, or “
Key
” and a piece of data or “
value
”.
Mutable = changeable

## Slide 5

Dictionaries in Python
To add an item to a dictionary, you just use a key that doesn’t exist yet, and set it with an “=“ operator. You can also use this approach to update existing entries:

## Slide 6

Dictionaries in Python
You can also use the “del” keyword to remove an element from a dictionary:

## Slide 7

Dictionaries in Python
You can also use the “pop” method, similarly to a list to remove an element from a dictionary:

## Slide 8

Dictionaries in Python
As you can see in the previous slides – if a key is missing from the dictionary – you will get an interpretation error called a “
KeyError
”

## Slide 9

Dictionaries in Python
You can check if a key currently exists in a dictionary, by using the “
in
” keyword

## Slide 10

Dictionaries in Python
Coding like that can be a bit tedious – so Python has our backs here, we can use a “get” method instead, which takes both a key to try and get – and a value to return if the key does not exist:

## Slide 11

Dictionaries in Python
Similarly we have a “
setdefault
” method, which takes both a key to check for, and a value to set that key to if it doesn’t exist

## Slide 12

Dictionaries in Python
In much the same way as lists can contain any valid variable type
Dictionaries can use almost any valid variable type as either a key or a value
So you could have a dictionary that matched up lists received from another class with equivalent lists, in order to populate a user interface – for example
Or you could use a dictionary as a cache, by turning your function arguments into a key, and the outputs of the function as a value – then checking whether the particular combination of arguments is already in the dictionary every time the function is called, and returning cached values if so
Hopefully it is clear that these can be very useful

## Slide 13

A word on performance
Different collection types perform differently – and it depends on the underlying implementation, so their performances may very from Python version to Python version, or programming language to programming language
Generally speaking, lists are slow, but very flexible (they are O(n) which means that the more items are in the list, the longer an operation on the list will take on average
Dictionaries are less flexible in some ways (no ordering, slow at iterating through) but very fast at inserting, deleting, and finding particular items (they are O(1) at these – i.e. no matter how many elements the dictionary has, the speed to do these things remains the same)
Therefore, there are particular things dictionaries are very useful for, and particular things lists are better for. Choosing the right data structures for your algorithm could easily be the difference between days of runtime vs minutes or even seconds – when dealing with very large datasets.
More information on python performance can be found
here

## Slide 14

Other collections in Python
We also mentioned Tuples, and Sets, this morning
A python Tuple is a collection of objects which are
ordered
and
immutable
They are defined as a comma separated list, or a comma separated list within ordinary brackets (parenthesis)
Immutable = Cannot be changed once created

## Slide 15

Other collections in Python
Most of the same functionality exists in tuples as in lists, with the exception of the functionality for changing the collection
You may ask why not just use a list – tuples are more memory efficient, and are more often used implicitly, than explicitly
By which I mean, rather than programmers really using tuples, the python language uses them to make python syntax work

## Slide 16

Other collections in Python
So for example, in a lot of languages, returning multiple values from a function is impossible – in python you just return a comma separated list… which is you guessed it, actually a tuple being returned
Or in a lot of languages, swapping the value of two variables without a third variable is surprisingly tricky – in python it’s easy – because python interprets this using tuples

## Slide 17

Other collections in Python
You may at some point have heard of sets, and set theory – these are statistical concepts – but they also are used in Python! Set theory is where we get
venn
diagrams from:

## Slide 18

Other collections in Python
In Python, a set is an
unordered
, collection with
unique
elements – i.e. elements of a set are not allowed to be duplicated
The set itself can be modified – but items stored within the set
must
be immutable
Sets can be created with the “set” function, to which an
iterable
must be passed
An
iterable
is a collection which can be iterated over

## Slide 19

Other collections in Python
If we pass in multiple identical elements in our tuple – our set will simply strip out duplicates and only store the unique items

## Slide 20

Other collections in Python
You can also declare sets with curly brackets – similarly to dictionaries. But rather than including key, value pairs separated by a colon, you supply an iterable of immutable values
Note how as a result of being
unordered
in the set – the order of the values has changed when output

## Slide 21

Other collections in Python
So when are sets useful?
Basically whenever you want a list of elements that should not be duplicated – which is a scenario you may well come across when processing messy data supplied by third parties.

## Slide 22

Other collections in Python
Sets do have some useful functions, for example the union function which returns a set of the contents of two or more sets – you may also use the operator “|” to achieve this:

## Slide 23

Other collections in Python
We also have an intersection function, which returns a set of all elements which are within two or more sets, you may also use the operator “&” to achieve this:

## Slide 24

Other collections in Python
A difference function, which returns the elements that are in one set, but not one or more other sets, this may also be achieved with the “-” operator:

## Slide 25

Other types and other functions
Information on other types available in python, as well as additional functions available on these described and other undescribed types, are available
here
.
We simply don’t have time to go over every single type, or even every single function on limited types, in this module – and in any case no programmer you will ever find has these things memorised – references such as the python docs or programming books, or the auto-complete in IDE’s, are what we use to look these up
This is why it’s essential that you gain an understanding of programming terminology, common approaches to problems, and get really pro-active about problem solving using documentation to guide you – that is the essence of developing into a great programmer

## Slide 26

Tutorial
Write a function, which will take two
iterables
as parameters, and return as a
list
, all of the elements that are contained in both
iterables
Write some python code, which will store in an appropriate data structure, the (made up) personal details of 5 individuals (first name, last name and age), including at least two that are identical
Then write some further code, which will remove any duplicates from that data structure
If you complete these tasks, proceed to some of the course resources for python exercises such as project
euler
, and start to work on
those exercises
