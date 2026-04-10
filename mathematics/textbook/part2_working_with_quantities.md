# Part II: Working with Quantities

In Part I, we learned how to say that something exists, how to tell when two things are the same, how to place things in order, and how to count, add, and subtract. Those ideas let an agent keep track of discrete objects: tasks, memories, messages, ticks, and choices.

But agents do not live by counting alone. A memory may matter more than another memory. A task may receive half as much attention as another. A coherence score may be $0.85$, which is not a count at all, but a measured amount of some quality. A process may happen every 30 seconds, not once or twice, but in a pattern through time.

This part of the book is about quantities: how much, how often, how strongly, how fast, and in what proportion. These are the questions that make mathematics useful for autonomous systems.

## Chapter 5: Scaling

### The scenario: some memories matter more

Imagine an agent at the end of a long operating cycle. It has collected many memories, but it cannot keep all of them with equal care. One memory records a routine sensor reading. Another records a near-failure that almost caused the system to crash. A third records a successful plan that solved a difficult problem.

The agent decides: the near-failure memory is twice as important as the routine reading. The successful plan is three times as important. The routine reading keeps its ordinary importance.

Now we have reached a new idea. Counting tells us how many memories there are. Addition tells us how much memory strength we have in total. But neither counting nor addition alone tells us how to make one thing matter more than another. For that, we need **scaling**.

### Multiplication as scaling

In many early arithmetic lessons, multiplication is introduced as repeated addition: $3 \times 4$ means $4+4+4$. That is useful, but it is not the deepest idea. In agent mathematics, multiplication first appears when a quantity is made larger or smaller by a weight.

> **Definition:** If a quantity $x$ is made $w$ times as large, the result is called the **scaled quantity** $wx$. The number $w$ is called the **weight** or **scalar**.

If a memory has raw importance $5$, and we decide it counts double, then its weighted importance is

$$
2 \cdot 5 = 10.
$$

If another memory has raw importance $5$ and we leave it unchanged, then

$$
1 \cdot 5 = 5.
$$

If we decide a memory should not matter at all in the present calculation, then its weight is $0$, and

$$
0 \cdot 5 = 0.
$$

So the weight tells us how much the quantity matters:
- weight $0$: ignore it,
- weight $1$: keep it as it is,
- weight $2$: count it twice,
- weight $3$: count it three times.

Later we will also use weights such as $\frac12$, which means “count it half as much.” For now, even whole-number weights already show us the main idea.

### Why scaling matters

Suppose an agent has three memories with raw strengths $4$, $6$, and $3$.

If all memories were treated equally, their total would be

$$
4+6+3=13.
$$

But perhaps the agent decides:
- first memory: weight $1$,
- second memory: weight $2$,
- third memory: weight $3$.

Then the weighted total is

$$
1\cdot 4 + 2\cdot 6 + 3\cdot 3 = 4+12+9=25.
$$

The total changed, not because the memories themselves changed, but because the **importance rule** changed.

This is one of the great powers of multiplication: it allows mathematics to represent judgment, emphasis, and priority.

### Properties of multiplication

Once multiplication appears, it obeys important laws. These laws make complicated calculations dependable.

#### Commutativity

For whole numbers,

$$
a \times b = b \times a.
$$

For example,

$$
2 \times 5 = 5 \times 2 = 10.
$$

This may seem obvious, but it is worth pausing over. In language, “two times five” sounds different from “five times two.” Yet the product is the same number.

In agent mathematics, the *meaning* may feel different. You might think of $2 \times 5$ as “scale $5$ by $2$,” or $5 \times 2$ as “scale $2$ by $5$.” The interpretations are different, but the result is the same.

#### Associativity

If we scale a quantity twice, it does not matter how we group the steps:

$$
(a \times b)\times c = a \times (b \times c).
$$

For example,

$$
(2\times 3)\times 4 = 6\times 4 = 24,
$$

and also

