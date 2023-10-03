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


<!-- ```{image} ./pics/control_flow_snake_circle.png
:width: 560px
:align: center
``` -->

In this section, we'll explore **control flow**, which determines the sequence in which a program's code runs.

Up until now, we've executed all our commands one after the other, like reading a book from start to finish. But there are times when we want the program to behave differently. Sometimes, we only want certain parts of the code to run if specific conditions are met, and other times, we want to repeat a piece of code several times. The following chart represents possible options for control flow in Python.

Before we dive into control flow, let's first understand the `input` function.

## `input` function

```{image} ./pics/flow.png
:align: center
```

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
To do so we can use an `else` statement which is used in conjunction with an `if` statement to specify what should happen if the condition in the `if` statement is false.
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

To resolve this task, the `elif` statement can be used. `elif` (short for "else if") is used when multiple conditions need to be checked in sequence. 
It allows you to test a series of conditions and execute the first block of code whose condition is true.
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
You can use arbitrary number of `elif` statements in your programs
```



### Nested `if` - `else`

You can nest `if-elif-else` statements inside other `if` statements. Let's consider the following simple example: we are receiving a message. First, we check if it is from `"Vladimir"`. If it is, we then check whether it is a text or audio message. If it is a text message, we read it; if it is an audio message, we ignore it.

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

### Ternary `if ... else` operator

There is one more way to use conditional statements, it is `if-else` ternary operator.
You can also use the if-else statement as a ternary operator, which is a concise way to express conditional expressions in a single line of code.

Here's the basic syntax for the if-else ternary operator:
```python
val_opt_a if condition else val_opt_b
```
Here:
- `condition` this is the condition that you want to check
- `val_opt_a` if the condition is true, this value will be returned
- `val_opt_b` if the condition is false, this value will be returned

Here's an example using the if-else ternary operator to determine the maximum of two numbers:
```{code-cell} ipython3
:tags: ['hide-output']
a = 10
b = 20

max_value = a if a > b else b
print(max_value)
```

In this example, the condition `a > b` is evaluated. If it's true, the value of `a` is assigned to `max_value`; otherwise, the value of `b` is assigned.

The if-else ternary operator is a concise and readable way to express simple conditional logic in one line of code. However, it's essential to use it judiciously, as it can become less readable if the conditions or expressions are complex.

## Loops/Cycles

Now, we will learn how to repeat a piece of code a required number of times in Python.
To accomplish this task in Python we can use `for` and `while` loops.

### `for` loop
A for loop in Python is a control structure used to iterate (repeat) a block of code a specific number of times. It is a fundamental programming construct for performing repetitive tasks efficiently.

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

#### `range()` function

Now let's take a look on `range()` function.
The `range()` function in Python is a built-in function used to generate a sequence of numbers within a specified range. It's commonly used in for loops to control the number of iterations or to create sequences of numbers. Here's how the `range()` function works:

<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/range_overview.mp4" type="video/mp4">
</video>

```python
range(stop)
range(start, stop)
range(start, stop, step)
```
`range()` function can take three arguments, two of them are optional and 1 is required.
- `start` (optional): The starting value of the sequence (inclusive). If not provided, it **defaults to 0**.
- `stop` (required): The end value of the sequence (exclusive). This value is not included in the generated sequence.
- `step` (optional): The step or increment between numbers in the sequence. If not provided, it **defaults to 1**.




<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/range_examples.mp4" type="video/mp4">
</video>


Examples:

```{code-cell} ipython3
:tags: ["hide-output"]
print("Example 1 -- range(4):")
for i in range(4):
    print(i)  # Outputs 0, 1, 2, 3

print("Example 2  -- range(2, 6):")
for i in range(2, 6):
    print(i)  # Outputs 2, 3, 4, 5

print("Example 3 -- range(1, 5, 2):")
for i in range(1, 5, 2):
    print(i)  # Outputs 1, 3

print("Example 4 -- range(4, 0, -1):")
for i in range(4, 0, -1):
    print(i)  # Outputs 4, 3, 2, 1
```

#### Nested `for` loops

It is possible to create more complex structures where one `for` loop is nested inside another.
Let's consider the task of generating all possible pairs `(i, j)` where i takes values from `{1, 2, ..., 5}` and j takes values from `{1, 2, 3}`.
To accomplish this, we can use the following code:

```{code-cell} ipython3
:tags: ["hide-output"]
for i in range(1, 6):
    for j in range(1, 4):
        print("(", i, ", ", j, ")", sep="")
```
Here, we are using the `sep` argument of the `print` function for the first time.
This argument controls the separator used to separate the elements passed to the function.
By default, the value for `sep` is a whitespace, but here we have changed it to an empty string.
You can try removing `sep=""` from the `print` function to see how it affects the output.

````{note}
There are often multiple ways to achieve the same task in programming. For example, in this case, we could omit the use of the `sep` argument by using the following approach:
```python
for i in range(1, 6):
    for j in range(1, 4):
        print("(" + str(i) + ", " + str(j) + ")")
```
````

In my opinion, the `for` loop is very useful when you already know the exact number of iterations needed in advance.
However, there are cases where it is not known or difficult to determine the number of iterations required to accomplish a specific task.
To handle such situations, Python provides the `while` loop. Let's take a closer look at it.


### `while` loop

Let's imagine that we want to obtain an integer number from the user that belongs to the interval from 0 to 100 (inclusive on both sides).
However, the user can enter a value that is outside of this interval, and we don't know in advance how many iterations it will take until the user enters the proper value.

Let's explore a possible implementation:
```python
inp_value = int(input("Enter number in interval from 0 to 100: "))

while not (0 <= inp_value <= 100):
    inp_value = int(input("Entered value was outisde of interval. Try one more time: "))
```

Here is a possible output:
```
Enter number in interval from 0 to 100: 1001
Entered value was outisde of interval. Try one more time: 500
Entered value was outisde of interval. Try one more time: 50
```


Aslo, it is possible to use `while` in the same manner as we used `for` loop:
```{code-cell} ipython3
:tags: ['hide-output']

i = 0
while i < 10:
    print(i)
    i = i + 1
```

````{note}
You can use plus-equals operator `+=` which provides a convenient way to add a value to an existing variable and assign the new value back to the same variable.
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

Also, there are operators for subtraction `-=`, multiplication `*=` and division `/=`. One more example:
```python
x = 5
x *= 3
print(x)
```

````

For example if you need to read the input until the empty string is passed you can use the following code:

```python3
inp_line = input()
while inp_line:
    print("Echo:", inp_line)
    inp_line = input()
```

Example of possible input-output:
```
Who
Echo: Who
You
Echo: You
Are
Echo: Are

```

### `continue` and `break`  statements

Sometimes, it is necessary to skip certain iterations or stop the entire loop. Python provides the `continue` and `break` statements to achieve this.

Let's take a look at some examples:
```{code-cell} ipython
:tags: ['hide-output']
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
In this example, we skip the remaining body of the loop if the number `i` is even.


In case you need to stop loop if some condition met:
```{code-cell} ipython
:tags: ['hide-output']
for i in range(10):
    if i > 5:
        break
    print(i)
```


Both `continue` and `break` work similar with `while` loop.


