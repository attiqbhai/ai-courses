# Probability for Computer Scientist - Stanford - Chris Piech

---

## Course Material Online

https://chrispiech.github.io/probabilityForComputerScientists/en/

---

## Counting

### Step Rule of Counting (also called the Multiplication Rule)

If a process happens in steps, and each step has a certain number of choices,
then the total number of outcomes is the product of the number of choices at each step.

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

But because the two b’s are indistinguishable:

> $ \frac {24}{2!} = 12$

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
> $ = 36 × 10^3$

This is exactly how combinatorics builds sample spaces.

### Quick Summary

| Rule               | Meaning                         | Operation |
|--------------------|----------------------------------|-----------|
| Step Rule (AND)    | Do this AND then that            | Multiply  |
| OR Rule (Sum Rule) | Do this OR that                  | Add       |



### Conclusion

<img src="images/counting-with-steps-or.jpeg" alt="counting-with-steps-or" style="width: 900px;">