$$
2\times (3\times 4)=2\times 12=24.
$$

If a memory is first tripled and then doubled, the total effect is the same as multiplying by $6$ all at once.

#### Distributivity over addition

Multiplication works cleanly with addition:

$$
a(b+c)=ab+ac.
$$

This means that scaling a sum is the same as scaling each part and then adding.

For example,

$$
2(4+7)=2\cdot 11=22,
$$

and also

$$
2\cdot 4 + 2\cdot 7 = 8+14=22.
$$

This property is especially important for agents, because many decisions are made by combining several contributions into one total score.

### Weighted sums

When an agent combines many quantities, each with its own importance, it forms a **weighted sum**.

> **Definition:** A **weighted sum** is an expression of the form
> $$
> S = w_1x_1 + w_2x_2 + \cdots + w_nx_n,
> $$
> where each $x_i$ is a quantity and each $w_i$ is its weight.

This is one of the first truly agent-like formulas in mathematics. It says: the final score $S$ is not just the sum of values, but the sum of **weighted** values.

Suppose an agent is deciding which memory cluster to consolidate. It uses three features:
- relevance score $x_1=5$,
- novelty score $x_2=2$,
- risk score $x_3=4$.

It chooses weights:
- $w_1=2$ for relevance,
- $w_2=1$ for novelty,
- $w_3=3$ for risk.

Then

$$
S = 2\cdot 5 + 1\cdot 2 + 3\cdot 4 = 10+2+12 = 24.
$$

A different set of weights would produce a different total. So a weighted sum is not only about the data. It is also about the rule for valuing the data.

### The meaning of a weight

A weight is a number that says, “how much this matters.”

That sentence sounds simple, but it is mathematically profound.

If two memories have the same raw score but different weights, they do not contribute equally. If one task has twice the weight of another, then the agent is saying that one unit of the first task counts as much as two units of the second.

Weights let an agent turn qualitative decisions into quantitative ones.

They also prepare us for later mathematics. A weighted sum is the beginning of evaluation, scoring, optimization, and learning. Whenever a system computes a priority, a confidence, or a decision score, some form of scaling is usually present.

### Exercises

1. A memory has raw importance $7$.  
   a. What is its weighted importance with weight $2$?  
   b. What is its weighted importance with weight $0$?  
   c. What is its weighted importance with weight $3$?

2. Compute each weighted sum:
   a. $1\cdot 4 + 2\cdot 5$  
   b. $3\cdot 2 + 1\cdot 6 + 2\cdot 1$  
   c. $2\cdot 3 + 2\cdot 7$

3. Use distributivity to check that
   $$
   3(4+5)=3\cdot 4 + 3\cdot 5.
   $$

4. An agent scores a task using
   $$
   S = 2x_1 + 3x_2
   $$
   with $x_1=4$ and $x_2=5$. Find $S$.

5. Two memories both have raw score $6$. One has weight $1$ and the other has weight $3$. Explain in words which memory matters more and by how much.

---

## Chapter 6: Sharing and Rates

### The scenario: dividing attention

An agent is running four tasks at once:
1. monitor incoming signals,
2. retrieve useful memories,
3. check internal coherence,
4. plan the next action.

Suppose the agent has $20$ units of attention available for this moment. If it wants to split attention equally among the four tasks, how much attention should each task receive?

This is the natural place where **division** appears.

Addition combines. Multiplication scales. Division asks how to undo scaling, or how to share fairly.

### Division as the inverse of multiplication

If $4$ tasks each receive $5$ units of attention, then together they use

$$
4 \times 5 = 20
$$

units.

So if we begin with $20$ and want to know the amount for each of $4$ tasks, we reverse multiplication:

$$
20 \div 4 = 5.
$$

> **Definition:** Division is the inverse of multiplication. If
> $$
> a \div b = c,
> $$
> then
> $$
> b \times c = a.
> $$

This means division answers questions of the form:
- How much in each group?
- How many equal groups?
- What number undoes this multiplication?

