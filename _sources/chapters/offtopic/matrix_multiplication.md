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

# Matrix Multiplication

In this section, I will cover matrix multiplication. My objective is to explain why the matrix multiplication $C = A \cdot B$ uses this expression to calculate the $c_{ij}$ entry:

$$
c_{ij} = a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{2j} + \ldots + a_{in} \cdot b_{nj} = \sum\limits_{k  = 1}^{n} a_{ik} \cdot b_{kj},
$$
where $A$ is an $(m \times n)$ matrix and $B$ is an $(n \times p)$ matrix.
```{code-cell} ipython3

```
