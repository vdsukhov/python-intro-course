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
# Control Flow

In this section, we'll explore **control flow**, which determines the sequence in which a program's code runs.

Up until now, we've executed all our commands one after the other, like reading a book from start to finish. But there are times when we want the program to behave differently. Sometimes, we only want certain parts of the code to run if specific conditions are met, and other times, we want to repeat a piece of code several times. The following chart represents possible options for control flow in Python.

Before we dive into control flow, let's first understand the `input` function.

## `input` function
Previously, we learned that programming generally involves input data, commands for the computer in Python's language, and resulting output from our programs. However, we have only covered the second and third components of this fundamental programming concept. Now, we will learn the first way to obtain input data and interact with users.

The `input()` function in Python is a fundamental tool for interactive programming. It allows you to collect user input directly from the keyboard during the execution of your program. When you call `input()`, the program pauses and waits for the user to type something and press "Enter". Whatever the user enters is typically stored as a string. You can then use this input to make your program more interactive and responsive, whether it's for gathering user preferences, processing user-generated data, or creating simple text-based games. It's important to note that you can convert the input to different data types (like integers or floats) using typecasting if needed. The `input()` function significantly enhances the user experience in Python programs by enabling two-way communication between the program and its users.

```python3
user_name = input("Enter your name: ")
print("user_name =", user_name)
print("type(user_name):", type(user_name))
```
Possible example of output:
```
Enter your name: Vladimir
user_name = Vladimir
type(user_name): <class 'str'>
```

In this example the string `"Enter your name: "` specifies the `prompt` of `input()` function.
This string is displayed in standard output. After that, Python reads all input until the Enter button is pressed.
The `prompt` could be omitted:
```python3
user_name = input()
print("user_name =", user_name)
print("type(user_name):", type(user_name))
```
In this case, the program behavior is the same except that we do not print the message of the `input` function in the standard output.

As you can see, by default, we read input and store it as a `str` data type object. If necessary, we can use type conversion:
```python3
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
print(number_1 * number_2)
```

```
Enter the first number: 42
Enter the second number: 8
336
```

## Conditional Statements

### `if`
### `if` - `else`
### `if` - `elif` - `else`
### Nested `if` - `else`
### `match`

## Iterative Statements

### `for` loop
### `while` loop


