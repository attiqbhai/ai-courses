# Calculus for Machine Learning

## Machine Learning House

<img src="images/machine-learning-house.jpeg" alt="machine-learning-house" style="width: 400px;">

---

## What Calculus Is

* Mathematical study of continuous change
* Two branches:
  * Differential calculus: focus of Calculus I
  * Integral calculus: a focus of Calculus II class

---

## What Differential Calculus Is

* Study of rates of change
* Consider a vehicle traveling some distance d over time t:

<img src="images/car-on-road.jpeg" alt="car-on-road" style="width: 400px;">

<img src="images/car-on-road-stopped-at-shop.jpeg" alt="car-on-road-stopped-at-shop" style="width: 400px;">

---

## Calculus of the Infinitesimals

* As integral accuracy improves as we approach an infinite-sided polygon, so too does differential accuracy improve as we approach a curve infinitely closely:

<img src="images/calculus-of-infinitesimals.jpeg" alt="calculus-of-infinitesimals" style="width: 700px;">

---

## Limits - Continuous function

* Trivially easy to calculate for a continuous function, e.g.:
  * What is the limit as x approaches 5 in the expression 2x<sup>2</sup> + 2x + 2 ?

 <img src="images/contineous-functions.jpeg" alt="contineous-functions" style="width: 700px;">

---

## Limits - DisContinuous function

* Some functions are not contineous
* In below function, we can't calculate y, if x = 1.
* It means. line breaks when x = 1. That makes it DisContinuous function.

 <img src="images/discontineous-functions.jpeg" alt="discontineous-functions" style="width: 700px;">

---

## Limits - Refactoring

* In some cases, we can solve the limit through algebra, e.g., factoring.

 <img src="images/limits-refactoring.jpeg" alt="limits-refactoring" style="width: 700px;">

---

## Limits - Refactoring Not an option

* In other cases, we can't use algebra, but approaching the limit still works:

 <img src="images/limits-refactoring-not-possible.jpeg" alt="limits-refactoring-not-possible" style="width: 700px;">

---

## Derivative

* A derivative is the instantaneous rate of change of a function. 

* It tells you exactly how fast something is changing at one precise moment, rather than over a period of time.

* Geometrically, if you look at a graph, the derivative represents the exact slope of the tangent line touching the curve at a single point.

---

## Delta Method (or differentiation from first principles)

* Delta Method is the foundational calculus technique used to find a function's derivative. 
* It calculates the exact slope of a curve at any point by finding the limit of the average rate of change as **the change in x approaches zero.**

* Δx --> 0 : You read this as change in x approaches zero.

<img src="images/delta-method.jpeg" alt="delta-method" style="width: 700px;">

---

## Slope

* Slope is a measure of the steepness and direction of a line. 

* It quantifies how much a vertical value changes compared to a horizontal value.

* In simple terms, slope tells you how steep a hill is and whether it goes up or down.

### Core Meanings of Slope

* **Rise Over Run:** The ratio of vertical change to horizontal change between any two points on a line.

* **Rate of Change:** How fast the dependent variable (y) changes for every single unit increase in the independent variable (x).

### Direction Indicator

* **Positive slope:** The line climbs from left to right.

* **Negative slope:** The line falls from left to right.

* **Zero slope:** The line is perfectly flat and horizontal.

* **Undefined slope:** The line is perfectly straight up and down (vertical).

### Formula

* The formula for the slope of a straight line passing through two points (x <sub>1</sub>, y <sub>1</sub>) and (x <sub>2</sub>, y <sub>2</sub>) is **"rise over run."**

* Mathematically, it is written as:

  $m = \frac{y_2 - y_1}{x_2 - x_1}$

* Key Terms ($m$): 
  * The standard symbol used for slope.
  * $(y_2 - y_1)$: The vertical change (rise).
  * $(x_2 - x_1)$: The horizontal change (run).

---

## Derivative of a Constant

* Assuming c is constant:
  * $m = \frac{d}{dx}$ c = 0

* **Intuition:** A constant has no variatio, so it's slope is nothing/zero.
  * $m = \frac{d}{dx}$ 25 = 0

---

## Derivatives: Power Rule

* The Power Rule is a fast shortcut in calculus used to find the derivative of a variable raised to a exponent (a power). 

* It eliminates the need to use the long, multi-step delta method every time you want to find a slope.

#### The Formula 

* If your function is   
    $f(x) = x^n$,  
Where n is any real number, the derivative is:  

  $f^{\prime }(x)=n\cdot x^{n-1}$

  Or

  $\frac{d}{dx} x^n = n\cdot x^{n-1}$

#### The Two-Step Rule

To apply the formula, follow these two quick steps:

1. Bring the power to the front (multiply the variable by the original exponent n).
2. Subtract 1 from the power (the new exponent becomes n-1).

