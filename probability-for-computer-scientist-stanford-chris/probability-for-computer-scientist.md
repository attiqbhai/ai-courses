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

#### Intuition

You’re building an outcome step by step.

Each step multiplies the number of possibilities.

Think of it like building a sequence:

- First position → choose something
- Second position → choose something
- Third position → choose something

Multiply all choices together.

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
