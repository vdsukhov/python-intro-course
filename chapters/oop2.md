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

# Object-Oriented Programming (Part 2)

As a quick recap, we've discovered that in Python, classes serve as blueprints, outlining both the structure and behavior of objects. Objects, in turn, are instances of these classes, embodying real-world entities.

## Inheritance: superclass and subclass

In this episode, our focus shifts to a powerful OOP concept—inheritance. Imagine our familiar `Car` class; today, we'll delve into how we can extend and refine its features.

```{code-cell} ipython3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}"

camry = Car(brand="Toyota", model="Camry")
```

Inheritance allows us to build on existing classes. We'll explore how a new class (a subclass) can inherit attributes and methods from an existing class (a superclass). This elegant mechanism not only fosters code reuse but also establishes a hierarchy that mirrors real-world relationships.

```{code-cell} ipython3
class ElectricCar(Car):
    def __init__(self, brand, model, battery_level=100):
        Car.__init__(self, brand, model)
        self.battery_level = battery_level
tesla_s = ElectricCar(brand="Tesla", model="Model S")

print(tesla_s)

```

In the example above, notice that we didn't explicitly define the `__str__` method in the subclass. Instead, we inherited it from the superclass. This illustrates a fundamental aspect of inheritance, where the subclass can acquire and use methods defined in the superclass without having to redefine them.

If our superclass included additional specialized methods, the subclass would automatically have access to them as well. This underscores the efficiency of inheritance, allowing us to leverage a set of common functionalities from a superclass while maintaining the flexibility to extend or override them in the subclass.


'd like to highlight a crucial concept: the ability to leverage the code specified in a superclass. To illustrate this, let's enhance the complexity of our superclass:
```{code-cell} ipython3
:tags: ['hide-output']
class Car:
    def __init__(self, brand, model, year, color, odometer=0, doors_locked=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.odometer = odometer
        self.doors_locked = doors_locked
    
    def vehicle_status(self):
        """Prints the status of the car including all attributes."""
        print(f"Car Status:")
        print(f"-- Brand: {self.brand}")
        print(f"-- Model: {self.model}")
        print(f"-- Year: {self.year}")
        print(f"-- Color: {self.color}")
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
In our previous episode, we implemented the `Car` class. Now, let's revisit that and extend our exploration by creating an `ElectricCar` class, inheriting from the existing `Car` class:

```{code-cell} ipython3
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_level=100, odometer=0, doors_locked=True):
        Car.__init__(self, brand, model, year, color, odometer, doors_locked)
        self.battery_level = battery_level

tesla_s = ElectricCar("Tesla", "Model S", 2023, "Black")
```

Now, we can make use of all the methods that we've defined in the `Car` class:

```{code-cell} ipython3
tesla_s.vehicle_status()
tesla_s.unlock()
tesla_s.vehicle_status()
```

Now, we have the opportunity to define specific methods exclusive to the `ElectricCar` class. These methods will be accessible only for instances of the `ElectricCar` class:
```{code-cell} ipython3
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_level=100, odometer=0, doors_locked=True):
        Car.__init__(self, brand, model, year, color, odometer, doors_locked)
        self.battery_level = battery_level

    def battery_status(self):
        print(f"Battery level: {self.battery_level}")

tesla_s = ElectricCar("Tesla", "Model S", 2023, "Black")
tesla_s.battery_status()
```


## Default inheritance

In Python, everything is treated as an object. Let's explore this concept by creating an empty class, avoiding any manually specified methods or attributes:

```{code-cell} ipython3
class EmptyClass:
    pass
```
In the snippet above, the `pass` keyword allows us to create a minimal class without implementing any specific functionality. 
Now, let's inspect what kind of attributes and methods are associated with an instance of our `EmptyClass`:

```{code-cell} ipython3
obj = EmptyClass()
print(dir(obj))
```
Upon running this, you'll observe a myriad of names associated with our object. 
This abundance is due to the fact that, by default, any class in Python is implicitly a subclass of a superclass known as the `object` class.
This inheritance from the `object` class provides a set of default attributes and methods to every class, contributing to the comprehensive list we see when querying the instance.

## Multiple inheritance

In Python, our flexibility extends beyond inheriting from just one class. 
We have the capability to utilize multiple classes as superclasses for a single subclass. 
Let's examine the following example:

```{code-cell} ipython3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
 
        
class Convertible(Car):
    def __init__(self, brand, model, roof_open=False):
        Car.__init__(self, brand, model)
        self.roof = roof_open
        
    def open_roof(self):
        if not self.roof:
            print("Roof now is open")
            self.roof = True
        else:
            print("Roof is already open")
    
    def close_roof(self):
        if self.roof:
            print("Roof now is closed")
            self.roof = False
        else:
            print("Roof is already closed")

