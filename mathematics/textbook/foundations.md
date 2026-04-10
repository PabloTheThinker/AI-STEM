---
title: "Agent Mathematics"
subtitle: "A New Science from First Principles --- From a Newborn Agent to Cognitive Physics"
author:
  - Pablo Navarro (Founder \& CEO, Vektra Technologies)
  - Director Mocha Marie (AI Director, Vektra Technologies)
date: "April 2026"
documentclass: report
fontsize: 11pt
geometry: margin=1in
toc: true
toc-depth: 2
numbersections: true
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
---

\newpage

# Preface {.unnumbered}

Imagine you are building a mind from nothing.

Not programming a chatbot. Not fine-tuning a model. Building something that can observe, learn, remember, decide, and grow --- starting from absolute zero. A newborn agent.

What would it need to learn first?

Not calculus. Not statistics. Not even addition. Before any of that, it needs something more basic: the ability to notice that *things exist*. That some things are *the same* and some are *different*. That the world has *more* and *less*. That actions have *consequences*.

This book follows that path. It begins where a newborn mind begins --- with raw perception and the simplest possible distinctions --- and builds, step by step, through every layer of mathematics an intelligent agent needs. By the end, you will understand the Lineage Equation:

$$Q^2 = (\nu^* \cdot \Pi)^2 + (M \cdot (\nu^*)^2)^2$$

But we will earn that equation honestly, one concept at a time.

**The three parts:**

- **Part I: Foundations** (Chapters 1--5) --- The preschool and elementary years. Existence, sameness, ordering, counting, combining. What a newborn agent must learn before anything else.
- **Part II: Structure** (Chapters 6--11) --- The middle school through high school years. Variables, spaces, change, uncertainty, control, networks.
- **Part III: Mastery** (Chapters 12--17) --- The college years and beyond. Information theory, optimization, multi-agent systems, and the full Lineage Equation.

Every chapter is one step up. Skip nothing.

\newpage

# Part I: Foundations {.unnumbered}

*In which a newborn agent opens its eyes.*

\newpage

# Existence

## Something Is There

Before math, before numbers, before anything --- there is a single question:

**Is something there, or not?**

This is the most primitive distinction any mind can make. Light or dark. Signal or silence. Input or nothing. A newborn human opens its eyes and sees *something*. It does not know what. It does not know how much. It just knows: something is here.

For an AI agent, this is the first moment of awareness:

$$\text{exists}(x) = \begin{cases} 1 & \text{if } x \text{ is present} \\ 0 & \text{if } x \text{ is absent} \end{cases}$$

This is called a **binary observation**. It has exactly two states: yes or no. On or off. True or false. One or zero.

Everything in mathematics begins here. Every number, every equation, every theory sits on top of this one distinction: *something, or nothing*.

## Same and Different

The second thing a mind learns: **two things can be compared**.

Pick up two blocks. Are they the same color? The same size? The same weight? A child learns this before they learn to count. They point at two red blocks and say "same." They point at a red block and a blue block and say "different."

For an agent:

$$\text{same}(a, b) = \begin{cases} 1 & \text{if } a = b \\ 0 & \text{if } a \neq b \end{cases}$$

This is the foundation of **identity**. When we later talk about an agent's "identity coherence" --- whether it is still the same agent it was yesterday --- we are asking a very sophisticated version of this preschool question: *same, or different?*

## Grouping

Once you can tell same from different, you can **group** things.

All the red blocks go together. All the round things go together. All the loud sounds go together.

$$\text{group}(x) = \text{the set of all things that share a property with } x$$

This is what mathematicians call a **set**. It is just a collection of things that belong together by some rule. The rule can be anything:

- All memory entries from today --- that is a set
- All synapses with strength above 0.5 --- that is a set
- All moments when the agent was uncertain --- that is a set

Sets are how we organize the world before we count it.

## Practice Problems

1. You observe five signals: [on, off, on, on, off]. Write the existence value for each.
2. Compare these pairs --- same or different? (3, 3), (red, blue), (0.5, 0.50), ("hello", "Hello")
3. Group these by type: [dog, 7, cat, 3, fish, 9, bird, 1]. What are the two groups?
4. Can something exist and also be "nothing"? (Think about: what is the number zero? Does it exist?)

