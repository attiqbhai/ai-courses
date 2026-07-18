# Series

---

## Introduction

* A Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.). 

* You can think of it as a single column in an Excel spreadsheet or a standard Python list but with a powerful, custom-labeled index.

---

## Creating a Series


```python

import pandas as pd
import numpy as np

# From a list (defaults to an integer index starting at 0)
prices = pd.Series([10.5, 24.0, 15.75])

# From a list with a custom index
temperatures = pd.Series([32, 28, 35], index=["Day 1", "Day 2", "Day 3"])

# From a dictionary (keys automatically become the index)
riddles = pd.Series({"Alice": 5, "Bob": 3, "Charlie": 8})

```

---

## Core Components: Index and Values

* A Series wraps both a sequence of values and a sequence of labels.

    * **.index:** 
      * Accesses the label array.
    * **.values:** 
      * Accesses the underlying NumPy array.
    * **.dtype:** 
      * Shows the data type of the internal elements.

```python

print(temperatures.index)   # Output: Index(['Day 1', 'Day 2', 'Day 3'], dtype='object')
print(temperatures.values)  # Output: [32 28 35]
print(temperatures.dtype)   # Output: int64

```

---

## Accessing Data (Indexing)

* You can retrieve elements using either position-based indexing or label-based indexing. 

* While standard bracket notation [] works, Pandas developers recommend using specific indexers for clarity:

  * **.iloc[]:** 
    * Strict positional (integer) indexing.
  
  * **.loc[]:**
    * Strict label-based indexing.

```python

# Position-based
print(temperatures.iloc[0])   # Output: 32

# Label-based
print(temperatures.loc["Day 2"]) # Output: 28

```

---

## Vectorized Operations & Filtering

* Unlike standard Python lists, you can perform math operations on an entire Series at once without writing loops.

  * **Vectorized Math:** 
    * Multiplies or modifies every single item.

  * **Boolean Masking:**
    * Filters data based on a true/false condition.

```python

# Multiply all temperatures by 2
double_temps = temperatures * 2 

# Filter for temperatures strictly greater than 30
hot_days = temperatures[temperatures > 30] 
print(hot_days)
# Output:
# Day 1    32
# Day 3    35

```

---

## Handling Missing Data

* Pandas naturally flags missing data using NaN (Not a Number). 

* You can quickly locate and sum up missing values:

```python

baking_log = pd.Series([12, np.nan, 15, np.nan])

print(baking_log.isnull())       # Returns a True/False series identifying NaNs
print(baking_log.isnull().sum()) # Output: 2 (counts the total empty cells)


```