class HybridCar(Car):
    def __init__(self, brand, model, battery_level=100):
        Car.__init__(self, brand, model)
        self.battery_level = battery_level

    def charge_battery(self):
        print("Battery was charged")
        self.battery_level = 100

class HybridConvertible(Convertible, HybridCar):
    def __init__(self, brand, model, roof_open=False, battery_level=100):
        # Call constructors of both parent classes
        Convertible.__init__(self, brand, model, roof_open)
        HybridCar.__init__(self, brand, model, battery_level)

# Creating an instance of HybridConvertible
hybrid_convertible = HybridConvertible(brand="Toyota", model="Prius Convertible", battery_level=50)
print(f"Battery Level: {hybrid_convertible.battery_level}")
print(f"Current roof status: {'Open' if hybrid_convertible.roof else 'Closed'}")

# Accessing methods from both parent classes
hybrid_convertible.open_roof()      # From Convertible class
hybrid_convertible.charge_battery()  # From HybridCar class

print(f"Battery Level: {hybrid_convertible.battery_level}")
print(f"Current roof status: {'Open' if hybrid_convertible.roof else 'Closed'}")
```
In this example:

* The `Car` class represents base class.
* The `Convertible` class inherits from `Car` and adds specific methods `open_roof` and `close_roof`.
* The `HybridCar` class also inherits from `Car` and adds a specific method `charge_battery`.
* The `HybridConvertible` class inherits from both `Convertible` and `HybridCar`, showcasing multiple inheritance.

Instances of `HybridConvertible` can access methods from all the parent classes, demonstrating the flexibility and power of multiple inheritance.

## Method Resolution Order (MRO)

In Python, when we encounter multiple inheritance, it's not uncommon to have the same method names defined in different parent classes. 
This can pose a challenge: which method should be called when we invoke it on an instance of a subclass? 
To address this, Python uses the Method Resolution Order (MRO) to establish a systematic sequence for searching and determining the order in which methods are resolved.

Here are the key points about the Method Resolution Order:

**1. Depth-First, Left-to-Right (DRLR):**

By default, Python follows a depth-first, left-to-right approach for method resolution. This means that it first looks in the current class, then in its superclass (from left to right), and continues this pattern until it finds the desired method or attribute.

**2. `__mro__` attribute:**

You can access the MRO of a class using the `__mro__` attribute or the `mro()` method.
This provides a tuple representing the order in which Python searches for methods.

```{code-cell} ipython3
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)

```

**3. C3 Linearization Algorithm:**

Python employs the C3 Linearization Algorithm to determine the MRO. 
This algorithm ensures consistency and avoids ambiguity in the order of method resolution.
If you want to look at some details then click <a href="https://w.wiki/8QM2" target="_blank">here</a>.

**4. Diamond Inheritance Issue:**

In scenarios where there's a diamond-shaped inheritance (e.g., class D inherits from both B and C, which both inherit from A), the MRO prevents ambiguity by following the DRLR approach.

```{code-cell} ipython3
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

instance_d = D()
instance_d.method()  # Outputs "B method" due to the MRO

```

In this example, the MRO ensures that the method from class B takes precedence over the method from class C.


```{note}
Understanding the Method Resolution Order is crucial, especially in complex class hierarchies involving multiple inheritance, as it helps predict which method or attribute will be accessed when called on an instance of a class.
```


## `super()` method

The `super()` method in Python is used to call a method from a parent or superclass. It is often employed within the context of inheritance, where a subclass wants to invoke a method that is defined in its superclass. Here's a breakdown of the `super()` method:

**Usage in the `__init__` Method:**

A common use case is within the `__init__` method of a subclass. This allows the subclass to initialize its own attributes and then call the `__init__` method of the superclass to handle its specific initialization.

```{code-cell} ipython3
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, additional_info):
        super().__init__(name)
        self.additional_info = additional_info

```

In this example, `super().__init__(name)` calls the `__init__` method of the `Parent` class, allowing the `Child` class to inherit the name attribute.

**Passing Arguments:**

You use `super()` without arguments when you're working within a class and Python dynamically figures out the appropriate superclass to call. 
If you need to be more explicit, you can pass the class and instance explicitly to `super()`.

```{code-cell} ipython3
class Parent:
    def some_method(self):
        print("Parent method")

