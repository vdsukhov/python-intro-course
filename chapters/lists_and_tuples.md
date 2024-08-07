---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
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

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_stress.mp4" type="video/mp4">
</video>

To address this issue, we can use lists in Python. Here is an example of how you can create a list in Python:

```{code-cell} ipython3
:tags: [hide-output]

stress_level = [0, 0, 10, 20, 100, 0, 0]
```

In general lists could contain different data types:

```{code-cell} ipython3
:tags: [hide-output]

l = ["abc", 1, 42.0]
print(l)
```

### Indexing

Let's create the following list:

```{code-cell} ipython3
:tags: [hide-output]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

In reality, each element in a list is associated with an index. This allows us to access specific elements from our list.

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_indexing.mp4" type="video/mp4">
</video>


In Python, indexing starts from `0`, so the first element in a list is associated with the index `0`.
Now let's use indexing to access elements from a list.Here are some examples:

```{code-cell} ipython3
:tags: [hide-output]

print("numbers[0]:", numbers[0])
print("numbers[3]:", numbers[3])
```

We can change specific elements of our list by using the indexes:

```{code-cell} ipython3
:tags: [hide-output]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers[0] = -100
numbers[-1] = 0
print(numbers)
```

### Slicing

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
:tags: [hide-output]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("numbers[:3]:", numbers[:3]) # same as numbers[0:3:1]
print("numbers[3:]:", numbers[3:]) # same as numbers[3:10:1]
print("numbers[::2]:", numbers[::2]) # same as numbers[0:10:2]
```

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_slicing.mp4" type="video/mp4">
</video>

### `list` assignments

Let's examine the list assignment, as it may appear challenging at first glance.
```python3
numbers_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_2 = numbers_1

numbers_2[0] = 100
```

````{tab-set}
```{tab-item} Question
What do you think stores in the `numbers_1` variable?
```

```{tab-item} Answer
`numbers_1` corresponds to the following list: `[100, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
```
````

This happens because in reality, in this specific case, the computer memory contains a dedicated place that contains the values of our list. After we specify a variable, it simply points to this object. When we use `numbers_2 = numbers_1`, we do not create another object (meaning we don't copy it), but rather create another pointer to the same object.
Because of this, when we modify `numbers_2`, we are also modifying the underlying object, which is the same as the `numbers_1` variable.

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/list_assignment.mp4" type="video/mp4">
</video>

If you need to create an actual copy of the list, you can use slicing. Slicing always results in a new list.
Here is an example:

```{code-cell} ipython3
:tags: [hide-output]

numbers_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_2 = numbers_1[::]

numbers_2[0] = 100
print("numbers_1:", numbers_1)
print("numbers_2:", numbers_2)
```

However, if you want to check whether the underlying objects of the variables are the same, you can use the built-in `id` function. Here is how it works:

```{code-cell} ipython3
:tags: [hide-output]

numbers_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_2 = numbers_1

print("Ids after numbers_2 = numbers_1")
print(id(numbers_1), id(numbers_2))

numbers_2 = numbers_1[::]
print("Ids after numbers_2 = numbers_1[::]")
print(id(numbers_1), id(numbers_2))
```

As you can see in the first case, the results of the "id" calls are the same. However, when we use slicing, we have two different underlying objects in memory.



### `list` methods
Before I did not mention it, but in reality, each object in Python has specific features that are specified by its data type. Lists are no exception. These features are called methods. Let's take a look at some of them.
You can append new element to list:

```{code-cell} ipython3
:tags: [hide-output]

stress_level = [0, 0, 10, 20, 100, 0, 0]
print("before append:", stress_level)
stress_level.append(100)
print("after append:", stress_level)
```

As you can see here, we use the following syntax: we put a `.` after the variable name and then specify the method name - `append`.
There are many <a href="https://www.w3schools.com/python/python_ref_list.asp" target="_blank">more</a> different methods associated with the `list` data type.
Let's take a look on some other examples:

```{code-cell} ipython3
:tags: [hide-output]

stress_level = [0, 0, 10, 20, 100, 0, 0]
stress_level.extend([90, 80, 70])
print("After extend:", stress_level)

stress_level.pop()
print("After pop:", stress_level)

stress_level.sort()
print("After sort:", stress_level)
```

If you want to remove an element, you can use the method `remove`. However, if you prefer to remove the element by index, you can use the `del` operator instead of the `remove` method. Here is an example of how it works:

```{code-cell} ipython3
:tags: [hide-output]

stress_level = [0, 0, 10, 20, 100, 0, 0]
print('stress_level before del:', stress_level)

del stress_level[2]
print('stress_level after del:', stress_level)
```

In the beginning, we will rely on the predefined methods that come with Python data objects by default. However, eventually, we will learn how to write our own data types (classes) and specify the methods we need.

### Operations with `list`-s

You can use the following operators with lists: `+` and `*`.
- `+` - concatenates two lists into one, similar to how it works with strings.
- `*` - repeats elements of a list a specified number of times.
Examples:

```{code-cell} ipython3
:tags: [hide-output]

# we can create list filled with zeros
stress_level = [0] * 10
print(stress_level)

stress_level = stress_level + [10] * 3
print(stress_level)
```

### `len` function

In python there is very easy and convinient way to get the length of the object.
To get the length you can simply use the `len` function.

```{code-cell} ipython3
:tags: [hide-output]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(numbers))
```

### `for` loop and lists
Now, let's imagine that we want to iterate over each element in a list and perform some action on it. In order to do this, we can use a `for` loop.

First, let's start by creating the list using a `for` loop:

```{code-cell} ipython3
:tags: [hide-output]

