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

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/modules_name.mp4" type="video/mp4">
</video>

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

## Building our own package

In this section, we will cover the basics of creating our own packages in Python. We will be using Poetry for package management. You can find instructions on how to install Poetry on your PC [here](https://python-poetry.org/docs/#installation).

Let's create our own package. I will call it `package-demo`:
```bash
poetry new package_demo
```
After that we have the following folder structure:
```bash
❯ tree package_demo/
package_demo/
├── README.md
├── package_demo
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py

2 directories, 4 files
```

Now let's add our `math_module` module into package. We need simply to create file `math_module.py` in `package_demo` folder.
The structure of our package after that is following:
```bash
❯ tree package_demo/
package_demo/
├── README.md
├── package_demo
│   ├── __init__.py
│   └── math_module.py
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py

2 directories, 6 files
```

Here is the content of our `math_module.py` file:
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
```

Great! Now we just need to package it into a `tar.gz` file, and then we can install it using `pip` (Python package installer).
To accomplish it let's execute the following command:
```bash
poetry build
```

Now, we can install our package:
```bash
pip install dist/package_demo-0.1.0.tar.gz 
```

That's it! Simple, isn't it? However, this example only covers a very simple case. If you want to build a more complex package with different dependencies, please refer to the poetry documentation.

Now, let's try to import it when we are not in the package's folder.




## Builtin packages

In this section we will briefly cover some of the builtin packages in Python, specifically:
1. [`decimal`](https://docs.python.org/3/library/decimal.html)
2. [`math`](https://docs.python.org/3/library/math.html)
3. [`os`](https://docs.python.org/3/library/os.html)
4. [`sys`](https://docs.python.org/3/library/sys.html)
5. [`itertools`](https://docs.python.org/3/library/itertools.html)
6. [`datetime`](https://docs.python.org/3/library/datetime.html)

### `decimal`
The decimal package in Python provides arbitrary-precision decimal arithmetic. It's particularly useful for applications where precision is critical, such as financial calculations, scientific research, and more. Here are some interesting examples of decimal package usage:

```{code-cell} ipython3
:tags: ['hide-output']
from decimal import Decimal

# Perform precise arithmetic
x = Decimal('0.1')
result = x + x + x
print(result)
```
As you remember in case of float numbers we could not get the precise result:
```{code-cell} ipython3
:tags: ['hide-output']
print(0.1 + 0.1 + 0.1)
```
Let's also calculate compound interest:
```{code-cell} ipython3
:tags: ['hide-output']
from decimal import Decimal

deposit = Decimal('1_000_000')
rate_per_year = Decimal('0.15')
years = 20
outcome = deposit * (1 + rate_per_year) ** years
print(outcome)
```



### `math`
The Python math package is a built-in library that provides a wide range of mathematical functions for various calculations. Here are some interesting examples of math package usage:
```{code-cell} ipython3
:tags: ['hide-output']
import math

# Basic math operations
print("math.sqrt(25):", math.sqrt(25))  # Square root
print("math.pow(2, 3)", math.pow(2, 3))  # Exponentiation
print("math.sin(math.radians(30)):", math.sin(math.radians(30)))  # Sine function (convert degrees to radians)
```

Trigonometric Calculations:
```{code-cell} ipython3
:tags: ['hide-output']
# Trigonometric functions
angle = math.radians(45)
sine = math.sin(angle)
cosine = math.cos(angle)
tangent = math.tan(angle)
print(sine, cosine, tangent)
```

Ceiling and Floor Functions:
```{code-cell} ipython3
:tags: ['hide-output']

# Ceiling (smallest integer >= number) and Floor (largest integer <= number) functions
result1 = math.ceil(4.3)  # Ceiling
result2 = math.floor(4.7)  # Floor
print(result1, result2)
```

### `os`
The `os` package in Python provides a way to interact with the operating system, allowing you to perform tasks related to file and directory management, process management, and more. Here are some interesting examples of `os` package usage.

File and directory operations:
```python
import os

# List files and directories in a directory
files = os.listdir('/path/to/directory')

# Check if a file or directory exists
exists = os.path.exists('/path/to/file_or_directory')

# Create a new directory
os.mkdir('/path/to/new_directory')

# Rename a file or directory
os.rename('/path/to/old_name', '/path/to/new_name')

# Remove a file
os.remove('/path/to/file')

# Remove an empty directory
os.rmdir('/path/to/empty_directory')

# Remove a directory and its contents
os.removedirs('/path/to/directory_and_contents')
```
Working with Paths:
```python
import os

# Join paths to create a new path
path = os.path.join('/path', 'to', 'file.txt')

# Get the absolute path
absolute_path = os.path.abspath('file.txt')

# Extract the filename from a path
filename = os.path.basename('/path/to/file.txt')

# Extract the directory from a path
directory = os.path.dirname('/path/to/file.txt')

```

### `sys`
The sys module in Python provides functions and variables that allow you to interact with the Python runtime environment and system-specific parameters. Here is interesting example of sys module usage.

Command-Line Arguments:
```python
import sys

# Access command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]  # Get all command-line arguments after the script name
print(f"Script name: {script_name}")
print(f"Command-line arguments: {arguments}")
```

### `itertools`
The itertools module in Python provides a collection of fast, memory-efficient tools for working with iterators and combinatorial functions. Here are some interesting examples of itertools package usage:

You can generate permutations and combinations of elements using `itertools.permutations` and `itertools.combinations`:

```{code-cell} ipython3
:tags: ['hide-output']
import itertools

elements = [1, 2, 3]
permutations = itertools.permutations(elements, 2)
combinations = itertools.combinations(elements, 2)
print("Permutations:")
for perm in permutations:
    print(perm)  # Generates all permutations of 2 elements

print("Combinations:")
for comb in combinations:
    print(comb)  # Generates all combinations of 2 elements
```

Cartesian product of input iterables:
```{code-cell} ipython3
:tags: ['hide-output']
from itertools import product

print("First product result:")
for elem in product('ABCD', 'xy'):
    print(elem)

print("Second product result:")
for elem in product(range(2), repeat=3):
    print(elem)
```

### `datetime`


The datetime module in Python provides classes for working with dates and times. Here are some interesting examples of datetime package usage.

Current Date and Time:
```{code-cell} ipython3
:tags: ['hide-output']
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print(current_datetime)
```

Formatting Dates and Times:
```{code-cell} ipython3
:tags: ['hide-output']

from datetime import datetime

# Format a date as a string
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
```

Parsing Date Strings:
```{code-cell} ipython3
:tags: ['hide-output']

from datetime import datetime

# Parse a date string into a datetime object
date_str = "2023-11-06 15:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed_date)

```

Date Arithmetic:

```{code-cell} ipython3
:tags: ['hide-output']
from datetime import datetime, timedelta

# Perform date arithmetic
current_date = datetime.now()
one_week_ago = current_date - timedelta(weeks=1)
print(one_week_ago)
```

Date Comparisons:
```{code-cell} ipython3
:tags: ['hide-output']
from datetime import datetime

# Compare dates
date1 = datetime(2023, 11, 6)
date2 = datetime(2023, 11, 7)
if date1 < date2:
    print("date1 is earlier than date2")
```

Calculating Time Differences:
```{code-cell} ipython3
:tags: ['hide-output']
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Calculate the difference between two dates
date1 = datetime(2023, 11, 6)
date2 = datetime(2024, 11, 6)
difference = relativedelta(date2, date1)
print(f"Years: {difference.years}, Months: {difference.months}, Days: {difference.days}")
```


## Third-party packages installation:
To install third-party packages in Python, you can use a package manager like pip. pip is the most commonly used package manager for Python and makes it easy to download and install packages from the Python Package Index (PyPI) or other sources. Here's how you can install third-party packages.

To install a third-party package, open a terminal or command prompt and use the pip install command, followed by the package name. For example (in your console):
```bash
pip install package-name
```