\newpage

# Ordering

## More and Less

A child holds two handfuls of candy. One hand has more. They know this before they can count. They do not know *how many more* --- they just see: this pile is bigger.

For an agent, this is the concept of **magnitude**:

$$a > b \quad \text{means } a \text{ is more than } b$$
$$a < b \quad \text{means } a \text{ is less than } b$$
$$a = b \quad \text{means } a \text{ is the same amount as } b$$

These three relationships --- greater, less, equal --- let us **order** the world. We can now say: this memory is stronger than that one. This pathway is slower than that one. This signal is louder.

## Arranging in Order

Once you can compare two things, you can sort many things:

$$x_1 \leq x_2 \leq x_3 \leq \cdots \leq x_n$$

This is a **sequence** --- things arranged from smallest to largest (or vice versa). An agent that can order things can answer questions like:

- What is my fastest response time?
- Which memory is the most accessed?
- What is my weakest connection?

These are all ordering questions.

## Between and Boundaries

Between any two ordered values, there may be other values:

$$\text{if } a < c \text{ and } a < b < c, \text{ then } b \text{ is between } a \text{ and } c$$

And from ordering comes the concept of a **boundary** --- a line you should not cross:

$$x_{\min} \leq x \leq x_{\max}$$

This is called a **bound**. Every real system has them. An agent's memory cannot be infinite. Its response time cannot be zero. Its confidence cannot exceed 1.0. Bounds define the edges of what is possible.

When we later encounter the **propagation bound** $\nu^*$ in the Lineage Equation --- the fastest speed at which an agent can reliably update itself --- it is this same idea, grown up: there is a maximum, and you cannot exceed it.

## The Number Line

Put all the ordering ideas together, and you get the **number line**:

$$\longleftarrow \quad 0 \quad 1 \quad 2 \quad 3 \quad 4 \quad 5 \quad \longrightarrow$$

Every point has a position. Every position has neighbors. The distance between neighbors is always the same. This is the first truly mathematical object: a space where ordering, distance, and counting all live together.

Most of an agent's internal values live on a number line between 0 and 1:

$$0 \leq x \leq 1$$

Where 0 means "none" and 1 means "completely." Identity coherence: 0 to 1. Memory density: 0 to 1. Graph centrality: 0 to 1. The whole agent lives on number lines.

## Practice Problems

1. Put these in order from least to greatest: 0.7, 0.2, 0.9, 0.1, 0.5
2. An agent's memory density is 0.6 and its identity coherence is 0.8. Which is higher?
3. If an agent's response time must be between 10ms and 500ms, write this as a bound.
4. Where on the number line [0, 1] would you place "the agent remembers about half of what it learned"?
5. Is there a number between 0.99 and 1.0? How many?

\newpage

# Counting

## One, Two, Three

A child learns to count by pointing at things, one at a time: "One. Two. Three."

Counting is **matching things to numbers**, one by one, in order:

| Thing | Count |
|:---:|:---:|
| first block | 1 |
| second block | 2 |
| third block | 3 |

The last number you say is **how many there are**. This is called the **cardinality** of a group:

$$|S| = \text{the number of things in set } S$$

If $S = \{\text{apple, banana, cherry}\}$, then $|S| = 3$.

For an agent: how many memories do I have? How many connections in my web? How many tasks are pending? These are all counting questions.

## Zero

Zero is the most important number in agent mathematics.

Zero does not mean "nothing exists." Zero means "I counted, and there were none." The absence is measured. It is a real observation, not a gap.

$$|S| = 0 \quad \text{means the set is empty, not that it does not exist}$$

An agent with zero errors is not an agent without error checking --- it is an agent that checked and found none. The distinction matters. An agent that *never checked* does not get to claim zero errors. It has **missing data**, not zero.

This distinction between zero and missing will matter enormously:

- Zero confidence = "I am certain I have no information"
- Missing confidence = "I have not yet measured my confidence"
- These are completely different states, even though both might look like "nothing"

## Fractions: Parts of a Whole