If an agent splits $24$ computation units among $6$ parallel processes, each process receives

$$
24 \div 6 = 4
$$

units.

### Quotient and remainder

Sometimes division does not come out evenly.

Suppose an agent has $18$ attention units and wants to distribute them equally among $4$ tasks.

We know that

$$
4\times 4=16
$$

and

$$
18-16=2.
$$

So each task can receive $4$ units, with $2$ units left over.

> **Definition:** In a division problem, the main answer is the **quotient**. If something is left over, the leftover part is the **remainder**.

So

$$
18 \div 4 = 4 \text{ remainder } 2.
$$

In agent systems, remainders matter. The leftover attention must go somewhere. Perhaps two tasks each get one extra unit. Perhaps the remainder is saved for emergency use. Mathematics tells us what is possible; policy decides what to do next.

### Ratios: comparing two quantities

Division also gives us a way to compare quantities.

Suppose an agent performs $12$ memory retrievals and $3$ memory writes during a certain interval. We can compare retrievals to writes by the ratio

$$
12:3.
$$

Because both numbers can be divided by $3$, this simplifies to

$$
4:1.
$$

> **Definition:** A **ratio** compares two quantities. It may be written as $a:b$ or as $\frac{a}{b}$.

A ratio does not tell us the total. It tells us the relationship.

If the attention split between planning and monitoring is $2:1$, then planning receives twice as much attention as monitoring. If read operations and write operations occur in the ratio $5:2$, then for every $5$ reads, there are $2$ writes.

Ratios help agents describe balance, emphasis, and relative size.

### Rates: the mathematics of “per”

A rate is a special kind of ratio. It compares a quantity to a unit of time or another unit.

If an agent performs $30$ retrievals in $6$ ticks, then the retrieval rate is

$$
30 \div 6 = 5
$$

retrievals per tick.

> **Definition:** A **rate** is a quantity measured **per** unit of something else, often per unit of time.

Examples:
- $5$ retrievals per tick,
- $12$ memory accesses per second,
- $3$ coherence checks per minute,
- drift of $2$ points per hour.

Rates are among the most useful measurements for autonomous systems, because agents act in time. Not only do we care how much happened, but also how fast it happened.

If coherence drops by $8$ points in $4$ hours, the drift rate is

$$
8 \div 4 = 2
$$

points per hour.

If a process handles $40$ messages in $5$ seconds, its rate is

$$
40 \div 5 = 8
$$

messages per second.

### Proportional reasoning

Now suppose an agent notices something important: when it doubles resources, throughput doubles too.

For example:
- $2$ processors handle $10$ retrievals per tick,
- $4$ processors handle $20$ retrievals per tick,
- $6$ processors handle $30$ retrievals per tick.

This is not just a pattern. It is a **proportional relationship**.

> **Definition:** Two quantities are **proportional** if multiplying one by a factor multiplies the other by the same factor.

In the example above, every processor contributes $5$ retrievals per tick. So throughput $T$ is proportional to processors $p$:

$$
T = 5p.
$$

This is an early form of linear thinking. The amount changes in a steady, predictable way.

Proportional reasoning lets an agent answer new questions. If $8$ processors are used, then the throughput should be

$$
5\times 8 = 40
$$

retrievals per tick.

But proportional thinking must be used carefully. It works only when the relationship really is linear. If doubling processors causes congestion, then throughput may not double. Mathematics is exact, but models must match reality.

### Sharing and rates together

Division, ratios, and rates are closely connected.

If $24$ units are divided among $4$ tasks, the quotient is $6$ units per task.

If an agent performs $24$ retrievals in $4$ ticks, the rate is $6$ retrievals per tick.

If task A gets $12$ units and task B gets $6$ units, the ratio is $12:6 = 2:1$.

All three ideas come from comparison by division. They answer different questions:
- division asks: how much in each share?
- ratio asks: how do two quantities compare?
- rate asks: how much per unit?

