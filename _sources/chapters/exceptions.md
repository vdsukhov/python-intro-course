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

# Exception Handling

Today, we will explore exceptions in Python. However, before we delve into exceptions, let's briefly discuss the data structure known as the stack.

## Stack

A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. It can be visualized as a collection of elements with two main operations: push, which adds an element to the top of the stack, and pop, which removes the top element from the stack.

Key points of stack:

* Abstract data type
* Collection of elements
* **Push** operation: adds an element to the collection
* **Pop** operation: removes the most recently added element

````{note}
Think of a stack data structure as a can of Pringles chips - a perfect analogy to understand how it works.

```{toggle}
In this analogy, the can symbolizes the stack, and the chips nestled inside represent the elements stored in the stack. Here's a breakdown of how the analogy mirrors the operations of a stack:

* **Push Operation (Adding Chips):**
    * Just like adding new chips to a can, the "push" operation allows us to add elements to the stack, but always at the top.
* **Pop Operation (Taking the Top Chip):**
    * The "pop" operation corresponds to taking a chip from the top of the can. It follows the principle of retrieving the most recently added element.
    * If you want a chip, you reach for the top one - the last chip added to the can.

```

By visualizing the stack as a can of Pringles, it's easy to grasp the Last In, First Out (LIFO) nature of the stack data structure. The can's opening serves as a reminder that we can only add or take chips from the top, illustrating the strict order in which elements are managed. This analogy provides a tangible way to understand the fundamental operations of a stack.
````

### Representing stack functionality using the `list` data type


We can simulate a stack data structure efficiently by leveraging the built-in list data type in Python.

```{warning}
In reality, a list and a stack are distinct data structures. To delve deeper into their individual characteristics and functionalities, you can explore the following links:

* <a href="https://w.wiki/8T8m" target="_blank">Stack</a>
* <a href="https://w.wiki/8T8n" target="_blank">List</a>
```



```{code-cell} ipython3
:tags: ['hide-output']
stack = []

stack.append("element 1") # append ~ pop
print(f"Stack is: {stack}")

stack.append("element 2")
stack.append("element 3")

popped_elem = stack.pop()
print(f"Popped element: {popped_elem}")
print(f"Stack is: {stack}")
```


### Call Stack


A call stack, often referred to simply as the "stack," is a region of memory used in computer science to manage function and method calls in a program. It keeps track of the active subroutines (functions or methods) and their respective local variables. The call stack operates on the Last In, First Out (LIFO) principle, meaning that the last function call made is the first one to be resolved.

#### Simple function calls

```{code-cell} ipython3
def func_a():
    print("Function A start")
    func_b()
    print("Function A end")

def func_b():
    print("Function B start")
    print("Function B end")

# Main program
func_a()

```

In this example, `func_a` calls `func_b`, and the call stack looks like this:

1. `func_a` is called.
2. Inside `func_a`, `func_b` is called.
3. `func_b` completes its execution.
4. Control returns to the point immediately after the call to `func_b` inside `func_a`.
5. `func_a` completes its execution.

We can use the `traceback` package to display the call stack at a particular point in our code:

```python
import traceback

def func_a():
    func_b()

def func_b():
    traceback.print_stack()


# Main program
func_a()
```
The output for the provided code snippet is as follows:

```
  File "...", line 11, in <module>
    func_a()
  File "...", line 4, in func_a
    func_b()
  File "...", line 7, in func_b
    traceback.print_stack()
```


#### Recursive function

```{code-cell} ipython3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5:", result)

```

In this example, the `factorial` function calls itself recursively.
The call stack looks like this:
```{toggle} 
1. `factorial(5)` calls `factorial(4)`
2. `factorial(4)` calls `factorial(3)`
3. `factorial(3)` calls `factorial(2)`
4. `factorial(2)` calls `factorial(1)`
5. `factorial(1)` returns 1 (base case)
6. Control returns to `factorial(2)`, which returns 2 * 1 = 2
7. Control returns to `factorial(3)`, which returns 3 * 2 = 6
8. Control returns to `factorial(4)`, which returns 4 * 6 = 24
9. Control returns to `factorial(5)`, which returns 5 * 24 = 120
```

#### Stack Overflow

