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
It never ceases to amaze me:

we all love ourselves more than other people, 

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

## `with` 