<img src="images/power-rule.jpeg" alt="power-rule" style="width: 400px;">

---

## Constant Product/Multiple/Multiplication Rule

* The derivative of a constant multiplied by a function is equal to the constant multiplied by the derivative of that function

* Essentially, a constant attached to a variable behaves like a "passenger"; it sits outside the differentiation process untouched, and then multiplies the final result at the very end.

#### The Formula

$\frac{d}{dx} [c\cdot f(x) ] = c\cdot \frac{d}{dx} [f(x)]$

OR

$\frac{d}{dx} (c\cdot y) = c\cdot \frac{d}{dx} (y) = c\cdot \frac{dy}{dx}$

<img src="images/constant-product-rule.jpeg" alt="constant-product-rule" style="width: 500px;">

---

## Sum Rule

* The Sum Rule in calculus states that the derivative of a sum of two or more functions is simply the sum of their individual derivatives.

* In plain terms, when you have a long polynomial expression with terms separated by plus signs, you do not need to do anything fancy. 

* You just find the derivative of each part separately, one by one, and keep the plus signs between them.

* The rule works exactly the same way for subtraction, which is known as the Difference Rule.

#### The Formula

$\frac{d}{dx} [f(x) + g(x)] = f^{\prime} (x) + g^{\prime} (x)$

OR

$\frac{d (y + w)}{dx} = \frac{dy}{dx} +  \frac{dw}{dx}$

<img src="images/sum-rule.jpeg" alt="sum-rule" style="width: 500px;">

---

## Product Rule

* The Product Rule is the calculus formula used to find the derivative when two different functions are multiplied together.

* A common trap in calculus is assuming you can just multiply the individual derivatives together. That does not work. Because both parts of the function are changing at the same time, they affect each other's rates of growth.

#### The Formula

$\frac{d}{dx} [f(y) \cdot f(w)] = f^{\prime }(x) \cdot f(w) +  f(x) \cdot f^{\prime }(w)$


<img src="images/product-rule.jpeg" alt="product-rule" style="width: 600px;">

---

## Quotient Rule / Fraction Rule

* The Quotient Rule is the calculus shortcut used to find the derivative when one function is divided by another function (a fraction).

* Just like multiplication, you cannot simply divide the derivative of the top by the derivative of the bottom. Because both the numerator and the denominator are changing at the same time, you must use a specific formula to balance their rates of change.

#### The Formula

* If your function is a fraction, $\frac{f(x)}{g(x)}$, the derivative is:

  $\frac{d}{dx} [\frac{f(x)}{g(x)}] = \frac{f^{\prime }(x) \cdot g(x) -  f(x) \cdot g^{\prime }(x)}{[g(x)]^{2}}$



<img src="images/quotient-rule.jpeg" alt="quotient-rule" style="width: 600px;">

---

## Chain Rule

* The Chain Rule is the calculus formula used to find the derivative of a composite function. A composite function is a "function inside a function"—like a set of nesting Russian dolls.

* You need the Chain Rule whenever an algebraic operation is wrapped inside another operation

### The Formula

* If your function is $y = f(g(x))$, where f is the outer function and g is the inner function, the derivative is:

  $\frac{dy}{dx} = f^{\prime }(g(x)) \cdot g^{\prime }(x)$

* In plain words, the process follows a strict two-step routine:
  1. Differentiate the outside layer, leaving the inside layer completely alone.
  2. Multiply by the derivative of the inside layer. 


<img src="images/chain-rule.jpeg" alt="chain-rule" style="width: 700px;">

<img src="images/chain-rule-example.jpeg" alt="chain-rule-example" style="width: 700px;">

---

## Power Rule on a Function Chain


<img src="images/powerrule-on-function-chain.jpeg" alt="powerrule-on-function-chain" style="width: 700px;">

---

## Automatic Differentiation

* A.K.A.: autodiff or autograd
  * Computational diff.
  * Reverse mode diff.
  * Algorithmic diff.
* Distinct from classical methods:
  * Numerical diff. (delta method; introduces rounding errors)
  * Symbolic diff. (algebraic rules; computationally inefficient)
* Relative to classical methods, better handles:
  * Functions with many inputs (common in ML)
  * Higher-order derivatives


* Application of chain rule (typically partial derivative) to
sequence (forward pass) of arithmetic operations
* Whereas chain rule by hand typically begins at most-nested function, autodiff proceeds from outermost function inward
* Small constant factor more compute than forward pass (at most)

---

## Multivariate Functions

* Even in a simple regression such as y = mx + b:
  * y is a function of multiple variables
  * -- in this case, m and b.
* Therefore, we can't calculate the simple derivative $\frac{dy}{dm}$ or $\frac{dy}{db}$.

---

## Partial Derivatives

* Enable the calculation of derivatives of multivariate equations.

* A partial derivative is the derivative of a multivariable function when you change only one variable at a time while holding all other variables constant.

