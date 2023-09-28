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

### Indexing

Let's create the following list:
```{code-cell} ipython3
:tags: ['hide-output']
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Now we want to access specific elements of a list. To do that, we can use indexing. In Python, indexing starts from `0`. This means that the first element in a list is associated with index `0`. Here are some examples:

```{code-cell} ipython3
:tags: ['hide-output']
print("numbers[0]:", numbers[0])
print("numbers[3]:", numbers[3])
```

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_indexing.mp4" type="video/mp4">
</video>

### Slicing

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
