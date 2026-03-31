## Slide 1

CT7201
Python Notebooks and Scripting
This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.
It makes use of the works of Mateus Machado Luna.

## Slide 2

In this session
Handling Categorical attributes
Ordinal encoder
One-Hot encoder
Embeddings
Transformer Classes
Feature Scaling
Pipelines

## Slide 3

Handling Categorical Attributes
In the dataset used,
ocean_proximity
attribute is categorical.
For the purpose of analysis, you can code categories to a range of possible values, representing particular categories.

## Slide 4

Handling Categorical Attributes
We can therefore use the “
OrdinalEncoder
” class in scikit-learn which will give is an encoding of these categories into numbers.
Can anyone remember why we wouldn’t want to use this encoding?

## Slide 5

Handling Categorical Attributes
A machine learning model will make incorrect assumptions about the categories, based on the numbers
i.e. that category 0 and 4 are more distinct than 0 and 1
This is not necessarily true, in fact if we bring up the categories as in the code below, we can see that 0 and 4 are probably a lot more related than 0 and 1.

## Slide 6

The days are labeled in the order of their appearance in the data.
The major problems here are:-
Natural ordering is lost
Common relationships between categories are not captured. (For example, Saturday and Sunday together make a weekend and hence should be closer to each other)

## Slide 7

One-Hot Encoding
A common solution you’ve seen before is to use one-hot encoding, i.e. a set of binary (0, 1) attributes representing each category separately
Scikit Learn has a one hot encoder class, which makes this easy

## Slide 8

Memory Efficiency
We don’t spend a lot of time worrying about memory efficiency in python – generally speaking the python way ™ is to assume that it’s a lot cheaper to add another stick of memory than to pay a programmer to spend a long time working around memory
However, it’s clear that this approach has the potential to waste a lot of memory, particularly with attributes that have many categories, storing a lot of zeros
The output from this function, is actually a SciPy “sparse matrix” which means that it only really stores the non-zero elements, and assumes everything else is a zero
If you want to use it in a way which isn’t supported by this datatype, you may need to call .
toarray
() which will give you a standard
numpy
array – at the expense of using a lot more memory
Hence the python text about sparse compression, and the
toarray
in the display of the encoding, on the previous slide

## Slide 9

Embeddings
When we’re using deep learning, we can use an alternate approach called Embedding.
This allows us to map our categories onto a feature space, which we then use to represent the similarities between them.
An embedding is a vector representation of a categorical variable.

## Slide 10

Embeddings
This is may be not the ideal embedding for the given categories, but you can get the idea from the figure.

## Slide 11

Transformer Classes
Transformer classes in Python can be used to clean, reduce, expand or generate features.
We can use the Scikit-learn API to develop our own transformer classes
Scikit-learn relies on python duck-typing rather than inheritance, so all we need to do is create a class and implement three methods
Fit() → self : learns parameters from a training set
transform() : transform data
fit_transform
() : Fit to data, then transform it.

## Slide 12

Transformer Classes
The last method we can get for free by adding the
TransformerMixin
class as a base class – this basically just runs fit and then transform. We can also add a
BaseEstimator
base class, that gives us two extra methods
get_params
()
set_params
()
These are useful for hyper-parameter tuning automatically
They just return parameters and their default values, and the second one allows parameters to be set via a dictionary.

## Slide 13

Example Class
This class adds the combined attributes that we set up earlier, with general python code
In this example, we have one hyper-parameter that lets us torn on and off whether we will add the bedrooms per room value – defaulting to true
Generally speaking any data prep you’re not totally confident of should be gated by a parameter like this – it allows for easy experimentation

## Slide 14

Feature Scaling
Most machine learning models don’t perform well when all the numerical attributes are at dramatically different scales
i.e. in our data, number of rooms ranges from 6 to 39,320 whereas incomes because of how it’s scaled, runs from 0 to 15
Two common ways to get attributes into the same scale are:
Min-max scaling
Standardisation
It is worth noting that it’s not normally necessary to scale your target values, only your training data

## Slide 15

Min-max Scaling
Min-max scaling (often called normalisation) is the simplest, values are scaled so they are all in the range 0-1
We do this by subtracting the minimum value, and dividing by the max minus the min. Scikit-learn provides a transformer class called “MinMaxScaler” for this purpose, with a “feature_range” hyper parameter that lets you set the range, if you want to

## Slide 16

Standardisation
Standardisation (often called standardization, because American
english
is insidious) is slightly different.
In standardisation, the mean is subtracted, then we divide by the standard deviation
This means that the result will have unit variance.
Unlike min-max, standardisation doesn’t lock a range, which may be a problem for algorithms which expect a specific range, however it’s less affected by outlier values.
A transformer class called “
StandardScaler
” is available in scikit-learn for standardisation.

## Slide 17

Transformation Pipelines
As should be becoming clear, there are lots of data transformation steps that you may be taking when implementing.
This is a small example, but in a real-world task there may be many more you want to do.
Scikit learn provides us with a handy “pipeline” class which can help with these sequences.

## Slide 18

Transformation Pipeline Example
The “Pipeline” constructor takes a list of name/estimator pairs (as tuples) which together define a sequence of transformations
All but the last element must be transformer classes (The final estimator only needs to implement fit.)
When you call the pipelines fit function, it will call all of the
fit_transform
functions of the transformers sequentially, using the output of each call as input for the next, until the final estimator, for which it calls “fit”.
The pipeline will have the same methods available as the final
estimater
– in this case because that is a
StandardScaler
, we have transform, and
fit_transform
(which we’ve used)
As a note, fit transforms the model to fit the data, transform applies the model to the data,
fit_transform
does fits the data then apply transform.

## Slide 19

And a Categorical pipeline
This pipeline is similarly set up, to deal with our categorical data, using
ColumnTransformer
ColumnTransformer
is very similar to pipeline, but expects a list of tuples with a name, a transformer and a list of names or indices that identify columns the transformer should be applied to.
It’s worth noting that this will return a sparse matrix as we discussed, whereas the
num_pipeline
will return a dense matrix
Where there is a mix like this, the
ColumnTransformer
will estimate the density of the final matrix – and return a sparse matrix if the density is lower than a threshold (by default 0.3), or a dense matrix if the density is higher

## Slide 20

And that is it
We now have a full pipeline for processing our data
The next step is to apply machine learning models
Try using scikit-learn machine learning models and see if you can identify which models are best suited for this data!

## Slide 21

Any Questions?
