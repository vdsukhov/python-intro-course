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

# Introduction to Python

## Python Interpreter
Today, we will go through the process of installing Python on your computer. 
Python is a versatile and powerful programming language widely used for various applications. 
Before we begin, let's understand the concept of a Python interpreter (programm that we are going to install) and draw an analogy to real life.

A Python interpreter is like a translator between you and your computer. 
Imagine you're in a foreign country, and you want to communicate with the locals. 
However, you don't speak their language. 
So, you have a translator who understands both languages and can help you convey your thoughts effectively. 
Similarly, a Python interpreter translates the human-readable code you write into a language that your computer understands.

## Installation Process

### Step 1: Downloading the Python installer

Open your web browser and navigate to the official Python website: [https://www.python.org/](https://www.python.org/).
Go to *Downloads* tab.
I will install the default suggested Python version which in my case is `Python 3.11.4`.

### Step 2: Starting the Installation

Once the installer is downloaded, locate the file and run it.

```{admonition} Installation on Windows
Check the box that says "Add Python X.X to PATH" (X.X represents the version number). 
This option ensures that you can use Python from the command line.
```
### Step 3: Completing the Installation
Once the installation is complete, you'll see a screen that says "Setup was successful."
```{admonition} Installation on Windows
You can also opt to disable the path length limit by checking the box. This can be useful if you plan to work with deeply nested directories.
```

## Verifying the Installation

To ensure that Python is installed correctly, open a command prompt (Windows) or a terminal (macOS/Linux) and type 
```bash
python --version
```
or 
```bash
python3 --version
```
This should display the version of Python you installed.

Congratulations! 
You've successfully installed Python on your computer. 
Just like a translator facilitates communication between you and locals in a foreign land, the Python interpreter bridges the gap between your code and your computer's understanding. 