numbers = [] # here we create an empty list
for i in range(10):
    numbers.append(i)

print(numbers)
```

Now we can perform some actions over the list:

```{code-cell} ipython3
:tags: [hide-output]

for i in range(len(numbers)):
    print(numbers[i] ** 2)
```

For example, we took each element from the list and calculated its square value.
Take a look that we did not modify the original list, since we just print some values.
However, if you want to modify values you can use indexing and reassign operator:

```{code-cell} ipython3
:tags: [hide-output]

print("List before modification:", numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * numbers[i]

print("List after modification:", numbers)
```

````{note}
Python offers an alternative method for iterating over list elements using the `for` loop. Instead of using the `range` function and index variable `i`, we can directly specify a variable to hold a copy of each element during the iteration. Let's take a look at that:
````

```{code-cell} ipython3
:tags: [hide-output]

for elem in numbers:
    print(elem, end = " ")
```

In this example, instead of iterating over all possible indexes, we are directly iterating through the elements. We used the variable name `elem` and replaced the `range` function with the name of the list object.
A key moment here is that the variable `elem` is associated with a new object that is a copy of the real element in the list. This means that we cannot directly change the elements of the list in-place.
Here is the example:

```{code-cell} ipython3
:tags: [hide-output]

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
:tags: [hide-output]

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)
```

However, it requires a total of 4 lines of code to perform this simple action. In such situations, we can use list comprehension to simplify it.

```{code-cell} ipython3
:tags: [hide-output]

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
:tags: [hide-output]

numbers = [i * 10 for i in range(10) if (i * 10) >= 50]
print(numbers)
```

Here we have three parts:
- The element `i * 10` will be added to the list.
- The statement `for i in range(10)` specifies the range for `i`.
- The condition `if i >= 50` is used as a filter to keep only those elements that meet the given criteria.

Additionally, you can use multiple for loops within a list comprehension.

```{code-cell} ipython3
:tags: [hide-output]

pairs = [str(i) + ", " + str(j) for i in range(3) for j in range(4)]
print(pairs)
```

```{warning}
List comprehensions are like shortcuts in Python for creating lists. They're great when you want to make a new list by applying a simple operation to every item in an existing list. For example, if you have a list of numbers and want to double each one, a list comprehension is perfect.

However, you should avoid list comprehensions when things get too complex. If you need to write a long, convoluted expression or if you're not working with lists, but instead need to perform actions that involve multiple lines of code or complex logic, it's better to use a regular `for` loop. List comprehensions are like race cars on a straight track; they're fast and efficient, but when the road gets twisty, it's better to go with the steady and reliable option.
```


## `tuple` data type
Tuples are another example of a data type that can store multiple objects. However, once you create a `tuple` object, you cannot change its elements. To create a `tuple` object, use parentheses `()`.

```{code-cell} ipython3
:tags: [hide-output]

coordinates = (3, 4)
```

In this example, we've created a tuple called coordinates with two values, (3, 4).

You can access the elements of a tuple object using indexing, in the same way as we did with a list.

```{code-cell} ipython3
:tags: [hide-output]

