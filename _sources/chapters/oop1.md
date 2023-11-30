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

### Interaction with namespaces

You can check namespaces using the `globals()`, `locals()` and `dir()` functions.
Let's explore each of them.



`globals()` function returns a dictionary representing the global namespace. 
When called within a function or at the module level, it provides access to the global namespace, allowing you to inspect or modify global variables.

```{code-cell} ipython3
:tags: ['hide-output']
global_variable = "I am global"

def check_globals():
    print(globals())

check_globals()
```

`locals()` returns a dictionary representing the local namepsace.
When called within a function, it provides access to the local namespace of that function, allowing you to inspect or modify local variables.
```{code-cell} ipython3
:tags: ['hide-output']
def check_locals():
    local_variable = "I am local"
    print(locals())

check_locals()
```

`dir` function returns a list of names in the current scope or a list of attributes of an object if an object is provided.
It's a versatile function. When used without arguments, it shows the names in the current scope. When used with an object as an argument, it lists the attributes of that object.

```python
print(dir())
```


## Classes

Let's create a simple class for a `Car` in Python. A class is a blueprint for creating objects, and it encapsulates both data (attributes) and behavior (methods) related to the object. In this case, we'll define a `Car` class with some basic attributes and methods.

We will use the following attributes to describe our class:
- `brand` - simply car brand 
- `model` - the model
- `year` - the year when car was assembled
- `color` - color of the car
- `fuel` - the current fuel level
-  `odometer` - the distance traveled by a vehicle
-  `doors_locked` - current doors status (i.e. locked or unloced)

```{code-cell} ipython3
:tags: ['hide-output']
class Car:
    def __init__(self, brand, model, year, color, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked
```
Here we defined our blueprint for objects using the `class` keyword. 
Think of a class as a template that outlines the structure and behavior of our objects.
Inside our class, we currently have one special method called `__init__`. 
This method is like a constructor and is used to create new instances (objects) of our class. It initializes the attributes of the object when it is first created.

Now, let's put our class to use by creating a couple of objects. These objects will be unique instances of the Car class, each with its own set of attributes.

```{code-cell} ipython3
:tags: ['hide-output']
camry = Car(brand="Toyota", model="Camry", year=2023, color="red")
tesla_x = Car(brand="Tesla", model="X", year=2023, color="black")
```

After specifying our objects, we can access their attributes by using a dot after the variable name and specifying the attribute name:
```{code-cell} ipython3
:tags: ['hide-output']
print("camry fuel level:", camry.fuel)
```

### `__init__` method

In Python, when we create a class, we use a special method called `__init__` to set up the initial state of the object.
This method is like a guidebook for creating new objects based on the class.

Now, here's the trick: when we define methods inside a class, we need a way to refer to object itslef.
That's where `self` comes in!

* What is `self`?
    * `self` is a convention (a tradition, you could say) in Python. It is like a placeholder that refers to the instance of the object that we are working with.
* Using `self`
    * When we create a new Car, like `camry = Car(brand="Toyota", model="Camry", year=2023, color="red")`, Python automatically passes `camry` as the `self` argument to the `__init__` method. So the `self.brand`, `self.model` and so on, refer specifically to the attributes of `camry`.


<video autoplay loop playsinline controls muted>
    <source src="../_static/videos/classes_init.mp4" type="video/mp4">
</video>

```{note}
You can consider the `__init__` method like the birthplace of an object in Python. At the beginning of this method, `self` is like an empty canvas - an object yet to be fully formed.
As we going through the `__init__` method, we are like architects adding features (attributes) to our object one by one.
```

### Class methodes

So far, we have explored the `__init__` method, and you may have observed that this particular method name includes leading and trailing double underscores. In Python, there are several reserved names that, when implemented, allow us to add additional functionality to our class. We will delve into more of these reserved names later in the course. However, we are not limited to using only these reserved methods. We have the flexibility to implement various custom methods of our own. Let's proceed by adding a couple of custom methods to our class.


```{code-cell} ipython3
:tags: ['hide-output']
class Car:
    def __init__(self, brand, model, year, color, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked
    
    def vehicle_status(self):
        """Prints the status of the car including all attributes."""
        print(f"Car Status:")
        print(f"-- Brand: {self.brand}")
        print(f"-- Model: {self.model}")
        print(f"-- Year: {self.year}")
        print(f"-- Color: {self.color}")
        print(f"-- Fuel Level: {self.fuel}%")
        print(f"-- Odometer: {self.odometer} miles")
        print(f"-- Doors: {'Locked' if self.doors_locked else 'Unlocked'}")

    def unlock(self):
        """Unlocks the doors of the car."""
        if self.doors_locked:
            print("Doors are now unlocked.")
            self.doors_locked = False
        else:
            print("Doors are already unlocked.")

    def lock(self):
        """Locks the doors of the car."""
        if not self.doors_locked:
            print("Doors are now locked.")
            self.doors_locked = True
        else:
            print("Doors are already locked.")
```

Here we implemented couple methods:
* `vehicle_status` prints the status of all attributes in a clear format
* `unlock` and `lock` methods handle the doors' locking status

