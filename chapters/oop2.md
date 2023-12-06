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

## Inheritance

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



