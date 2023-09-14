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

Now we are ready to start learning the different ways of controlling program code flow. Let's consider the following situation, which should help us understand conditional statements. Imagine you have written a message, and now another person must decide whether to read it or skip it.

### `if`

In the first case, let's make our decision very simple: if we write something, person will always read it. 
Now, we just need to use proper Python syntax to implement such a program.

```python
message = input("Enter your message: ")

if message != "":
    print("Your message was read")
print("End of the program")
```
Here is the possible example of output:
```python
Enter your message: I always wanted to say you something
Your message was read
End of the program
```

In this case, we have a message specified by us. To specify the part of the code that is specific to a condition, we use the following statements:

First, we use the Python keyword `if`, and after that, we place the condition. In our case, the condition is very simple: we check whether the message is non-empty.

After that, we have the body of the conditional statement, which is specified by indentation and goes after the `:` symbol. Indentation refers to the space at the beginning of a line of writing when it starts further away from the edge of the paper than all the other lines.
Ok, now let's assume that we do not send anything and let's check result of our program.
Then the output of programs is following one:

```python
Enter your message: 
End of the program
```
As you can see, if we write something, the condition `message != ""` is true, and we execute the code inside the conditional statement body. Otherwise, we skip all statements inside the conditional construction. 

In reality, you can put several statements inside the body by using indentation for all of them to emphasize that they are statements inside the condition.

````{note}
Actually, there is no need to explicitly use the statement `if message != "":`. Instead, we can simply replace it with `if message:`. Python automatically tries to convert the object to a `bool` type inside of condition, and an empty string is a falsy value.
To summarize, we can use the following code:
```python
message = input("Enter your message: ")

if message:
    print("Your message was read")
print("End of the program")
```
````

### `if` - `else`
Ok, now let's consider another situation where a person reads all messages except for messages from a specific person.
If we got the message from this person we on purpose ignore it.
Here is an possible code example to handle such case:

```python
name = input("Enter your name: ")
message = input("Enter your message: ")

if message and name == "Vladimir":
    print("Your message was read")
else:
    print("Message was ignored")
print("End of the program")
```

Here are possible outputs for two different inputs:
::::{grid}
:gutter: 2

:::{grid-item-card} Input-1
```
Enter your name: Vladimir
Enter your message: I always wanted to say u smth
Your message was read
End of the program
```
:::

:::{grid-item-card} Input-2
```
Enter your name: Lucy
Enter your message: Hi. How are u?
Message was ignored
End of the program
```
:::

::::

In this example person reads message if the message came from `"Vladimir"` otherwise the person ingore it.


### `if` - `elif` - `else`

Now let's consider the following scenario:

- If the message is from `"Vladimir"`, the person reads it and starts typing back.
- If the message is from `"Lucy"`, the person ignores it.
- In all other cases person just read the message.

The possible code could be:

```python
name = input("Enter your name: ")
message = input("Enter your message: ")

if message and name == "Vladimir":
    print("Message was read")
    print("Typing ...")
elif message and name == "Lucy":
    print("Message was ignored")
else:
    print("Message was read")
```

Here are examples of output with different input:

::::{grid}
:gutter: 2

:::{grid-item-card} Input-1
```
Enter your name: Vladimir
Enter your message: I always wanted to say u smth
Message was read
Typing ...
```
:::

:::{grid-item-card} Input-2
```
Enter your name: Lucy
Enter your message: Hey. How are u?
Message was ignored
```
:::

:::{grid-item-card} Input-2
```
Enter your name: Jim
Enter your message: Hey
Message was read
```
:::
::::

```{note}
`elif` - stands for else if

You can use arbitrary number of `elif` statements in your programs
```



### Nested `if` - `else`

You can nest `if-elif-else` statements inside other `if` statements. Let's consider the following simple example: we are receiving a message. First, we check if it is from `"Vladimir"`. Then, we check if it is a text or audio message. If it is a text message, we read it; if it is an audio message, we ignore it.

```python
name = input("Enter your name: ")
message = input("Enter message: ")
msg_type = input("Enter message type (audio or text): ")

if name == "Vladimir":
    if msg_type == "text":
        print("Message was read")
    elif msg_type == "audio":
        print("Message was ignored")
    else:
        print("Unknown message type")
```

Here are possible output for different input:

::::{grid}
:gutter: 2

:::{grid-item-card} Input-1
```
Enter your name: Vladimir
Enter message: Hello
Enter message type (audio or text): text
Message was read
```
:::

:::{grid-item-card} Input-2
```
Enter your name: Vladimir
Enter message: Hello
Enter message type (audio or text): audio
Message was ignored
```
:::

::::

```{admonition} Great job
Congratulations 🎉! You have learnt about conditional statements in Python.
```

## Iterative Statements

Now, we will learn how to repeat a piece of code a required number of times in Python.
To accomplish this task in Python we can use `for` and `while` loops (or also cycles).

### `for` loop
I usually use this type of loop if I know in advance how many iterations I need to perform.
The syntax of loop is very easy:

```{code-cell} ipython3
for i in range(3):
    print("Iteration:", i)
```
Let's break this down into parts to make it easier to understand:

1. `for` is the keyword that Python interprets as the start of a loop declaration.
2. `i in range(3)` specifies the number of iterations (we will take a closer look at this shortly).
3. `print("Iteration:", i)` the statement that should be repeated.

As you can see, we specify the body of a loop using indentation, as we do with conditional statements.

Now let's take a look on `range()` function.



### `while` loop


