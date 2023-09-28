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

<!-- ```{image} ./pics/variables_and_data_types_box.png
:width: 560px
:align: center
``` -->

In the world of programming, our focus is on understanding things through a computer's eyes, like looking at objects in a special way. To make this happen, we need to pick out the most crucial details about these objects that will help us answer our questions. This is where the magic of Python comes in. Python is like a toolkit full of different kinds of containers. Some containers are like boxes for holding whole numbers, others are for numbers with decimal points, and some are for words and sentences. These containers help us gather and sort the important details about objects, and each type of container is designed to hold a different kind of detail. So, if we're trying to understand things in the world using Python, we use these containers to hold the important bits of information, like the numbers and words that matter most for the questions we want to answer.


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
I would recommend use enclosing (`\'` and `\"`).

### Operations on strings
- **Concatenation**.
We can merge strings into one by using the `+` operator or by simply putting them one after the other.
Here are some examples:
```{code-cell} ipthon3
:tags: ["hide-output"]
print("Hello" " World!")
print("Hello" + " World!")
```
- **String repeation**.
If you need to repeat a string, you can use the  operator, followed by the desired number of repeats. Here is an example:
```{code-cell} ipthon3
:tags: ["hide-output"]
print("You talking to me? " * 3)
```

These are exaples of basic string operations further in the course we will see some other things that we could do with strings.
## Logical data type

In programming, we often encounter situations that demand binary decision.
When I think about it I always recall the moment from "Matrix" movie where there is the Neo making decision between red and blue pills.
Logical data types serve as the digital manifestation of this choice.
To manipulate between with different decisions python has `bool` data type with two objects `True` and `False`.
They enable us to represent two distinct possibilities: true or false.

This data type will assist us in making decisions within our programs. There will be situations where we need to execute one part of the code if certain statements are true, and another part if they are false.

### Logical operators

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

### Comparison operators
You can get `bool` data type as result after performing comparison of other objects.
Here is the list of comparison operators:
- `==` - equal
- `!=` - no equal
- `>` - greater than
- `<` - less than
- `>=` - greater than or equal to
- `<=` - less than or equal to

Let's take a look on couple examples:
```{code-cell} ipython3
:tags: ["hide-output"]
print(1 == 0)
print(1 != 0)
print(1 > 0)
print(1 <= 0)

# it is possible to compare strings as well
print("Hello" == "Hello")
print("alpha" <= "beta")
```

```{note}
:class: dropdown
In my opinion, the section about comparison operators is highly important. While it is obvious when dealing with real numbers, there will be times when you need to compare other types of objects, such as genes for example. In such cases, it is important to find a way to map your object to real numbers to make comparison possible. For instance, when comparing genes, you may need to consider the number of nucleotides that make them up, or the value expression, depending on the task at hand.
```

## Precedence of Operators
Okay, we have looked at some operations separately. In reality, we often need to combine them in a more complex way. To do this, we need to remember the precedence of operators. The following table summarizes the operator precedence from highest to lowest:
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
* - 1 (low)
  - `or`
```
````
As usual you can enforce order of operations with parentheses `()`.

## Variables
Okay, so far we have learned how to create objects in Python and print them immediately. However, we usually want to store objects and reuse them in our code. To do this, we use variables in Python. We can create a specific name and assign it to a specific object in Python. Here is an example:
```{code-cell} ipython3
:tags: ["hide-output"]
name = "Vladimir"
print("Hello " + name)
print(name + ", how are you today?")
```

```{note}
In programming, the concept of variables is very important because it allows for the reuse of specific parts of code. Throughout our course, we will also cover other concepts that enable code reuse.
Code reuse refers to the practice of writing code in a way that it can be used in multiple parts of a program or even in different programs. This promotes efficiency, reduces redundancy, and simplifies maintenance and debugging.
We will also cover functions and packages, which demonstrate the beauty of code reuse further along in the course.
```

A commonly used analogy for variables is to think of them as named boxes where we can store our objects. 
In the example above, we can think that we have a box named `name` that contains the string `"Vladimir"`.

Some other examples of possible operations over variables:
```{code-cell} ipython3
:tags: ["hide-output"]
value_1 = 101
value_2 = 42

print(value_1 + value_2)
value_1 = 0 # we can assign a new value to a variable
print(value_1)
```

In case you need to assign multiple variables at once you can use the following syntax:
```{code-cell} ipython3
:tags: ["hide-output"]

x, y, z = "User", 1, True
print(x, y, z)
```

In Python, it is very easy to swap the values of two variables. While other programming languages often require an additional variable to accomplish this task, Python makes it much simpler:
```{code-cell} ipython3
:tags: ["hide-output"]
x, y = 1, 2
print("x and y before swap:", x, y)
x, y = y, x
print("x and y after swap:", x, y)
```


### Rules for Python variables
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp).


## Type Conversion
Sometimes, you need to change the way a computer understands data. 
Imagine you have two pieces of text, `"4"` and `"2"` and you want to put them together like words. You can do this with a plus `+` operator, like `"4" + "2"` which makes `"42"`.

But what if you want the computer to treat these like numbers instead of just text? 
That's when Python Type Conversions come to the rescue. 
Let's look at some everyday examples of how to do this.

### `int` to `float`

You can convert an integer to a floating-point number using the `float()` function. For example:
```{code-cell} ipython3
:tags: ["hide-output"]
integer_num = 5
print(integer_num)
float_num = float(integer_num)
print(float_num)
```

### `float` to `int`
To convert a floating-point number to an integer, you can use the `int()` function. Be aware that this truncates the decimal part, not rounding. For example:
```{code-cell} ipython3
:tags: ["hide-output"]
float_num = 3.14
print("float_num =", float_num)
integer_num = int(float_num)  # int_num will be 3
print("int_num =", integer_num)
```

### `str` to `int` or `float`
You can convert a string containing a numeric value to an integer or float using `int()` or `float()`. For example:
```{code-cell} ipython3
:tags: ["hide-output"]
num_str = "42"
int_num = int(num_str)
float_num = float(num_str)
print("int_num =", int_num)
print("float_num =", float_num)
```

But if your string doesn't represent number then you will get an error if you try to convert it to numerical data type:

```python3
line = "xyz"
int_num = int(line)
float_num = float(line)
print("int_num =", int_num)
print("float_num =", float_num)
```
You shoud get the following error:
```
ValueError: invalid literal for int() with base 10: 'xyz'
```

### `int` or `float` to `str`
To convert an integer or float object to a string, you can use the `str()` function. For example:
```{code-cell} ipython3
:tags: ["hide-output"]

int_num = 42
float_num = 3.1415
str_int = str(int_num)
str_float = str(float_num)
print("type(str_int):", type(str_int), " str_int = ", str_int)
print("type(str_float):", type(str_float), " str_float = ", str_float)
```

### `bool` Truthy and Falsy values
To change an object into a logical data type, you can use the `bool()` function. Here's a simple rule for how this conversion works:

- If you have `0`, `0.0`, or an empty text `""`, they turn into `False`.
- For all other values, they become `True`.

This rule helps you understand how different values are seen by the computer in a true or false way.
Examples:
```{code-cell} ipython3
:tags: ["hide-output"]
print(bool(0), bool(0.0), bool(""))
print(bool(101), bool(-10), bool("ABC"))
```
When certain values act like they are `True` in a computer's eyes, we call them **Truthy**. 
Similarly, when values act like they are `False` we call them **Falsy**. 
Understanding these concepts is important when dealing with conditions and decisions in programming. 









