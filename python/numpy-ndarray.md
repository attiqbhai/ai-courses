# NumPy (Numerical Python) ndArray

---

## Introduction

* The NumPy ndarray (N-dimensional array) is a fast, multi-dimensional container of items that are all of the same data type and size. 

* It is the foundation of data science and machine learning in Python because it runs up to 50x faster than traditional Python lists by storing data continuously in memory.

---

## Creating an ndarray

* You should rarely instantiate an ndarray using its low-level class constructor. 

* Instead, you use helper functions provided by the NumPy Library.

* **From Python Sequences:** 
  * Pass a list or a tuple directly into np.array()

* **Built-in Initializers:** 
  * Generate arrays of specific sizes filled with placeholders.

```python

import numpy as np

# Create a 1D array (from a list)
arr_1d = np.array([1, 2, 3, 4])

# Create a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 3x4 array filled entirely with zeros
zeros_arr = np.zeros((3, 4))

# Create a 2x2 array filled with random numbers
random_arr = np.random.default_rng().random((2, 2))

```