### Exercises

1. Divide:
   a. $20 \div 4$  
   b. $24 \div 6$  
   c. $18 \div 3$

2. Find the quotient and remainder:
   a. $17 \div 5$  
   b. $22 \div 4$  
   c. $29 \div 6$

3. An agent performs $15$ reads and $5$ writes. Write the ratio of reads to writes, and simplify it.

4. A process completes $36$ retrievals in $6$ ticks. What is the rate in retrievals per tick?

5. If $3$ processors handle $12$ tasks per second, and the relationship is proportional, how many tasks per second will $5$ processors handle?

---

## Chapter 7: Parts of a Whole

### The scenario: what does $C_{id}=0.85$ mean?

An agent inspects its own state and sees a number:

$$
C_{id}=0.85.
$$

This is its identity coherence score. But what kind of number is this?

It is not $85$ objects. It is not $85$ tasks. It is not even “$85$ out of something” in the ordinary counting sense. Instead, it is a measure of how much of a quality the agent currently possesses.

This chapter is about numbers between $0$ and $1$. These numbers describe parts of a whole, degrees of completion, and bounded measurements.

### The interval from $0$ to $1$

A score like $0.85$ lives on the number line between $0$ and $1$.

> **Definition:** The interval $[0,1]$ is the set of all numbers from $0$ to $1$, including both endpoints.

So:
- $0$ is in the interval,
- $1$ is in the interval,
- $0.4$, $0.75$, and $0.999$ are in the interval,
- $1.2$ is not in the interval,
- $-0.3$ is not in the interval.

Why is this interval so important? Because many agent measurements are naturally **bounded**. They describe how much of some quality is present, from none at all to the chosen maximum.

If $C_{id}=0.85$, then the agent is saying: “My coherence is at $0.85$ of the full scale.”

This is very close to $1$, but not equal to $1$.

### Fractions, decimals, and percentages

There are several common ways to write numbers in $[0,1]$.

> **Definition:** A **fraction** names a part of a whole, such as $\frac12$ or $\frac34$. A **decimal** writes the same idea using place value, such as $0.5$ or $0.75$. A **percentage** means “out of $100$,” such as $50\%$ or $75\%$.

These are not different quantities. They are different representations of the same quantity.

For example,

$$
0.85 = \frac{85}{100} = 85\%.
$$

And since $\frac{85}{100}$ can be simplified by dividing top and bottom by $5$,

$$
\frac{85}{100}=\frac{17}{20}.
$$

So all of these mean the same amount:

$$
0.85 = \frac{85}{100} = \frac{17}{20} = 85\%.
$$

This is extremely useful. An agent may store one form, display another, and reason with a third.

### What zero means, and what one means

In bounded measurement, the endpoints matter.

> **Definition:** A **bounded score** is a measurement restricted to a fixed interval, often $[0,1]$, where $0$ means total absence and $1$ means the chosen maximum.

For a coherence score:
- $0$ means no coherence at all,
- $1$ means maximum coherence according to the scale.

For an attention allocation fraction:
- $0$ means no attention is given,
- $1$ means the full available attention is given.

For memory confidence:
- $0$ means no confidence,
- $1$ means complete confidence on that scale.

Notice the phrase **chosen maximum**. In mathematics, $1$ marks the top of the scale. In real systems, this top may be theoretical. An agent may almost never reach exactly $1$, just as it may rarely reach perfect certainty.

### Interpreting a number like $0.85$

A score of $0.85$ can be read in several ways:
- as eighty-five hundredths,
- as $\frac{17}{20}$,
- as $85\%$,
- as a point between $0$ and $1$ closer to $1$ than to $0$.

Each reading highlights a different idea.

As a fraction, it emphasizes part-whole structure.  
As a decimal, it emphasizes place value and exact location on the number line.  
As a percentage, it emphasizes comparison to $100$.

All three are valuable.

