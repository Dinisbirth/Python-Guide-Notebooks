## Slide 1

C7201
Data Analysis Basics

## Slide 2

In this session
We’re going to take a second look at analysing a dataset
We’re going to be looking at this using a housing dataset, with the idea of predicting house prices

## Slide 3

Taking an initial look at our
dataset
We can start by using the .head() function to take a look at the data – simple, but it’s usually a sensible first step in any data analysis.

## Slide 4

Taking an initial look at our
dataset
It also makes sense to use the basic .info() function

## Slide 5

What can we see from this?
Each row appears to represent one district
There are 10 total attributes
There are 20640 total rows of data
This dataset is a magical unicorn of a dataset, with almost no missing values
The total_bedrooms feature is the only feature with some missing information
Most features are numerical
ocean_proximity is the only non-numerical feature

## Slide 6

Taking an initial look at our
dataset
One final function which will give us some basic info on the dataset is the “describe()” function – running that gives us this output:

## Slide 7

Taking an initial look at our
dataset
This gives us an idea of some of the rough statistics around our data. We basically have the count, mean, std, min, 25, 50 and 75
percentiles
, as well as the max value for each feature.

## Slide 8

Taking an initial look at our
dataset
This gives us an idea of some of the rough statistics around our data. We basically have the count, mean, std, min, 25, 50 and 75
percentiles
, as well as the max value for each feature.
Percentiles
give us the number of values that a given percentage of observations fall below in a group of observations. I.e. in this example, 25% of districts have a housing_median_age less than 18, and 50% have housing_median_age less than 29

## Slide 9

Lets have a look at
ocean_proximity
As it seems like a potential issue that’s going to need solving, lets have an initial look at ocean_proximity.

## Slide 10

Lets have a look at
ocean_proximity
As it seems like a potential issue that’s going to need solving, lets have an initial look at ocean_proximity
This should be pretty easy to solve, it’s just a categorised variable, with 5 categories available
We will likely need this to be numerical, to allow for us to use our machine learning models
We can solve this with something like
one-hot-encoding

## Slide 11

Starting to plot stuff!
This visualisation gives us a bunch of information
The median income doesn’t look like it’s in USD for starters

## Slide 12

Starting to plot stuff!
This is because it’s been scaled to 0.5 – 15 (actually 0.4999-15.0001) and the numbers represent tens of thousands of dollars – i.e. a number 3 represents $30k

## Slide 13

Starting to plot stuff!
We can also see that housing age, and median house value are capped
The median house value is our target (what we’re going to try to predict with our regression) so may actually be an issue
The likelihood is that our models will never or rarely predict prices above 500k, certainly their predictions above that number are unlikely to be reliable
Whether that’s an issue or not, depends on the project – so in a real scenario would need to be checked

## Slide 14

Starting to plot stuff!
Finally, we can see that all of the attributes are scaled differently – something we will need to address with normalisation
And the features are tail-heavy – they have more values to the right of the median than to the left – this may affect the performance of some machine learning models

## Slide 15

Creating a Test Set
The next step is to start modifying our data set, ready for machine learning, and plotting further information.
Before we do that, we should split out a test set – you need to do it now before you look too much more at the data, or you’ll be in danger of introducing
bias
into your model, in this case
data-snooping bias
.

## Slide 16

Okay so lets do that
Creating a test set naively involves just taking roughly 20% of our data, and setting it aside.
We can’t assume that the data is shuffled (it may be organised in some way) so we need to select a random 20% from our data in order to avoid inadvertently having either a biased test set – or even a test set which our models have no chance of working with, as we’ve removed an entire category of data from the training set.

## Slide 17

So lets write a function

## Slide 18

And contin.. Nope.
This works – but it has issues.
If we run the program again, we will get a different test/train set, and we may need to run this multiple times during our project
Over time, our machine learning model may even get to see the whole dataset, exactly what we’re trying to avoid

## Slide 19

The simplest solution
Is to simply set the random number seed:

## Slide 20

The simplest solution
This gives us the same result, provided the dataset is always identical. If we modify that dataset at all (add more data) we would have issues again.

## Slide 21

Tutorial
Within your groups, start to apply some of these techniques to your datasets
What insights can you glean from stats and information? Make notes of these to demonstrate this
What visualisations would help you to identify biases and errors in the data, as well as ongoing trends? There’s a good blog post here:
http://www.biosci.global/customer-stories-en/data-visualization-cheat-sheet/
which may help you to decide on some visualisations to try out
What cleaning / tidying of your data is likely to be necessary? Will you need to encode any variables? Have a think on this.
