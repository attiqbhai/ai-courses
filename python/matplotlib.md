# MatPlotLib PyPlot

---

## PyPlot

* matplotlib.pyplot is a sub-module of the Matplotlib library that provides a MATLAB-like interface for creating static, animated, and interactive visualizations in Python. 

* It is the most widely used data visualization tool in the Python data science ecosystem.

---

## Line Chart

* To create a basic chart, you provide X and Y coordinates as lists or NumPy arrays, call plt.plot(), and then display it with plt.show()

```python

import matplotlib.pyplot as plt

# 1. Define data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the line plot
plt.plot(x, y)

# 3. Add details
plt.title("Simple Line Plot")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

# 4. Render and show the plot
plt.show()

```

---

## Scatter Plot (Relationships)

* Used to show individual data points rather than connecting lines.

```python

plt.scatter(x, y, color='red', marker='o')
plt.show()

```

---

## Bar Chart (Categories)

```python

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
plt.bar(categories, values, color='skyblue')
plt.show()

```

---

## Histogram (Distributions)

```python

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, edgecolor='black')
plt.show()

```

---

## Customizing Your Plots

* You can control visual properties directly inside the plotting functions using keyword arguments:

  * **color:** 
    * Sets color (e.g., 'r', 'blue', '#FF5733').
  * **linestyle:** 
    * Changes line pattern (e.g., '--' for dashed, ':' for dotted).
  
  * **linewidth:** 
    * Adjusts line thickness (e.g., lw=3).
    
  * **marker:** 
    * Adds symbols to points (e.g., 'o', 's' for square, '*' for star).


```python

days = [1, 2, 3, 4, 5]
product_a = [10, 15, 12, 18, 20]
product_b = [8, 11, 14, 13, 19]

# Plot with custom styles and labels
plt.plot(days, product_a, color='green', linestyle='--', marker='o', label='Product A')
plt.plot(days, product_b, color='purple', linestyle='-', marker='s', label='Product B')

# Layout decorations
plt.title("Daily Product Sales")
plt.grid(True)     # Adds a grid background
plt.legend()       # Renders the label boxes

plt.show()


```