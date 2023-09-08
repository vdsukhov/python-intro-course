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

# Variables and Data Types

In the world of programming, our focus is on understanding things through a computer's eyes, like looking at objects in a special way. To make this happen, we need to pick out the most crucial details about these objects that will help us answer our questions. This is where the magic of Python comes in. Python is like a toolkit full of different kinds of containers. Some containers are like boxes for holding whole numbers, others are for numbers with decimal points, and some are for words and sentences. These containers help us gather and sort the important details about objects, and each type of container is designed to hold a different kind of detail. So, if we're trying to understand things in the world using Python, we use these containers to hold the important bits of information, like the numbers and words that matter most for the questions we want to ask.


## Numbers
We can use numbers in Python in obvious way. To demonstrate this, we will use the `print` function to output some examples. Simply specify a number and print it to the standard output.

```{code-cell} ipython3
:tags: ["hide-output"]
print(42)
```
This is an example of an integer number. In Python, integer numbers have the type `int`. Numbers with a fractional part (e.g. `42.3`, `1.0`) have the type `float`. You can always get the type of an object in Python by using the `type` function. Let's check out a couple of examples:

```{code-cell} ipython3
:tags: ["hide-output"]
print(type(42))
print(type(42.3))
```

We can perform various operations with numbers (both for `int` and `float` types), which will work as expected from a mathematical point of view:
````{margin}
```{note}
Almost always as expected, however you should try to execute the following code: `print(0.3 + 0.3 + 0.3)`
```
````

- `+` - addition
- `-` - difference
- `*` - multiplication
- `/` - division
- `//` - integer division (rounds down for both positive and negative numbers)
- `%` - modulo operation
- `**` - exponentiation
- `()` - we can enforce order of operations with parentheses

Now let's look usage examples:

```{code-cell} ipython3
:tags: ["hide-output"]
print(3 + 5)
print(8 - 3)
print(3 * 5)
print(8 / 3)
print(8 // 3)
print(8 % 5)
print(3**5)
print((3 + 5) * 8)
```

## Strings
We already saw the first example of strings in python in our first program: `"I'm Python. Nice to meet you!"`.
Strings are used in python to handle and operate with texts.
There are couple different ways how you can specify string in python:
- `'content'` - single quotes
- `"content"` - double quotes
- `"""content"""` or `'''content'''` - triple quotes (used for multiline strings)

Examples:

```{code-cell} ipython3
:tags: ["hide-output"]
print("Line")
print('Also line')
print("""First Line
Second Line
Third Line""")
```

If you need to use `'` or `"` inside of your string there are examples how to do it:
```{code-cell} ipython3
:tags: ["hide-output"]
print("I'm a human")
print('I\'m a human') # Here we use enclosing for `'` symbol
print('I am a "human"') 
print("I am a \"human\"") 
```
I would recommend always use enclosing (`\'` and `\"`).
## Logical data type

In programming, we often encounter situations that demand binary decision.
When I think about it I always recall the moment from "Matrix" movie where there is the Neo making decision between red and blue pills.
Logical data types serve as the digital manifestation of this choice.
To manipulate between with different decisions python has `bool` data type with two objects `True` and `False`.
They enable us to represent two distinct possibilities: true or false.

This data type will assist us in making decisions within our programs. There will be situations where we need to execute one part of the code if certain statements are true, and another part if they are false.

For now, let's review some basic logical operations:
- `and` - logical and
- `or` - logical or
- `not` - logical not

```{code-cell} ipython3
:tags: ["hide-output"]
# and
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

# or
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

# not
print("not True:", not True)
print("not False:", not False)
```

```{tip}
:class: dropdown
Possible examples of the logic for `and` and `or`:
1. Let's say someone wants to be a bioinformatician. When can we actually call them a bioinformatician? To me, it's when they understand biology and computer science. We call someone a bioinformatician only when both of these things are true at the same time. This is possible example of `and` operator logic.
2. Imagine you want to choose a movie to watch, but it must meet certain criteria: it must be either a drama OR a comedy. If the movie doesn't fit into either of these categories, then we won't consider watching it. In all other cases, we can watch it. This is an example of the logic for the `or` operator.
```

## Precedence of Operators
Ok, we took a look on some operations separately.
In reality often we need to combine them in more complex way.
To do so we should remember about precedence of operators.
The following table summarizes the operator precedence from highest to lowest:
````{card}
```{list-table} Precedence of Operators
:header-rows: 1
:name: precedence-of-operators

* - Level
  - Operators
* - 7 (high)
  - `**`
* - 6
  - `*` `/` `//` `%`
* - 5
  - `+` `-`
* - 4
  - `==` `!=` `<=` `>=` `>` `<`
* - 3
  - `not`
* - 2
  - `and`
* - 1
  - `or`
```
````
As ususal you can enforce order of operations with parentheses `()`.