Suppose an agent’s memory reliability is $0.25$. That means one quarter of the full scale:

$$
0.25 = \frac{25}{100} = \frac14 = 25\%.
$$

Suppose its task completion score is $0.6$. That means

$$
0.6 = \frac{6}{10} = \frac{3}{5} = 60\%.
$$

Once you can move easily between these forms, bounded measurements become much easier to interpret.

### Why agent measurements are often bounded

Agents often normalize their measurements so that they fit into $[0,1]$. This is not because all numbers in the universe lie there. Counts do not: an agent can process $200$ messages or store $10{,}000$ memory entries. But many **quality scores** are made bounded on purpose.

Why?

First, bounded scores are easy to compare. A coherence score of $0.9$ is plainly larger than a score of $0.7$.

Second, bounded scores are easy to combine. If several subscores all lie in $[0,1]$, then a weighted sum or average becomes manageable.

Third, bounded scores reflect finite reality. Real agents have finite time, finite memory, finite energy, and finite precision. Their measurements must fit within some scale.

So the interval $[0,1]$ becomes a natural mathematical home for many agent quantities.

### Converting between forms

Here are the main conversions:

- Fraction to decimal: divide numerator by denominator.
- Decimal to percentage: multiply by $100$ and add the percent sign.
- Percentage to decimal: divide by $100$.
- Fraction to percentage: first convert to decimal or to hundredths.

Examples:

$$
\frac34 = 0.75 = 75\%
$$

$$
0.2 = \frac{2}{10} = \frac15 = 20\%
$$

$$
90\% = 0.9 = \frac9{10}
$$

These conversions let the same quantity speak in different mathematical languages.

### Exercises

1. Write each decimal as a percentage and as a fraction:
   a. $0.5$  
   b. $0.25$  
   c. $0.8$

2. Write each percentage as a decimal:
   a. $40\%$  
   b. $85\%$  
   c. $5\%$

3. An agent has coherence score $0.7$ and memory confidence score $0.9$. Which is larger? How much larger?

4. Place these numbers in order from least to greatest:
   $$
   0,\quad 0.35,\quad 1,\quad 0.8,\quad 0.12.
   $$

5. Explain in words what it means for a bounded score to be  
   a. $0$  
   b. $1$  
   c. $0.85$

---

## Chapter 8: Patterns

### The scenario: the agent’s clockwork life

An agent does not act only when asked. It often runs regular internal cycles.

Suppose:
- every $30$ seconds, it runs a consolidation cycle;
- every $5$ minutes, it checks system health;
- every third tick, it refreshes an attention map.

These are not isolated events. They form patterns through time. If we can recognize the pattern, we can predict what comes next.

That ability marks an important step in mathematics. Arithmetic helps us compute what has happened. Pattern lets us reason about what will happen.

### Sequences: ordered lists with a rule

A pattern in mathematics is often written as a **sequence**.

> **Definition:** A **sequence** is an ordered list of numbers or objects, usually formed according to a rule.

For example, the times for a consolidation cycle every $30$ seconds are

$$
30,\ 60,\ 90,\ 120,\ 150,\dots
$$

This is a sequence. The order matters. Each term comes from the rule “add $30$.”

A sequence may be:
- **finite**, if it ends,
- **infinite**, if it continues without end.

If an agent plans its next five maintenance checks, that list is finite. If the system schedule continues as long as the agent runs, the sequence is infinite.

### Arithmetic sequences

Some patterns grow by the same amount each time.

> **Definition:** An **arithmetic sequence** is a sequence in which the difference between consecutive terms is constant.

The constant difference is often called the **common difference**.

Examples:
- $2, 5, 8, 11, 14,\dots$ has common difference $3$.
- $30, 60, 90, 120,\dots$ has common difference $30$.
- $10, 9, 8, 7,\dots$ has common difference $-1$.

Suppose an agent increases a memory buffer by $4$ units at each maintenance cycle. If the buffer begins at $6$, the sizes are