x = coordinates[0]
y = coordinates[1]
print(x, y)
```

However, if you try to change an element of a tuple object, you will get an error. You can try executing the following code:
```python
coordinates = (3, 4)
coordinates[0] = 0
```
The error message is the following:
```
TypeError: 'tuple' object does not support item assignment
```


Now, let's highlight some key differences between tuples and lists:

- Immutability: Tuples are immutable, meaning you can't change their contents once created, while lists are mutable, so you can modify them.
- Syntax: Tuples use parentheses `()` for creation, while lists use square brackets `[]`.
- Use Cases: Tuples are useful when you want to ensure data remains constant, like latitude and longitude coordinates or information in a database record. Lists, being mutable, are better when you need a flexible collection to add or remove items.

So, in summary, when you want data that won't change, use a tuple, and when you need flexibility, go with a list. It's like choosing between a sealed bag (tuple) and a versatile backpack (list) based on your specific needs in Python.


## `str` data type

### Methods
Previously, we have already seen the data type for strings in Python. Today, we will take a closer look at them and learn about their new features.
Strings come with some helpful built-in functions, often called methods, that let you perform various operations on them. Here are a few common ones (the full list of methods you can find <a href="https://www.w3schools.com/python/python_ref_string.asp" target="_blank">here</a>):
- `upper()`: Transforms all characters to uppercase.
- `lower()`: Converts all characters to lowercase.
- `replace()`: Substitutes one part of the string with another.
- `split()`: Breaks the string into a list using a separator.

```{code-cell} ipython3
:tags: [hide-output]

text = "Random text"
upper_text = text.upper()
lower_text = text.lower()
repl_text = text.replace("Random", "Non-random")
words = text.split()

print("upper_text:", upper_text)
print("lower_text:", lower_text)
print("repl_text:", repl_text)
print("words:", words)
```

An important note is that strings are immutable objects. In all cases of method usage, we did not modify the original string.

```{code-cell} ipython3
:tags: [hide-output]

print(text)
```

We can determine the length of a string using the same method as we did with lists. Additionally, we can use indexing:

```{code-cell} ipython3
:tags: [hide-output]

for i in range(len(text)):
    print(str(i) + ": " + text[i])
```

Since strings are immutable, we cannot reassign specific elements.
```python
text = "Random text"
text[0] = "W"
```

```
TypeError: 'str' object does not support item assignment
```

### Converting a List to a String

If you have a list and want to turn it into a single string, you can use the join() method. This method joins the elements of a list into a single string, with a specified separator in between.

```{code-cell} ipython3
:tags: [hide-output]

fruits = ["apple", "banana", "cherry"]
fruit_string = "_".join(fruits)
print(fruit_string)
```

### Converting a String to a List

If you have a string and want to split it into a list of elements, you can use the split() method. This method breaks the string into parts using a specified separator.

```{code-cell} ipython3
:tags: [hide-output]

fruit_string = "apple, banana, cherry"
fruits = fruit_string.split(", ")
print(fruits)
```

If you want to create a list where each symbol is a separate element, you can use the following approach:

```{code-cell} ipython3
:tags: [hide-output]

name_str = "Vladimir"
name_list = list(name_str)
print(name_list)
```

## Similarities between lists, tuples, and strings
Despite their differences, lists, strings, and tuples also share some common features.

- **One common feature is that they all have a length, which can be obtained using the `len` function:**

```{code-cell} ipython3
:tags: [hide-output]

line = "The happiness of your life depends upon the quality of your thoughts."
numbers = [i * 10 for i in range(10)]
configs = (1920, 1080, "Windows")

print(len(line)) # number of symbols
print(len(numbers)) # number of elements 
print(len(configs)) # number of elements
```

- **Lists, strings, and tuples are iterable objects, allowing iteration over them using a `for` loop:**

```{code-cell} ipython3
:tags: [hide-output]

for elem in line:
    print(elem, end="")
print()

for elem in numbers:
    print(elem, end=" ")
print()

for elem in configs:
    print(elem, end=" ")
print()
```

Here we use an additional `end` argument in the `print` function, which allows us to replace the default new line symbol `\n` with a custom one.

- **We can check whether an element or substring is part of a list, tuple, or string by using the `in` operator:**

```{code-cell} ipython3
:tags: [hide-output]

print("happiness" in line)
print(10 in numbers)
print(1920 in configs)
```
