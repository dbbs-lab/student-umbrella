Get your umbrellas and brace the storm, we'll be diving right into it: making pretty things from data.

Not considering data curation (long term management of data) there will be a few key skills to practice here:

* Interpreting questions
* Visually organizing data
* Using Python & common packages
* Organizing basic code into reusable blocks

# Getting started

## Requirements

* Working [development environment]
* `pip install numpy scipy plotly`

## Practice datasets

<sub><super>
  Datasets taken from [this article](
    https://towardsdatascience.com/all-the-datasets-you-need-to-practice-data-science-skills-and-make-a-great-portfolio-74f2eb53b38a
  )
</super></sub>

Click around a bit in this repository until you stumble upon the datasets, and a way to download them. 
The best practices for obtaining files from repositories are in the [git lesson].

## Loading datasets in Python

Once you found a way to download the datasets, put them in a working directory and navigate to the folder (see [shell basics]).
In the folder, save the following snippet as ``starter.py``, modify and run it:

```python
# Some conventional imports that make your
# life super easy when getting started!
import pandas as pd
import numpy as np

file = "my_dataset.csv"
column = "my_column"

dataset = pd.readcsv(file)
column_data = dataset[column]
print("My dataset column has", len(column_data), "datapoints")
```

You should thoroughly understand **every** statement in this script (and ofcourse, exactly what `statement`s and `expression`s are!).
If you do not, look for a nice tutorial and introduction to Python. Make sure it teaches you what statements, expressions,
variables, literals, operators, attributes and functions are.

Let's list what you have to understand at this point to continue:

* The working directory, shell and Python interpreter
* How to run Python scripts
* Variables and literals
  * What is the difference between `hello` and `"hello"`?
  * What is a `NameError: hello is undefined`?
  * Data structures such as lists, dictionaries, arrays (`numpy`, `pandas`)
  * Indexing of data structures
* Statements (what do these do?)
  * `# comments`
  * `x = y`
  * `x.y`
  * `x(y, z)`

## Guidelines

* Use a search engine to find your answers (see [search guide])
* If you encounter any errors, see the [error guide] to deal with them!
* Use Plotly's `simple_white` theme, I like it, it makes me happy and lenient.
* Factor shared code into functions (see [function guide]).

## Exercises

From here on out it's up to you (and Google) to find answers. Make the following
exercises and send me your results!

### Plots

#### Housing prices

* Show a histogram of the distribution of `floors` in the dataset.
* Show a line plot of the average price vs the amount of floors.
* Show a line of the average price per floor vs the amount of floors.
* Show a line plot with error bars (stdev) of the price  
