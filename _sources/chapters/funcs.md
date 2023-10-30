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

# Functions

## Function Definition

Functions are the workhorses of Python and many other programming languages. 
They are like versatile tools in a programmer's toolbox, allowing you to encapsulate a set of instructions and give them a name. 
Functions play a pivotal role in making code organized, reusable, and easier to understand. 
Their importance cannot be overstated, as they enable you to break down complex tasks into manageable chunks, making your code more modular and maintainable. 
Key features of functions include the ability to accept input, perform specific operations, and return results. 
This versatility, along with the power to create your functions, empowers programmers to tackle a wide range of problems with elegance and efficiency.

In our previous explorations, we've already encountered some of Python's built-in functions like `print()`, `len()`, and `type()`, which have been important for various tasks. 
Today, we're taking the next step in our journey by delving into the art of crafting our own functions. 
We'll learn how to create custom functions for our specific needs, allowing us to open the full creative power of Python in solving problems and simplifying complex tasks. 
So, let's embark on this exciting journey of writing our very own Python functions!

```{code-cell} ipython3
def greeting(name):
    result = "Hello, " + name + "!"
    return result
```

Here, we made our very first function. We started by using the `def` keyword to tell Python that we're creating a function. Then, we gave our function a name, which is `greeting` in this case. Inside the brackets, we put things that our function needs to work with. After that, we wrote the actual instructions for the function after a colon. Inside those instructions, we used the `return` word to say what the function will give back as the result.

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/function_definition.mp4" type="video/mp4">
</video>

Now, we can use our function with different inputs, and we don't have to rewrite the instructions inside the function every time we want to do that action. It's like having a magic tool that can do the same thing with different stuff without us having to start from scratch each time:

```{code-cell} ipython3
print(greeting("Vladimir"))

# also we can assign result to some variable
line = greeting("Alice")
print("line:", line)
```


```{note}
Defining a function in programming is a bit like creating your own recipe in the kitchen. You gather specific ingredients (input), follow a series of steps (instructions), and then you have a dish (output). Once you've perfected your recipe (function), you can use it anytime to cook that delicious meal (solve a specific task) without having to start from scratch each time. It's your customized, reusable cooking method, just as functions are custom, reusable sets of instructions in coding.
```

## Docstring

Python has a special built-in function called `help`. It's like an information guide for Python functions. With `help`, you can find out what different functions do without having to dig into their inner workings. For instance, you can use `help` to learn about the `print` function. It's a bit like getting a manual that explains how something works!
```{code-cell} ipython3
:tags: ['hide-output']
help(print)
```

But if we try to use `help` with our `greeting` function, we won't get helpful information. It's like looking for answers in a book that has no useful information about our specific topic.
```{code-cell} ipython3
:tags: ['hide-output']
help(greeting)
```

To add information about our function, we can use something called a "docstring." This is just a special string that we put at the beginning of our function. Let's see an example:
```{code-cell} ipython3
:tags: ['hide-output']
def greeting(name):
    """
    This function creates a greeting message for the given name.

    Parameters:
    - name (str): A string representing the name.

    Returns:
    str: A string containing the personalized greeting.
    """
    result = "Hello, " + name + "!"
    return result
    
help(greeting)
```

Writing docstrings for functions is essential for several reasons. First, it serves as documentation, making it easier for other programmers (and your future self) to understand how the function works and how to use it correctly. Second, it provides clarity on the expected input and output, reducing the chances of errors and misunderstandings. Additionally, docstrings facilitate code maintenance and collaboration, as they act as a reference point for anyone working with the code. Lastly, it promotes good coding practices, making your codebase more professional and accessible to a wider audience.

## Function arguments
Now let's take a closer look at function arguments. In general, you can specify an arbitrary number of arguments. Let's look at a couple of examples:

```{code-cell} ipython3
:tags: ['hide-output']
def pi_constant():
    return 3.1415926535897932

def custom_sum(a, b):
    return a + b
```

If your function requires a specific number of values, you must specify those values during the function call. Otherwise, you will encounter an error:

```{code-cell} ipython3
:tags: ['hide-output']
print(custom_sum(1, 3))
```
But in case you provide a fewer number of arguments:
```python
print(custom_sum(1))
```
you will get an error:
```python
TypeError: custom_sum() missing 1 required positional argument: 'b'
```

