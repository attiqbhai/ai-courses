<H1>Probability for Computer Scientist - Stanford - Chris Piech</H1>

---

<H2>TABLE OF CONTENT</H2>

- [Cheat Sheet](#cheat-sheet)
- [Course Material Online](#course-material-online)
- [Counting - Step Rule / And Rule of Counting (also called the Multiplication Rule)](#counting---step-rule--and-rule-of-counting-also-called-the-multiplication-rule)
  - [The Core Formula](#the-core-formula)
  - [Examples](#examples)
    - [1. 10 coin flips](#1-10-coin-flips)
    - [2. Password of length 6 using digits (0–9)](#2-password-of-length-6-using-digits-09)
      - [3. License plate with 3 letters + 3 digits](#3-license-plate-with-3-letters--3-digits)
      - [4. Rolling 3 dice](#4-rolling-3-dice)
      - [5. Word: "BOBA"](#5-word-boba)
- [Counting: OR Rule / Counting With OR (The Sum Rule)](#counting-or-rule--counting-with-or-the-sum-rule)
  - [Intuition](#intuition)
  - [Simple Example](#simple-example)
  - [Important Condition](#important-condition)
  - [Die Example](#die-example)
  - [Example : Choosing a letter](#example--choosing-a-letter)
  - [Example: Password rules](#example-password-rules)
  - [8 Bits Problem](#8-bits-problem)
- [Counting: Combining AND + OR (the real power)](#counting-combining-and--or-the-real-power)
- [Counting: Quick Summary](#counting-quick-summary)
- [Counting: Conclusion](#counting-conclusion)
- [Counting: Step Rule Counting](#counting-step-rule-counting)
- [Permutations](#permutations)
- [Why Overcounting Happens in Permutations](#why-overcounting-happens-in-permutations)
  - [The Core Idea](#the-core-idea)
  - [How We Fix Overcounting](#how-we-fix-overcounting)
  - [Example 1: “boba”](#example-1-boba)
  - [Example 2: “banana”](#example-2-banana)
  - [Example 3: Mississippi](#example-3-mississippi)
  - [Quick Summary](#quick-summary)
- [General Approach to counting Permutations](#general-approach-to-counting-permutations)
- [Summary of Combinatorics](#summary-of-combinatorics)
- [Combinations](#combinations)
- [Combinations](#combinations-1)
- [Combinations](#combinations-2)
  - [Big Idea](#big-idea)
  - [Why “order doesn’t matter”](#why-order-doesnt-matter)
  - [The Formula](#the-formula)
  - [Why the formula works (the intuition you’ve been building toward)](#why-the-formula-works-the-intuition-youve-been-building-toward)
    - [Step 1 — Count all permutations](#step-1--count-all-permutations)
    - [Step 2 — Fix overcounting](#step-2--fix-overcounting)
  - [Examples (this is where it becomes clear)](#examples-this-is-where-it-becomes-clear)
    - [Choose 3 students from 10](#choose-3-students-from-10)
    - [Choose 2 toppings for a pizza from 5](#choose-2-toppings-for-a-pizza-from-5)
- [When to use combinations vs permutations](#when-to-use-combinations-vs-permutations)
- [Cards Problem](#cards-problem)
- [Summary of Combinatorics](#summary-of-combinatorics-1)
- [What “put objects into buckets” means](#what-put-objects-into-buckets-means)
  - [Case 1 — Objects are DISTINCT, Buckets are DISTINCT](#case-1--objects-are-distinct-buckets-are-distinct)
    - [Step Rule:](#step-rule)
    - [When to use:](#when-to-use)
  - [Case 2 — Objects are DISTINCT, Buckets are DISTINCT, but with RESTRICTIONS](#case-2--objects-are-distinct-buckets-are-distinct-but-with-restrictions)
    - [Example: Put 5 distinct people into 2 distinct teams of sizes 2 and 3.](#example-put-5-distinct-people-into-2-distinct-teams-of-sizes-2-and-3)
  - [Case 3 — Objects are IDENTICAL, Buckets are DISTINCT](#case-3--objects-are-identical-buckets-are-distinct)
    - [Example: Put 10 identical balls into 3 distinct buckets.](#example-put-10-identical-balls-into-3-distinct-buckets)
    - [When to use:](#when-to-use-1)
  - [Case 4 — Objects are IDENTICAL, Buckets are IDENTICAL](#case-4--objects-are-identical-buckets-are-identical)
    - [Example: Put 5 identical balls into identical buckets.](#example-put-5-identical-balls-into-identical-buckets)
  - [How to know which case you’re in](#how-to-know-which-case-youre-in)
  - [Quick examples to make it click](#quick-examples-to-make-it-click)
- [Summary of Combinatorics](#summary-of-combinatorics-2)
- [Distinct Strings and Distinct Buckets](#distinct-strings-and-distinct-buckets)
- [Summary of Combinatorics](#summary-of-combinatorics-3)
- [Address Over Counting General Rule](#address-over-counting-general-rule)
- [The Divider Method](#the-divider-method)
- [Summary of Combinatorics](#summary-of-combinatorics-4)
- [Counting Review](#counting-review)
  - [Step 1 — What are we counting?](#step-1--what-are-we-counting)
  - [Step 2 — Why “N choose 2”?](#step-2--why-n-choose-2)
  - [Step 3 — Expand the formula](#step-3--expand-the-formula)
  - [Step 4 — Apply it to the slide](#step-4--apply-it-to-the-slide)
  - [Why this makes sense](#why-this-makes-sense)
- [Sample Space](#sample-space)
- [ℤ — The Set of Integers](#ℤ--the-set-of-integers)
- [ℝ — The Set of Real Numbers](#ℝ--the-set-of-real-numbers)
- [Event Space](#event-space)
- [Sample Space and Event Space](#sample-space-and-event-space)
- [Probability](#probability)
- [What is Probability](#what-is-probability)
- [Axioms of Probability](#axioms-of-probability)
- [Core Rules of Probability](#core-rules-of-probability)
- [Equally Likely Income](#equally-likely-income)
- [Not everything is Equally Likely](#not-everything-is-equally-likely)
- [Sum of Two dice is 7](#sum-of-two-dice-is-7)
- [Sum of Two dice is 2](#sum-of-two-dice-is-2)
- [Other Ways to make Sample Space](#other-ways-to-make-sample-space)
- [Sum of two dice is 7 - Other Way](#sum-of-two-dice-is-7---other-way)
- [Cows Problem](#cows-problem)
  - [Let’s solve this pigs-and-cows problem carefully.](#lets-solve-this-pigs-and-cows-problem-carefully)
  - [Total ways to draw 3 animals from 7](#total-ways-to-draw-3-animals-from-7)
  - [Favorable ways: 1 cow and 2 pigs](#favorable-ways-1-cow-and-2-pigs)
    - [Choose 1 cow from 4 cows:](#choose-1-cow-from-4-cows)
    - [Choose 2 pigs from 3 pigs:](#choose-2-pigs-from-3-pigs)
    - [Multiply (AND rule):](#multiply-and-rule)
  - [Probability](#probability-1)
- [Straight Poker Hand Problem](#straight-poker-hand-problem)
- [Key Tip](#key-tip)
- [Chip Defect Detection Problem](#chip-defect-detection-problem)
- [Taget Re-visited](#taget-re-visited)
- [Serendipity](#serendipity)
  - [Review Mutually Exclusive Events](#review-mutually-exclusive-events)
- [E Complement](#e-complement)
- [Serendipity](#serendipity-1)
- [Rule to Make Problem Easy](#rule-to-make-problem-easy)
- [Conditional Probability](#conditional-probability)
- [Dice, our Misunderstood friends](#dice-our-misunderstood-friends)
- [Conditional Probability](#conditional-probability-1)
- [Conditional Probability - Visual intuition](#conditional-probability---visual-intuition)
- [Conditional Probability - In general](#conditional-probability---in-general)
- [Netflix and Learn](#netflix-and-learn)
- [What is Machine Learning](#what-is-machine-learning)
- [Probability Notation](#probability-notation)
- [Chain Rule and Baby](#chain-rule-and-baby)
- [Probability Chain Rule](#probability-chain-rule)
- [Law of Total Probability](#law-of-total-probability)
- [Baby and Law of Total Probability](#baby-and-law-of-total-probability)
- [Law of Total Probability Relation](#law-of-total-probability-relation)
- [Law of Total Probability Formula](#law-of-total-probability-formula)
- [Evolution of Bacteria](#evolution-of-bacteria)
- [Real Question](#real-question)
- [Relationship b/w Probabilities](#relationship-bw-probabilities)
- [Bayes Theorem](#bayes-theorem)
- [](#)
- [Bayes Theorem Formula](#bayes-theorem-formula)
- [Detecting Spam email](#detecting-spam-email)
- [Bayes Theorem Terminology](#bayes-theorem-terminology)
- [SARS Virus Test](#sars-virus-test)
- [Multiple Choice Theory](#multiple-choice-theory)
- [Review](#review)
- [Telling in Cards](#telling-in-cards)
- [DNA Data](#dna-data)
- [Lecture-5: Learning Goals of today](#lecture-5-learning-goals-of-today)
- [OR With Mutually Exclusive Events](#or-with-mutually-exclusive-events)
- [What about When not Mutually Exclusive](#what-about-when-not-mutually-exclusive)
- [OR Without Mutually Exclusive Events](#or-without-mutually-exclusive-events)
- [More than two sets](#more-than-two-sets)
- [Inclusion / Exclusion with three events](#inclusion--exclusion-with-three-events)
- [OR \& AND Probability Summary](#or--and-probability-summary)
- [Probability of AND](#probability-of-and)
- [AND Probability -  Independent](#and-probability----independent)
- [AND Probability -  Independent - Key](#and-probability----independent---key)
- [AND Probability -  Independent - Reciprocal](#and-probability----independent---reciprocal)
- [AND Probability -  Independent - Dice](#and-probability----independent---dice)
- [AND Probability -  Independent - Looks like](#and-probability----independent---looks-like)
- [What does Mutual Exclusiveness Looks Like](#what-does-mutual-exclusiveness-looks-like)
- [This is what Independence Looks Like](#this-is-what-independence-looks-like)
- [This is what dependence Looks Like](#this-is-what-dependence-looks-like)
- [AND Probability -  Independent - Intuition](#and-probability----independent---intuition)
- [AND Probability -  Independent - Generalization](#and-probability----independent---generalization)
- [AND Probability -  Independent - Generalization - Example](#and-probability----independent---generalization---example)
- [Properties of Pairs of Events](#properties-of-pairs-of-events)
- [Properties of Pairs of Events - Example](#properties-of-pairs-of-events---example)
- [Properties of Pairs of Events - Example](#properties-of-pairs-of-events---example-1)
- [Conditonal Independence](#conditonal-independence)
- [Random Variables](#random-variables)
- [Probability Mass function](#probability-mass-function)
- [Expectations](#expectations)
  - [What expected value means](#what-expected-value-means)
- [Lecture - 7](#lecture---7)
  - [Probability of exactly K Heads in N experiments is](#probability-of-exactly-k-heads-in-n-experiments-is)
  - [Find Probability that H is less than 10](#find-probability-that-h-is-less-than-10)
- [Some people who lie with statistics, they use Expectations to back their lies.](#some-people-who-lie-with-statistics-they-use-expectations-to-back-their-lies)
- [Lecture-8](#lecture-8)
- [Lecture 9](#lecture-9)




---
## Cheat Sheet

<img src="images/summary-of-combinatorics-4.jpeg" alt="summary-of-combinatorics-4.jpeg" style="width: 800px;">

<img src="images/core-rules-of-probability.jpeg" alt="core-rules-of-probability.jpeg" style="width: 800px;">

<img src="images/equally-likely-outcome-1.jpeg" alt="equally-likely-income-1.jpeg" style="width: 800px;">

<img src="images/conditional-probability-visual-intuition.jpeg" alt="conditional-probability-visual-intuition.jpeg" style="width: 800px;">

<img src="images/conditional-probability-in-general.jpeg" alt="conditional-probability-in-general.jpeg" style="width: 800px;">

<img src="images/law-of-total-probability-formula.jpeg" alt="law-of-total-probability-formula.jpeg" style="width: 800px;">

<img src="images/bayes-theorem-formula-3.jpeg" alt="bayes-theorem-formula-3.jpeg" style="width: 800px;">

<img src="images/bayes-theorem-terminology.jpeg" alt="bayes-theorem-terminology.jpeg" style="width: 800px;">

<img src="images/Probability of exactly K Heads Formula.jpeg" alt="Probability of exactly K Heads Formula" style="width: 800px;">

<img src="images/random-variable-binomial.jpeg" alt="random-variable-binomial" style="width: 800px;">

<img src="images/coins-with-bionomials.jpeg" alt="coins-with-bionomials" style="width: 800px;">

---

## Course Material Online

https://chrispiech.github.io/probabilityForComputerScientists/en/

---

## Counting - Step Rule / And Rule of Counting (also called the Multiplication Rule)

If a process happens in steps, and each step has a certain number of choices,
then the total number of outcomes is the product of the number of choices at each step.

If an experiment has two parts, where the first part can result in one of 
$m$ outcomes and the second part can result in one of $n$ outcomes regardless of the outcome of the first part, then the total number of outcomes for the experiment is $m * n$.

Rewritten using set notation, the Step Rule of Counting states that if an experiment with two parts has an outcome from set $A$ in the first part, where 
$|A| = m$, and an outcome from set $B$ in the second part (where the number of outcomes in $B$ is the same regardless of the outcome of the first part), where 
$|B| = n$, then the total number of outcomes of the experiment is $|A||B| = m * n$
.

### The Core Formula

If a process has k steps:

- Step 1 has n₁ choices
- Step 2 has n₂ choices
- Step 3 has n₃ choices
…
- Step k has nₖ choices

Then the total number of possible outcomes is:

> $𝑛_1 × 𝑛_2 × 𝑛_3 × ⋯ × 𝑛_𝑘$

That’s the Step Rule.

### Examples

#### 1. 10 coin flips

Each flip has 2 choices (outcomes): H or T.

There are 10 steps, each with 2 choices.

> $2^{10} = 1024$

#### 2. Password of length 6 using digits (0–9)

Each position has 10 choices.

> $10^6 = 1,000,000$

##### 3. License plate with 3 letters + 3 digits

- Step 1: 26 choices
- Step 2: 26 choices
- Step 3: 26 choices
- Step 4: 10 choices
- Step 5: 10 choices
- Step 6: 10 choices

> $Total\ outcomes =  26^3 × 10^3$

##### 4. Rolling 3 dice

Each die has 6 choices.

> $6^3 = 216$

##### 5. Word: "BOBA"

The word BOBA has 4 letters:
- B
- O
- B
- A

Notice: the letter B repeats twice — this matters.

If all letters were distinct, the number of permutations would be:

> $4 ! = 24$

But because B appears twice, we must divide by the number of ways to permute the repeated letters:

Step 1: Choose the 1st letter  
4 choices → b, o, b, a (b is repeated)

Step 2: Choose the 2nd letter  
3 remaining choices

Step 3: Choose the 3rd letter  
2 remaining choices

Step 4: Choose the 4th letter
1 remaining choice

Using the step rule:

> $4 × 3 × 2 × 1 = 24$

But because the two B’s are indistinguishable:

> $\frac {24}{2!} = 12$

| Concept                     | Value                         |
|-----------------------------|-------------------------------|
| Word                        | BOBA                          |
| Letters                     | B, O, B, A                    |
| Total permutations (raw)    | 4! = 24                       |
| Adjustment for repeats      | divide by 2!                  |
| Distinct permutations       | 12                            |
| Method used                 | Step Rule of Counting         |

---

## Counting: OR Rule / Counting With OR (The Sum Rule)

The OR Rule says:

> If an outcome can happen in one way OR another (and the ways do not overlap),
> then the total number of outcomes is the sum of the counts of each way.

This is also called the Sum Rule of Counting.

It complements the Step Rule:

- Step Rule = AND → multiply

- OR Rule = OR → add

### Intuition

Think of OR as choosing between options.

If you can do Option A OR Option B,
you add the number of ways each option can happen.

### Simple Example

You want to choose a drink:

- 3 coffee options

- 2 tea options

You can choose coffee OR tea.

> $3 + 2 = 5$

### Important Condition

The OR rule works only if the options do not overlap.

If they overlap, you must subtract the overlap (like in set theory):

> $∣ 𝐴 \cup 𝐵 ∣ = ∣ 𝐴 ∣ + ∣ 𝐵 ∣ − ∣ 𝐴 \cap 𝐵 ∣$

### Die Example

Event A = “roll a 1 or a 6”

> $1 + 1 = 2$

Two outcomes.

### Example : Choosing a letter

Choose a vowel OR a consonant from the English alphabet.

- Vowels = 5

- Consonants = 21

> $5 + 21 = 26$

### Example: Password rules

A password must start with:

- a digit (10 choices)

OR

- a letter (26 choices)

Total choices for the first character:
> $10 + 26 = 36$

### 8 Bits Problem

<img src="images/8-bits-problem.jpeg" alt="8-bits-problem" style="width: 600px;">

<img src="images/a-and-b.jpeg" alt="a-and-b" style="width: 600px;">

---

## Counting: Combining AND + OR (the real power)

Most real problems use both rules.

Example:

A license plate is:

- Letter OR digit for the first character

- Digit for the next 3 characters

First character:
> $26 + 10 = 36$

Next three characters:
> $10 × 10 × 10 = 10^3$

Total plates:
> $36 × 10^3$

This is exactly how combinatorics builds sample spaces.

---

## Counting: Quick Summary

| Rule               | Meaning                         | Operation |
|--------------------|----------------------------------|-----------|
| Step Rule (AND)    | Do this AND then that            | Multiply  |
| OR Rule (Sum Rule) | Do this OR that                  | Add       |

---

## Counting: Conclusion

<img src="images/counting-with-steps-or.jpeg" alt="counting-with-steps-or" style="width: 600px;">

---

## Counting: Step Rule Counting


<img src="images/ordering-of-letter-chris.jpeg" alt="ordering-of-letter-chris.jpeg" style="width: 600px;">

---

## Permutations

<img src="images/permutations.jpeg" alt="permutations.jpeg" style="width: 600px;">

<img src="images/unique-six-digit-passcode.jpeg" alt="unique-six-digit-passcode.jpeg" style="width: 600px;">

<img src="images/six-digit-passcode.jpeg" alt="six-digit-passcode.jpeg" style="width: 600px;">

---

## Why Overcounting Happens in Permutations

When you compute permutations using:

> $n!$

you are assuming all items are distinct.

But many real problems have repeated elements:

- boba → b repeats

- level → l and e repeat

- banana → a repeats 3 times, n repeats 2 times

If you treat repeated items as distinct, you end up counting the same arrangement multiple times.

That’s overcounting.

### The Core Idea

When items repeat, swapping those repeated items does not create a new permutation.

Example with “boba”:

- The two b’s are identical

- So “boba” and “boba” (swapping the b’s) are the same

- But the factorial formula counts them as different

This is the overcounting we must fix.

### How We Fix Overcounting

We divide by the factorial of the number of times each repeated item appears.

General formula:
If you have:

- $n$ total items

- $𝑘_1$ repeats of item 1

- $𝑘_2$ repeats of item 2

…

Then:

> $Permutations = \frac {𝑛!}{𝑘_1! * 𝑘_2!⋯}$

### Example 1: “boba”

Letters: b, o, b, a

Repeated: b appears twice

> $\frac {4 !} {2 !} = \frac {24} {2} = 12$

Without dividing by $2!$, you would count each arrangement twice.

### Example 2: “banana”

Letters: b, a, n, a, n, a
Repeated:

- a appears 3 times

- n appears 2 times

> $\frac {6 !} {3 !   2 !} = \frac {720} {6 ⋅ 2} = 60$

### Example 3: Mississippi

Total letters: 11
Repeated:

- i appears 4 times

- s appears 4 times

- p appears 2 times

> $\frac {11 !} {4 ! . 4 ! . 2 !} = \frac {39916800} {24 . 24 . 2} = 34650$


### Quick Summary

| Problem                     | Why Overcounting Happens                  | Fix                                      |
|:-----------------------------:|:--------------------------------------------:|:-------------------------------------------:|
| Permutations with repeats   | Factorial treats repeated items as unique | Divide by factorial of repeat counts      |
| Example: boba               | Two b’s counted as different               | 4! / 2! = 12                              |
| Example: banana             | a repeats 3 times, n repeats 2 times       | 6! / (3! 2!) = 60                         |

---

## General Approach to counting Permutations

<img src="images/general-permutations-formula.jpeg" alt="general-permutations-formula.jpeg" style="width: 600px;">

<img src="images/5-smughes-six-digit-passcode.jpeg" alt="5-smughes-six-digit-passcode.jpeg" style="width: 600px;">

---

## Summary of Combinatorics

<img src="images/summary-of-combinatorics.jpeg" alt="summary-of-combinatorics.jpeg" style="width: 600px;">

---

## Combinations

<img src="images/combinations-with-cake-1.jpeg" alt="combinations-with-cake-1.jpeg" style="width: 600px;">

<img src="images/combinations-with-cake-2.jpeg" alt="combinations-with-cake-2.jpeg" style="width: 600px;">

<img src="images/combinations-with-cake-3.jpeg" alt="combinations-with-cake-3.jpeg" style="width: 600px;">

<img src="images/combinations-with-cake-4.jpeg" alt="combinations-with-cake-4.jpeg" style="width: 600px;">

<img src="images/combinations-with-cake-5.jpeg" alt="combinations-with-cake-5.jpeg" style="width: 600px;">

---

## Combinations

<img src="images/combinations.jpeg" alt="combinations.jpeg" style="width: 600px;">

<img src="images/combinations-2.jpeg" alt="combinations-2.jpeg" style="width: 600px;">

<img src="images/combinations-3.jpeg" alt="combinations-3.jpeg" style="width: 600px;">

<img src="images/combinations-4.jpeg" alt="combinations-4.jpeg" style="width: 600px;">

---

## Combinations

### Big Idea

Combinations count how many ways you can choose items when order does NOT matter.

- If order does matter → **permutations**

- If order does NOT matter → **combinations**

This is the single most important distinction.

### Why “order doesn’t matter”

Choosing $\{A, B\}$ is the same as choosing $\{B, A\}$.

Combinations treat these as one outcome.

Permutations treat them as two outcomes.

### The Formula

If you choose k items from n items, the number of combinations is:

$\binom{n}{k} = \frac {n!} {K!. (n - k)!}$

This is pronounced “n choose k”.

### Why the formula works (the intuition you’ve been building toward)

#### Step 1 — Count all permutations

If order mattered, choosing k items from n would be:

$\frac {n!} {(n - k)!}$

This counts all ordered selections.

#### Step 2 — Fix overcounting

But combinations don’t care about order.

Every group of k items is counted k! times (once for each ordering).

So we divide by k!:

$\frac {n!} {K!. (n - k)!}$

This is exactly the same overcounting idea you learned with “boba”, “banana”, etc.

### Examples (this is where it becomes clear)

#### Choose 3 students from 10

Order doesn’t matter.

$\binom{10}{3} = \frac {10!} {3!. (10 - 3)!} = 120$

#### Choose 2 toppings for a pizza from 5

Order doesn’t matter.

$\binom{5}{2} = \frac {5!} {2!. (5 - 2)!} = 10$

---

## When to use combinations vs permutations

| Situation | Order matters? | Use |
| :---: | :---: | :---: |
| Passwords | Yes | Permutations |
| Seating people | Yes | Permutations |
| Choosing a committee | No | Combinations |
| Picking lottery numbers | No | Combinations |
| Selecting toppings | No | Combinations |

---

## Cards Problem

<img src="images/cards-problem.jpeg" alt="cards-problem.jpeg" style="width: 600px;">

--- 

## Summary of Combinatorics

<img src="images/summary-of-combinatorics-1.jpeg" alt="summary-of-combinatorics-1.jpeg" style="width: 600px;">

---

## What “put objects into buckets” means

You have:

- objects (balls, digits, people, items)

- buckets (bins, groups, categories)

The question is:
How many ways can you distribute the objects into the buckets?

> Different rules → different formulas.

There are three main cases.

### Case 1 — Objects are DISTINCT, Buckets are DISTINCT

This is the easiest case.

Example:
Put 4 distinct balls into 3 distinct buckets.

Each ball chooses a bucket.

#### Step Rule:

Each ball has 3 choices → multiply.

> $3^4$

This is the same logic as counting passwords or coin flips.

#### When to use:

- People assigned to teams

- Files assigned to folders

- Digits assigned to positions

- Anything where both objects and buckets are labeled

### Case 2 — Objects are DISTINCT, Buckets are DISTINCT, but with RESTRICTIONS

Example restrictions:

- No bucket can be empty

- Each bucket must have exactly k objects

- Bucket sizes must follow a pattern

This becomes a combinations + permutations problem.

#### Example: Put 5 distinct people into 2 distinct teams of sizes 2 and 3.

Step 1: Choose 2 people for Team A

> $\binom{5}{2}$

Step 2: Remaining 3 automatically go to Team B

> $\binom{3}{3} = 1$

Total:

> $\binom{5}{2}$

This is the classic “committee selection” logic.

### Case 3 — Objects are IDENTICAL, Buckets are DISTINCT

This is the famous stars and bars formula.

#### Example: Put 10 identical balls into 3 distinct buckets.

Let the bucket counts be:

> $𝑥_1 + 𝑥_2 + 𝑥_3 = 10$

Number of solutions:

> $\binom{10 + 3 - 1}{3 - 1} = \binom{12}{2}$

#### When to use:

- Distributing money

- Distributing identical candies

- Counting integer solutions

- Probability distributions over counts

This is extremely important in probability.

### Case 4 — Objects are IDENTICAL, Buckets are IDENTICAL

This is the hardest case — partitions of integers.

#### Example: Put 5 identical balls into identical buckets.

You count unique distributions, not arrangements.

Example distributions of 5:

- 5

- 4 + 1

- 3 + 2

- 3 + 1 + 1

- 2 + 2 + 1

- 2 + 1 + 1 + 1

- 1 + 1 + 1 + 1 + 1

This is called integer partitioning.

You rarely need this in basic probability, but it appears in advanced combinatorics.


### How to know which case you’re in

| Objects | Buckets | Restrictions | Method |
|:---------:|:----------:|:--------------:|:--------:|
| Distinct | Distinct | None | $k^n$ (step rule) |
| Distinct | Distinct | Bucket sizes fixed | Combinations |
| Distinct | Distinct | No bucket empty | Inclusion–exclusion |
| Identical | Distinct | None | Stars and Bars |
| Identical | Identical | None | Integer partitions |

### Quick examples to make it click

Example 1:  
Put 6 distinct digits into 3 distinct buckets.

> $3^6$

Example 2  
Put 6 distinct digits into 3 buckets, each bucket must have 2 digits.

> $\binom{6}{2}\binom{4}{2}\binom{2}{2}$

Example 3  
Put 10 identical candies into 4 distinct bags.

> $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3}$

Example 4  
Put 5 identical candies into identical bags.

Count partitions of 5.

---

## Summary of Combinatorics

<img src="images/summary-of-combinatorics-2.jpeg" alt="summary-of-combinatorics-2.jpeg" style="width: 600px;">

---

## Distinct Strings and Distinct Buckets

<img src="images/distinct-strings-distinct-buckets.jpeg" alt="distinct-strings-distinct-buckets.jpeg" style="width: 600px;">

---

## Summary of Combinatorics

<img src="images/summary-of-combinatorics-3.jpeg" alt="summary-of-combinatorics-3.jpeg" style="width: 600px;">

---

## Address Over Counting General Rule

- Overcount by fixed number: **You subtract it off**

- Sometime you overcount by multiplicative: **you divide it out**.

---

## The Divider Method

<img src="images/divider-method.jpeg" alt="divider-method.jpeg" style="width: 600px;">

<img src="images/divider-method-1.jpeg" alt="divider-method-1.jpeg" style="width: 600px;">

--- 

## Summary of Combinatorics

<img src="images/summary-of-combinatorics-4.jpeg" alt="summary-of-combinatorics-4.jpeg" style="width: 800px;">

---

## Counting Review

<img src="images/dna-tree-question.jpeg" alt="dna-tree-question.jpeg" style="width: 800px;">

### Step 1 — What are we counting?

We want pairs of animals.

A DNA distance is computed between two animals, so each calculation corresponds to one pair.

So the question is:

> How many pairs can be formed from N animals?

This is exactly “N choose 2”.

### Step 2 — Why “N choose 2”?

Because:

- Order does not matter (distance between A and B is the same as B and A)

- We are choosing 2 animals out of N

So the number of pairs is:

> $\binom{N}{2}$

### Step 3 — Expand the formula

> $\binom{N}{2} = \frac {N(N - 1)}{2}$

This is the number of DNA distance calculations needed.

### Step 4 — Apply it to the slide

Count the animals in the tree:

Porifera  
Ctenophora  
Cnidaria  
Acoela  
Echinodermata  
Chordata  
Platyhelminthes  
Rotifera  
Ectoprocta  
Brachiopoda  
Mollusca  
Annelida  
Nematoda  
Arthropoda  

There are 14 animals shown.

So the number of pairwise DNA distance calculations is:

> $\binom{14}{2} = \frac {14 . 13}{2} = 91$

### Why this makes sense

If you list all pairs:

- Porifera–Ctenophora

- Porifera–Cnidaria

- …

- Arthropoda–Nematoda

You will get 91 unique pairs.

This is exactly what combinations count.

---

## Sample Space

<img src="images/sample-space.jpeg" alt="sample-space.jpeg" style="width: 800px;">

--- 

## ℤ — The Set of Integers

The symbol ℤ represents all integers:

… −3, −2, −1, 0, 1, 2, 3 …

It includes:

- all positive whole numbers

- all negative whole numbers

- zero

- No fractions, no decimals.

---

## ℝ — The Set of Real Numbers

The symbol ℝ represents all real numbers, meaning every number on the number line:

- Integers (like 5, −2)

- Fractions (like 3/4)

- Decimals (like 2.71828)

- Irrational numbers (like √2, π)

Basically:

> If you can place it on the number line, it’s a real number.

---

## Event Space

<img src="images/event-space.jpeg" alt="event-space.jpeg" style="width: 800px;">

---

## Sample Space and Event Space

<img src="images/sample-event-space.jpeg" alt="sample-event-space.jpeg" style="width: 800px;">

---

## Probability

<img src="images/probability.jpeg" alt="probability.jpeg" style="width: 800px;">

---

## What is Probability

<img src="images/what-is-probability.jpeg" alt="what-is-probability.jpeg" style="width: 800px;">

<img src="images/what-is-probability-1.jpeg" alt="what-is-probability-1.jpeg" style="width: 800px;">

---

## Axioms of Probability

<img src="images/axioms-of-probability.jpeg" alt="axioms-of-probability.jpeg" style="width: 800px;">

---

## Core Rules of Probability

<img src="images/core-rules-of-probability.jpeg" alt="core-rules-of-probability.jpeg" style="width: 800px;">

---

## Equally Likely Income

<img src="images/equally-likely-outcome.jpeg" alt="equally-likely-income.jpeg" style="width: 800px;">

<img src="images/equally-likely-outcome-1.jpeg" alt="equally-likely-income-1.jpeg" style="width: 800px;">

---

## Not everything is Equally Likely

<img src="images/not-equally-likely.jpeg" alt="not-equally-likely.jpeg" style="width: 800px;">

---

## Sum of Two dice is 7

<img src="images/sum-of-two-dice-7.jpeg" alt="sum-of-two-dice-7.jpeg" style="width: 800px;">

<img src="images/is-it-correct.jpeg" alt="is-it-correct.jpeg" style="width: 800px;">

<img src="images/sum-of-two-dice-7-1.jpeg" alt="sum-of-two-dice-7-1.jpeg" style="width: 800px;">

> Note:- The close you get to infinity, the more close true answer you will have.

---

## Sum of Two dice is 2

<img src="images/sum-of-two-dice-2.jpeg" alt="sum-of-two-dice-2.jpeg" style="width: 800px;">

<img src="images/sum-of-two-dice-2-1.jpeg" alt="sum-of-two-dice-2-1.jpeg" style="width: 800px;">

---

## Other Ways to make Sample Space

<img src="images/other-ways-to-make-sample-space.jpeg" alt="other-ways-to-make-sample-space.jpeg" style="width: 800px;">

---

## Sum of two dice is 7 - Other Way

<img src="images/sum-of-two-dice-7-other-way.jpeg" alt="sum-of-two-dice-7-other-way.jpeg" style="width: 800px;">

<img src="images/sum-of-two-dice-7-other-way-1.jpeg" alt="sum-of-two-dice-7-other-way-1.jpeg" style="width: 800px;">

---

## Cows Problem

<img src="images/cows-problem.jpeg" alt="cows-problem.jpeg" style="width: 800px;">

<img src="images/choice-of-sample-space.jpeg" alt="choice-of-sample-space.jpeg" style="width: 800px;">

<img src="images/cows-problem-2.jpeg" alt="cows-problem-2.jpeg" style="width: 800px;">

<img src="images/make-indistinct-distinct.jpeg" alt="make-indistinct-distinct.jpeg" style="width: 800px;">

### Let’s solve this pigs-and-cows problem carefully.

We have:

- 4 cows

- 3 pigs

- 3 animals drawn (without replacement)

- We want: P(1 cow and 2 pigs)

### Total ways to draw 3 animals from 7

We’re just choosing which 3 animals, order doesn’t matter:

> $Total\ ways = \binom{7}{3} = \frac {7!}{3! * (7\ -\ 3)!} = \frac {7\ *\ 6\ *\ 5}{3\ *\ 2} = 35$

### Favorable ways: 1 cow and 2 pigs

#### Choose 1 cow from 4 cows:

> $\binom{4}{1} = \frac {4!}{1!\ *\ (4 - 1)!} = \frac {4}{1} = 4$

#### Choose 2 pigs from 3 pigs:

> $\binom{3}{2} = \frac {3!}{2!\ *\ (3 - 2)!} = \frac {3}{1} = 3$

#### Multiply (AND rule):


> $Favorable\ ways\ =\ 4\ ×\ 3\ =\ 12$

### Probability

> $𝑃(1\ cow\ and\ 2\ pigs)\ =\frac {favorable}{total} =\frac {12}{35}$

So: 

> $𝑃(1 cow and 2 pigs) = \frac {12}{35}$

---

## Straight Poker Hand Problem

<img src="images/straight-poker-hand.jpeg" alt="straight-poker-hand.jpeg" style="width: 800px;">

<img src="images/straight-poker-hand-1.jpeg" alt="straight-poker-hand-1.jpeg" style="width: 800px;">

<img src="images/straight-poker-hand-2.jpeg" alt="straight-poker-hand-2.jpeg" style="width: 800px;">

---

## Key Tip

<img src="images/equally-likely-probability.jpeg" alt="equally-likely-probability.jpeg" style="width: 600px;">

---

## Chip Defect Detection Problem

<img src="images/chip-defect-detection.jpeg" alt="chip-defect-detection.jpeg" style="width: 800px;">

<img src="images/chip-defect-detection-1.jpeg" alt="chip-defect-detection-1.jpeg" style="width: 800px;">

---

## Taget Re-visited

<img src="images/target-revisited.jpeg" alt="target-revisited.jpeg" style="width: 800px;">

---

## Serendipity

<img src="images/serendipity.jpeg" alt="serendipity.jpeg" style="width: 800px;">

---

### Review Mutually Exclusive Events

<img src="images/review-axiom-3.jpeg" alt="review-axiom-3.jpeg" style="width: 800px;">

<img src="images/review-axiom-3-1.jpeg" alt="review-axiom-3-1.jpeg" style="width: 800px;">

<img src="images/review-axiom-3-2.jpeg" alt="review-axiom-3-2.jpeg" style="width: 800px;">

<img src="images/review-axiom-3-3.jpeg" alt="review-axiom-3-3.jpeg" style="width: 800px;">

---

## E Complement

<img src="images/probability-of-e-and-e-complement.jpeg" alt="probability-of-e-and-e-complement.jpeg" style="width: 800px;">

<img src="images/probability-of-e-and-e-complement-1.jpeg" alt="probability-of-e-and-e-complement-1.jpeg" style="width: 800px;">

---

## Serendipity

<img src="images/serendipity.jpeg" alt="serendipity.jpeg" style="width: 800px;">

---

## Rule to Make Problem Easy

<img src="images/rule-to make it easy.jpeg" alt="rule-to make it easy.jpeg" style="width: 800px;">

---

## Conditional Probability

<img src="images/conditional-probability-1.jpeg" alt="conditional-probability-1.jpeg" style="width: 800px;">

<img src="images/conditional-probability.jpeg" alt="conditional-probability.jpeg" style="width: 800px;">

---

## Dice, our Misunderstood friends

<img src="images/dice-misunderstood-friends.jpeg" alt="dice-misunderstood-friends.jpeg" style="width: 800px;">

<img src="images/dice-misunderstood-friends-1.jpeg" alt="dice-misunderstood-friends-1.jpeg" style="width: 800px;">

<img src="images/dice-misunderstood-friends-2.jpeg" alt="dice-misunderstood-friends-2.jpeg" style="width: 800px;">

---

## Conditional Probability

<img src="images/conditional-probability-2.jpeg" alt="conditional-probability-2.jpeg" style="width: 800px;">

---

## Conditional Probability - Visual intuition

<img src="images/conditional-probability-visual-intuition.jpeg" alt="conditional-probability-visual-intuition.jpeg" style="width: 800px;">

---

## Conditional Probability - In general

<img src="images/conditional-probability-in-general.jpeg" alt="conditional-probability-in-general.jpeg" style="width: 800px;">

---

## Netflix and Learn

<img src="images/life-is-beautiful.jpeg" alt="life-is-beautiful.jpeg" style="width: 800px;">

<img src="images/life-is-beautiful-conditional-probability.jpeg" alt="life-is-beautiful-conditional-probability.jpeg" style="width: 800px;">

<img src="images/life-is-beautiful-conditional-probability-1.jpeg" alt="life-is-beautiful-conditional-probability-1.jpeg" style="width: 800px;">

---

## What is Machine Learning

<img src="images/what-is-machine-learning.jpeg" alt="what-is-machine-learning.jpeg" style="width: 800px;">

---

## Probability Notation

<img src="images/probability-notation.jpeg" alt="probability-notation.jpeg" style="width: 800px;">

---

## Chain Rule and Baby

<img src="images/chain-rule-and-baby.jpeg" alt="chain-rule-and-baby.jpeg" style="width: 800px;">

---

## Probability Chain Rule

<img src="images/probability-chain-rule.jpeg" alt="probability-chain-rule.jpeg" style="width: 800px;">

---

## Law of Total Probability

<img src="images/law-of-total-probability.jpeg" alt="law-of-total-probability.jpeg" style="width: 800px;">

---

## Baby and Law of Total Probability

<img src="images/baby-and-total-porbability.jpeg" alt="baby-and-total-porbability.jpeg" style="width: 800px;">

---

## Law of Total Probability Relation

<img src="images/law-of-total-probability-relation.jpeg" alt="law-of-total-probability-relation.jpeg" style="width: 800px;">

---

## Law of Total Probability Formula

<img src="images/law-of-total-probability-formula.jpeg" alt="law-of-total-probability-formula.jpeg" style="width: 800px;">

<img src="images/law-of-total-probability-formula-1.jpeg" alt="law-of-total-probability-formula-1.jpeg" style="width: 800px;">

<img src="images/law-of-total-probability-formula-2.jpeg" alt="law-of-total-probability-formula-2.jpeg" style="width: 800px;">

<img src="images/law-of-total-probability-formula-3.jpeg" alt="law-of-total-probability-formula-3.jpeg" style="width: 800px;">

---

## Evolution of Bacteria

<img src="images/evolution-of-bacteria.jpeg" alt="evolution-of-bacteria.jpeg" style="width: 800px;">

<img src="images/evolution-of-bacteria-1.jpeg" alt="evolution-of-bacteria-1.jpeg" style="width: 800px;">

---

## Real Question 

<img src="images/evolution-of-bacteria-surviving-mutation.jpeg" alt="evolution-of-bacteria-surviving-mutation.jpeg" style="width: 800px;">

---

## Relationship b/w Probabilities 

<img src="images/relationship-between-probabilities.jpeg" alt="relationship-between-probabilities.jpeg" style="width: 800px;">

---

## Bayes Theorem

<img src="images/bayes-theorem.jpeg" alt="bayes-theorem.jpeg" 
style="width: 800px;">

<img src="images/bayes-theorem-1.jpeg" alt="bayes-theorem-1.jpeg" style="width: 800px;">
---

## Bayes Theorem Formula

<img src="images/bayes-theorem-formula.jpeg" alt="bayes-theorem-formula.jpeg" style="width: 800px;">

<img src="images/bayes-theorem-formula-1.jpeg" alt="bayes-theorem-formula-1.jpeg" style="width: 800px;">

<img src="images/bayes-theorem-formula-2.jpeg" alt="bayes-theorem-formula-2.jpeg" style="width: 800px;">

<img src="images/bayes-theorem-formula-3.jpeg" alt="bayes-theorem-formula-3.jpeg" style="width: 800px;">

---

## Detecting Spam email

<img src="images/detecting-spam-email.jpeg" alt="detecting-spam-email.jpeg" style="width: 800px;">

<img src="images/detecting-spam-email-1.jpeg" alt="detecting-spam-email-1.jpeg" style="width: 800px;">

---

## Bayes Theorem Terminology

<img src="images/bayes-theorem-terminology.jpeg" alt="bayes-theorem-terminology.jpeg" style="width: 800px;">

---

## SARS Virus Test

<img src="images/sars-virus-test.jpeg" alt="sars-virus-test.jpeg" style="width: 800px;">

<img src="images/sars-virus-test-1.jpeg" alt="sars-virus-test-1.jpeg" style="width: 800px;">

<img src="images/sars-virus-test-2.jpeg" alt="sars-virus-test-2.jpeg" style="width: 800px;">

<img src="images/sars-virus-test-3.jpeg" alt="sars-virus-test-3.
jpeg" style="width: 800px;">

<img src="images/sars-virus-test-4.jpeg" alt="sars-virus-test-4.jpeg" style="width: 800px;">

<img src="images/sars-virus-test-5.jpeg" alt="sars-virus-test-5.jpeg" style="width: 800px;">

---

## Multiple Choice Theory

<img src="images/multiple-choice-theory.jpeg" alt="multiple-choice-theory.jpeg" style="width: 800px;">

---
## Review

<img src="images/lecture-5-review-1.jpeg" alt="lecture-5-review-1.jpeg" style="width: 800px;">

<img src="images/lecture-5-review-2.jpeg" alt="lecture-5-review-2.jpeg" style="width: 800px;">

<img src="images/lecture-5-review-3.jpeg" alt="lecture-5-review-3.jpeg" style="width: 800px;">

<img src="images/lecture-5-review-4.jpeg" alt="lecture-5-review-4.jpeg" style="width: 800px;">

<img src="images/lecture-5-review-5.jpeg" alt="lecture-5-review-5.jpeg" style="width: 800px;">

---

## Telling in Cards

<img src="images/telling-in-cards.jpeg" alt="telling-in-cards.jpeg" style="width: 800px;">

<img src="images/telling-in-cards-1.jpeg" alt="telling-in-cards-1.jpeg" style="width: 800px;">

---

## DNA Data

<img src="images/dna-data.jpeg" alt="dna-data.jpeg" style="width: 800px;">

<img src="images/discovered-hypotheis.jpeg" alt="discovered-hypotheis.jpeg" style="width: 800px;">

---

## Lecture-5: Learning Goals of today

<img src="images/lecture-5-learning-goals of today.jpeg" alt="lecture-5-learning-goals of today.jpeg" style="width: 800px;">

---

## OR With Mutually Exclusive Events

<img src="images/or-with-mutually-exclusive-events.jpeg" alt="or-with-mutually-exclusive-events.jpeg" style="width: 800px;">

---

## What about When not Mutually Exclusive

<img src="images/what-about-when-not-mutually-exclusive.jpeg" alt="what-about-when-not-mutually-exclusive.jpeg" style="width: 800px;">

---

## OR Without Mutually Exclusive Events

<img src="images/or-with-not-mutually-exclusive-events.jpeg" alt="or-with-not-mutually-exclusive-events.jpeg" style="width: 800px;">

---

## More than two sets

<img src="images/more-than-two-sets.jpeg" alt="more-than-two-sets.jpeg" style="width: 800px;">

---

## Inclusion / Exclusion with three events

<img src="images/inclusion-exclusion-with-three-events.jpeg" alt="inclusion-exclusion-with-three-events.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-1.jpeg" alt="inclusion-exclusion-with-three-events-1.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-2.jpeg" alt="inclusion-exclusion-with-three-events-2.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-3.jpeg" alt="inclusion-exclusion-with-three-events-3.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-4.jpeg" alt="inclusion-exclusion-with-three-events-4.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-5.jpeg" alt="inclusion-exclusion-with-three-events-5.jpeg" style="width: 800px;">

<img src="images/inclusion-exclusion-with-three-events-6.jpeg" alt="inclusion-exclusion-with-three-events-6.jpeg" style="width: 800px;">

---

## OR & AND Probability Summary

<img src="images/or-n-and-probability-summary.jpeg" alt="or-n-and-probability-summary.jpeg" style="width: 800px;">

---

## Probability of AND

<img src="images/probability-of-and.jpeg" alt="probability-of-and.jpeg" style="width: 800px;">

---

## AND Probability -  Independent

<img src="images/and-independent-probability.jpeg" alt="and-independent-probability.jpeg" style="width: 800px;">

<img src="images/and-independent-probability-1.jpeg" alt="and-independent-probability-1.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Key

<img src="images/and-independent-probability-key.jpeg" alt="and-independent-probability-key.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Reciprocal

<img src="images/and-independent-probability-reciprocal.jpeg" alt="and-independent-probability-reciprocal.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Dice

<img src="images/and-independent-probability-dice.jpeg" alt="and-independent-probability-dice.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Looks like

<img src="images/and-independent-probability-lookslike.jpeg" alt="and-independent-probability-lookslike.jpeg" style="width: 800px;">

---

## What does Mutual Exclusiveness Looks Like

<img src="images/mutual-exclusiveness-lookslike.jpeg" alt="mutual-exclusiveness-lookslike.jpeg" style="width: 800px;">

---

## This is what Independence Looks Like

<img src="images/what-Independence-Looks-Like.jpeg" alt="what-Independence-Looks-Like.jpeg" style="width: 800px;">

---

## This is what dependence Looks Like

<img src="images/what-dependence-Looks-Like.jpeg" alt="what-dependence-Looks-Like.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Intuition

<img src="images/and-independent-probability-intuition-1.jpeg" alt="and-independent-probability-intuition-1.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Generalization

<img src="images/and-independent-probability-generalization.jpeg" alt="and-independent-probability-generalization.jpeg" style="width: 800px;">

---

## AND Probability -  Independent - Generalization - Example

<img src="images/and-independent-probability-generalization-example.jpeg" alt="and-independent-probability-generalization-example.jpeg" style="width: 800px;">

---

## Properties of Pairs of Events

<img src="images/properties-of-pairs-of-events.jpeg" alt="properties-of-pairs-of-events.jpeg" style="width: 800px;">

---

## Properties of Pairs of Events - Example

<img src="images/properties-of-pairs-of-events-example.jpeg" alt="properties-of-pairs-of-events-example.jpeg" style="width: 800px;">

---

## Properties of Pairs of Events - Example

<img src="images/properties-of-pairs-of-events-example-1.jpeg" alt="properties-of-pairs-of-events-example-1.jpeg" style="width: 800px;">

---

## Conditonal Independence

<img src="images/and-probability-conditional-independence.jpeg" alt="and-probability-conditional-independence.jpeg" style="width: 800px;">

Two events A and B are conditionally independent given C if:

> Once you know C happened, learning A tells you nothing new about B.

Formally:

> $𝑃 ( 𝐴 ∣ 𝐵 , 𝐶 ) = 𝑃 ( 𝐴 ∣ 𝐶 )$

and equivalently:

> $𝑃 ( 𝐵 ∣ 𝐴 , 𝐶 ) = 𝑃 ( 𝐵 ∣ 𝐶 )$

This means:

> **C explains everything that connects A and B.**

<img src="images/conditional-independence-formula.jpeg" alt="conditional-independence-formula.jpeg" style="width: 800px;">

<img src="images/independent-relationship-changes.jpeg" alt="independent-relationship-changes.jpeg" style="width: 800px;">

<img src="images/probability-based-how-many-watched.jpeg" alt="probability-based-how-many-watched.jpeg" style="width: 800px;">

<img src="images/probability-based-on-condition.jpeg" alt="probability-based-on-condition.jpeg" style="width: 800px;">

<img src="images/probability-based-on-set-of-conditions.jpeg" alt="probability-based-on-set-of-conditions.jpeg" style="width: 800px;">

<img src="images/watched-four-movies.jpeg" alt="watched-four-movies.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-1.jpeg" alt="watched-four-movies-1.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-2.jpeg" alt="watched-four-movies-2.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-out-of-thirty.jpeg" alt="watched-four-movies-out-of-thirty.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-out-of-thirty-solution.jpeg" alt="watched-four-movies-out-of-thirty-solution.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-out-of-thirty-conditional-independence.jpeg" alt="watched-four-movies-out-of-thirty-conditional-independence.jpeg" style="width: 800px;">

<img src="images/watched-four-movies-out-of-thirty-tag-based-dependence.jpeg" alt="watched-four-movies-out-of-thirty-tag-based-dependence.jpeg" style="width: 800px;">

<img src="images/conditional-independence-is-practical.jpeg" alt="conditional-independence-is-practical.jpeg" style="width: 800px;">

<img src="images/conditional-dependence-changes.jpeg" alt="conditional-dependence-changes.jpeg" style="width: 800px;">

<img src="images/conditional-independence-changes.jpeg" alt="conditional-independence-changes.jpeg" style="width: 800px;">

---

## Random Variables

<img src="images/random-variables.jpeg" alt="random-variables.jpeg" style="width: 800px;">

<img src="images/learning-random-variables.jpeg" alt="learning-random-variables.jpeg" style="width: 800px;">

<img src="images/pirates-of-variables.jpeg" alt="pirates-of-variables.jpeg" style="width: 800px;">

<img src="images/random-variable-definition.jpeg" alt="random-variable-definition.jpeg" style="width: 800px;">

<img src="images/random-variable-and-events.jpeg" alt="random-variable-and-events.jpeg" style="width: 800px;">

<img src="images/example-of-random-variables.jpeg" alt="example-of-random-variables.jpeg" style="width: 800px;">

<img src="images/properties-of-random-variables.jpeg" alt="properties-of-random-variables.jpeg" style="width: 800px;">

<img src="images/probability-mass-function.jpeg" alt="probability-mass-function.jpeg" style="width: 800px;">

---

## Probability Mass function

<img src="images/probability-mass-function-definition.jpeg" alt="probability-mass-function-definition.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-1.jpeg" alt="probability-mass-function-definition-1.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-2.jpeg" alt="probability-mass-function-definition-2.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-3.jpeg" alt="probability-mass-function-definition-3.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-4.jpeg" alt="probability-mass-function-definition-4.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-5.jpeg" alt="probability-mass-function-definition-5.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-6.jpeg" alt="probability-mass-function-definition-6.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-7.jpeg" alt="probability-mass-function-definition-7.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-8.jpeg" alt="probability-mass-function-definition-8.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-9.jpeg" alt="probability-mass-function-definition-9.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-10.jpeg" alt="probability-mass-function-definition-10.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-11.jpeg" alt="probability-mass-function-definition-11.jpeg" style="width: 800px;">

<img src="images/probability-mass-function-definition-12.jpeg" alt="probability-mass-function-definition-12.jpeg" style="width: 800px;">

---

## Expectations

Expected value is the probability‑weighted average of all possible outcomes of a random variable. It tells you the long‑run average you would see if you repeated the same random experiment many times.

### What expected value means

If you repeat a random process (like rolling a die or flipping a coin) thousands of times, the average result will approach the expected value. It’s the “center of gravity” of a probability distribution. 


<img src="images/expectations.jpeg" alt="expectations.jpeg" style="width: 800px;">

<img src="images/expected-value.jpeg" alt="expected-value" style="width: 800px;">

<img src="images/expected-value-definition.jpeg" alt="expected-value-definition" style="width: 800px;">

<img src="images/expected-value-example.jpeg" alt="expected-value-example" style="width: 800px;">

<img src="images/lying-with-statistics.jpeg" alt="lying-with-statistics" style="width: 800px;">

<img src="images/lying-with-statistics-part-2.jpeg" alt="lying-with-statistics-part-2" style="width: 800px;">

<img src="images/properties-of-expectations.jpeg" alt="properties-of-expectations" style="width: 800px;">

<img src="images/expectations-game.jpeg" alt="expectations-game" style="width: 800px;">

<img src="images/expectations-game-1.jpeg" alt="expectations-game-1" style="width: 800px;">

---

## Lecture - 7

<img src="images/leacture-7-learning-goal.jpeg" alt="leacture-7-learning-goal" style="width: 800px;">

<img src="images/is-peer-grading-accurate.jpeg" alt="is-peer-grading-accurate" style="width: 800px;">

<img src="images/lecture-7-review.jpeg" alt="lecture-7-review" style="width: 800px;">

<img src="images/probability-mass-function-value.jpeg" alt="probability-mass-function-value" style="width: 800px;">

<img src="images/probability-mass-function-as-an-equation.jpeg" alt="probability-mass-function-as-an-equation" style="width: 800px;">

<img src="images/random-variable-fundamental-properties.jpeg" alt="random-variable-fundamental-properties" style="width: 800px;">

<img src="images/expectations-formula-with-comments.jpeg" alt="expectations-formula-with-comments" style="width: 800px;">

<img src="images/properties-of-expectations-in-review.jpeg" alt="properties-of-expectations-in-review" style="width: 800px;">

<img src="images/expectations-from-data.jpeg" alt="expectations-from-data" style="width: 800px;">

<img src="images/expectation-of-sum.jpeg" alt="expectation-of-sum" style="width: 800px;">

<img src="images/linearity-of-expectations.jpeg" alt="linearity-of-expectations" style="width: 800px;">

<img src="images/is-expectation-enough.jpeg" alt="is-expectation-enough" style="width: 800px;">

<img src="images/pmf-is-complete.jpeg" alt="pmf-is-complete" style="width: 800px;">

<img src="images/cas-109-we-are-here-lecture-7.jpeg" alt="cas-109-we-are-here-lecture-7" style="width: 800px;">

<img src="images/coins-everywhere.jpeg" alt="coins-everywhere" style="width: 800px;">

<img src="images/many-random-variables-follow-this.jpeg" alt="many-random-variables-follow-this" style="width: 800px;">


### Probability of exactly K Heads in N experiments is

<img src="images/Probability of exactly K Heads.jpeg" alt="Probability of exactly K Heads" style="width: 800px;">

<img src="images/Probability of exactly K Heads Formula.jpeg" alt="Probability of exactly K Heads Formula" style="width: 800px;">

<img src="images/random-variable-binomial.jpeg" alt="random-variable-binomial" style="width: 800px;">

<img src="images/automatically-know-pmf.jpeg" alt="automatically-know-pmf" style="width: 800px;">

<img src="images/pmf-as-graph.jpeg" alt="pmf-as-graph" style="width: 800px;">

<img src="images/pmf-as-graph-1.jpeg" alt="pmf-as-graph-1" style="width: 800px;">

<img src="images/pmf-as-graph-2.jpeg" alt="pmf-as-graph-2" style="width: 800px;">

<img src="images/coins-with-bionomials.jpeg" alt="coins-with-bionomials" style="width: 800px;">

<img src="images/how-many-ads-clicked.jpeg" alt="how-many-ads-clicked" style="width: 800px;">

### Find Probability that H is less than 10

<img src="images/find-probability-that-h-lt-10.jpeg" alt="find-probability-that-h-lt-10" style="width: 800px;">

<img src="images/how-many-ads-clicked-python.jpeg" alt="how-many-ads-clicked-python" style="width: 800px;">

<img src="images/how-many-ads-clicked-python-1.jpeg" alt="how-many-ads-clicked-python-1" style="width: 800px;">

<img src="images/how-many-ads-clicked-graph.jpeg" alt="how-many-ads-clicked-graph" style="width: 800px;">

<img src="images/how-many-servers-crash.jpeg" alt="how-many-servers-crash" style="width: 800px;">

<img src="images/galton-board.jpeg" alt="galton-board" style="width: 800px;">

<img src="images/galton-board-1.jpeg" alt="galton-board-1" style="width: 800px;">

<img src="images/galton-board-2.jpeg" alt="galton-board-2" style="width: 800px;">

<img src="images/galton-board-3.jpeg" alt="galton-board-3" style="width: 800px;">

<img src="images/galton-board-4.jpeg" alt="galton-board-4" style="width: 800px;">

<img src="images/galton-board-5.jpeg" alt="galton-board-5" style="width: 800px;">

<img src="images/galton-board-6.jpeg" alt="galton-board-6" style="width: 800px;">

<img src="images/galton-board-7.jpeg" alt="galton-board-7" style="width: 800px;">

<img src="images/basket-ball-series.jpeg" alt="basket-ball-series" style="width: 800px;">

<img src="images/basket-ball-series-1.jpeg" alt="basket-ball-series-1" style="width: 800px;">

<img src="images/debugging-probability.jpeg" alt="debugging-probability" style="width: 800px;">

<img src="images/binomial-related-free-benefits.jpeg" alt="binomial-related-free-benefits" style="width: 800px;">

<img src="images/bernoulli.jpeg" alt="bernoulli" style="width: 800px;">

<img src="images/bernoulli-random-variable.jpeg" alt="bernoulli-random-variable" style="width: 800px;">

<img src="images/bernoulli-random-variable-example-1.jpeg" alt="bernoulli-random-variable-example-1" style="width: 800px;">

<img src="images/bernoulli-random-variable-example-2.jpeg" alt="bernoulli-random-variable-example-2" style="width: 800px;">

<img src="images/bernoulli-vs-binomials.jpeg" alt="bernoulli-vs-binomials" style="width: 800px;">

<img src="images/expectation-of-binomials.jpeg" alt="expectation-of-binomials" style="width: 800px;">

<img src="images/binomial-related-free-benefits-1.jpeg" alt="binomial-related-free-benefits-1" style="width: 800px;">

<img src="images/expectation-is-single-number.jpeg" alt="expectation-is-single-number" style="width: 800px;">

<img src="images/expectation-is-single-number.jpeg" alt="expectation-is-single-number" style="width: 800px;">

## Some people who lie with statistics, they use Expectations to back their lies.

<img src="images/expectation-is-leaving-behind-alot.jpeg" alt="expectation-is-leaving-behind-alot" style="width: 800px;">

<img src="images/invent-another-summary-number.jpeg" alt="invent-another-summary-number" style="width: 800px;">

<img src="images/intuition-peer-grading.jpeg" alt="intuition-peer-grading" style="width: 800px;">

<img src="images/measure-of-spread.jpeg" alt="measure-of-spread" style="width: 800px;">

<img src="images/peer-grading-in-coursera-1.jpeg" alt="peer-grading-in-coursera-1" style="width: 800px;">

<img src="images/peer-grading-in-coursera-2.jpeg" alt="peer-grading-in-coursera-2" style="width: 800px;">

<img src="images/peer-grading-in-coursera-3.jpeg" alt="peer-grading-in-coursera-3" style="width: 800px;">

<img src="images/peer-grading-in-coursera-4.jpeg" alt="peer-grading-in-coursera-4" style="width: 800px;">

<img src="images/peer-grading-in-coursera-5.jpeg" alt="peer-grading-in-coursera-5" style="width: 800px;">

<img src="images/variance.jpeg" alt="variance" style="width: 800px;">

<img src="images/variance-key.jpeg" alt="variance-key" style="width: 800px;">

<img src="images/approx-of-pmf.jpeg" alt="approx-of-pmf" style="width: 800px;">

<img src="images/computing-variance.jpeg" alt="computing-variance.jpeg" style="width: 800px;">

<img src="images/computing-variance-1.jpeg" alt="computing-variance-1.jpeg" style="width: 800px;">

<img src="images/standard-deviation.jpeg" alt="standard-deviation.jpeg" style="width: 800px;">

---

## Lecture-8

<img src="images/lecture-8-review-1.jpeg" alt="lecture-8-review-1" style="width: 800px;">

<img src="images/lecture-8-review-2.jpeg" alt="lecture-8-review-2" style="width: 800px;">

<img src="images/lecture-8-review-3.jpeg" alt="lecture-8-review-3" style="width: 800px;">

<img src="images/lecture-8-review-4.jpeg" alt="lecture-8-review-4" style="width: 800px;">

<img src="images/lecture-8-review-5.jpeg" alt="lecture-8-review-5" style="width: 800px;">

<img src="images/lecture-8-review-6.jpeg" alt="lecture-8-review-6" style="width: 800px;">

<img src="images/lecture-8-review-7.jpeg" alt="lecture-8-review-7" style="width: 800px;">

<img src="images/natural-exponent-definition.jpeg" alt="natural-exponent-definition" style="width: 800px;">

<img src="images/ride-share-problem-1.jpeg" alt="ride-share-problem-1" style="width: 800px;">

<img src="images/ride-share-problem-2.jpeg" alt="ride-share-problem-2" style="width: 800px;">

<img src="images/ride-share-problem-3.jpeg" alt="ride-share-problem-3" style="width: 800px;">

<img src="images/ride-share-problem-4.jpeg" alt="ride-share-problem-4" style="width: 800px;">

<img src="images/ride-share-problem-5.jpeg" alt="ride-share-problem-5" style="width: 800px;">

<img src="images/ride-share-problem-6.jpeg" alt="ride-share-problem-6" style="width: 800px;">

<img src="images/ride-share-problem-7.jpeg" alt="ride-share-problem-7" style="width: 800px;">

<img src="images/ride-share-problem-8.jpeg" alt="ride-share-problem-8" style="width: 800px;">

<img src="images/ride-share-problem-9.jpeg" alt="ride-share-problem-9" style="width: 800px;">

<img src="images/poisson-random-variable.jpeg" alt="poisson-random-variable" style="width: 800px;">

<img src="images/poisson-process.jpeg" alt="poisson-process" style="width: 800px;">

<img src="images/poisson-process-1.jpeg" alt="poisson-process-1" style="width: 800px;">

<img src="images/poisson-to-the-reader.jpeg" alt="poisson-to-the-reader" style="width: 800px;">

<img src="images/poisson-key.jpeg" alt="poisson-key" style="width: 800px;">

<img src="images/poisson-key-1.jpeg" alt="poisson-key-1" style="width: 800px;">

<img src="images/earthquake-problem.jpeg" alt="earthquake-problem" style="width: 800px;">

<img src="images/earthquake-problem-1.jpeg" alt="earthquake-problem-1" style="width: 800px;">

<img src="images/poisson-binomial.jpeg" alt="poisson-binomial" style="width: 800px;">

<img src="images/data-in-dna.jpeg" alt="data-in-dna" style="width: 800px;">

<img src="images/data-in-dna-1.jpeg" alt="data-in-dna-1" style="width: 800px;">

<img src="images/data-in-dna-2.jpeg" alt="data-in-dna-2" style="width: 800px;">

<img src="images/data-in-dna-3.jpeg" alt="data-in-dna-3" style="width: 800px;">

<img src="images/data-in-dna-4.jpeg" alt="data-in-dna-4" style="width: 800px;">

<img src="images/poisson-is-binomial-in-limits.jpeg" alt="poisson-is-binomial-in-limits" style="width: 800px;">

<img src="images/binomial-vs-poisson.jpeg" alt="binomial-vs-poisson" style="width: 800px;">

<img src="images/poisson-key-2.jpeg" alt="poisson-key-2" style="width: 800px;">

<img src="images/poisson-expectation-variance.jpeg" alt="poisson-expectation-variance" style="width: 800px;">

<img src="images/poisson-expectation-variance-1.jpeg" alt="poisson-expectation-variance-1" style="width: 800px;">

<img src="images/web-server-load-question.jpeg" alt="web-server-load-question" style="width: 800px;">

<img src="images/probability-for-extreme-weather-1.jpeg" alt="probability-for-extreme-weather-1" style="width: 800px;">

<img src="images/probability-for-extreme-weather-2.jpeg" alt="probability-for-extreme-weather-2" style="width: 800px;">

<img src="images/probability-for-extreme-weather-3.jpeg" alt="probability-for-extreme-weather-3" style="width: 800px;">

<img src="images/probability-for-extreme-weather-4.jpeg" alt="probability-for-extreme-weather-4" style="width: 800px;">

<img src="images/probability-for-extreme-weather-5.jpeg" alt="probability-for-extreme-weather-5" style="width: 800px;">

<img src="images/probability-for-extreme-weather-6.jpeg" alt="probability-for-extreme-weather-6" style="width: 800px;">

<img src="images/probability-for-extreme-weather-7.jpeg" alt="probability-for-extreme-weather-7" style="width: 800px;">

<img src="images/probability-for-extreme-weather-8.jpeg" alt="probability-for-extreme-weather-8" style="width: 800px;">

---

## Lecture 9

<img src="images/lecture-9-review-1.jpeg" alt="lecture-9-review-1" style="width: 800px;">

<img src="images/lecture-9-review-2.jpeg" alt="lecture-9-review-2" style="width: 800px;">

<img src="images/lecture-9-review-3.jpeg" alt="lecture-9-review-3" style="width: 800px;">

<img src="images/lecture-9-learning-goals.jpeg" alt="lecture-9-learning-goals" style="width: 800px;">

<img src="images/lecture-9-goals.jpeg" alt="lecture-9-goals" style="width: 800px;">

<img src="images/be-able-to-use-new-random-variables.jpeg" alt="be-able-to-use-new-random-variables" style="width: 800px;">

<img src="images/be-able-to-use-new-random-variables-1.jpeg" alt="be-able-to-use-new-random-variables-1" style="width: 800px;">

<img src="images/geometric-random-variables.jpeg" alt="geometric-random-variables" style="width: 800px;">

<img src="images/negative-binomial-random-variables.jpeg" alt="negative-binomial-random-variables" style="width: 800px;">

<img src="images/negative-binomial-random-variables-1.jpeg" alt="negative-binomial-random-variables-1" style="width: 800px;">

<img src="images/geometric-vs-negative-binomials.jpeg" alt="geometric-vs-negative-binomials" style="width: 800px;">

<img src="images/discrete-distributions.jpeg" alt="discrete-distributions" style="width: 800px;">

<img src="images/dating-at-stanford.jpeg" alt="dating-at-stanford" style="width: 800px;">

<img src="images/dating-at-stanford-solution.jpeg" alt="dating-at-stanford-solution" style="width: 800px;">

<img src="images/equity-in-the-courts.jpeg" alt="equity-in-the-courts" style="width: 800px;">

<img src="images/equity-in-the-courts-solution.jpeg" alt="equity-in-the-courts-solution" style="width: 800px;">

<img src="images/equity-in-the-courts-solution-1.jpeg" alt="equity-in-the-courts-solution-1" style="width: 800px;">

<img src="images/bitcoin-mining.jpeg" alt="bitcoin-mining" style="width: 800px;">

<img src="images/bitcoin-mining-1.jpeg" alt="bitcoin-mining-1" style="width: 800px;">

<img src="images/bitcoin-mining-2.jpeg" alt="bitcoin-mining-2" style="width: 800px;">

<img src="images/bitcoin-mining-3.jpeg" alt="bitcoin-mining-3" style="width: 800px;">

<img src="images/poisson.jpeg" alt="poisson" style="width: 800px;">

<img src="images/riding-a-bus.jpeg" alt="riding-a-bus" style="width: 800px;">

<img src="images/riding-a-bus-1.jpeg" alt="riding-a-bus-1" style="width: 800px;">

<img src="images/riding-a-bus-2.jpeg" alt="riding-a-bus-2" style="width: 800px;">

<img src="images/riding-a-bus-3.jpeg" alt="riding-a-bus-3" style="width: 800px;">

<img src="images/probability-density-function.jpeg" alt="probability-density-function" style="width: 800px;">

<img src="images/probability-density-function-1.jpeg" alt="probability-density-function-1" style="width: 800px;">

<img src="images/integrals.jpeg" alt="integrals" style="width: 800px;">

<img src="images/integrals-1.jpeg" alt="integrals-1" style="width: 800px;">

<img src="images/riding-a-bus-4.jpeg" alt="riding-a-bus-4" style="width: 800px;">

<img src="images/properties-of-pdf.jpeg" alt="properties-of-pdf" style="width: 800px;">

<img src="images/probability-density-function-outcome.jpeg" alt="probability-density-function-outcome" style="width: 800px;">

<img src="images/probability-density-function-1.jpeg" alt="probability-density-function-1" style="width: 800px;">

<img src="images/probability-density-function-key.jpeg" alt="probability-density-function-key" style="width: 800px;">

<img src="images/probability-density-function-2.jpeg" alt="probability-density-function-2" style="width: 800px;">

<img src="images/probability-density-function-3.jpeg" alt="probability-density-function-3" style="width: 800px;">

<img src="images/probability-density-function-4.jpeg" alt="probability-density-function-4" style="width: 800px;">

<img src="images/probability-density-function-5.jpeg" alt="probability-density-function-5" style="width: 800px;">

<img src="images/probability-density-function-6.jpeg" alt="probability-density-function-6" style="width: 800px;">

<img src="images/probability-density-function-7.jpeg" alt="probability-density-function-7" style="width: 800px;">

<img src="images/uniform-random-variable.jpeg" alt="uniform-random-variable" style="width: 800px;">

<img src="images/riding-a-bus-5.jpeg" alt="riding-a-bus-5" style="width: 800px;">

<img src="images/exponential-random-variable.jpeg" alt="exponential-random-variable" style="width: 800px;">

<img src="images/how-long-until-next-earthquake.jpeg" alt="how-long-until-next-earthquake.jpeg" style="width: 800px;">

<img src="images/how-long-until-next-earthquake-1.jpeg" alt="how-long-until-next-earthquake-1.jpeg" style="width: 800px;">

<img src="images/integral-review.jpeg" alt="integral-review.jpeg" style="width: 800px;">

<img src="images/how-long-until-next-earthquake-2.jpeg" alt="how-long-until-next-earthquake-2.jpeg" style="width: 800px;">

<img src="images/how-long-until-next-earthquake-3.jpeg" alt="how-long-until-next-earthquake-3.jpeg" style="width: 800px;">

<img src="images/how-long-until-next-earthquake-4.jpeg" alt="how-long-until-next-earthquake-4.jpeg" style="width: 800px;">

<img src="images/avoid-integrals.jpeg" alt="avoid-integrals.jpeg" style="width: 800px;">

<img src="images/cumulative-density-function.jpeg" alt="cumulative-density-function" style="width: 800px;">

<img src="images/cumulative-density-function-1.jpeg" alt="cumulative-density-function-1" style="width: 800px;">

<img src="images/cumulative-density-function-2.jpeg" alt="cumulative-density-function-2" style="width: 800px;">

<img src="images/cumulative-density-function-3.jpeg" alt="cumulative-density-function-3" style="width: 800px;">

<img src="images/cumulative-density-function-4.jpeg" alt="cumulative-density-function-4" style="width: 800px;">

<img src="images/cumulative-density-function-5.jpeg" alt="cumulative-density-function-5" style="width: 800px;">

<img src="images/cumulative-density-function-6.jpeg" alt="cumulative-density-function-6" style="width: 800px;">

<img src="images/cumulative-density-function-7.jpeg" alt="cumulative-density-function-7" style="width: 800px;">

<img src="images/cumulative-density-function-8.jpeg" alt="cumulative-density-function-8" style="width: 800px;">

