# Probability and Statistics For Machine Learning
---

## What Probability Theory Is

* Mathematical study of processes that include uncertainty
* Probabilities expressed over range of 0 (will not happen) to 1 (will happen)
* Enables models of future non-deterministic events based on historical data
  * **Statistics**
    * Quantifies confidence in inferences based on probabilistic events
    * Provides framework for supporting or rejecting hypotheses
  * **Machine learning**
    * Modeling approach that scales to large, high-dimensional data

---

## Law of Large Numbers (LLN)

* The Law of Large Numbers (LLN) is a fundamental theorem in probability and statistics stating that as a sample size grows, its average gets closer to the true average of the whole population. 
* Simply put, repeating an experiment many times ensures your results will accurately reflect the real-world probability of an event.

#### The Two Versions

* **Weak Law of Large Numbers:**
  *  States that the sample average converges in probability to the expected value.
  * This means that with a sufficiently large sample size, it is highly likely that the average of the observations will be close to (within an acceptable margin of) the expected value.

* **Strong Law of Large Numbers:**

  *  States that the sample average converges almost surely (with probability 1) to the expected value.
  * This is a more rigorous mathematical standard, indicating that as the number of samples approaches infinity, it is virtually certain that the sample mean will exactly equal the population mean.

---

## Random variable

* A random variable is a mathematical rule that assigns a numerical value to each possible outcome of a random event. 

* Instead of dealing with descriptive outcomes like "heads" or "tails," it translates those real-world events into numbers so you can analyze them mathematically.

#### Understand with an Example

* If you flip a coin twice, your possible outcomes are:
  * Outcomes = { Heads-Heads, Heads-Tails, Tails-Heads, Tails-Tails }

* You can define a random variable X to represent the number of heads. The variable X automatically assigns a number to each outcome:
  * If the outcome is Tails-Tails, X = 0
  * If the outcome is Heads-Tails or Tails-Heads, X = 1
  * If the outcome is Heads-Heads, X = 2

#### The Two Main Types
  * **Discrete Random Variables:**
    * These variables have countable values. 
    * There are distinct gaps between the numbers, and they usually represent counts.
      * Examples: The number of cars passing a toll booth, the result of rolling a die, or the number of children in a family.
  * **Continuous Random Variables:**
    * These variables can take any value within a given range or interval. 
    * They have infinite possibilities and usually represent measurements.
      * Examples: The exact height of a student, the temperature outside, or the time it takes for a website to load.

