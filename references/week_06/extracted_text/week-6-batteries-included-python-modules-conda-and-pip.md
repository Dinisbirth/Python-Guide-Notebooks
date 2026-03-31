## Slide 1

CT7201 Python Notebooks and Scripting
Week 6

## Slide 2

Batteries included!
Python has what is called a “Batteries included” philosophy
This means that it’s standard library is very comprehensive – the idea is that python can be a useful programming language even without the addition of further librarys

## Slide 3

Libraries?
Yes, but not like your standard library
In coding terms a library is a collection of code, written by someone else, that does something useful, that can be called from your code
A languages “standard” library, is the library that is included with the language itself, i.e. the selection of functions that are part of the language
Other libraries come from third parties

## Slide 4

Okay, so what does it include?
We’re going to do an overview of a whole bunch of potentially useful functions today, that you can use within your code.
You shouldn’t view this as a lesson to memorise, but perhaps a slide deck that you can save, or even print out, and refer too
This isn’t an exhaustive list of all included functions, but merely the ones I’ve found most useful.

## Slide 5

abs()
Stands for “absolute value” i.e. the magnitude of the different from zero, regardless of whether that is positive or negative.
Examples:

## Slide 6

all() any()
All and any, are very similar functions, and both accept an iterable as a parameter
All will return true if
all
elements within the iterable are True (or if the iterable is empty)
Any will return true if
any
elements within the iterable are True, or False if the iterable is empty.

## Slide 7

help()
The help function displays help associated with the object that is passed into it – i.e. you can ask python to help you understand a function or object and it will try to do so


## Slide 8

len()
This function returns the number of items in an object – i.e. the length of a string, or the number of items in a list – you’ll find yourself using this quite often, particularly when using loops etc.

## Slide 9

max() and min()
We’ve seen these before, max will
return the largest element of an
iterable, or the largest of the
arguments it’s given. Min will do
similar, except returning the
smallest element of an iterable or
the smallest of the arguments it’s
given.

## Slide 10

reversed(), sorted(),
Reversed returns a reversed iterator of the iterator supplied. Sorted returns a sorted list of the iterator supplied.

## Slide 11

zip()
Zip returns an iterator that combines two or more iterators together, alternately, using tuplies – it’s probably easier to visualise than to explain.

## Slide 12

Usefulness of Zip
Zip is used a lot to turn situations that would otherwise require multiple loops, or numerical indices, into a single loop, as in the demo.
This both avoids multiple loops (which are slow in python) and makes the code clearer, so long as you understand what zip does.

## Slide 13

Included Python modules
As well as the built in functions, we can use some modules that
Python has included by default
We briefly demonstrated this with a import statement
This import statement is one way to bring in a third-party module to
python, so for example python includes a math library – we can use
import math to access functionality

## Slide 14

How do I know what modules to use?
We can get a list of the currently available modules, by calling help(‘modules’):

## Slide 15

How many modules are available?
There is a list of built in default modules available
here
Which demonstrates how much functionality is included in python by default – remember as well as this there are thousands of third-party packages – this is just what python includes with the standard installation.

## Slide 16

Installing Packages
Okay – say you want to use one of those third-party packages
Perhaps a tool to create graphs, like matplotlib, or a tool to do some automated data-profiling, like pandas-profiling, or a tool for loading and handling data, like pandas?
You can install these using conda, or pip.

## Slide 17

A note on environments
By default python is “system-wide” this means that if you install packages, they are installed for every python program on your system.
This may not seem like an issue, but different versions of libraries have different compatibilities, and require specific other versions of libraries – over time you can end up entirely breaking your system-wide python and making it unusable.

## Slide 18

So what do we do?
This is why we’ve been using conda – it is one available tool, popular among data scientists, for managing python environments.
Each conda environment has its own copy of python, and its own set of python libraries installed, that are only available when a python program is run from that environment.
My advice would be
never
to install anything in
base
always keep that default – and create new environments for every project you do – that should very much minimise any library compatibility issues you encounter.

## Slide 19

Creating a Conda Environment
You’ve already seen me do this – way back in session 1.
The command is:
conda create –n MY_NEW_ENVIRONMENT_NAME
Then to install modules into this – we can use the command:
conda install PACKAGE_NAME
Conda will attempt to find the package in its repositories to download and install it for you. We’ve all had a go at this already.

## Slide 20

What if the module isn’t in conda?
Conda doesn’t have every single module unfortunately.
A lot of the time, packages that aren’t in conda, are available through conda-forge, which is another repository that users can place packages in for use.
Sometimes when even that fails – you need to resort to using pip – pip is the standard python package manager, and has pretty much every python package available – but it doesn’t always play perfectly with conda

## Slide 21

Using Pip
Pip can be used to install a package or packages with the command:
pip install PACKAGE_NAME, PACKAGE_NAME2, …
As it doesn’t always work perfectly with conda’s installer, my advice is to always install everything you can in an environment using conda, and then add any packages not available using pip. Once you’ve installed packages using pip in a conda environment, try to steer clear of using conda any further or you could break the environment.

## Slide 22

User Guides
The conda user guide is available
here
And the pip user guide is available
here
Whilst I’m at it the git documentation is available
here
Unfortunately – there are a lot of tools that professional programmers and data scientists utilise
You will start to get good at learning tools quickly, because you’ll have lots of practice
As the tools tend to change relatively frequently – in five years time the standard tools may well be different…

## Slide 23

Tutorial
Use the zip function, to loop through 4 lists simultaneously.
Try out each of the other functions listed in the slides.
Investigate the python modules available, pick out one that does something interesting (suggestions: math, multiprocessing, pickle) and based purely on the documentation available, try to use it for its intended purpose
Install and utilise a module from conda – maybe try out fuzzywuzzy from conda-forge – this library lets you compare strings in various ways and get a numerical estimate to how similar they are
Install and utilise a module from pip – maybe try out handcalcs? That lets you render your python maths in a jupyter notebook with real maths notation.
