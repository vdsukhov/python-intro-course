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

### Iterating over list