The call stack has a specific size, meaning that if a program has an excessive number of function calls, it can lead to a stack overflow error. This occurs when the available memory for the call stack is exhausted. Let's examine an example to illustrate this:

```python
def factorial(arg):
    """Custom function calculating factorial"""
    assert_msg = "Ordinary factorial defined for"\
    " numbers greater or equal than zero"
    assert arg >= 0, assert_msg
    if arg == 0:
        return 1
    return arg * factorial(arg - 1)

print(factorial(2000))
```

This situation emphasizes the importance of carefully managing recursion and function calls to prevent stack overflow errors, as exceeding the stack size can lead to program termination. Recursive functions should be designed with appropriate base cases to ensure that the recursion stops and doesn't lead to an infinite loop, ultimately causing a stack overflow.

However, In Python sometimes we could need to manually increase the call stack size. In this case we can use the `sys` module:

```{code-cell} ipython3
:tags: ['hide-output']
import sys
import math

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

def factorial(arg):
    """Custom function calculating factorial"""
    assert_msg = "Ordinary factorial defined for"\
    " numbers greater or equal than zero"
    assert arg >= 0, assert_msg
    if arg == 0:
        return 1
    return arg * factorial(arg - 1)

print(f"{math.log10(factorial(2000))}")
```

```{note}
Chances are you've come across a valuable resource known as Stack Overflow. If you're curious about why it's named the way it is, <a href="https://w.wiki/8T9F" target="_blank">here</a> you can find a few intriguing possibilities.
```


Understanding the call stack becomes particularly crucial when handling exceptions and interpreting their output. A solid grasp of the call stack allows developers to navigate through the sequence of function calls leading to an exception, aiding in the identification and resolution of issues within the code.


## Syntax Errors and Exceptions

In Python, errors can be broadly classified into two main categories: Syntax Errors and Exceptions. 
While they both signal that something has gone awry in our code, they play different roles in the debugging and error-handling process.

### Syntax Errors

Let's start by looking at Syntax Errors. These occur when the Python interpreter encounters code that violates the language's syntax rules. In other words, it's like a grammatical mistake in our code.

```python
# Example of a Syntax Error
print("Hello, world!"
```

In this example, a missing closing parenthesis will result in a SyntaxError. These errors are caught by the interpreter during the compilation phase, preventing the program from running.

```{note}
Understanding and fixing syntax errors is fundamental. They are often the first roadblock we face when translating our ideas into executable code. Fortunately, Python provides clear error messages that guide us to the problematic lines.
```

### Exceptions

In Python, an exception is a runtime error that interrupts the normal flow of a program. These errors can occur due to various reasons, such as invalid input, file not found, or division by zero. Understanding and handling exceptions is crucial for writing robust and reliable Python code.


Python comes with a set of built-in exceptions, each serving a specific purpose. Some common built-in exceptions include:

1. `SyntaxError`: Raised when the Python interpreter encounters a syntax error.
2. `TypeError`: Raised when an operation or function is applied to an object of an inappropriate type.
3. `ValueError`: Raised when a built-in operation or function receives an argument of the correct type but an inappropriate value.
4. `FileNotFoundError`: Raised when a file or directory is requested but cannot be found.

Some examples that can cause different exceptions include:

```python
print(1 / 0)
```
```
ZeroDivisionError: division by zero
```

```python
print(int('abc'))
```
```
ValueError: invalid literal for int() with base 10: 'abc'
```


In Python, exceptions follow a structured inheritance hierarchy, forming a conceptual tree that represents their relationships. This hierarchy is instrumental in understanding the various types of exceptions and how they relate to one another. Think of it as an organized family tree for Python's exception classes.

To explore this hierarchy comprehensively, you can refer to the complete structure <a href="https://docs.python.org/3/library/exceptions.html#exception-hierarchy" target="_blank">here</a>. This visual representation provides insights into the parent-child relationships among different exception classes, showcasing the inheritance patterns that define the Python exception system.



### Exception Handling

We can handle exceptions in the Python. Let's start from the classic example:

```python
while True:
    try:
        a = int(input("Enter integer: "))
        b = int(input("Enter integer: "))
        result = a / b
        print("result of division is:", result)
        break
    except ZeroDivisionError:
        print("You're trying to divide by zero ")
```


