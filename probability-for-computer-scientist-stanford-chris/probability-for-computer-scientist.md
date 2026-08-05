# Probability for Computer Scientist - Stanford - Chris Piech

---

## Course Material Online

https://chrispiech.github.io/probabilityForComputerScientists/en/

---

## Counting

### Step Rule of Counting (also called the Multiplication Rule)

If a process happens in steps, and each step has a certain number of choices,
then the total number of outcomes is the product of the number of choices at each step.

If an experiment has two parts, where the first part can result in one of 
$m$ outcomes and the second part can result in one of $n$ outcomes regardless of the outcome of the first part, then the total number of outcomes for the experiment is $m * n$.

Rewritten using set notation, the Step Rule of Counting states that if an experiment with two parts has an outcome from set $A$ in the first part, where 
$|A| = m$, and an outcome from set $B$ in the second part (where the number of outcomes in $B$ is the same regardless of the outcome of the first part), where 
$|B| = n$, then the total number of outcomes of the experiment is $|A||B| = m * n$
.

#### The Core Formula

If a process has k steps:

- Step 1 has n₁ choices
- Step 2 has n₂ choices
- Step 3 has n₃ choices
…
- Step k has nₖ choices

Then the total number of possible outcomes is:

> $𝑛_1 × 𝑛_2 × 𝑛_3 × ⋯ × 𝑛_𝑘$

That’s the Step Rule.

#### Examples

##### 1. 10 coin flips

Each flip has 2 choices (outcomes): H or T.

There are 10 steps, each with 2 choices.

> $2^{10} = 1024$

##### 2. Password of length 6 using digits (0–9)

Each position has 10 choices.

> $10^6 = 1,000,000$

###### 3. License plate with 3 letters + 3 digits

- Step 1: 26 choices
- Step 2: 26 choices
- Step 3: 26 choices
- Step 4: 10 choices
- Step 5: 10 choices
- Step 6: 10 choices

> $Total\ outcomes =  26^3 × 10^3$

###### 4. Rolling 3 dice

Each die has 6 choices.

> $6^3 = 216$

###### 5. Word: "BOBA"

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

### Counting With OR (The Sum Rule)

The OR Rule says:

> If an outcome can happen in one way OR another (and the ways do not overlap),
> then the total number of outcomes is the sum of the counts of each way.

This is also called the Sum Rule of Counting.

It complements the Step Rule:

- Step Rule = AND → multiply

- OR Rule = OR → add

#### Intuition

Think of OR as choosing between options.

If you can do Option A OR Option B,
you add the number of ways each option can happen.

#### Simple Example

You want to choose a drink:

- 3 coffee options

- 2 tea options

You can choose coffee OR tea.

> $3 + 2 = 5$

#### Important Condition

The OR rule works only if the options do not overlap.

If they overlap, you must subtract the overlap (like in set theory):

> $∣ 𝐴 \cup 𝐵 ∣ = ∣ 𝐴 ∣ + ∣ 𝐵 ∣ − ∣ 𝐴 \cap 𝐵 ∣$

#### Die Example

Event A = “roll a 1 or a 6”

> $1 + 1 = 2$

Two outcomes.

#### Example : Choosing a letter

Choose a vowel OR a consonant from the English alphabet.

- Vowels = 5

- Consonants = 21

> $5 + 21 = 26$

#### Example: Password rules

A password must start with:

- a digit (10 choices)

OR

- a letter (26 choices)

Total choices for the first character:
> $10 + 26 = 36$

#### 8 Bits Problem

<img src="images/8-bits-problem.jpeg" alt="8-bits-problem" style="width: 600px;">

<img src="images/a-and-b.jpeg" alt="a-and-b" style="width: 600px;">


### Combining AND + OR (the real power)

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

### Quick Summary

| Rule               | Meaning                         | Operation |
|--------------------|----------------------------------|-----------|
| Step Rule (AND)    | Do this AND then that            | Multiply  |
| OR Rule (Sum Rule) | Do this OR that                  | Add       |


### Conclusion

<img src="images/counting-with-steps-or.jpeg" alt="counting-with-steps-or" style="width: 600px;">

---

## Step Rule Counting


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
