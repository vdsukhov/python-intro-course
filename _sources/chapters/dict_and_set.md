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

# 2D Lists, Dictionaries and Sets

In this episode, we will learn more about Python data types, such as dictionaries and sets. However, I want to begin with a brief overview of 2-dimensional lists, as they can be used effectively to understand some basics of linear algebra.

## 2-Dimensional Lists
In our previous discussion, we learned that we can create lists in Python. I mentioned that we can use objects of different data types as elements of a list. But have you ever thought about using lists themselves as elements? Surprisingly, there is nothing stopping us from doing so.

```{code-cell} ipython3
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M)
```

After that we can work with such list as it was a matrix:
```{code-cell} ipython3
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M[0][0])
print(M[1][2])
```

You can create more complex nested structures.
Now, I will show you examples of how to create 2D lists using list comprehensions:

```{code-cell} ipython3
n, m = 5, 10 # let n corresponds to rows, and m to columns
zeros = [[0] * m for i in range(n)]

for row in zeros:
    print(row)
```

Let's take a look at matrix multiplication as an example. 
Here, I would like to ask if you know how matrix multiplication looks like and why it is defined in this way?

`````{tab-set}
````{tab-item} Question
Attempt to implement matrix multiplication for 2D lists.
````

````{tab-item} Answer
Here is possible implementation for two lists `A` and `B`
```python
C = [[0] * len(B[0]) for i in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
```
````
`````



## Dictionaries

A Python's dictionary (`dict`) is like a real-life dictionary or a phone book. It contains key-value pairs, where each key maps to a specific value. In Python, we create dictionaries using curly braces `{}`.

```{code-cell} ipython3
:tags: ['hide-output']
person = {
    "name": "Vladimir",
    "dob": "10/08/1994",
    "age": 29
}
print(person)
```
Here, as you can see, we have a map between keys and values. In this specific case, we have the following keys: `"name"`, `"dob"`, `"age"`, and their corresponding values: `"Vladimir"`, `"10/08/1994"`, and `29`. It's important to note that as keys of a dictionary, you can use not just strings, but also other immutable objects.


````{warning}
Python does not permit the use of mutable objects as dictionary keys. Therefore, the following example will result in an error:
```python
wrong_dict = {[1, 2, 3]: "list"}
```
````

### Access the element of a dict
We can access values in dictionary by specifying the key.

```{code-cell} ipython3
:tags: ['hide-output']
name = person["name"]
print(name)
```
As you can see, the syntax is similar to a list where we use the index to access specific elements. However, when it comes to dictionaries (`dict`), we should use key instead.

```{warning}
In Python dictionaries, the order of keys was traditionally considered arbitrary and not guaranteed. This means that the keys were stored in an unpredictable order, based on how Python's internal data structures managed them. However, starting from Python 3.7 and later versions, dictionaries maintain the insertion order of keys. This means that when you iterate through a dictionary, the keys are returned in the order in which they were added. This order-preserving behavior simplifies many operations, making dictionaries even more versatile for tasks like data processing and maintaining a sense of order in your data structures. So, while in older Python versions, the order of keys was unpredictable, in Python 3.7 and beyond, you can rely on the order of keys in dictionaries.
```
### Modifying Elements
You can change values just like you would in a list
```{code-cell} ipython3
:tags: ['hide-output']
person["name"] = "Vlad"
print(person)
```

### Adding a new element
You can also add new key-value pairs to a dictionary.
```{code-cell} ipython3
:tags: ['hide-output']
person["interests"] = ["Photography", "Chess"]
print(person)
```
Here we used a new key, `"interests"`, and assigned it a list value of `["Photography", "Chess"]`.

### Iterating throught a Dictionary
There are various ways to iterate over dictionaries. Let's explore some examples.

**Iterate over dict keys**
```{code-cell} ipython3
:tags: ['hide-output']
# In this example we will iterate throught the values
for k in person:
    print("Current key:", k)
    print("Value for this key:", person[k])
```
Here, we use the syntax `k in person` within a `for` loop to iterate over all possible keys inside the dictionary.


**Iterate over dict values**
```{code-cell} ipython3
:tags: ['hide-output']
# In this example we will iterate throught the keys
for value in person.values():
    print("Current value:", value)
```
Here, we use the `.values()` method of the dict which generates a sequence of all values in the dict.

**Iterate over dict key-value pairs**
```{code-cell} ipython3
:tags: ['hide-output']
for k, v in person.items():
    print(k, v)
```
Here, we use the `.items()` method of the dict which generates a sequence of all key-value pairs of the dict.


Sometimes, there may be a need to convert either keys, values, or key-value pairs into a list. To accomplish this, we can use the following syntax:
```{code-cell} ipython3
:tags: ['hide-output']
keys = list(person.keys())
values = list(person.values())
items = list(person.items())

print("keys:", keys)
print("values:", values)
print("itmes:", items)
```

### Checking for Key Existence

We can check if a key exists in a dictionary using `in`.
```{code-cell} ipython3
:tags: ['hide-output']
print("name" in person)
print("country" in person)
```

Why is it important? If you try to access an element with the wrong key, you will receive an error.
Here is an example:

```python
print(person["Country"])
```

In this case we get the following error:
```
KeyError: 'Country'
```

### Dictionary comprehension

Last week, we explored list comprehension, a more advanced approach for creating lists. A similar method can be used for creating dictionaries. Let's examine an example
```{code-cell} ipython3
:tags: ['hide-output']
letters = {i: chr(97 + i) for i in range(26)}
print(letters)
```
Here, we set our key-value pair with the expression `i: chr(97 + i)`. After that, we defined the interval for the `i` value using the `range` function.
```{note}
The `ord()` and `chr()` functions in Python are a dynamic duo for working with character data. `ord()` stands for "ordinal" and is used to find the Unicode code point of a character. For example, `ord('A')` returns 65, which is the code point for the uppercase 'A'. On the other hand, `chr()` is short for "character" and does the reverse - it converts a Unicode code point back into the corresponding character. So, `chr(65)` will give you 'A'. These functions are handy for text processing and character manipulation in various applications, from encoding to cryptography.
```


`````{tab-set}
````{tab-item} Question
Try to complete the following task: you're given a string. Your goal is to find the frequency of all unique elements, separated by whitespaces.
````

````{tab-item} Answer
Here is possible implementation for some string `line`
```python
freq_dict = {}
for w in line.split():
    if w not in freq_dict:
        freq_dict[w] = line.count(w)

print(freq_dict)
```
````
`````


## Sets
A set is a collection of unique elements, just like a bag of distinct objects. In Python, we create sets using curly braces `{}` or the `set()` constructor.

```{code-cell} ipython3
:tags: ['hide-output']
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(digits)
```
Here, you can notice that we use the same braces as we do for `dict` definition. However, in this case, we don't use `key: value` syntax, which signals to Python that this is a different data type. As always, you can verify the type of an object by using the built-in `type` function.
```{code-cell} ipython3
:tags: ['hide-output']
print(type(digits))
```

We can check whether an element is in the set by using the `in` operator:
```{code-cell} ipython3
:tags: ['hide-output']
print(0 in digits)
print(10 not in digits) # here we check wheather 10 is not in the set by using 'not in'
```

### Set methods
Here I will cover just some part of [all](https://www.w3schools.com/python/python_ref_set.asp) possible set methods:

- `add()` - adds an element to the set
- `clear()` - removes all elements from the set
- `copy()` - returns a copy of the set
- `remove()` - removes the specified element from the set

```{code-cell} ipython3
:tags: ['hide-output']
numbers = {10, 20}

numbers.add(30)
numbers.add(10)
print("numbers after add:", numbers)

numbers.remove(10)
print("numbers after remove:", numbers)

values = numbers.copy()
print("values after copy:", values)

values.clear()
print("values after clear:", values)
```

### Set Operations

Let's create two sets:
```{code-cell} ipython3
:tags: ['hide-output']
A = {1, 2, 3, 4, 5}
B = {2, 4, 5, 6, 7}
```

Python allows basic operations on sets, working as expected from a mathematical perspective:

- `==` - checks whether two sets are equal (i.e., composed of the same elements)
- `|` - represents the union of two sets
- `&` - stands for set intersection
- `-` - stands for set difference
- `<=` - checks whether the left operand is a subset of the right one
- `>=` - checks whether the right operand is a subset of the left one

```{code-cell} ipython3
:tags: ['hide-output']
print("A == B:", A == B)
print("A | B:", A | B)
print("A & B:", A & B)
print("A - B", A - B)
print("A <= B:", A <= B)
print("A >= B:", A >= B)
```

### Iterating Through a Set

You can use `for` loops to go through all elements in a set:
```{code-cell} ipython3
:tags: ['hide-output']
A = {1, 2, 3, 4, 5}
for elem in A:
    print(elem)
```

````{warning}
Sets in Python are unordered objects. 
This means there's no guarantee that different runs of your program will have the same order of elements during iterations. 
You can verify this by running the following example several times:
```python
elements = set(["ABC", "L" * 10, "B" * 5, "DEF"])
for elem in elements:
    print(elem)
```
````