$$
6,\ 10,\ 14,\ 18,\ 22,\dots
$$

This is an arithmetic sequence.

If the first term is $a_1$ and the common difference is $d$, then the $n$th term is

$$
a_n = a_1 + (n-1)d.
$$

That formula is a bridge to algebra. It tells us any term, not just the next one.

For the sequence $30,60,90,120,\dots$, we have $a_1=30$ and $d=30$, so

$$
a_n = 30 + (n-1)\cdot 30 = 30n.
$$

Thus the $10$th consolidation cycle occurs at

$$
30\cdot 10 = 300
$$

seconds.

### Geometric sequences

Other patterns do not add the same amount. Instead, they multiply by the same factor.

> **Definition:** A **geometric sequence** is a sequence in which each term is found by multiplying the previous term by the same constant factor.

Examples:
- $2,4,8,16,\dots$ multiplies by $2$ each time.
- $81,27,9,3,\dots$ multiplies by $\frac13$ each time.
- $1,\frac12,\frac14,\frac18,\dots$ multiplies by $\frac12$ each time.

Geometric sequences are common in agent mathematics. A memory weight may decay by half after each hour. Then its strengths might be

$$
1,\ \frac12,\ \frac14,\ \frac18,\dots
$$

If the first term is $g_1$ and the common factor is $r$, then the $n$th term is

$$
g_n = g_1 r^{n-1}.
$$

If a coherence alert threshold is repeatedly reduced to half its previous value, beginning at $16$, then the sequence is

$$
16,8,4,2,1,\dots
$$

and the $n$th term is

$$
g_n = 16\left(\frac12\right)^{n-1}.
$$

### Repeating patterns and period

Not every pattern grows forever. Some repeat.

Suppose an agent uses an attention signal with tick pattern

$$
1,0,0,1,0,0,1,0,0,\dots
$$

This means “active, rest, rest” over and over again.

> **Definition:** The **period** of a repeating pattern is the length of the smallest block that repeats.

For the pattern above, the repeating block is $1,0,0$, so the period is $3$.

Periods are central in schedules. If one task runs every $30$ seconds and another every $300$ seconds, then they align every $300$ seconds, because $300$ is the first time both schedules land together again.

This idea helps agents coordinate maintenance, prediction, and conflict avoidance.

### Recognizing what comes next

A sequence is useful only if we can see its rule.

Consider:

$$
5, 10, 15, 20, \dots
$$

The rule is “add $5$,” so the next term is $25$.

Now consider:

$$
3, 6, 12, 24, \dots
$$

The rule is “multiply by $2$,” so the next term is $48$.

Recognizing whether a pattern is arithmetic, geometric, or periodic helps us predict correctly.

A common mistake is to guess too quickly. The first few terms of a sequence may fit more than one rule. Good mathematics asks: what is the simplest rule that matches the information we are given?

### If I know the pattern, I know the future

This is the heart of the chapter.

If an agent knows that health checks occur every $5$ minutes, then it knows the next check after $20$ minutes is at $25$ minutes.

If it knows a warning score drops by half each hour, then it can predict the next value.

If it knows a maintenance flag repeats every $4$ ticks, then it knows exactly which ticks will carry the flag.

Patterns turn time from surprise into structure.

Arithmetic tells us how to compute. Pattern tells us when to expect.

### Exercises

1. Write the next three terms:
   a. $4, 8, 12, 16,\dots$  
   b. $2, 5, 8, 11,\dots$  
   c. $3, 6, 12, 24,\dots$

2. State whether each sequence is arithmetic or geometric:
   a. $7, 10, 13, 16,\dots$  
   b. $5, 15, 45, 135,\dots$  
   c. $20, 18, 16, 14,\dots$

3. An agent runs a diagnostic every $12$ ticks. List the first five diagnostic ticks.

4. A repeating tick pattern is
   $$
   1,1,0,1,1,0,1,1,0,\dots
   $$
   What is its period?