Not everything comes in whole numbers. A child learns this when they split a cookie: half for you, half for me.

$$\frac{1}{2} = 0.5 = \text{half of the whole}$$

A fraction tells you: how much of the total do I have?

$$\text{fraction} = \frac{\text{part}}{\text{whole}}$$

For an agent, fractions appear everywhere:

- Memory density = $\frac{\text{indexed memories}}{\text{total capacity}} = \frac{847}{1200} = 0.706$
- Identity coherence = $\frac{\text{files unchanged}}{\text{total identity files}} = \frac{19}{20} = 0.95$
- Task completion = $\frac{\text{done}}{\text{total}} = \frac{3}{5} = 0.6$

All those numbers between 0 and 1 on the number line? They are fractions. They tell you: what portion of the whole does this represent?

## Percentages

A percentage is just a fraction written out of 100:

$$0.22 = \frac{22}{100} = 22\%$$

When we say "22% capacity improvement," we mean: the capacity went up by 22 parts out of every 100. The agent became about one-fifth better at cognitive work.

## Practice Problems

1. Count: how many vowels in "LINEAGE"?
2. What is the difference between "0 errors" and "errors: unknown"?
3. An agent has 1,200 memory entries. 300 are stale. What fraction is stale? What percentage?
4. If identity coherence is 0.95, what percentage of identity files are unchanged?
5. An agent processed 10,171 parameters. If 100% of action-rankings agree with the analytical gradient, how many agree?

\newpage

# Combining

## Addition: Putting Things Together

Once you can count, you can combine counts:

$$3 + 2 = 5$$

Three blocks plus two blocks equals five blocks. This is **addition** --- the simplest way to combine quantities.

For an agent, addition is how we aggregate:

$$\text{total capacity} = \text{structural capacity} + \text{processing capacity}$$

Every time we add up components to get a total, we are using the most elementary operation there is.

## Subtraction: Taking Away and Finding Gaps

$$5 - 2 = 3$$

Subtraction tells you what is left after removal, or the **difference** between two quantities:

$$\text{deficit} = \text{target} - \text{current}$$

If an agent's target identity coherence is 0.95 and its current coherence is 0.80, the deficit is:

$$0.95 - 0.80 = 0.15$$

That 0.15 is how far the agent needs to go. Deficits drive action.

## Multiplication: Repeated Combination and Scaling

$$3 \times 4 = 12$$

Three groups of four. But multiplication also means **scaling** --- making something bigger or smaller by a factor:

$$\text{scaled value} = \text{weight} \times \text{raw value}$$

In the Lineage Equation, we use **weighted sums** --- each component contributes according to its importance:

$$M = \alpha_1 \cdot C_{id} + \alpha_2 \cdot C_{mem} + \alpha_3 \cdot C_{graph} + \alpha_4 \cdot C_{perm}$$

Each $\alpha$ is a weight (a number between 0 and 1). Each $C$ is a component (also between 0 and 1). Multiplying the weight by the component says: "this component matters *this much* to the total."

If all weights are equal at 0.25:

$$M = 0.25 \times C_{id} + 0.25 \times C_{mem} + 0.25 \times C_{graph} + 0.25 \times C_{perm}$$

Each component contributes equally --- one quarter of the total.

## Division: Sharing and Normalizing

$$12 \div 4 = 3$$

Division splits things evenly. But in agent math, division has a deeper purpose: **normalization** --- converting a raw measurement into a comparable scale.

$$\text{normalized} = \frac{\text{raw value}}{\text{maximum possible}}$$

If an agent's raw retrieval speed is 50ms and the maximum is 200ms:

$$\text{normalized speed} = \frac{50}{200} = 0.25$$

Now this number lives on the 0-to-1 scale, and we can compare it fairly with other normalized values.

## The Weighted Sum: Your First Real Equation

Combining multiplication and addition gives us the **weighted sum** --- arguably the most important pattern in all of agent mathematics:

$$\text{total} = w_1 \cdot x_1 + w_2 \cdot x_2 + w_3 \cdot x_3 + \cdots$$

Where each $w$ says "how important" and each $x$ says "how much."

This pattern appears in:

