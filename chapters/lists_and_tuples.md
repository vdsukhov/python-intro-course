---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
# Lists, Tuples and Strings

In this episode, we will discuss some iterable objects in Python, such as lists, tuples, and strings.

Previously, we talked about the `int` data type, where each object could only store one specific value of this type. However, there are times when it is crucial to combine objects into a collection for easier manipulation and work with them.

Let's begin by exploring the `list` data type.

## `list` data type
Imagine wanting to measure your stress level every five minutes. In this case, you would have 288 observations for just one day. However, storing and operating on this data in Python would require 288 different variables, which is not very efficient.

To address this issue, we can use lists in Python. Here is an example of how you can create a list in Python:
```{code-cell} ipython3
:tags: ['hide-output']

stress_level = [0, 0, 10, 20, 100, 0, 0]
```

In general lists could contain different data types:
```{code-cell} ipython3
:tags: ['hide-output']
l = ["abc", 1, 42.0]
print(l)
```

### `list` methods
Before I did not mention it, but in reality, each object in Python has specific features that are specified by its data type. Lists are no exception. These features are called methods. Let's take a look at some of them.
You can append new element to list:
```{code-cell} ipython3
:tags: ['hide-output']

stress_level = [0, 0, 10, 20, 100, 0, 0]
print("before append:", stress_level)
stress_level.append(100)
print("after append:", stress_level)
```
As you can see here, we use the following syntax: we put a `.` after the variable name and then specify the method name - `append`.
There are many [more](https://www.w3schools.com/python/python_ref_list.asp) different methods associated with the `list` data type.
Let's take a look on some other examples:
```{code-cell} ipython3
:tags: ['hide-output']

stress_level = [0, 0, 10, 20, 100, 0, 0]
stress_level.extend([90, 80, 70])
print("After extend:", stress_level)

stress_level.pop()
print("After pop:", stress_level)

stress_level.sort()
print("After sort:", stress_level)
```
In the beginning, we will rely on the predefined methods that come with Python data objects by default. However, eventually, we will learn how to write our own data types (classes) and specify the methods we need.

### Operations with `list`-s

You can use the following operators with lists: `+` and `*`.
- `+` - concatenates two lists into one, similar to how it works with strings.
- `*` - repeats elements of a list a specified number of times.
Examples:
```{code-cell} ipython3
:tags: ['hide-output']

# we can create list filled with zeros
stress_level = [0] * 10
print(stress_level)

stress_level = stress_level + [10] * 3
print(stress_level)
```

### Indexing and Slicing

Let's create the following list:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

In reality, each element in a list is associated with an index. This allows us to access specific elements from our list.

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_indexing.mp4" type="video/mp4">
</video>


In Python, indexing starts from `0`, so the first element in a list is associated with the index `0`.
Now let's use indexing to access elements from a list.Here are some examples:

```{code-cell} ipython3
:tags: ['hide-output']
print("numbers[0]:", numbers[0])
print("numbers[3]:", numbers[3])
```



Great! Now we need to learn how to access specific elements from our list.
There are times when we need to retrieve a specific part of the list, not just a single value.
To efficiently do that, we can use slicing techniques.
The concept is somewhat similar to the `range` function that we previously learned in the course.
The general syntax for slicing is as follows:
```python
list_object[start:stop:step]
```
Here:
- `start` is the starting point from which we want to begin our slice. Default value is `0`.
- `stop` the position where we want to stop the slicing (take a look at the fact that the value itself is not included in the range, just like with the `range` function). Default value is length of the list object.
- `step` is the step for our slicing. Default value is `1`

Let's take a look on some exapmles:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("numbers[:3]:", numbers[:3]) # same as numbers[0:3:1]
print("numbers[3:]:", numbers[3:]) # same as numbers[3:10:1]
print("numbers[::2]:", numbers[::2]) # same as numbers[0:10:2]
```

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_slicing.mp4" type="video/mp4">
</video>

### `len` function

In python there is very easy and convinient way to get the length of the object.
To get the length you can simply use the `len` function.

```{code-cell} ipython3
:tags: ['hide-output']
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(numbers))
```

### `for` loop and lists
Now, let's imagine that we want to iterate over each element in a list and perform some action on it. In order to do this, we can use a `for` loop.

First, let's start by creating the list using a `for` loop:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [] # here we create an empty list
for i in range(10):
    numbers.append(i)

print(numbers)
```

Now we can perform some actions over the list:
```{code-cell} ipython3
:tags: ['hide-output']
for i in range(len(numbers)):
    print(numbers[i] ** 2)
```
For example, we took each element from the list and calculated its square value.
Take a look that we did not modify the original list, since we just print some values.
However, if you want to modify values you can use indexing and reassign operator:
```{code-cell} ipython3
:tags: ['hide-output']
print("List before modification:", numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * numbers[i]

print("List after modification:", numbers)
```

````{note}
Python offers an alternative method for iterating over list elements using the `for` loop. Instead of using the `range` function and index variable `i`, we can directly specify a variable to hold a copy of each element during the iteration. Let's take a look at that:
````

```{code-cell} ipython3
:tags: ['hide-output']
for elem in numbers:
    print(elem, end = " ")
```
In this example, instead of iterating over all possible indexes, we are directly iterating through the elements. We used the variable name `elem` and replaced the `range` function with the name of the list object.
A key moment here is that the variable `elem` is associated with a new object that is a copy of the real element in the list. This means that we cannot directly change the elements of the list in-place.
Here is the example:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [0, 1, 2, 3, 4]
for elem in numbers:
    elem = elem + 5
print(numbers)
```

So, you can use this approach if you do not want to modify the values in your list.


### List comprehension

List comprehension is very cool way to define the list and fill it.
We saw previously this way to fill list with using for loop:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = []
for i in range(10):
    numbers.append(i)
```
However, it requires a total of 4 lines of code to perform this simple action. In such situations, we can use list comprehension to simplify it.

```{code-cell} ipython3
:tags: ['hide-output']
numbers = [i for i in range(10)]
print(numbers)
```
Cool, isn't it? 
It appears that we have placed the for loop inside the list declaration.
Let's split it into two parts:

- `i`: This is the value that will be placed inside the list. You can modify it and check the results.
- `for i in range(10)`: This statement specifies the number of objects and the elements that should be used as a specimen to be placed into the list.

Also we can specify some condition which will filter out elements from the list which don't meet some property:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [i * 10 for i in range(10) if (i * 10) >= 50]
print(numbers)
```
Here we have three parts:
- The element `i * 10` will be added to the list.
- The statement `for i in range(10)` specifies the range for `i`.
- The condition `if i >= 50` is used as a filter to keep only those elements that meet the given criteria.