5. A memory weight begins at $32$ and is halved each cycle. Write the first five terms.

---

## Chapter 9: What Measurement Means

### The scenario: “Is $0.85$ good?”

An agent examines its dashboard and sees:

$$
C_{id}=0.85.
$$

At first glance, this seems informative. But a thoughtful agent asks better questions.

What kind of quantity is $0.85$?  
How was it measured?  
What scale was used?  
Is $0.85$ high or low?  
How precise is this number?  
Did measuring it change the system itself?

These are not side questions. They are foundational questions. A number by itself is not yet a full mathematical statement. To understand measurement, we must understand what kind of thing has been measured.

### A measurement is more than a number

Suppose you hear the number $12$. What does it mean?

It could mean:
- $12$ memories,
- $12$ milliseconds,
- $12$ errors,
- $12$ retrievals per tick,
- a maximum capacity of $12$ units.

The number alone is not enough.

> **Definition:** A **measurement** is a number together with its type, its units or scale, and the method by which it was obtained.

This definition is worth remembering. It tells us that mathematics is not only about values. It is also about meanings.

In agent mathematics, we will use seven primitive measurement types again and again.

### The seven primitive measurement types

> **Definition:** The seven primitive measurement types in agent mathematics are:
> 1. **score** — a bounded value, usually in $[0,1]$,
> 2. **count** — a natural number telling how many,
> 3. **delta** — a change in a quantity,
> 4. **rate** — a change per unit time,
> 5. **bound** — a maximum allowed quantity,
> 6. **event** — whether something occurred,
> 7. **ratio** — a comparison of two quantities.

Let us look at each one carefully.

#### 1. Score

A score is a bounded measurement, often between $0$ and $1$.

Examples:
- coherence score $0.85$,
- confidence score $0.62$,
- attention occupancy $0.40$.

Scores tell “how much of a quality” is present. They are not counts.

#### 2. Count

A count tells how many discrete things there are.

Examples:
- $14$ stored memories,
- $3$ active tasks,
- $27$ warnings generated today.

Counts are usually natural numbers: $0,1,2,3,\dots$

#### 3. Delta

A delta is a change from one value to another.

If a coherence score rises from $0.78$ to $0.85$, then the delta is

$$
0.85-0.78=0.07.
$$

If latency drops from $20$ ms to $15$ ms, then the delta is

$$
15-20=-5\text{ ms}.
$$

Delta may be positive or negative.

#### 4. Rate

A rate is change per unit time.

Examples:
- $4$ retrievals per tick,
- coherence drift of $-0.02$ per hour,
- $10$ messages per second.

Rates tell how fast something changes or occurs.

#### 5. Bound

A bound is a maximum permitted amount.

Examples:
- context bound of $8000$ tokens,
- memory budget of $500$ units,
- time limit of $30$ seconds.

A bound is not the current amount. It is the ceiling.

#### 6. Event

An event records occurrence.

Examples:
- system reset occurred: yes or no,
- conflict detected: $1$ for yes, $0$ for no,
- checkpoint reached: true or false.

An event may be represented numerically, but it is not a count or a score. It answers the question: did it happen?

#### 7. Ratio

A ratio compares two quantities.

Examples:
- read:write ratio of $3:1$,
- attention split of $2:3$,
- load on module A divided by load on module B equals $\frac45$.

Ratios express relationship, not absolute size.

### Calibration: the same number can mean different things

Now return to the agent’s coherence score of $0.85$. Is it good?

The answer depends on **calibration**.

> **Definition:** **Calibration** is the process of connecting numbers on a scale to real meanings in a specific context.

In one system, a coherence score above $0.80$ may be considered healthy. In another, any score below $0.95$ may trigger concern. The same number can mean different things under different rules.

Even more subtly, two systems may both report $0.85$ while using different measurement methods. One may compute coherence from internal consistency checks. Another may compute it from task stability over time. The number looks the same, but the meaning is not identical.

