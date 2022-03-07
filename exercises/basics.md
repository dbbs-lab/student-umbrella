# Basic exercises

## A) Variable assignment

1. Assign the value `12` to the variable `example`
2. Create 3 different variables with 3 different values
3. Create 3 different variables with 3 different values *of different data types*.
4. Can you give me 2 examples of incorrect variable names?
5. Correct the following piece of code:

```python
  Yyy = 5
  X = Vyy
```

6. Make assumptions to my intention and correct the following piece of code:

```python
  print(hello)
```

## B) Assigment operator

1. Give an example of an assignment.
2. Assign the same value to 2 variables.
3. Assign the same value to 2 variables, in the same statement.
4. Assign a variable's value to another variable.
5. Copy paste the error you get when using an undefined variable.
6. Create a value, do not assign it. What happened?

## C) Literal data types

1. Assign an integer value to `x`.
2. Assign a float value to `y`.
3. Create a float value from `x`.
4. Assign a string value to `z`.
5. Assign the integer value of `y` to `a`.
6. Assign the string value of `y` to `b`.
7. (tricky) Convert `b` into an integer.

## D) Operators

1. Sum `5` and `3` together. Subtract `9` and `2`. Multiply `5`, `7` and `3`.
2. Divide `9.3` by `3.0`. Integer divide `9.3` by `3.0`.
3. Give me the modulus of `9.3` by `3.0`, using the modulus operator.
4. Give me the modulus of `9.3` by `3.0`, without using the modulus operator.
5. Evaluate whether `5` is equal to `2`.
6. Evaluate whether `5` is larger than `2`.
7. Evaluate whether `2` is smaller than `3` and `3` is smaller than `4`, using only the
  smaller-than operator.
8. Evaluate whether `3` is larger than `3` and `"hello"` is equal to `"goobye"`.
9. (tricky) Assign values to 4 variables. Create a variable that is `True` when the first
  2 variables are equal to eachother and the latter 2 are not; or when the  first 2
  variables are not equal to eachother and the latter 2 are; but not if both pairs are
  equal or both pairs aren't equal.

## E) Functions

1. Define a function `f` without any parameters, and with a syntactically valid empty
  function body.
2. Define a function that returns the sum of 2 parameters.
3. Define a function that returns the subtraction of any number of parameters.
5. Define a function that returns `"cake"` if you pass a number larger than `5`.
6. What does the function in (5) return when it is called with an argument less than `5`?
What particularities can an online search tell you about that return value? (optional)
  What are some technical terms for such values?
7. Define a function with 1 required, and 2 optional arguments with default values, that
  returns all the values. Call that function with the first and last argument.
8. Define a function that accepts any positional argument, and returns them.
9. Define a function that accepts any function signature and prints the collected data
  structures.
10. (tricky) Define a function with 3 optional arguments. The value of the third argument
  should by default be `"sum"`, and specifies the operation to be performed on the first 2
  arguments. Implement a `"sum"`, `"sub"` (subtraction), `"mult"` and `"division"` case.
  If the first and second argument aren't given, print `"missing values!"`. Otherwise,
  return the result of the operation.
11. (tricky) Define a function that takes 1 positional argument `n`, and when called,
  calls itself again `n` times, each time it is called, it should print how many times it
  is still going to call itself.
12. (tricky) Define a function that when called, calls itself exactly 1 more time. You
  may assume that the function is always called without arguments by the user.
13. What is the technique called when a function calls itself? Did you find any examples
  online using this technique that you found interesting or useful? You may paste the
  example in your answer and I will explain how they work for you!

PS: I hope the exercises (10) and (11) give you a little peek into the power of functions.

## F) Collections

### F1) Lists

1. Assign a list of strings.
2. Sort the list of (1).
3. Reverse the list of exercise (1).
4. Assign `[1]` to `x` and add an element to the end of it.
5. Assign element 0 of `x` to `y`.
6. At this point, what is `x[y]`? And, what is `x[x[x[0]]]`? Explain why?
7. Assign `[1]` to `x` and assign `x` to `y`. Add an element to `x`.
8. What is the value of `y`? Why? Google an explanation and provide me with a summary of
  your findings. (optional) From your search, can you give me an exact term for the
  phenomenon?
9. Assign `[1]` to `x`. Make `y` equal to `x` in such a way that we can add values to
  `x`, without affecting `y`.