* A partial derivative measures how a multivariable function changes when you tweak one variable while holding all others completely constant. 

* You use the symbol ∂ (often called "del" or "partial") instead of d. It is essentially regular calculus, but you treat other letters like regular numbers.

#### The Golden Rule

* When differentiating with respect to x, treat all other variables (like y or z) as constants. When differentiating with respect to y, treat all other variables as constants.

#### Let's Try an Example

1. Imagine you run a shop and your profit, P, depends on the price of two items, x and y. Your profit equation is:  
  $P(x, y) = 3x² + 5xy + 2y³$

2. **Find the partial derivative with respect to x (written as $\frac{\partial P}{\partial x}$)**. 

    To do this, treat y as if it were a normal number:

    * The derivative of $3x²$ is 6x.

    * In the term $5xy$, $5y$ acts as a constant multiplier attached to $x$. The derivative of $x$ is 1, so it leaves just $5y$.

    * The term $2y³$ has no $x$ in it at all. It is entirely a constant, so its derivative is $0$.  

       $\frac{\partial P}{\partial x} = 6x + 5y$

3. **Find the partial derivative with respect to y (written as $\frac{\partial P}{\partial y})$**

    Now, we do the exact opposite. Treat x as a constant and y as the variable:

    * The term 3x² has no y, so its derivative is 0.
    * In $5xy, 5x$ acts as a constant multiplier. The derivative of y is 1, leaving $5x$.
    * The derivative of $2y³$ is $6y²$ (using the standard power rule).

      $\frac{\partial P}{\partial y} = 5x + 6y^2$
---

## Single-point regression 

* Single-point regression (often referred to as Simple Linear Regression) is the simplest machine learning or statistical modeling technique. 
* It uses exactly one independent variable (input) to predict a continuous dependent variable (output) by fitting a straight line, defined by the formula:  
$y = mx + b$
* Where:
  * y is the predicted value (dependent variable)
  * x is your input (independent variable)
  * m is the slope (how much y changes for each unit of x)
  * b is the y-intercept (where the line crosses the y-axis)

---

## Quadratic Cost

* A quadratic cost (or quadratic cost function) calculates how wrong a model or system is by squaring the errors. 
* Because it uses a squared term, it heavily penalizes large mistakes while treating small ones as negligible.
* It is widely used in Machine Learning, Economics, and Control Systems for optimization.

#### The Core Math

* The general formula for a quadratic cost is:  

  $C(x) = ax² + bx + c$

* Where:
  * a, b, and c are constants that define the curve's shape and fixed costs.
  * x is your input variable (e.g., number of items produced, or the difference between a prediction and reality).

---

## Backpropagation

* Backpropagation is the core algorithm that allows neural networks to "learn" from their mistakes. 

* It works by calculating how much every single weight and bias in the network contributed to the final output error. 

* By measuring this contribution, the network can adjust its parameters to make more accurate predictions next time.

#### The Two-Pass Learning Process

* Neural network training consists of two main steps:
  * **The Forward Pass:** 
    * Information (like an image or numerical data) goes into the network. 
    * The network guesses an answer (e.g., "This image is a dog"), and we measure how wrong that guess is using a mathematical formula called a loss function.
  * **The Backward Pass (Backpropagation):**
    * The network takes the calculated error at the end and "backpropagates" it through the network layer by layer. 
    * It uses a calculus formula known as the chain rule to trace backward and figure out exactly how much each specific weight and bias influenced the error.

---

## Gradient

* The gradient is simply the multi-variable version of a derivative. 
* While a derivative tells you the slope and rate of change for a function with only one variable, a gradient packs the derivatives of all individual variables together into a single vector to show the overall slope in multi-dimensional space.

#### From Derivative to Gradient

* **Single Variable (x):** If you have a function like $f(x) = x²$, the derivative $f'(x) = 2x$ tells you how much $f(x)$ changes when you nudge x. It only points left or right along a flat number line.
* **Multiple Variables (x, y, z):** If your function depends on multiple inputs, like $f(x, y) = x² + y²$, you can no longer find a single overall slope with standard calculus. Instead, you look at one variable at a time while holding the others perfectly still.

---

## Understanding the Difference: The Gradient vs. Gradient Descent (The "Hiker")

* **The Gradient (The "Slope"):** 
  * In simple single-variable math, the derivative tells you the slope of a line. 
  * When dealing with multiple variables at once, you collect all those individual slopes into a single vector called the gradient. 
  * The gradient always points directly uphill toward the steepest path.
* **Gradient Descent (The "Hiker"):** 
  * This is the actual strategy or algorithm. 
  * Because the gradient points uphill, the algorithm multiplies the gradient by a negative number to face directly downhill.
  * It then takes a small step downward, recalculates the new slope, and repeats the process until it reaches the bottom of the valley.