Python assigns values to function arguments based on their positions. Let's clarify this with an example:

```{code-cell} ipython3
:tags: ['hide-output']
def custom_division(a, b):
    return a / b

print(custom_division(1, 2))
```
In this example, Python assigns the value `1` to `a` and the value `2` to `b`.

However, if you want to specify `b` first and then `a`, you can call the function by mentioning the argument names like this:
```{code-cell} ipython3
:tags: ['hide-output']

print(custom_division(b = 1, a = 2))
```
In Python, we call this a "Keyword Argument" or "named argument." It gives you more control over the order of arguments.

## Default Arguments
Default arguments in Python allow you to assign a default value to a function parameter. If a value is not provided when the function is called, the default value is used instead. This is particularly useful when you want to make a function more flexible and provide a sensible default behavior.

Here's an example:

```{code-cell} ipython3
:tags: ['hide-output']

def greet(name, message="Hello"):
    result = message + " " + name
    return result

# Calling the function with both name and message
print(greet("Alice", "Hi"))

# Calling the function with only name (uses the default message)
print(greet("Bob"))
```

In this example, we defined a function `greet` with two parameters: `name` and `message`. The `message` parameter has a default value of `"Hello"`. When we call the function with both `name` and `message`, it uses the provided values. However, if we call the function with just `name`, it uses the default message, `"Hello"`.

Default arguments are a powerful way to make functions more versatile while providing sensible fallback values when needed.

````{warning}
Using mutable objects as default arguments in Python is not recommended because it can lead to unexpected behavior. When you modify a mutable default argument within a function, those modifications persist across function calls. It's better to use immutable objects as default arguments. If you need a mutable object, create it within the function to ensure a clean slate with each call. This practice avoids unexpected side effects and makes your code more predictable.

Try to execute the following example:
```
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

result1 = add_item("apple")
result2 = add_item("banana")

print(result1)  # Output: ['apple', 'banana']
```
````

## Arbitrary Number of Arguments

In situations where we don't know in advance how many arguments will be passed to a function, Python offers a solution. 
Let's consider an example where we want to find the minimum value among given arguments. Initially, we create a simple function for two arguments:

```{code-cell} ipython3
:tags: ['hide-output']
def custom_min(a, b):
    return b if a >= b else a

print(custom_min(10, 5))
```

Now, suppose we want to handle an arbitrary number of arguments (at least two). In this scenario, we can use a specific Python syntax that allows us to gather all arguments into one variable stored as a tuple. Here's an example:
```{code-cell} ipython3
:tags: ['hide-output']
def custom_min(a, b, *args):
    res = b if a >= b else a
    for elem in args:
        res = res if elem >= res else elem
    return res

print(custom_min(10, 5, 1))
print(custom_min(10, 5, 1, 100, 0, -10))
```
In this code, we employ the `*args` syntax, which lets us collect all extra arguments into a variable named args. 
This flexibility allows us to work with any number of arguments while maintaining code simplicity and clarity.

```{note}
Instead of using the name `args`, you can also use another name such as `arguments`.
```

You can find more specific details regarding Python function arguments, including rules about their order in both function definition and calls. 
For in-depth information, you can explore this [source](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions). 
Additionally, I highly recommend you to read about `**kwargs` for a deeper understanding of handling keyword arguments in Python. 
It's a powerful feature that can enhance your code's flexibility and readability.


## `return` statement

In our functions, it's important to understand that we may or may not include a return statement. 
We've previously encountered various examples with explicit `return` statements. 
Now, let's explore what happens when we don't specify a `return` statement explicitly.

```{code-cell} ipython3
:tags: ['hide-output']
def custom_sum(a, b):
    result = a + b

print(custom_sum(0, 5))
```

As you can observe, when a function lacks an explicit `return` statement, Python automatically returns a specific object, which is `None`. This is the default behavior when no return statement is provided.
`None` is a special data type in Python. `None` means nothing. In order to check that something is `None` use the `is` operator

```{note}
The `return` statement also denotes that the function has ended. Any code after return is not executed.
```


