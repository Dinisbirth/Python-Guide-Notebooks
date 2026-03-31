## Page 1

CT7201
Data Analysis Continued
This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.It makes use of the works of Mateus Machado Luna.

## Page 2

Finding Correlations
●Continuing from where we left off on our machine learning 
project
●As the dataset in this case is not all that large, you can compute 
pearson’s r, or the standard correlation coeffficient between 
every pair of attributes, using the “corr()” methodr=¿

## Page 3

Finding Correlations
r=¿

## Page 4

What does this mean?
r=¿●These measurements are 
correlations against the median 
house value
●The correlation value ranges from -1 
to 1, the closer it is to 1, the 
stronger the positive correlation
●The closer it is to -1, the stronger 
the negative correlation
●At the 0 point, there is no correlation

## Page 5

What does this mean?
r=¿●Watch out, because this measure 
will only catch linear correlations
●i.e. “if X goes up, Y goes up”
●Or “if X goes up, Y goes down”
●Or similar measures
●It will miss “If X goes up then Y 
goes up and then curves back 
down” or anything else non-linear 
or more complex

## Page 6

Scatter Matrix Plots
●Another approach to identify correlations, is to use a scatter 
matrix plot
●This plots every numerical attribute against every other 
numerical attribute
●With 11 numerical attributes, we would get 121 plots, which isn’t 
going to fit well on the page, so we can investigate just the 
attributes which we already know appear to be correlating well 
with median house value

## Page 7

Scatter Matrix Plots

## Page 8

Scatter Matrix Plots

## Page 9

Looking deeper
●The first thing to notice is the diagonal – if pandas plotted each 
variable against itself, you’d end up with a diagonal row of 
straight lines which isn’t all that helpful – so it displays a 
histogram of the attribute instead in those boxes
●Each section can then be analysed to identify how well it 
correlates with median house value
●The clearest correlation (as indicated by our earlier test also) is 
with median income

## Page 10

Looking deeper
●The first thing to notice is the diagonal – if pandas plotted each 
variable against itself, you’d end up with a diagonal row of 
straight lines which isn’t all that helpful – so it displays a 
histogram of the attribute instead in those boxes
●Each section can then be analysed to identify how well it 
correlates with median house value
●The clearest correlation (as indicated by our earlier test also) is 
with median income, so lets plot that

## Page 11

Looking deeper

## Page 12

Looking deeper

## Page 13

Looking deeper
●We can see a few clear trends 
in the data here
●First of all, the clear upward 
trend showing that positive 
correlation we saw – and it’s 
quite strong because the points 
are fairly well aligned rather 
than spread out

## Page 14

Looking deeper
●Secondly, we can see a 
horizontal line at the top, 
representing the price-capping 
we saw before
●Thirdly, and perhaps most 
interestingly, we can see 
several other horizontal lines, 
at around $450k, and $350k 
and $250k

## Page 15

Looking deeper
●We may want to try to 
algorithmically remove these 
quirks, to avoid machine 
learning models trying to learn 
to emulate them
●Particularly the top, very strong 
and obvious line

## Page 16

Feature Engineering
●Finally, before we prepare the data for machine learning we may want 
to consider engineering new features from our existing ones
●This mostly means combining them together in ways that make sense
●For example, the total number of rooms in a district isn’t all that useful, 
if you don’t know how many households there are. What you actually 
want is number of rooms per household.
●Similarly, the total number of bedrooms isn’t that useful by itself, you 
probably want to compare it to overall number of rooms.
●Population per household also seems like it could be interesting

## Page 17

Feature Engineering

## Page 18

Feature Engineering

## Page 19

Looking good!
●The newly created bedrooms per room attribute is well 
correlated with the median house value compared to either 
total number of rooms, or bedrooms.
●The number of rooms per household is more informative,as 
the larger the houses, the more expensive they will clearly 
be

## Page 20

Data Exploration
●This is a fairly swift data exploration step
●In reality, this would merely be the initial step – once we 
had a good feel for the data and had tried some machine 
learning, we would likely revisit this step
●Other attributes may appear more promising, other things 
may suggest themselves on revisiting

## Page 21

Data Cleaning
●We will revert to a clean data set for now, we should be able to do 
this by copying our initial training set
●
●We saw in a previous session, that total_bedrooms has missing 
values which we need to fix, we have three options to deal with this
–Remove the districts with missing data for total bedrooms
–Get rid of the total bedrooms attribute, thus negating the problem that it 
has missing data
–Set the missing values to some imputed value

## Page 22

Data Cleaning
●We do have functions available for all of these options

## Page 23

Data Cleaning
●Another option than doing it manually using pandas 
functions is to use scikit-learns “SimpleImputer” class
●
●This can only be used on numerical attributes, so to use it 
you need a copy of the data without the textual attribute 
(ocean_proximity)

## Page 24

Data Cleaning
●This imputer is now “trained”  and can be used on the 
training set to replace missing values with the calculated 
medians
●
●That returns a raw numpy array (rather than a pandas 
dataframe) so we can load it back into a dataframe by 
doing the following

## Page 25

Tutorial
In your groups
●Try out some of these techniques on your data
●What variables are correlating well with your target value?
●What feature engineering can you do to create more variables that may be more informative?
●How do those correlate?
●Are any of the other visualisations we’ve looked at in the past interesting when linked to those 
data?
●Can you find other ways to impute values that may be more effective than the methods 
demonstrated?
●Remember, even if your eventual task is to train a machine learning algorithm (which it may not 
always be) you will still likely need a good report with some informed science and 
experimentation to inform this process, and allow you to justify it if necessary