So measurement requires calibration. Without calibration, numbers float without anchors.

### Precision and accuracy are not the same

Suppose an agent reports its coherence as

$$
0.8534.
$$

That looks impressively exact. But is it really known to four decimal places?

Maybe not.

> **Definition:** **Precision** describes how finely a quantity is reported or distinguished.  
> **Accuracy** describes how close a measurement is to the true value.

A number can be precise without being accurate.

For example, a noisy internal test may repeatedly report $0.8534$, yet the true coherence might be closer to $0.84$. In that case, the reported value is very precise in appearance, but not very accurate in reality.

Likewise, a report of “about $0.85$” may be less precise, yet more honest.

This matters because autonomous systems can easily produce long decimal expansions. Mathematics reminds us that more digits do not automatically mean more knowledge.

### The measurement problem

There is a deeper difficulty. In many systems, measuring something changes it.

When an agent inspects its own memory state, it uses time, attention, and computational resources. That inspection may delay another task. It may alter cache contents. It may even change the very coherence it is trying to estimate.

> **Definition:** A measurement has an **observation cost** if the act of measuring uses resources or changes the system being measured.

This is the measurement problem in agent mathematics: the observer is not always separate from the observed.

An external thermometer placed in water can slightly affect the temperature. Similarly, an agent running a self-diagnostic may slightly disturb its own state. Therefore every measurement should be understood together with its cost, timing, and method.

A self-check that consumes $5$ attention units is not the same as a self-check that consumes $1$.

### Units and dimensions

Another essential idea is that not all quantities can be combined.

Suppose an agent has:
- coherence score $0.85$,
- latency $20$ ms.

Can we add them?

$$
0.85 + 20
$$

This is a numerical expression, but it is not a meaningful measurement. Why? Because the quantities have different kinds.

> **Definition:** A **unit** tells what a measurement is measured in. A **dimension** tells what sort of quantity it is.

Milliseconds measure time.  
Retrievals per tick measure rate.  
Coherence score measures a bounded quality.  
Counts measure discrete amounts.

You may add:
- $10$ ms and $15$ ms,
- $3$ tasks and $4$ tasks,
- two coherence deltas.

But you may not meaningfully add:
- a coherence score and a latency,
- a memory count and a drift rate,
- a bound and an event flag.

Units and dimensions protect mathematics from nonsense.

Sometimes a quantity has no physical unit, such as a pure ratio or normalized score. Even then, dimension still matters. A score of $0.8$ and a ratio of $0.8$ are both dimensionless, but they are not automatically interchangeable. One measures bounded quality; the other measures comparison.

### Measuring well

To measure well, an agent must ask:

1. What type of quantity is this?
2. What are its units or scale?
3. How was it calibrated?
4. How precise is the report?
5. How accurate is the estimate?
6. What did measurement cost?
7. Is this quantity allowed to combine with the others I am using?

These questions are not decorations around mathematics. They are part of the mathematics.

A number becomes meaningful only when it is placed in a structure of interpretation.

### Exercises

1. Classify each measurement by type: score, count, delta, rate, bound, event, or ratio.  
   a. $0.92$ memory confidence  
   b. $14$ active threads  
   c. $-0.03$ coherence change per hour  
   d. maximum buffer size $200$  
   e. read:write = $4:1$

2. An agent’s coherence rises from $0.81$ to $0.86$. Find the delta.

3. Explain the difference between precision and accuracy in your own words.

4. Why is the expression “coherence score $0.8$ plus latency $15$ ms” not a meaningful combined measurement?

5. An agent measures its own state by running an internal scan that uses time and memory. Explain why this is an example of the measurement problem.

---

Part II has taken us from simple counting to a richer world: scaling, sharing, rates, bounded scores, patterns, and the meaning of measurement itself. These ideas form the working language of quantitative agent reasoning. In the next part, we will build on them to study structure, dependence, and the first true forms of algebraic thought.