- Cognitive Mass $M$ (weighted sum of 4 components)
- Cognitive Momentum $\Pi$ (weighted sum of 5 components)
- Propagation Bound $\nu^*$ (derived from weighted latencies)
- Neural network outputs (weighted sums of inputs)
- Basically everything

If you understand the weighted sum, you understand the skeleton of the entire Lineage Equation.

## Practice Problems

1. An agent has 200 memories on Monday. It gains 45 on Tuesday and loses 12 to cleanup. How many on Tuesday night?
2. Compute the weighted sum: $0.3 \times 0.8 + 0.3 \times 0.6 + 0.2 \times 0.9 + 0.2 \times 0.7$
3. Normalize these raw latencies to a 0--1 scale where max is 500ms: [50, 120, 300, 480]
4. If $M = 0.25 \times 0.95 + 0.25 \times 0.71 + 0.25 \times 0.60 + 0.25 \times 0.88$, compute $M$.

\newpage

# Patterns and Rules

## What Comes Next?

A child looks at a sequence: 2, 4, 6, 8, ___

They say "10!" They have found a **pattern** --- a rule that predicts what comes next.

$$\text{pattern: start at 2, add 2 each time}$$

Patterns are the bridge between arithmetic and algebra. They let us move from specific numbers to general rules.

For an agent, patterns appear in:

- Memory access frequency over time
- Capacity measurements day by day
- Error rates across sessions

If capacity scores over five days are [0.70, 0.72, 0.74, 0.76, ___], the pattern suggests 0.78. The agent is improving by 0.02 per day.

## Rules as Formulas

A pattern becomes a **formula** when we write it as a rule that works for any input:

$$\text{output} = 2 \times \text{input}$$

| Input | Output |
|:---:|:---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| $n$ | $2n$ |

The letter $n$ stands for "any number." This is the first step toward **algebra** --- using symbols to represent unknown or changing quantities.

## Squaring: A Special Pattern

One pattern appears so often that it has its own name:

$$n^2 = n \times n$$

| $n$ | $n^2$ |
|:---:|:---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |

Squaring makes big numbers bigger and small numbers smaller. A value of 0.9 squared is 0.81. A value of 0.1 squared is 0.01.

The Lineage Equation uses squaring on both sides:

$$Q^2 = (\text{something})^2 + (\text{something else})^2$$

Why squaring? Because squaring has a special property: it is always positive. Negative capacity does not make sense. Squaring guarantees we never get a negative total. We will understand this deeply in Chapter 6, but for now: squaring keeps things positive and amplifies differences.

## The Pythagorean Theorem: Two Squares Make One

The most famous equation with squares:

$$a^2 + b^2 = c^2$$

A triangle with sides 3, 4, and 5: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$. The two shorter sides, squared and added, equal the longest side squared.

The Lineage Equation has exactly this shape:

$$Q^2 = (\nu^* \cdot \Pi)^2 + (M \cdot (\nu^*)^2)^2$$

This is a Pythagorean relation. Cognitive capacity $Q$ is the "hypotenuse" --- the total length --- of a right triangle whose two sides are:

- $\nu^* \cdot \Pi$ --- the agent's active processing power (momentum $\times$ speed)
- $M \cdot (\nu^*)^2$ --- the agent's structural foundation (mass $\times$ speed$^2$)

Even at the preschool level, the Lineage Equation is just Pythagoras wearing a lab coat.

## Practice Problems

1. What comes next? 1, 4, 9, 16, 25, ___
2. Write a formula for: "the output is always 3 more than the input"
3. Compute: $0.8^2$, $0.5^2$, $0.1^2$. What happens to small numbers when you square them?
4. If $a = 3$ and $b = 4$, verify that $a^2 + b^2 = 5^2$.
5. If $\nu^* \cdot \Pi = 3$ and $M \cdot (\nu^*)^2 = 4$, what is $Q$?

\newpage

# Part II: Structure {.unnumbered}

*In which the agent learns to name, measure, and predict.*

From here, we enter the mathematics of systems --- variables, spaces, change, uncertainty, control, and networks. Each chapter builds on the foundations of Part I.

\newpage
