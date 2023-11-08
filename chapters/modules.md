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

# Modules and Packages

In this episode, we will dive into the world of Python modules and packages.
If you are new to Python or looking to organize your code better, you're in the right place.
We will break down modules and packages using simple examples. Let's start.

## Modules
In Python, a module is like a file that contains Python code. It can be functions, variables, or classes.
Modules help you organize your code and make it reusable.
Let's create a simple module.
To do that let's create the separate folder and file with following name `math_module.py`.
Here is the structure of our directory:
```bash
❯ tree module_example/
module_example/
└── math_module.py
```
Now let's specify some relative code inside of our module (`math_module.py`):

```{code-cell} ipython3
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def absolute_value(a):
    return a if a >= 0 else -a

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

e = 2.718281828459045090795598298427648842334747314453125
pi = 3.141592653589793115997963468544185161590576171875
```

Here, we have created our first module.

Now, we can use our functions in other Python files. Let's create another file named `usage.py`.
The current directory structure is as follows:
```bash
❯ tree module_example/
module_example/
├── math_module.py
└── usage.py
```

The `usage.py` file:
```{code-cell} ipython3
:tags: ['hide-output']
import math_module

a = 10
b = 5

print(math_module.gcd(a, b))
print(math_module.factorial(a))
print(math_module.e)
print(math_module.pi)
```
Now, we can access all objects from the `math_module.py` file using the following syntax: `import math_module`. After importing, we can access the objects by specifying the module name followed by a dot and the name of the object we want to access. For example, `math_module.gcd(a, b)` is a call to the gcd function.


## Module import

The `import` statement in Python is used to bring external code into your program. There are several ways to use the `import` syntax, each with its own purpose. Here are the different ways to use import:

#### Importing a module:
The simplest use of import is to import an entire module. This makes all functions, variables, and classes from that module available in your code. (Examples we saw previously)

#### Renaming a module:
You can give an imported module an alias to make it easier to reference in your code. This is especially useful when dealing with modules with long names.
```{code-cell} ipython3
:tags: ['hide-output']
import math_module as mm

a = 10
b = 5

print(mm.gcd(a, b))
```

#### Importing Specific Functions or Variables:
Sometimes, you only need specific functions or variables from a module. You can import them individually.
```{code-cell} ipython3
:tags: ['hide-output']
from math_module import gcd

a = 10
b = 5

print(gcd(a, b))
```

#### Importing Everything from a Module:

You can import everything from a module and use its functions, variables, and classes directly without the module name prefix. However, this approach is generally discouraged as it can lead to naming conflicts.

```{code-cell} ipython3
:tags: ['hide-output']
from math_module import *

print(e)
print(pi)
```
#### Importing a Specific Function or Variable with an Alias:
You can combine aliasing and importing specific functions or variables for a more concise reference.

```{code-cell} ipython3
:tags: ['hide-output']
from math_module import factorial as f

print(f(10))
```

## `__name__`
Now we understand that we can consider each Python file as a module.
Before running a program, the Python interpreter assigns the name of the Python module to a special variable called `__name__`.
The value assigned to `__name__` depends on whether you run the program from the command line or import the module into another module.
If you run your module as a script, like this:

```bash
python program.py
```

then the Python interpreter will automatically set the value of `__name__` to the string `"__main__"`.

To check it let's fill the `program.py` file with following code:
```{code-cell} ipython3
:tags: ['hide-output']
print(__name__)
```
As you can see, we have access to the `__name__` variable inside our program. When running the program from the command line, the value of this variable is `"__main__"`. 

However, if your module is imported in another module, the value will be different. 
Let's use our `math_module.py` module as an example again, but this time let's rewrite the `usage.py` as follows:
```{code-cell} ipython3
:tags: ['hide-output']
import math_module
print(math_module.__name__)
```
Here, you can see that if you import the module, the value of `__name__` is not equal to `"__main__"`.

### Possible `__name__` usage
Sometimes, we need a Python file that contains reusable functionality, but we also want to include certain instructions that should only be executed when we run the file directly from the console. In this scenario, we can use the `__name__` variable's behavior to achieve this dual functionality.

Let's take the example of a Python module named "math_module.py." This module contains various functions and constants:

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def absolute_value(a):
    return a if a >= 0 else -a

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

e = 2.718281828459045090795598298427648842334747314453125
pi = 3.141592653589793115997963468544185161590576171875

a = 10
b = 5
print(gcd(a, b))
```

No matter whether we import or run this module from the console, it will always display the output as follows:

```
5
```

However, if we want to run only specific parts of the program when it's executed from the console, we can use the following syntax:

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def absolute_value(a):
    return a if a >= 0 else -a

def factorial(a):
    if a is 0:
        return 1
    return a * factorial(a - 1)

e = 2.718281828459045090795598298427648842334747314453125
pi = 3.141592653589793115997963468544185161590576171875

if __name__ == "__main__":
    a = 10
    b = 5
    print(gcd(a, b))
```

Now, when we import the module, we won't see any output. However, if we run the module directly from the console, it will execute the specified code:

```
5
```

This technique allows us to create modules that can be used both for their functions and, when necessary, for standalone execution, providing flexibility and reusability in our code.
