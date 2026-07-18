# Pandas DataFrame

---

## Introduction

* A Pandas DataFrame is a two-dimensional, size-mutable, and tabular data structure with labeled axes (rows and columns), exactly like an Excel spreadsheet or a SQL table. 

* It is the most fundamental tool for data analysis and data science in Python.

---

## Creating a DataFrame

```python

# Define the dictionary data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 22],
    "City": ["New York", "London", "Paris", "San Francisco"]
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)

```