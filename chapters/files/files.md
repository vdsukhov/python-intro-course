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
# File Handling

In this episode we will cover some aspects of working with files in Python.


## File

A computer file is a collection of data that is stored as a single unit and is identified by a filename. The data within a file is organized in a specific format or structure, and this organization is defined by a file format.

The term "byte" refers to a unit of digital information that consists of 8 bits. Files are composed of bytes, and the arrangement and interpretation of these bytes are dictated by the file format. Different types of files (such as text files, image files, or executable files) have different rules and structures for how the bytes are organized.

I will categorize files into two distinct groups:
1. Text files
2. Binary files

The key distinction between these two types lies in how the data is represented and stored within the files.


1. Text Files:
    * **Content:** Text files contain human-readable text and are often used to store plain text documents.
    * **Character Encoding:** Text files use character encoding (e.g. ASCII, UTF-8) to represent characters.
    * Examples: `.txt`, `.html` `.css`
2. Binary files:
    * **Content:** Binary files contain non-human readable data, which may include images, audio, video, or program executables.
    * **Representation:** Binary files store data in a format not directly interpretable by humans. They may include a combination of text and binary data.
    * **Examples:** `.jpg`, `.mp3`, `.exe`
    

## File Path

To work with files in Python, it is important to have some basic knowledge about paths within the operating system. Assuming that you are already familiar with this concept, let's proceed.



## Opening and closing files in Python

To open file inside of Python program we can use built-in function `open`.
Let's create the text file `quote.txt` with following content:

```{admonition} File Content
It never ceases to amaze me:\
we all love ourselves more than other people,\
but care more about their opinion than our own.
```

Now to work with this file inside of Python we can use the following syntax:
```{code-cell} ipython3
file = open("./quote.txt", "r")
```
Here, the first argument specifies the relative path to the file, and the second argument specifies the mode used for reading the file.
Here are the different modes available in Python:

1. `r` - read file
2. `w` - write file
3. `rb` - read binary file
4. `wb` - write binary file
5. `a` - append to file


```{warning}
We've covered the process of opening files, and it's important to note that, before extracting data, understanding how to properly close files is essential. Closing files in Python is vital for efficient resource management. When a file is opened, system resources are allocated, and neglecting to close it can result in leaks and unpredictable behavior. It is crucial to adhere to proper file-handling practices to ensure optimal resource utilization and maintain the integrity and reliability of the code. <a href="https://realpython.com/why-close-file-python/" target="_blank">Here</a> you can read more about why it is important to close files.
```


```{code-cell} ipython3
file.close()
```

## `with` statement
However, in Python there's a cool trick that lets you forget about remembering to close files.
It is the `with` statement that provides a concise and clean way to work with external resources, such as files. 
Its primary purpose is to simplify resource management, ensuring that acquired resources are properly and automatically released, even if an exception occurs during the execution of the code block. 
When it comes to file handling, the with statement is particularly advantageous.

```{code-cell} ipython3
with open("./quote.txt", "r") as inp_f:
    print(inp_f)
```

## Working with text files in Python

### Reading

Excellent! With our understanding of file manipulation in Python, we're ready to delve into extracting data from text files within the Python environment. Let's begin by exploring the methods available to achieve this goal:
- The `read()` method returns the specified number of bytes from the file. Default is -1 which means the whole file.
- The `readline()` method returns one line from the file. You can also specified how many bytes from the line to return, by using the size parameter.

Let's take a closer look on both of them
```{code-cell} ipython3
with open("./quote.txt", "r") as inp_f:
   print(inp_f.read())
```

In this instance, we utilize the `read` method to access the entire file. Feel free to experiment by specifying the size of the file in bytes that you wish to read, rather than reading the entire file.

```{code-cell} ipython3
with open("./quote.txt", "r") as inp_f:
   line_1 = inp_f.readline().strip()
   line_2 = inp_f.readline().strip()
   print(f"line_1: {line_1}")
   print(f"line_2: {line_2}")
```
Here I used the `strip()` method to trim the new line symbol which is by default returned in the `readline()` method.

If you prefer to iterate over each line in your file, you can achieve this using a `for` loop in the following manner:
```{code-cell} ipython3
with open("./quote.txt", "r") as inp_f:
   for line in inp_f:
       print(f"current line: {line.strip()}")
```

```{note}
Using a `for` loop to iterate over each line of a file is advantageous for several reasons. It promotes memory efficiency by processing one line at a time, making it suitable for large files. The lazy loading approach allows incremental processing without loading the entire file into memory. This method is more performant for certain operations and supports a streaming approach, enabling real-time data processing. In contrast, the `read` method loads the entire content into memory, which can be inefficient for large files. Therefore, when dealing with files, particularly those with substantial data, the `for` loop provides a more resource-friendly and responsive solution.
```

### Writing

Now, let's explore the process of creating a new file and adding content to it:
```python
"""
Embrace what you cannot change, 
and focus your energy 
on mastering what lies within your control.
"""
```

```python
text = """
Embrace what you cannot change, 
and focus your energy 
on mastering what lies within your control.
"""

with open("./out.txt", "w") as out_f:
    out_f.write(text.strip())
```
After executing this code snippet, you will discover that a new file has been successfully created in your current working directory, named `out.txt`. The main distinction from previous examples lies in the use of the argument `"w"`, which signifies that the file is opened in write mode. This allows you write content in the file as needed.
It's crucial to note that if the file already existed, executing this code will result in the loss of any information it previously contained. To demonstrate this, let's rerun our program with a slightly modified variable, `'text'`

```python
text = """
Have I been made for this, to lie under the blankets and keep myself warm?
"""

with open("./out.txt", "w") as out_f:
    out_f.write(text.strip())
```

As you can see we completly lost our previous text.
In case you want to append new information to existed file you can use the `"a"` argument.

```python
text = """
Embrace what you cannot change, 
and focus your energy 
on mastering what lies within your control.
"""

with open("./out.txt", "a") as out_f:
    out_f.write(text.rstrip())
```