Now let's call our methods:

```{code-cell} ipython3
camry = Car(brand="Toyota", model="Camry", year=2023, color="red")
camry.vehicle_status()
camry.unlock()
```

We could say that methods are functions that are associated with objects.
They are defined within a class and operate on instances (objects) of that class.
The crucial difference between methods and functions is that methods are linked to specific objects.
When you call a method, often it operates on the particular instance (object) it is associated with.
This connection enables objects to have behaviors tailored to their own state.
For example, a `Car` object might have a `start_engine` method that makes sense for cars but might not make sense for other objects.

When you execute a method with an object (`object.method()`), behind the scenes, it's like saying `Car.method(object)`. In this context, `self` refers to the instance of the object you're working with.

For a quick check, you can run the explicit version by specifying the class name directly. It's a way of saying, "Hey, this method is designed to work with this specific object."
```{code-cell} ipython3
Car.vehicle_status(camry)
```
The code above is same as `camry.vehicle_status()`. The idea is that we can run it directly using the object without always explicitly specifying the class name. As you can see, `self` corresponds to `camry` in this specific case.

### Class as a factory

Think of a class as a versatile factory capable of creating (instantiating) objects with distinct features. In the earlier example, our `Car` class allowed us to model and handle real-world objects — cars complete with their own attributes and behaviors.

In a broader sense, you can create different classes tailored to your specific needs, each with its own set of attributes and methods. For instance, imagine a class designed for working with gene expression data. Here, attributes might include a matrix of counts, while methods could encompass various normalizations and differential expression analysis techniques.

To underscore this concept, consider the popular Python package scanpy designed for the analysis of single-cell data. In scanpy, you encounter specific classes and data types crafted for the nuanced demands of single-cell analysis. These classes seamlessly handle various tasks, showcasing the adaptability and power of object-oriented programming.

### Sharable class attributes

We can create class attributes that will be shared among all instances of the class. For example, let's say we want to store the geographical location of our factory and have access to this information from any instance. Here is an example of how we can achieve this:

```{code-cell} ipython3
class Car:
    factory_location = "51.010406, 10.256190"
    def __init__(self, brand, model, year, color, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked

camry = Car(brand="Toyota", model="Camry", year=2023, color="red")
tesla_x = Car(brand="Tesla", model="X", year=2023, color="black")

print(camry.factory_location)
print(tesla_x.factory_location)
```

### Magic methods

Let's consider the following setup: we want to add a special attribute to cars that measures their horsepower. Now, let's say we have a list of different cars and we want to sort them based on their horsepower values. Ideally, we would like to use `sorted([car1, car2, car3])` to achieve this.

However, we cannot run this code right away because Python doesn't know how to compare our car objects. In order to sort our objects, we need to be able to compare them. Currently, if we try to compare our car objects, we will encounter an error.

```{code-cell} ipython3
class Car:
    def __init__(self, brand, model, year, color, horsepower, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked
        self.horsepower = horsepower


camry = Car(brand="Toyota", model="Camry", year=2023, color="red", horsepower=210)
tesla_x = Car(brand="Tesla", model="X", year=2023, color="black", horsepower=800)
```

Comparison `print(camry < tesla_x)` lead us to the following error:
```
TypeError: '<' not supported between instances of 'Car' and 'Car'
```

This is where magic methods come to our rescue. Basically, Python has a lot of reserved method names that, when implemented, add new possibilities for our objects.
In this specific case, we want to check whether the left object is less than the right one. To do this, we can implement a method with the name `__lt__`. Let's implement it:

```{code-cell} ipython3
class Car:
    def __init__(self, brand, model, year, color, horsepower, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked
        self.horsepower = horsepower
    def __lt__(self, other):
        return self.horsepower < other.horsepower


camry = Car(brand="Toyota", model="Camry", year=2023, color="red", horsepower=210)
tesla_x = Car(brand="Tesla", model="X", year=2023, color="black", horsepower=800)

print("Camry has higher power rather Tesla:", tesla_x < camry)
```

Now we can sort our objects in ascending order.
```{code-cell} ipython3
nissan_gtr = Car(brand="Tesla", model="X", year=2023, color="black", horsepower=565)
cars = [tesla_x, camry, nissan_gtr]
print(sorted(cars))
```

As you can see, the `sorted` method works without any problems.
However, the output doesn't make a lot of sense to us.
To address this, we can implement another magic method called `__repr__`.


```{code-cell} ipython3
class Car:
    def __init__(self, brand, model, year, color, horsepower, fuel=100, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.odometer = odometer
        self.doors_locked = doors_locked
        self.horsepower = horsepower
    def __lt__(self, other):
        return self.horsepower < other.horsepower
    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}"


camry = Car(brand="Toyota", model="Camry", year=2023, color="red", horsepower=210)
tesla_x = Car(brand="Tesla", model="X", year=2023, color="black", horsepower=800)
nissan_gtr = Car(brand="Nissan", model="GT-R", year=2023, color="black", horsepower=565)

cars = [tesla_x, camry, nissan_gtr]
print(*sorted(cars), sep='\n')
```