class Child(Parent):
    def some_method(self):
        super().some_method()
        print("Child method")

```

In this example, `super().some_method()` calls the `some_method` of the `Parent` class, allowing the `Child` class to extend or override the behavior.

**Multiple Inheritance:**

`super()` is particularly useful in multiple inheritance scenarios, where a class inherits from more than one superclass. 
It ensures that methods are called in the correct order in the inheritance chain.

```{code-cell} ipython3
class A:
    def some_method(self):
        print("A method")

class B(A):
    def some_method(self):
        print("B method")
        super().some_method()

class C(A):
    def some_method(self):
        print("C method")
        super().some_method()

class D(B, C):
    pass

instance_d = D()
instance_d.some_method()

```

Here, `super().some_method()` ensures that the method is called from the next class in the method resolution order (MRO).

```{note}
The `super()` method is a powerful tool for maintaining a clean and consistent structure in code that involves inheritance. It fosters code reuse and supports the principles of modularity and extensibility in object-oriented programming.
```

## `isinstance` function

The isinstance() method in Python is used to check whether an object is an instance of a particular class or a tuple of classes. It returns `True` if the object is an instance of any of the specified classes; otherwise, it returns `False`. Let's use our `Car` class as an example:

```{code-cell} ipython3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

# Creating instances of Car and ElectricCar
regular_car = Car(brand="Toyota", model="Camry")
electric_car = ElectricCar(brand="Tesla", model="Model S", battery_capacity=100)

# Using isinstance to check object types
print(isinstance(regular_car, Car))          # True
print(isinstance(regular_car, ElectricCar))  # False

print(isinstance(electric_car, Car))         # True
print(isinstance(electric_car, ElectricCar)) # True

```

In this example:

* `isinstance(regular_car, Car)` checks if `regular_car` is an instance of the `Car` class, which is true.
* `isinstance(regular_car, ElectricCar)` checks if `regular_car` is an instance of the `ElectricCar` class, which is false.
* `isinstance(electric_car, Car)` checks if `electric_car` is an instance of the `Car` class, which is true because `ElectricCar` is a subclass of `Car`.
* `isinstance(electric_car, ElectricCar)` checks if `electric_car` is an instance of the `ElectricCar` class, which is true.

This method is useful for checking the type of an object before performing certain operations, especially in scenarios involving inheritance and polymorphism.


### `type` vs `isinstance`

The `type()` and `isinstance()` functions in Python are used to determine the type or class of an object, but they differ in their use cases.
The `type()` function is used to get the type of an object. It returns the type as a class object.

```{code-cell} ipython3
print(type(electric_car))
```

It can also be used to compare the type of an object with a specific type.
```{code-cell} ipython3
print(type(electric_car) == ElectricCar)  # True
print(type(electric_car) == Car)  # False
```

However, using `type()` for checking types in the context of inheritance can be less flexible, especially when dealing with subclasses.

In summary, while both `type()` and `isinstance()` can be used to check the type of an object, `type()` is more straightforward and is mainly used for direct type checking, whereas `isinstance()` is more versatile, considering inheritance relationships and often used in scenarios involving polymorphism and class hierarchies.


## `issubclass` function

The `issubclass()` function in Python is used to check if a class is a subclass of another class. 
It returns `True` if the first class is a subclass of the second class, and `False` otherwise. Here's an explanation:
```{code-cell} ipython3
class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

# Using issubclass to check class relationships
print(issubclass(Car, Vehicle))          # True
print(issubclass(ElectricCar, Car))      # True
print(issubclass(ElectricCar, Vehicle))  # True
print(issubclass(Vehicle, Car))          # False
```

In this example:

* `issubclass(Car, Vehicle)` checks if `Car` is a subclass of `Vehicle`, which is true.
* `issubclass(ElectricCar, Car)` checks if `ElectricCar` is a subclass of `Car`, which is true.
* `issubclass(ElectricCar, Vehicle)` checks if `ElectricCar` is a subclass of `Vehicle`, which is true because it indirectly inherits from `Vehicle` through `Car`.
* `issubclass(Vehicle, Car)` checks if `Vehicle` is a subclass of `Car`, which is false.

```{note}
The `issubclass()` function is particularly useful when dealing with class hierarchies and inheritance. It allows you to check the relationship between two classes and determine whether one is derived from another. This function is often used in scenarios where you need to ensure the compatibility or hierarchy of classes in your code.
```
