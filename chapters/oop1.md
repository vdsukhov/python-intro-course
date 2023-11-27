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
# Object-Oriented Programming (Part 1)

In this episode we will take a look at Object-Oriented Programming (OOP) in Python! 
Object-oriented programming is a powerful paradigm that allows you to structure your code in a way that reflects the real-world entities and their interactions. 
In Python, OOP is a fundamental aspect of the language, providing a robust and flexible approach to designing and organizing code.

However before we will start learning OOP I want to cover some aspects of Namespaces and Scopes in Python.

## Namespace and Scopes

### Namespace

Earlier in our discussions about variables in Python, we established that a variable essentially acts as a link to an object in the computer's memory. Visualizing this relationship, we can group variables and their corresponding objects into pairs, creating a structured mapping.

```python
namespace = {"obj1": obj1, "obj2": obj2, ...}
```

This simply is a namespace in Python. So in Python, namespace act as dynamic containers, responsible for establishing a mapping between names and objects. Think of a namespace as an intelligent dictionary, where names are keys, and objects are values. This dynamic mapping allows Python to efficiently manage and organize the various elements within your program.
For next code snippet:

```python
# Variable "x" pointing to an object in memory
x = [1, 2, 3]
```
we could say that namespace mapping is `{"x": [1, 2, 3]}`.

In Python, we like to keep things organized. So, the `print` function and our variable `x` don't share the same space. 
Why? Well, Python has different areas, called "scopes", and each of them has its own place to store names and their stuff. 
It's like having separate rooms for different things. Now, let's explore these scopes in Python.

### Scopes

#### Local scope
**Local scope** refers to the part of your code, usually within a function or method, where variables have local significance. Each function call creates its own local namespace.

When a function is called, a local namespace is created, acting as a container for variables within that function. This namespace is isolated from the global namespace.
```{code-cell} ipython3
def local_scope_example():
    local_variable = "I am local"
    print(local_variable)

local_scope_example()
# This line would raise an error as local_variable is not accessible here.
# print(local_variable)
```

#### Enclosing scope

**Enclosed scope**. This scope occur when functions are defined within other functions. Each function has its own local namespace, and it can access variables from its own namespace as well as those from the enclosing scopes.

In the example below, `inner_function` has access to both its local namespace and the namespace of `outer_function`.
```{code-cell} ipython3
def outer_function():
    outer_variable = "I am in the outer function"

    def inner_function():
        inner_variable = "I am in the inner function"
        print(outer_variable)
        print(inner_variable)

    inner_function()

outer_function()
```

#### Global scope

**Global scope** encompasses the entire Python script or module. Variables in the global scope are accessible from any part of the code.

Variables defined outside any function or method belong to the global namespace. They persist throughout the program.
```{code-cell} ipython3
global_variable = "I am global"

def global_scope_example():
    print(global_variable)

global_scope_example()
print(global_variable)
```

#### Built-in scope

The **built-in scope** is encompassing all reserved keywords. They can be readily accessed anywhere in the program without requiring explicit definition before usage.
For example built-in scope contain such names as `print`, `len`, `sum`, etc.


### LEGB Rule and Namespace Search Order
The LEGB rule (Local, Enclosing, Global, Built-in) determines the order in which Python searches for a variable.

When a variable is referenced, Python searches for it in the following order:
1. Local (L): Inside the current function's local namespace.
2. Enclosing (E): In the local scopes of any enclosing functions (for nested functions).
3. Global (G): In the global namespace.
4. Built-in (B): In the built-in namespace where Python's predefined names reside.


```{note}
When I think about namespaces and scopes, I picture it like looking for things in different rooms. Imagine your current room as your "local scope." If you're trying to find something (an object), you'd check your current room first. If it's not there, you might check another room nearby (enclosing room), and so on. It's like a step-by-step search through rooms until you find what you're looking for!
```

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/scopes_analogy.mp4" type="video/mp4">
</video>

