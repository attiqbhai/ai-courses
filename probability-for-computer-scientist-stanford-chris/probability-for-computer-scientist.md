<H1>Probability for Computer Scientist - Stanford - Chris Piech</H1>

---

<H2>TABLE OF CONTENT</H2>

- [Course Material Online](#course-material-online)
- [Lecture 1](#lecture-1)
- [Lecture 2](#lecture-2)
- [Leacture 3](#leacture-3)
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
  - [Probability](#probability)
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

## Course Material Online

https://chrispiech.github.io/probabilityForComputerScientists/en/

---

## Lecture 1

<img src="images/lecture-1-pre-requisites.jpeg" alt="lecture-1-pre-requisites.jpeg" style="width: 800px;">

<img src="images/lecture-1-human-brain.jpeg" alt="lecture-1-human-brain.jpeg" style="width: 800px;">

<img src="images/lecture-1-two-geat-ideas.jpeg" alt="lecture-1-two-geat-ideas.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons.jpeg" alt="lecture-1-artifical-neurons.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon.jpeg" alt="lecture-1-artifical-neurons-cartoon.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-1.jpeg" alt="lecture-1-artifical-neurons-cartoon-1.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-2.jpeg" alt="lecture-1-artifical-neurons-cartoon-2.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-3.jpeg" alt="lecture-1-artifical-neurons-cartoon-3.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-4.jpeg" alt="lecture-1-artifical-neurons-cartoon-4.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-5.jpeg" alt="lecture-1-artifical-neurons-cartoon-5.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-6.jpeg" alt="lecture-1-artifical-neurons-cartoon-6.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-7.jpeg" alt="lecture-1-artifical-neurons-cartoon-7.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-8.jpeg" alt="lecture-1-artifical-neurons-cartoon-8.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-9.jpeg" alt="lecture-1-artifical-neurons-cartoon-9.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-10.jpeg" alt="lecture-1-artifical-neurons-cartoon-10.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-11.jpeg" alt="lecture-1-artifical-neurons-cartoon-11.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-12.jpeg" alt="lecture-1-artifical-neurons-cartoon-12.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-13.jpeg" alt="lecture-1-artifical-neurons-cartoon-13.jpeg" style="width: 800px;">

<img src="images/lecture-1-artifical-neurons-cartoon-14.jpeg" alt="lecture-1-artifical-neurons-cartoon-14.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-1.jpeg" alt="lecture-1-learb-by-example-1.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-2.jpeg" alt="lecture-1-learb-by-example-2.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-3.jpeg" alt="lecture-1-learb-by-example-3.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-4.jpeg" alt="lecture-1-learb-by-example-4.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-5.jpeg" alt="lecture-1-learb-by-example-5.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-6.jpeg" alt="lecture-1-learb-by-example-6.jpeg" style="width: 800px;">

<img src="images/lecture-1-learb-by-example-7.jpeg" alt="lecture-1-learb-by-example-7.jpeg" style="width: 800px;">

<img src="images/lecture-1-we-will-get-there.jpeg" alt="lecture-1-we-will-get-there.jpeg" style="width: 800px;">

<img src="images/lecture-1-we-will-solve-problems.jpeg" alt="lecture-1-we-will-solve-problems.jpeg" style="width: 800px;">

<img src="images/lecture-1-where-it-is-useful.jpeg" alt="lecture-1-where-it-is-useful.jpeg" style="width: 800px;">

<img src="images/lecture-1-zeka-test.jpeg" alt="lecture-1-zeka-test.jpeg" style="width: 800px;">

<img src="images/lecture-1-probability.jpeg" alt="lecture-1-probability.jpeg" style="width: 800px;">

<img src="images/lecture-1-math.jpeg" alt="lecture-1-math.jpeg" style="width: 800px;">

<img src="images/lecture-1-ai-map.jpeg" alt="lecture-1-ai-map.jpeg" style="width: 800px;">

<img src="images/lecture-1-what-is-counting-1.jpeg" alt="lecture-1-what-is-counting-1.jpeg" style="width: 800px;">

<img src="images/lecture-1-what-is-counting-2.jpeg" alt="lecture-1-what-is-counting-2.jpeg" style="width: 800px;">

<img src="images/lecture-1-step-rule-of-counting.jpeg" alt="lecture-1-step-rule-of-counting.jpeg" style="width: 800px;">

<img src="images/lecture-1-step-rule-of-counting-1.jpeg" alt="lecture-1-step-rule-of-counting-1.jpeg" style="width: 800px;">

<img src="images/lecture-1-step-rule-of-counting-2.jpeg" alt="lecture-1-step-rule-of-counting-2.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-1.jpeg" alt="lecture-1-sum-rule-of-counting-1.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-2.jpeg" alt="lecture-1-sum-rule-of-counting-2.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-3.jpeg" alt="lecture-1-sum-rule-of-counting-3.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-4.jpeg" alt="lecture-1-sum-rule-of-counting-4.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-5.jpeg" alt="lecture-1-sum-rule-of-counting-5.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-6.jpeg" alt="lecture-1-sum-rule-of-counting-6.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-7.jpeg" alt="lecture-1-sum-rule-of-counting-7.jpeg" style="width: 800px;">

<img src="images/lecture-1-sum-rule-of-counting-8.jpeg" alt="lecture-1-sum-rule-of-counting-8.jpeg" style="width: 800px;">

<img src="images/lecture-1-ste-rule-vs-sum-rule.jpeg" alt="lecture-1-ste-rule-vs-sum-rule.jpeg" style="width: 800px;">


---

## Lecture 2

<img src="images/lecture-2-permutations-1.jpeg" alt="lecture-2-permutations-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-permutations-2.jpeg" alt="lecture-2-permutations-2.jpeg" style="width: 800px;">

<img src="images/lecture-2-step-rule-of-counting.jpeg" alt="lecture-2-step-rule-of-counting.jpeg" style="width: 800px;">

<img src="images/lecture-2-permutations-3.jpeg" alt="lecture-2-permutations-3.jpeg" style="width: 800px;">

<img src="images/lecture-2-six-digit-passcode.jpeg" alt="lecture-2-six-digit-passcode.jpeg" style="width: 800px;">

<img src="images/lecture-2-step-rule-of-counting-1.jpeg" alt="lecture-2-step-rule-of-counting-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-six-digit-passcode-1.jpeg" alt="lecture-2-six-digit-passcode-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct.jpeg" alt="lecture-2-objects-indistinct.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-1.jpeg" alt="lecture-2-objects-indistinct-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-2.jpeg" alt="lecture-2-objects-indistinct-2.jpeg" style="width: 800px;">

<img src="images/general-permutations-formula.jpeg" alt="general-permutations-formula.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-3.jpeg" alt="lecture-2-objects-indistinct-3.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-4.jpeg" alt="lecture-2-objects-indistinct-4.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-5.jpeg" alt="lecture-2-objects-indistinct-5.jpeg" style="width: 800px;">

<img src="images/lecture-2-objects-indistinct-6.jpeg" alt="lecture-2-objects-indistinct-6.jpeg" style="width: 800px;">

<img src="images/lecture-2-5-smughes-six-digit-passcode-1.jpeg" alt="lecture-2-5-smughes-six-digit-passcode-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-5-smughes-six-digit-passcode-2.jpeg" alt="lecture-2-5-smughes-six-digit-passcode-2.jpeg" style="width: 800px;">

<img src="images/lecture-2-5-smughes-six-digit-passcode-3.jpeg" alt="lecture-2-5-smughes-six-digit-passcode-3.jpeg" style="width: 800px;">

<img src="images/5-smughes-six-digit-passcode.jpeg" alt="5-smughes-six-digit-passcode.jpeg" style="width: 800px;">

<img src="images/summary-of-combinatorics.jpeg" alt="summary-of-combinatorics.jpeg" style="width: 800px;">

<img src="images/lecture-2-combinations-with-cake-1.jpeg" alt="lecture-2-combinations-with-cake-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-combinations-with-cake-2.jpeg" alt="lecture-2-combinations-with-cake-2.jpeg" style="width: 800px;">

<img src="images/lecture-2-combinations-with-cake-3.jpeg" alt="lecture-2-combinations-with-cake-3.jpeg" style="width: 800px;">

<img src="images/lecture-2-combinations-with-cake-4.jpeg" alt="lecture-2-combinations-with-cake-4.jpeg" style="width: 800px;">

<img src="images/lecture-2-combinations-with-cake-5.jpeg" alt="lecture-2-combinations-with-cake-5.jpeg" style="width: 800px;">

<img src="images/combinations-with-cake-1.jpeg" alt="combinations-with-cake-1.jpeg" style="width: 800px;">

<img src="images/combinations-with-cake-2.jpeg" alt="combinations-with-cake-2.jpeg" style="width: 800px;">

<img src="images/combinations-with-cake-3.jpeg" alt="combinations-with-cake-3.jpeg" style="width: 800px;">

<img src="images/combinations-with-cake-4.jpeg" alt="combinations-with-cake-4.jpeg" style="width: 800px;">

<img src="images/combinations-with-cake-5.jpeg" alt="combinations-with-cake-5.jpeg" style="width: 800px;">

<img src="images/combinations.jpeg" alt="combinations.jpeg" style="width: 800px;">

<img src="images/combinations-2.jpeg" alt="combinations-2.jpeg" style="width: 800px;">

<img src="images/combinations-3.jpeg" alt="combinations-3.jpeg" style="width: 800px;">

<img src="images/combinations-4.jpeg" alt="combinations-4.jpeg" style="width: 800px;">

<img src="images/lecture-2-cards-problem-1.jpeg" alt="lecture-2-cards-problem-1.jpeg" style="width: 800px;">

<img src="images/cards-problem.jpeg" alt="cards-problem.jpeg" style="width: 800px;">

<img src="images/summary-of-combinatorics-1.jpeg" alt="summary-of-combinatorics-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-summary-of-combinatorics-1.jpeg" alt="lecture-2-summary-of-combinatorics-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-put-objects-in-buckets-1.jpeg" alt="lecture-2-put-objects-in-buckets-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-summary-of-combinatorics-2.jpeg" alt="lecture-2-summary-of-combinatorics-2.jpeg" style="width: 800px;">

<img src="images/lecture-2-put-indistinct-objects-in-buckets-1.jpeg" alt="lecture-2-put-indistinct-objects-in-buckets-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-divider-method.jpeg" alt="lecture-2-divider-method.jpeg" style="width: 800px;">

<img src="images/lecture-2-divider-method-1.jpeg" alt="lecture-2-divider-method-1.jpeg" style="width: 800px;">

<img src="images/lecture-2-summary-of-combinatorics-3.jpeg" alt="lecture-2-summary-of-combinatorics-3.jpeg" style="width: 800px;">

---

## Leacture 3

<img src="images/leacture-3-learn-probability-1.jpeg" alt="leacture-3-learn-probability-1.jpeg" style="width: 800px;">

<img src="images/leacture-3-enigma-machine.jpeg" alt="leacture-3-enigma-machine.jpeg" style="width: 800px;">

<img src="images/leacture-3-review-1.jpeg" alt="leacture-3-review-1.jpeg" style="width: 800px;">

<img src="images/leacture-3-review-2.jpeg" alt="leacture-3-review-2.jpeg" style="width: 800px;">

<img src="images/leacture-3-review-3.jpeg" alt="leacture-3-review-3.jpeg" style="width: 800px;">

<img src="images/event-space.jpeg" alt="event-space.jpeg" style="width: 800px;">

<img src="images/sample-event-space.jpeg" alt="sample-event-space.jpeg" style="width: 800px;">

<img src="images/probability.jpeg" alt="probability.jpeg" style="width: 800px;">

<img src="images/what-is-probability.jpeg" alt="what-is-probability.jpeg" style="width: 800px;">

<img src="images/what-is-probability-1.jpeg" alt="what-is-probability-1.jpeg" style="width: 800px;">

<img src="images/axioms-of-probability.jpeg" alt="axioms-of-probability.jpeg" style="width: 800px;">

<img src="images/core-rules-of-probability.jpeg" alt="core-rules-of-probability.jpeg" style="width: 800px;">

<img src="images/equally-likely-outcome.jpeg" alt="equally-likely-income.jpeg" style="width: 800px;">

<img src="images/equally-likely-outcome-1.jpeg" alt="equally-likely-income-1.jpeg" style="width: 800px;">

<img src="images/not-equally-likely.jpeg" alt="not-equally-likely.jpeg" style="width: 800px;">

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

<img src="images/equally-likely-probability.jpeg" alt="equally-likely-probability.jpeg" style="width: 800px;">

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

