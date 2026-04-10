# Part IV: The Language of Change

In Parts I-III, we built the language of states, structure, and measurement. We learned how to describe an agent, how to compare agents, and how to formalize quantities such as capacity, performance, and promotion criteria. But a mature mathematics of autonomous systems cannot stop at description. An agent is not static. It responds, adapts, improves, saturates, drifts, and learns.

This part introduces the mathematics of change.

We begin with vectors, because many important agent quantities are built from several components at once. We then move to nonlinear response, where thresholds and saturation replace simple straight-line behavior. From there we study derivatives, which quantify sensitivity, and integrals, which quantify accumulation. Finally, we develop the mathematics of uncertainty and statistical learning, because real measurements are noisy and real conclusions must be drawn from data rather than certainty.

These chapters are not merely borrowed tools from classical mathematics. In the setting of autonomous systems, they become a coherent language for asking practical questions:

- Which ingredient matters most?
- When does a small improvement produce a large effect?
- How much total output was produced over time?
- How certain are we about a measured capacity?
- When does fitted evidence justify a structural change in the model?

That is the language of change.

---

## Chapter 15: Vectors and Weighted Sums

An evaluation agent has just completed a diagnostic battery. Its four core component scores are recorded as

$$
C = (C_{\text{id}}, C_{\text{mem}}, C_{\text{graph}}, C_{\text{perm}})
= (0.72, 0.68, 0.81, 0.64).
$$

A research team decides to compute a single summary quantity called cognitive mass:

$$
M = \alpha_1 C_{\text{id}} + \alpha_2 C_{\text{mem}} + \alpha_3 C_{\text{graph}} + \alpha_4 C_{\text{perm}}.
$$

Suppose the weights are

$$
\alpha = (0.20, 0.25, 0.35, 0.20).
$$

Then the cognitive mass is a weighted combination of the four ingredients. This is one of the most common mathematical structures in agent science: several measurements combined into one quantity, with different levels of importance assigned to each part.

To speak clearly about such combinations, we need vectors.

### 15.1 Ordered lists as mathematical objects

A vector is an ordered list of numbers. The word “ordered” matters. The vector

$$
(0.72, 0.68, 0.81, 0.64)
$$

is not the same as

$$
(0.68, 0.72, 0.81, 0.64),
$$

because the first entry refers to identity stability, the second to memory capacity, and so on. In agent mathematics, each position in a vector carries meaning.

> **Definition:** A **vector** in $\mathbb{R}^n$ is an ordered list of $n$ real numbers:
> $$
> v = (v_1, v_2, \dots, v_n).
> $$

For our four-component model, the capacity vector is

$$
C = (C_{\text{id}}, C_{\text{mem}}, C_{\text{graph}}, C_{\text{perm}}) \in \mathbb{R}^4.
$$

The weight vector is

$$
\alpha = (\alpha_1, \alpha_2, \alpha_3, \alpha_4) \in \mathbb{R}^4.
$$

Vectors allow us to treat multi-component quantities as single mathematical objects.

### 15.2 Vector addition and scalar multiplication

Once vectors are defined, we can combine them.

> **Definition:** If $u = (u_1,\dots,u_n)$ and $v = (v_1,\dots,v_n)$, then their **sum** is
> $$
> u+v = (u_1+v_1,\dots,u_n+v_n).
> $$

> **Definition:** If $c$ is a real number and $v=(v_1,\dots,v_n)$, then the **scalar multiple** $cv$ is
> $$
> cv = (cv_1,\dots,cv_n).
> $$

These operations are simple, but they are powerful. Suppose an agent undergoes two upgrades:

- a memory improvement represented by
  $$
  u=(0,0.10,0,0),
  $$
- and a graph-reasoning improvement represented by
  $$
  v=(0,0,0.08,0).
  $$

Then the total improvement is

$$
u+v=(0,0.10,0.08,0).
$$

If only half of the graph upgrade is deployed, we use scalar multiplication:

$$
\frac12 v = (0,0,0.04,0).
$$

Thus vectors let us represent not only states, but also changes in state.

### 15.3 Linear combinations

Many important quantities are built by multiplying vectors by numbers and then adding the results.

> **Definition:** A **linear combination** of vectors $v^{(1)}, v^{(2)}, \dots, v^{(k)}$ is any expression of the form
> $$
> c_1 v^{(1)} + c_2 v^{(2)} + \cdots + c_k v^{(k)},
> $$
> where the coefficients $c_1,\dots,c_k$ are real numbers.

In agent work, linear combinations often describe blends of influences. For example, suppose a composite adaptation direction is formed by combining three intervention profiles:

$$
d_1=(1,0,0,0), \quad d_2=(0,1,0,0), \quad d_3=(0,0,1,0).
$$

Then

$$
0.2d_1 + 0.5d_2 + 0.3d_3 = (0.2,0.5,0.3,0)
$$

describes a plan emphasizing memory most heavily, with moderate identity and graph improvement, and no permission change.

A linear combination answers the question: how much of each ingredient is present?

### 15.4 The dot product

Weighted sums are so common that they receive a special name.

> **Definition:** If $a=(a_1,\dots,a_n)$ and $b=(b_1,\dots,b_n)$, their **dot product** is
> $$
> a\cdot b = \sum_{i=1}^n a_i b_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n.
> $$

For our agent, the cognitive mass formula

$$
M = \alpha_1 C_{\text{id}} + \alpha_2 C_{\text{mem}} + \alpha_3 C_{\text{graph}} + \alpha_4 C_{\text{perm}}
$$

can be written compactly as

$$
M = \alpha \cdot C.
$$

This notation is not merely shorter. It reveals structure. We are taking a vector of weights and applying it to a vector of capacities.

Using the values above,

$$
M = (0.20, 0.25, 0.35, 0.20)\cdot(0.72,0.68,0.81,0.64).
$$

Compute term by term:

$$
M = 0.20(0.72)+0.25(0.68)+0.35(0.81)+0.20(0.64).
$$

So

$$
M = 0.144+0.170+0.2835+0.128 = 0.7255.
$$

Thus the agent’s cognitive mass is $0.7255$.

### 15.5 Weighted sums and the simplex

Not every choice of weights is equally meaningful. In many settings, weights represent fractions of total emphasis. Then they should be nonnegative and add to $1$.

> **Definition:** The **simplex of weights** in $\mathbb{R}^n$ is the set of vectors
> $$
> \alpha = (\alpha_1,\dots,\alpha_n)
> $$
> such that
> $$
> \alpha_i \ge 0 \quad \text{for all } i,
> $$
> and
> $$
> \alpha_1+\cdots+\alpha_n = 1.
> $$

When $\alpha$ lies in the simplex, the weighted sum

$$
\alpha \cdot C
$$

is a convex average of the entries of $C$. It cannot exceed the largest component or fall below the smallest component.

For example, if

$$
C=(0.72,0.68,0.81,0.64)
$$

and $\alpha$ is in the simplex, then

$$
0.64 \le \alpha\cdot C \le 0.81.
$$

This is mathematically useful and conceptually reassuring: a weighted average of scores should remain within the range of those scores.

If the weights did not sum to $1$, then the result would no longer represent a true average. It might instead represent an amplified or damped score. That is sometimes appropriate, but the interpretation changes.

### 15.6 Geometric meaning: magnitude and direction

Vectors are not only lists; they also have geometry.

> **Definition:** The **magnitude** or **length** of a vector $v=(v_1,\dots,v_n)$ is
> $$
> \|v\| = \sqrt{v_1^2 + \cdots + v_n^2}.
> $$

A vector’s magnitude tells us how large it is. Its direction tells us where it points in the multi-dimensional space of capacities.

For a simple example, compare the vectors

$$
u=(1,1,1,1), \qquad v=(2,2,2,2).
$$

They point in the same direction, but $v$ has twice the magnitude.

In agent mathematics, direction often matters more than raw size. An improvement vector such as

$$
(0.05,0.05,0.05,0.05)
$$

represents balanced growth. By contrast,

$$
(0,0.15,0,0)
$$

represents specialized growth in memory only.

The dot product has a geometric interpretation connecting size and direction:

$$
a\cdot b = \|a\|\,\|b\|\cos\theta,
$$

where $\theta$ is the angle between the vectors.

This formula tells us several important things.

- If $a$ and $b$ point in similar directions, then $\cos\theta$ is positive and large, so the dot product is large.
- If they are perpendicular, then $\cos\theta=0$, so the dot product is $0$.
- If they point in opposite directions, the dot product is negative.

This geometric viewpoint is especially useful when the weight vector $\alpha$ is interpreted as a direction of evaluative preference. Then $\alpha\cdot C$ measures how strongly the capacity vector $C$ aligns with that preference direction.

An agent whose strengths lie where the weights are largest will have a high dot product. An agent whose strengths lie in less-valued components will have a lower one, even if its total raw capacity is substantial.

### 15.7 An agent-specific example

Consider two agents:

$$
C^{(A)}=(0.90,0.50,0.85,0.40), \qquad C^{(B)}=(0.70,0.72,0.75,0.68).
$$

Suppose the evaluation weights are

$$
\alpha=(0.15,0.20,0.45,0.20).
$$

Then

$$
M_A=\alpha\cdot C^{(A)}
$$

and

$$
M_B=\alpha\cdot C^{(B)}.
$$

Compute:

$$
M_A = 0.15(0.90)+0.20(0.50)+0.45(0.85)+0.20(0.40)
=0.135+0.100+0.3825+0.080=0.6975.
$$

And

$$
M_B = 0.15(0.70)+0.20(0.72)+0.45(0.75)+0.20(0.68)
=0.105+0.144+0.3375+0.136=0.7225.
$$

Although Agent A has stronger identity and graph peaks, Agent B achieves the larger cognitive mass because it is more balanced and avoids severe weakness in permission capacity. Weighted sums make such comparisons precise.

### 15.8 Why vectors matter

Vectors and weighted sums are the grammar of multi-factor systems. Whenever we speak of:

- combining component scores,
- describing a direction of improvement,
- measuring alignment with priorities,
- averaging multiple influences,

we are doing vector mathematics.

Later in this part, derivatives will tell us how outputs change as vectors change, and statistics will help us estimate good weight vectors from data. But the foundation is already here: a state is often a vector, and a summary quantity is often a dot product.

The mathematics of “how much of each ingredient” begins with vectors.

### Exercises

1. Let
   $$
   C=(0.80,0.65,0.70,0.75), \qquad \alpha=(0.25,0.25,0.30,0.20).
   $$
   Compute the cognitive mass $M=\alpha\cdot C$.

2. For
   $$
   u=(0.10,0,0.05,0), \qquad v=(0,0.08,0,0.04),
   $$
   find $u+v$ and $2u-v$.

3. Determine whether each of the following is in the simplex of weights in $\mathbb{R}^4$:
   - $(0.4,0.3,0.2,0.1)$
   - $(0.5,0.5,0.2,-0.2)$
   - $(0.1,0.1,0.1,0.1)$

4. Two agents have capacity vectors
   $$
   C^{(1)}=(0.60,0.90,0.70,0.80), \qquad C^{(2)}=(0.75,0.75,0.75,0.75).
   $$
   Using weights
   $$
   \alpha=(0.10,0.50,0.20,0.20),
   $$
   which agent has larger cognitive mass?

5. Explain in words what it means, in an agent evaluation setting, for two vectors to point in nearly the same direction.

---

## Chapter 16: Nonlinear Response

An agent completes a sequence of task batteries. For each task, a raw score is first computed from component capacities. But the final activation probability is not taken to be that raw score itself. Instead, the system passes the score through a link function:

$$
p = \sigma(x) = \frac{1}{1+e^{-x}}.
$$

When the raw score is very negative, the probability is near $0$. When the raw score is very positive, the probability is near $1$. And near the middle, small changes in score can produce noticeable changes in outcome.

This is not linear behavior. It is nonlinear response.

In autonomous systems, linear models are useful, but they are rarely the whole story. Real agents have thresholds, bottlenecks, saturation effects, and diminishing returns. A straight line cannot capture all of that. We therefore need functions whose behavior bends.

### 16.1 Linear and nonlinear functions

A linear function of one variable has the form

$$
f(x)=mx+b.
$$

Its graph is a straight line, and its rate of change is constant. If $x$ increases by $1$, the output changes by the same amount every time: always $m$.

This is mathematically elegant, and often a good first approximation. If an agent’s response quality were exactly

$$
Q=0.4+0.3M,
$$

then every increase of $0.1$ in cognitive mass would increase $Q$ by exactly $0.03$, regardless of whether $M$ was already low or already high.

But many agent responses do not work this way.

- A small improvement may do almost nothing until a threshold is crossed.
- Beyond a certain level, additional improvement may have less and less effect.
- Outputs such as probabilities must remain between $0$ and $1$.

These phenomena require nonlinear functions.

> **Definition:** A function is **nonlinear** if it is not of the form $mx+b$. Its graph is not a straight line, and its rate of change may depend on the input.

Examples include $x^2$, $\sqrt{x}$, $e^x$, and the sigmoid function.

### 16.2 The sigmoid function

The most famous threshold-like response function is the sigmoid.

> **Definition:** The **sigmoid function** is
> $$
> \sigma(x)=\frac{1}{1+e^{-x}}.
> $$

It is also called the logistic function. Its graph has an S-shape.

Let us inspect a few values:

$$
\sigma(0)=\frac{1}{2}=0.5,
$$

$$
\sigma(2)\approx 0.881,
$$

$$
\sigma(-2)\approx 0.119.
$$

So a raw score of $0$ maps to a neutral output of $0.5$, a moderately positive score maps close to $1$, and a moderately negative score maps close to $0$.

This is already useful for agent mathematics. Suppose a task battery produces an internal score

$$
x = 3M - 2.
$$

Then the success probability is

$$
p = \sigma(3M-2).
$$

If $M$ is low, success remains unlikely. If $M$ rises past a certain region, probability climbs rapidly. Once $M$ is high enough, further gains still help, but much less dramatically.

### 16.3 Key properties of the sigmoid

The sigmoid is popular because its mathematical behavior matches many real decision processes.

> **Definition:** A function is **bounded** if its outputs stay within a fixed interval.

The sigmoid is bounded between $0$ and $1$:

$$
0 < \sigma(x) < 1 \quad \text{for all } x.
$$

As $x\to\infty$, $\sigma(x)\to 1$, and as $x\to -\infty$, $\sigma(x)\to 0$. It never quite reaches the endpoints, but it gets arbitrarily close.

This makes it ideal for representing probabilities, normalized activations, or confidence levels.

The sigmoid is also monotonic.

> **Definition:** A function is **monotonic increasing** if larger inputs always produce larger outputs.

If $x_1<x_2$, then

$$
\sigma(x_1)<\sigma(x_2).
$$

So better internal scores always produce larger activation probabilities.

Finally, the sigmoid is S-shaped. In the middle region, around $x=0$, it changes quickly. At the extremes, it flattens out. This reflects diminishing returns. Once an agent is already almost certain to succeed, more improvement cannot increase probability by much, because probability cannot exceed $1$.

### 16.4 Why nonlinear worlds are natural for agents

Nonlinearity is not a mathematical complication added from outside. It is built into the reality of autonomous systems.

#### Thresholds

Some tasks require a minimum level of integrated competence. An agent with graph reasoning of $0.39$ may fail consistently, while one with $0.41$ begins to succeed. The change in raw capacity is small; the change in behavior is large.

#### Saturation

Suppose a task is already almost guaranteed. Increasing capacity further still helps in principle, but the observable success probability cannot rise beyond $1$. Gains compress near the top.

#### Diminishing returns

An increase from $0.20$ to $0.30$ may be transformative if it lifts an agent from severe deficiency into usable functioning. An increase from $0.90$ to $1.00$ may matter less. Nonlinear functions naturally represent that asymmetry.

#### Interaction effects

Even when a score begins as a linear weighted sum such as

$$
x=\alpha\cdot C,
$$

the observed output may be nonlinear in that score:

$$
Q=\sigma(\alpha\cdot C).
$$

Thus linear combination and nonlinear response often work together.

### 16.5 A detailed example

Suppose a task relies on cognitive mass $M$ through the rule

$$
p=\sigma(8(M-0.7)).
$$

This formula says that the critical region is near $M=0.7$. Let us compare several agents.

If $M=0.5$, then

$$
p=\sigma(8(0.5-0.7))=\sigma(-1.6)\approx 0.168.
$$

If $M=0.7$, then

$$
p=\sigma(0)=0.5.
$$

If $M=0.9$, then

$$
p=\sigma(1.6)\approx 0.832.
$$

This illustrates the threshold effect clearly. A shift of $0.2$ in mass below the threshold and the same shift above the threshold produce dramatic differences in outcome.

The factor $8$ controls steepness. A larger coefficient makes the transition sharper; a smaller one makes it more gradual.

### 16.6 Softmax: multiple choices instead of one

The sigmoid is especially useful when there are two outcomes, such as “activate” or “do not activate,” “pass” or “fail,” “promote” or “not yet.”

But many agent systems must choose among several actions.

Suppose an agent assigns raw scores

$$
z_1, z_2, \dots, z_k
$$

to $k$ possible actions. To convert these into probabilities that sum to $1$, we use softmax.

> **Definition:** For scores $z_1,\dots,z_k$, the **softmax** probability of choice $i$ is
> $$
> \operatorname{softmax}(z_i)=\frac{e^{z_i}}{e^{z_1}+e^{z_2}+\cdots+e^{z_k}}.
> $$

Each probability is positive, and the total is

$$
\sum_{i=1}^k \operatorname{softmax}(z_i)=1.
$$

If one score is much larger than the others, its probability becomes dominant. If the scores are similar, the probabilities are spread out.

For an agent choosing between memory retrieval, graph search, and identity verification, softmax turns internal action scores into a distribution over next moves.

### 16.7 Other activation shapes

The sigmoid is important, but it is not the only nonlinear response shape.

A brief survey:

- **Step-like response:** almost nothing below a threshold, almost full activation above it.
- **ReLU**:
  $$
  \operatorname{ReLU}(x)=\max(0,x),
  $$
  which is flat for negative input and linear for positive input.
- **Hyperbolic tangent**:
  $$
  \tanh(x),
  $$
  which is S-shaped like the sigmoid but ranges from $-1$ to $1$.

Each shape models a different response regime. ReLU captures “inactive until stimulated.” Sigmoid captures bounded probability-like response. Tanh captures balanced positive and negative activation.

The general lesson is more important than any one formula: autonomous systems often transform inputs through nonlinear links before behavior appears.

### 16.8 Linear structure inside nonlinear systems

Even when the final response is nonlinear, the input to that response often begins linearly. For instance,

$$
x = \alpha\cdot C
$$

may compute a raw integrated score, and then

$$
Q = \sigma(x)
$$

translates that score into a bounded quality or activation probability.

This layered structure is common:

1. combine ingredients linearly,
2. pass the result through a nonlinear function,
3. obtain a realistic bounded response.

In later chapters, derivatives will help us ask how sensitive $Q$ is to each component of $C$. That question depends crucially on the shape of the nonlinearity. Near the middle of a sigmoid, the system may be highly sensitive. Near the extremes, it may be relatively insensitive.

That is why nonlinear response is not a side topic. It determines when improvement matters most.

### Exercises

1. Compute the following values, to three decimal places:
   $$
   \sigma(0), \quad \sigma(1), \quad \sigma(-1).
   $$

2. Explain why a linear function is not always suitable for modeling a probability.

3. Suppose an agent’s activation probability is
   $$
   p=\sigma(5(M-0.6)).
   $$
   Estimate $p$ when $M=0.6$, $M=0.8$, and $M=0.4$.

4. An agent assigns raw action scores
   $$
   z_1=1,\quad z_2=2,\quad z_3=0.
   $$
   Write the softmax probability for each action.

5. Describe, in words, a situation in agent behavior where diminishing returns would make a nonlinear model more appropriate than a linear one.

---

## Chapter 17: Sensitivity — The Derivative

A research agent is running an ascent procedure on a quality function $Q$. At the current state, it asks two questions:

- If cognitive mass $M$ increases slightly, how much will $Q$ change?
- If permission stability $\Pi$ shifts slightly, how much will $Q$ change?

These are not questions about total output. They are questions about sensitivity. Which direction of improvement matters most right now? Which component is worth investing effort in? Where is the quality landscape steep, and where is it flat?

The derivative is the mathematical answer.

### 17.1 Rate of change

Suppose a quantity $Q$ depends on a variable $x$. If $x$ changes from $x$ to $x+h$, the output changes from $Q(x)$ to $Q(x+h)$. The average rate of change over that interval is

$$
\frac{Q(x+h)-Q(x)}{h}.
$$

This is the slope of the secant line joining the two points on the graph.

If $h$ is small, this average rate tells us how rapidly the function is changing near $x$. The derivative is what we get when we let the interval shrink to zero.

> **Definition:** The **derivative** of a function $f$ at a point $x$ is
> $$
> f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h},
> $$
> provided the limit exists.

The derivative is the instantaneous rate of change. Geometrically, it is the slope of the tangent line to the graph at that point.

### 17.2 Why derivatives matter for agents

Suppose an agent’s performance quality depends on cognitive mass:

$$
Q=f(M).
$$

Then $f'(M)$ tells us how responsive quality is to a small change in mass at the current value of $M$.

- If $f'(M)$ is large and positive, then a small increase in $M$ produces a noticeable increase in quality.
- If $f'(M)$ is near $0$, then local improvements in $M$ have little immediate effect.
- If $f'(M)$ is negative, then increasing $M$ would actually reduce the output—rare in basic capacity models, but possible in overloading or instability regimes.

The derivative therefore answers the practical question: what matters most right now?

### 17.3 A simple example

Take

$$
f(M)=M^2.
$$

Then

$$
f(M+h)=(M+h)^2=M^2+2Mh+h^2.
$$

So

$$
\frac{f(M+h)-f(M)}{h}
=
\frac{M^2+2Mh+h^2-M^2}{h}
=
2M+h.
$$

As $h\to 0$, this approaches $2M$. Therefore,

$$
f'(M)=2M.
$$

The sensitivity depends on where we are.

- At $M=0.2$, the derivative is $0.4$.
- At $M=0.8$, the derivative is $1.6$.

So the same small increase in mass matters more when mass is already large.

This example illustrates a central idea: in nonlinear systems, sensitivity is not constant. It changes with state.

### 17.4 Derivatives and the sigmoid

Now consider a more agent-relevant example:

$$
Q(M)=\sigma(8(M-0.7)).
$$

This is a thresholded quality response. Without even computing the exact derivative formula, we can reason about its meaning.

- Near $M=0.7$, the sigmoid is steep.
- Far below $0.7$, it is nearly flat.
- Far above $0.7$, it is nearly flat again.

Thus the derivative is largest near the threshold. That is where a marginal improvement in capacity has the greatest effect.

This matches intuition. If an agent is in the transition zone between failure and success, even a modest gain can matter enormously. If it is already almost certain to fail or almost certain to succeed, the same gain has less immediate effect.

### 17.5 Partial derivatives

Most agent outputs depend on more than one variable. A quality function might depend on identity, memory, graph reasoning, and permission simultaneously:

$$
Q=Q(C_{\text{id}}, C_{\text{mem}}, C_{\text{graph}}, C_{\text{perm}}).
$$

In that case we measure sensitivity to one variable at a time, holding the others fixed.

> **Definition:** The **partial derivative** of $Q$ with respect to $C_{\text{id}}$ is
> $$
> \frac{\partial Q}{\partial C_{\text{id}}},
> $$
> the rate at which $Q$ changes when $C_{\text{id}}$ varies and all other variables are treated as constant.

Similarly, we can form

$$
\frac{\partial Q}{\partial C_{\text{mem}}}, \qquad
\frac{\partial Q}{\partial C_{\text{graph}}}, \qquad
\frac{\partial Q}{\partial C_{\text{perm}}}.
$$

These quantities need not be equal. A small improvement in graph reasoning may currently matter much more than the same improvement in permission capacity, or vice versa.

### 17.6 An explicit multivariable example

Suppose

$$
Q = 2C_{\text{id}} + 3C_{\text{mem}}^2 + C_{\text{graph}}C_{\text{perm}}.
$$

Then:

- With respect to $C_{\text{id}}$, the derivative is
  $$
  \frac{\partial Q}{\partial C_{\text{id}}}=2.
  $$
- With respect to $C_{\text{mem}}$,
  $$
  \frac{\partial Q}{\partial C_{\text{mem}}}=6C_{\text{mem}}.
  $$
- With respect to $C_{\text{graph}}$,
  $$
  \frac{\partial Q}{\partial C_{\text{graph}}}=C_{\text{perm}}.
  $$
- With respect to $C_{\text{perm}}$,
  $$
  \frac{\partial Q}{\partial C_{\text{perm}}}=C_{\text{graph}}.
  $$

Notice what these expressions reveal.

- Identity contributes at a constant marginal rate.
- Memory has increasing marginal importance: as memory gets larger, its derivative gets larger.
- Graph and permission interact: the value of improving one depends on the current level of the other.

This is the mathematics of “what matters depends on context.”

### 17.7 The gradient

It is useful to collect all partial derivatives into a single vector.

> **Definition:** The **gradient** of a function $Q$ of several variables is the vector of its partial derivatives:
> $$
> \nabla Q=
> \left(
> \frac{\partial Q}{\partial C_{\text{id}}},
> \frac{\partial Q}{\partial C_{\text{mem}}},
> \frac{\partial Q}{\partial C_{\text{graph}}},
> \frac{\partial Q}{\partial C_{\text{perm}}}
> \right).
> $$

The gradient points in the direction of steepest increase of the function.

This is one of the most important facts in applied mathematics. If an agent is allowed to make only a small adjustment to its state, then moving in the direction of the gradient gives the greatest immediate increase in $Q$.

For the previous example,

$$
\nabla Q = (2,\;6C_{\text{mem}},\;C_{\text{perm}},\;C_{\text{graph}}).
$$

If the current state is

$$
(C_{\text{id}},C_{\text{mem}},C_{\text{graph}},C_{\text{perm}})
=
(0.7,0.5,0.8,0.4),
$$

then

$$
\nabla Q=(2,3,0.4,0.8).
$$

The largest component is the memory derivative, so a small improvement in memory gives the greatest local gain in $Q$.

### 17.8 The chain rule: sensitivity through layers

Many agent functions are built in layers. For example,

$$
M=\alpha\cdot C,
$$

and then

$$
Q=f(M).
$$

So $Q$ depends on the capacity vector $C$ indirectly through $M$.

The chain rule explains how sensitivities propagate through such compositions.

> **Definition:** The **chain rule** states that when one variable depends on another through an intermediate function, the derivative of the overall composition is the product of the relevant rates of change.

In the present setting, if

$$
Q=f(M), \qquad M=\alpha\cdot C,
$$

then for each component $C_i$,

$$
\frac{\partial Q}{\partial C_i}=f'(M)\frac{\partial M}{\partial C_i}.
$$

But since

$$
M=\alpha_1C_1+\cdots+\alpha_nC_n,
$$

we have

$$
\frac{\partial M}{\partial C_i}=\alpha_i.
$$

Therefore,

$$
\frac{\partial Q}{\partial C_i}=f'(M)\alpha_i.
$$

This is a beautiful and useful formula. It says that the sensitivity of quality to a component is the product of two things:

1. how sensitive quality is to mass overall, and
2. how strongly that component contributes to mass.

If the system is in a flat sigmoid region, then $f'(M)$ is small, and no component matters much right now. If the system is in a steep region, then components with large weights become especially influential.

### 17.9 Local information, not total truth

A derivative is local. It tells us what happens for very small changes near the current point. It does not automatically describe large changes over long distances.

This matters in agent mathematics. A component with the largest current derivative may not remain the most important after a substantial intervention. Improving one variable can move the system into a different regime, changing the derivatives themselves.

So derivatives are best understood as local guidance. They are the mathematics of immediate sensitivity, not final destiny.

### Exercises

1. Using the definition of derivative, find the derivative of
   $$
   f(x)=x^2
   $$
   at a general point $x$.

2. Suppose
   $$
   Q(C_{\text{id}},C_{\text{mem}})=C_{\text{id}}^2+4C_{\text{mem}}.
   $$
   Compute
   $$
   \frac{\partial Q}{\partial C_{\text{id}}}
   \quad \text{and} \quad
   \frac{\partial Q}{\partial C_{\text{mem}}}.
   $$

3. Let
   $$
   Q = 3C_{\text{id}} + C_{\text{graph}}C_{\text{perm}}.
   $$
   Find the gradient $\nabla Q$.

4. If
   $$
   M=0.2C_{\text{id}}+0.3C_{\text{mem}}+0.4C_{\text{graph}}+0.1C_{\text{perm}}
   $$
   and
   $$
   Q=M^2,
   $$
   write an expression for
   $$
   \frac{\partial Q}{\partial C_{\text{graph}}}.
   $$

5. In words, explain why the derivative of a sigmoid-based quality function is usually largest near the threshold region.

---

## Chapter 18: Accumulation — The Integral

An agent operates for six continuous hours in a planning environment. Its instantaneous cognitive output is not constant; it rises during warm-up, stabilizes, and later declines slightly under fatigue. At each moment $t$, the output rate is given by a function $q(t)$.

A natural question arises: how much total work did the agent produce over the full session?

If the rate were constant, we would multiply rate by time. But when the rate changes continuously, we must add together infinitely many tiny contributions. That is what the integral does.

The derivative measures local change. The integral measures total accumulation.

### 18.1 From discrete sums to continuous accumulation

Suppose an agent produces output at a constant rate of $5$ units per hour for $6$ hours. Then the total is simply

$$
5\cdot 6 = 30.
$$

Now suppose the rate changes over time. We can estimate total output by dividing the time interval into smaller pieces. Over a short interval of length $\Delta t$, if the rate is approximately $q(t)$, then the output contributed during that interval is approximately

$$
q(t)\,\Delta t.
$$

Adding many such pieces gives a Riemann sum:

$$
q(t_1)\Delta t + q(t_2)\Delta t + \cdots + q(t_n)\Delta t.
$$

As we make the intervals thinner and thinner, the approximation becomes exact in the limit.

> **Definition:** The **definite integral** of a function $f$ from $a$ to $b$ is the accumulated total
> $$
> \int_a^b f(x)\,dx,
> $$
> defined as the limit of sums of the form
> $$
> \sum f(x_i)\Delta x
> $$
> as the partition becomes arbitrarily fine.

The integral is therefore the mathematics of adding up continuously varying contributions.

### 18.2 Area under a curve

When $f(x)\ge 0$, the definite integral has a geometric interpretation.

> **Definition:** If $f(x)\ge 0$ on the interval $[a,b]$, then
> $$
> \int_a^b f(x)\,dx
> $$
> is the **area under the curve** $y=f(x)$ from $x=a$ to $x=b$.

This picture is more than a visual aid. It explains why the integral captures accumulation. A rectangle of height rate and width time has area equal to rate times time. Curved regions are built from the limit of many thin rectangles.

For an agent whose output rate is always nonnegative, the integral of output rate over time is total output.

### 18.3 Total cognitive output over time

Let $q(t)$ be the instantaneous output rate of an agent at time $t$, measured in standardized output units per hour. Then the total output produced from time $0$ to time $T$ is

$$
W=\int_0^T q(t)\,dt.
$$

If, for example,

$$
q(t)=2+t
$$

for $0\le t\le 3$, then output starts at $2$ and rises linearly to $5$.

The total work is

$$
\int_0^3 (2+t)\,dt.
$$

We can compute this using antiderivatives:

$$
\int (2+t)\,dt = 2t+\frac{t^2}{2}.
$$

Therefore,

$$
\int_0^3 (2+t)\,dt
=
\left(2t+\frac{t^2}{2}\right)\Bigg|_0^3
=
\left(6+\frac{9}{2}\right)-0
=
10.5.
$$

So the agent produces a total of $10.5$ output units.

### 18.4 Running totals

Sometimes we care not only about the final accumulated amount, but also about how accumulation grows as time passes.

> **Definition:** If $f$ is a rate function, the **accumulation function** from a starting time $a$ is
> $$
> A(x)=\int_a^x f(t)\,dt.
> $$

This function gives the total amount accumulated from $a$ up to the current point $x$.

For an agent session, we might define

$$
A(t)=\int_0^t q(s)\,ds.
$$

Then $A(1)$ is total output after one hour, $A(2)$ after two hours, and so on.

This perspective is useful in monitoring. An oversight system may track cumulative capacity utilization, cumulative energy expenditure, or cumulative memory consolidation during a deployment.

### 18.5 Positive and negative accumulation

Not all quantities being integrated are strictly positive. Suppose $r(t)$ measures net change in a memory bank: positive when new content is consolidated, negative when forgetting or overwrite dominates. Then

$$
\int_a^b r(t)\,dt
$$

represents net accumulation, not just total positive contribution.

This distinction matters.

- If $r(t)\ge 0$, the integral is total buildup.
- If $r(t)$ changes sign, the integral is gain minus loss.

In agent mathematics, this can model net knowledge retention, trust balance, or stability drift.

### 18.6 The Fundamental Theorem of Calculus

Derivatives measure rates of change. Integrals measure accumulation. One of the deepest results in mathematics is that these two ideas are inverse to each other.

> **Definition:** The **Fundamental Theorem of Calculus** states, in one of its central forms, that if
> $$
> A(x)=\int_a^x f(t)\,dt,
> $$
> then
> $$
> A'(x)=f(x).
> $$

In words: the derivative of the accumulated total is the original rate.

This is profoundly natural. If $A(x)$ records the total output up to time $x$, then the rate at which that total is increasing at time $x$ is exactly the instantaneous output rate $f(x)$.

The theorem also gives a practical method of computing definite integrals.

> **Definition:** A function $F$ is an **antiderivative** of $f$ if
> $$
> F'(x)=f(x).
> $$

If $F$ is an antiderivative of $f$, then

$$
\int_a^b f(x)\,dx = F(b)-F(a).
$$

This is the rule used in the previous example.

### 18.7 Agent applications

#### Capacity utilization over time

Suppose an agent uses a fraction $u(t)$ of its total cognitive capacity at time $t$. Then

$$
\int_0^T u(t)\,dt
$$

measures cumulative utilization over the interval $[0,T]$. If one agent runs near saturation for long periods while another uses moderate capacity steadily, the integrals may reveal different operational profiles even when final task counts look similar.

#### Memory consolidation

Suppose memory consolidation occurs at rate $m(t)$. Then

$$
\int_0^T m(t)\,dt
$$

is the total amount of consolidated content over the session. If $m(t)$ is high early and low later, the integral still collects the total effect.

#### Reliability exposure

If $p(t)$ denotes instantaneous probability density of failure pressure or instability load, an integral over time can measure cumulative exposure. Such cumulative measures often matter more than momentary snapshots.

### 18.8 An example with decay

Suppose consolidation rate is

$$
m(t)=e^{-t}
$$

for $0\le t\le 2$.

At first the rate is high, then it decays. The total consolidation is

$$
\int_0^2 e^{-t}\,dt.
$$

An antiderivative of $e^{-t}$ is $-e^{-t}$, so

$$
\int_0^2 e^{-t}\,dt
=
\left(-e^{-t}\right)\Bigg|_0^2
=
(-e^{-2})-(-1)
=
1-e^{-2}.
$$

This is approximately $0.865$.

The interpretation is important. Even though consolidation rate decreases over time, the integral adds the small later contributions to the larger early ones. Total effect is not determined by the rate at a single moment.

### 18.9 The integral as a continuous sum

A useful sentence to remember is this: an integral is a continuous sum.

When we write

$$
\int_a^b f(x)\,dx,
$$

we are summing tiny pieces of size

$$
f(x)\,dx
$$

across the whole interval. The variable of integration tells us what kind of accumulation is occurring.

- Integrating with respect to time accumulates over time.
- Integrating with respect to space accumulates over position.
- Integrating with respect to capacity level can accumulate over levels or distributions.

In agent mathematics, accumulation is everywhere: work over time, exposure over time, risk over states, and gain over phases of operation.

The derivative tells us how fast. The integral tells us how much in total.

### Exercises

1. Interpret in words the quantity
   $$
   \int_0^5 q(t)\,dt
   $$
   if $q(t)$ is an agent’s output rate.

2. Compute
   $$
   \int_0^4 3\,dt.
   $$

3. Compute
   $$
   \int_1^3 x\,dx.
   $$

4. If
   $$
   A(t)=\int_0^t r(s)\,ds,
   $$
   what does the Fundamental Theorem of Calculus say about $A'(t)$?

5. A memory consolidation rate is
   $$
   m(t)=2-t
   $$
   for $0\le t\le 2$. Find the total consolidation
   $$
   \int_0^2 (2-t)\,dt.
   $$

---

## Chapter 19: Uncertainty

A parameter identification experiment is underway. The memory capacity of an agent is recorded as

$$
C_{\text{mem}} = 0.68.
$$

But the research team knows better than to interpret this as exact. The battery is noisy. The calibration process is imperfect. Repeated measurement under slightly different task conditions might produce $0.66$, $0.70$, or $0.67$.

So what does $0.68$ really mean?

It means: somewhere around $0.68$, with uncertainty.

Probability is the mathematics of uncertainty. It does not replace measurement; it refines it. In the real world of autonomous systems, every observation contains approximation, variability, and noise. A mature mathematical theory must account for that.

### 19.1 Random variables

When outcomes are uncertain, we often describe them using a random variable.

> **Definition:** A **random variable** is a variable whose value depends on the outcome of an uncertain process.

If we repeatedly measure memory capacity under noisy conditions, the observed value is a random variable, say $X$. One run might produce $0.67$, another $0.69$, another $0.66$.

The underlying capacity may be stable, but the measurement process is not exact. Thus the observed quantity varies.

Random variables may be discrete or continuous.

- A **discrete** random variable takes countable values, such as the number of failed retrievals in $10$ trials.
- A **continuous** random variable takes values in an interval, such as a measured capacity score.

In agent mathematics, both kinds arise naturally.

### 19.2 Probability distributions

A random variable is not fully described by listing its possible values. We also need to know how likely those values are.

> **Definition:** A **probability distribution** describes how probability is assigned across the possible values of a random variable.

For a discrete variable, a distribution might say:

- probability $0.1$ of value $0$,
- probability $0.4$ of value $1$,
- probability $0.5$ of value $2$.

For a continuous variable, probability is distributed over an interval according to a density curve. The exact value $0.680000\ldots$ may have probability $0$ by itself, but small intervals around it can have substantial probability.

When we say a noisy measurement is “likely near $0.68$,” we are speaking about its distribution.

### 19.3 Expected value

A random process may vary, yet still have a center.

> **Definition:** The **expected value** or **mean** of a random variable is its long-run average value.

For a discrete random variable $X$ with values $x_i$ and probabilities $p_i$,

$$
E[X] = \sum_i x_i p_i.
$$

This is a weighted average.

For example, suppose a task failure count $X$ satisfies

- $P(X=0)=0.2$,
- $P(X=1)=0.5$,
- $P(X=2)=0.3$.

Then

$$
E[X]=0(0.2)+1(0.5)+2(0.3)=1.1.
$$

The agent will not literally fail $1.1$ times in a single trial, but over many trials the average failure count will approach $1.1$.

For continuous variables, expected value is defined by an integral rather than a sum, but the idea is the same: the center of the distribution.

In noisy measurement, the expected value often represents the underlying value the experiment is trying to estimate.

### 19.4 Variance and standard deviation

The mean tells us the center, but not the spread. Two measurement systems can have the same average and very different reliability.

> **Definition:** The **variance** of a random variable $X$ is
> $$
> \operatorname{Var}(X)=E[(X-E[X])^2].
> $$
> It measures the average squared distance from the mean.

> **Definition:** The **standard deviation** of $X$ is
> $$
> \operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}.
> $$
> It measures spread in the same units as the variable itself.

If repeated measurements of $C_{\text{mem}}$ cluster tightly near $0.68$, the variance is small. If they range widely from $0.55$ to $0.80$, the variance is larger.

Why square the deviations? Because positive and negative deviations would otherwise cancel out. Squaring also gives extra weight to large errors, which is often appropriate in measurement contexts.

### 19.5 An agent measurement example

Suppose a memory battery reports the following observed values with probabilities:

- $0.66$ with probability $0.2$,
- $0.68$ with probability $0.5$,
- $0.70$ with probability $0.3$.

Then the expected value is

$$
E[X]=0.66(0.2)+0.68(0.5)+0.70(0.3).
$$

So

$$
E[X]=0.132+0.340+0.210=0.682.
$$

Thus the center of the measurement process is $0.682$.

Now consider the deviations from the mean:

- $0.66-0.682=-0.022$,
- $0.68-0.682=-0.002$,
- $0.70-0.682=0.018$.

Squaring and weighting would give the variance. Even without carrying out the full arithmetic, we can see that the spread is small. The observation process is reasonably concentrated.

This is exactly the kind of reasoning needed when interpreting noisy agent diagnostics.

### 19.6 The normal distribution

Many measurement errors in science are approximately bell-shaped. Small deviations are common; large deviations are rare. This pattern is modeled by the normal distribution.

> **Definition:** A **normal distribution** is a bell-shaped probability distribution determined by two parameters:
> - its mean $\mu$,
> - its standard deviation $\sigma$.

A normal distribution with mean $\mu$ is centered at $\mu$. A larger $\sigma$ makes it wider and flatter; a smaller $\sigma$ makes it narrower and taller.

In practice, if measured capacities arise from many small independent sources of noise, the resulting distribution is often close to normal. This is one reason the normal distribution is so central in statistics.

A useful rule of thumb for normal data is the $68$-$95$-$99.7$ rule:

- about $68\%$ of values lie within one standard deviation of the mean,
- about $95\%$ lie within two,
- about $99.7\%$ lie within three.

So if an observed capacity is approximately normal with mean $0.68$ and standard deviation $0.02$, then most measurements will fall between $0.66$ and $0.70$.

### 19.7 Probability as rational caution

In agent mathematics, probabilistic thinking is not optional. It is the correct response to imperfect information.

Measurements are noisy. Environments fluctuate. Internal states are partly hidden. Task outcomes vary from trial to trial. A deterministic number may be convenient, but probability tells us how much trust to place in that number.

This changes interpretation.

- Instead of saying “the agent’s memory is exactly $0.68$,” we say “the measured memory is centered near $0.68$, with some spread.”
- Instead of saying “the next task will succeed,” we say “the next task has probability $0.81$ of success.”
- Instead of saying “the parameter equals this value,” we say “this value is plausible, with uncertainty.”

Probability is the mathematics of disciplined humility.

### 19.8 Why uncertainty matters for decision-making

Suppose two agents have estimated memory capacities:

- Agent A: mean $0.70$, standard deviation $0.01$,
- Agent B: mean $0.71$, standard deviation $0.08$.

If one only looks at mean, B appears better. But B is much less stable. Depending on the context, A may be preferable because its performance is more predictable.

This is a general principle: decision-making under uncertainty depends not only on the center, but also on the spread.

For autonomous systems, reliability is often as important as peak ability. Probability gives us the tools to formalize that distinction.

### Exercises

1. In your own words, explain why a noisy measurement should be modeled by a random variable.

2. A discrete random variable $X$ takes values $1,2,3$ with probabilities $0.2,0.5,0.3$. Compute $E[X]$.

3. Two measurement systems have the same mean. One has standard deviation $0.01$ and the other has standard deviation $0.10$. Which is more consistent, and why?

4. What do the mean and standard deviation of a normal distribution each describe?

5. If a measured quantity is approximately normal with mean $0.50$ and standard deviation $0.04$, give an interval that contains about $68\%$ of measurements.

---

## Chapter 20: Learning from Data

A promotion review is being conducted for the transition from D-level to E-level modeling. The research team has collected $300$ samples from an identification experiment. For each sample, they recorded component capacities and an observed quality score. They then fitted a weighted model, estimated the importance of graph capacity, and tested whether the fitted weights outperform the default equal-weight rule.

Their report includes statements such as:

- “Estimated $\alpha_{\text{graph}} = 0.380$.”
- “Confidence interval: $[0.363, 0.397]$.”
- “Fitted weights beat equal weights with $p=0.014$.”
- “Cross-validated $R^2$ improved by $0.07$.”

These are statistical statements. They do not describe one agent in isolation. They describe what can be learned from many observations.

Statistics is the mathematics of learning from data.

### 20.1 Estimation: from samples to parameters

In the previous chapter, probability described uncertainty in measurements. Statistics uses observed data to infer unknown quantities.

> **Definition:** A **parameter** is a fixed but unknown quantity in a model.

In an agent quality model,

$$
Q \approx \alpha_1 C_{\text{id}}+\alpha_2 C_{\text{mem}}+\alpha_3 C_{\text{graph}}+\alpha_4 C_{\text{perm}},
$$

the weights $\alpha_1,\dots,\alpha_4$ are parameters. They describe how strongly each capacity contributes to quality.

> **Definition:** An **estimate** is a value computed from data and used as a best guess for an unknown parameter.

Suppose the data suggest

$$
\hat\alpha=(0.18,0.22,0.38,0.22).
$$

The hat reminds us that these are estimated weights, not known truths.

If the default model used equal weights,

$$
\alpha^{(0)}=(0.25,0.25,0.25,0.25),
$$

then the fitted model says graph capacity appears more influential than the default assumption suggested.

Estimation is the first step in learning from data: use many observed examples to infer the structure behind them.

### 20.2 Samples and populations

A central statistical distinction is between the data we have and the larger process that generated them.

> **Definition:** The **population** is the full collection of cases we want to understand. A **sample** is the subset of cases we actually observe.

In agent mathematics, the population might be all relevant future tasks or all agents of a given architecture. The sample might be the $300$ cases collected in the promotion experiment.

Why does this distinction matter? Because the sample is only one finite glimpse of a larger reality. A different sample would produce slightly different fitted weights. Statistics studies how much those fitted values may fluctuate.

### 20.3 Confidence intervals

A single estimate is useful, but incomplete. We also want to know how precise it is.

> **Definition:** A **confidence interval** is a range of plausible values for a parameter, computed from data.

For example, suppose the fitted graph weight has a $95\%$ confidence interval

$$
[0.363,\,0.397].
$$

This means the data support graph weight values in that range as reasonable possibilities. Values far outside that range are less compatible with the observed evidence.

Confidence intervals are important because they combine two ideas:

1. estimation of a central value,
2. uncertainty about that estimate.

A narrow interval suggests high precision; a wide interval suggests more uncertainty.

In practice, interval width depends on factors such as sample size and noise level. More data usually produce tighter intervals, all else equal.

### 20.4 Hypothesis testing

Often we want to compare a new claim against a default or baseline claim.

In the promotion experiment, the question may be:

“Do fitted weights outperform equal weights?”

This is expressed through hypothesis testing.

> **Definition:** A **hypothesis test** compares a null hypothesis, usually representing no effect or no improvement, against an alternative hypothesis representing a meaningful effect.

For example:

- Null hypothesis $H_0$: fitted weights do not outperform equal weights.
- Alternative hypothesis $H_1$: fitted weights do outperform equal weights.

After computing an appropriate test statistic from the data, we obtain a p-value.

> **Definition:** A **p-value** is the probability, assuming the null hypothesis is true, of obtaining data at least as extreme as those observed.

If the p-value is small, then the data would be unusual under the null hypothesis, so we gain evidence against the null.

For instance, if

$$
p=0.014,
$$

then under the “no real improvement” assumption, data this favorable to the fitted model would occur only about $1.4\%$ of the time. This is commonly taken as evidence that the improvement is real.

A crucial warning: a p-value is not the probability that the null hypothesis is true. It is a statement about the data under the assumption that the null is true. That distinction matters.

### 20.5 Cross-validation: testing on unseen data

A model can appear excellent simply because it has adapted too closely to the data used to fit it. This is especially dangerous when many parameters are available.

To guard against this, we test the model on data it did not train on.

> **Definition:** **Cross-validation** is a procedure in which a model is fitted on one subset of data and evaluated on a different subset, to measure how well it generalizes.

The logic is simple and powerful.

- Training performance asks: how well does the model describe the data it already saw?
- Cross-validated performance asks: how well does it predict new cases?

In agent science, this distinction is vital. A promotion-worthy model must do more than memorize a particular experiment. It must capture stable structure that transfers to unseen agent-task instances.

Even a mathematically elegant fitted weight vector is not persuasive unless it survives out-of-sample testing.

### 20.6 $R^2$: explanatory power

When a model predicts a quantitative outcome, we need a measure of how much variation in the outcome it explains.

> **Definition:** The **coefficient of determination**, written $R^2$, measures the fraction of variation in the observed output explained by the model.

Its common formula is

$$
R^2 = 1-\frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}},
$$

where:

- $\text{SS}_{\text{res}}$ is the residual sum of squares,
- $\text{SS}_{\text{tot}}$ is the total sum of squares.

Intuitively:

- $R^2=1$ means perfect explanation,
- $R^2=0$ means the model explains no more variation than a baseline mean-only predictor,
- larger values indicate better explanatory power.

Suppose the equal-weights model gives

$$
R^2 = 0.41,
$$

while the fitted-weights model gives

$$
R^2 = 0.48.
$$

Then the improvement is

$$
0.48-0.41=0.07.
$$

That is not merely a numerical difference. It means the fitted model explains an additional $7\%$ of the total variation in observed quality.

### 20.7 The promotion criterion

To decide whether a new model deserves promotion, one must combine statistical significance with practical significance.

A result can be statistically significant but too small to matter. Conversely, a large observed improvement may fail to reach significance if the data are too noisy or too scarce.

In our setting, the promotion criterion is:

- cross-validated $R^2$ improvement $> 0.05$,
- and $p<0.05$.

This means the new model must both:

1. improve explanatory power by a meaningful amount, and
2. do so with evidence strong enough that the result is unlikely to be a chance fluctuation.

With the example values

$$
\Delta R^2 = 0.07, \qquad p=0.014,
$$

both conditions are met. The model therefore qualifies for promotion.

### 20.8 A worked interpretation

Suppose the experiment reports:

- estimated weight
  $$
  \hat\alpha_{\text{graph}}=0.380,
  $$
- confidence interval
  $$
  [0.363,0.397],
  $$
- cross-validated $R^2$ improvement
  $$
  \Delta R^2=0.07,
  $$
- hypothesis test p-value
  $$
  p=0.014.
  $$

What do these numbers say?

First, the fitted model assigns substantial importance to graph capacity. Second, the interval suggests this importance is estimated with reasonable precision. Third, the model’s predictive advantage is not confined to the training set; it persists under cross-validation. Fourth, the improvement is statistically persuasive under conventional criteria.

The conclusion is not “the model is absolutely true.” Statistics almost never grants that. Rather, the conclusion is that the evidence is strong enough to justify using the improved model in place of the default one.

That is how learning from data works: not through certainty, but through disciplined inference.

### 20.9 Statistics as the bridge from measurement to judgment

By now we can see the progression clearly.

- Measurement gives us observed values.
- Probability tells us those values are noisy.
- Statistics helps us infer stable structure from many noisy observations.

This is indispensable for autonomous systems. We do not merely want to describe one experiment. We want to decide:

- which components truly matter,
- whether a fitted model generalizes,
- when new evidence justifies revising our standard formulas,
- and whether promotion criteria have genuinely been met.

Statistics is therefore not the final chapter by accident. It is the culmination of the language of change. Once systems vary, respond, accumulate, and fluctuate, data become the path by which mathematics learns from reality.

### Exercises

1. Explain the difference between a parameter and an estimate.

2. A fitted model reports a $95\%$ confidence interval
   $$
   [0.12,0.18]
   $$
   for a weight parameter. What does this suggest about plausible values of the parameter?

3. In a model comparison study, the null hypothesis is “the new model is no better than the old model.” If the p-value is $0.03$, what is the usual statistical conclusion at the $0.05$ level?

4. Why is cross-validation more informative than training performance alone?

5. A default model has cross-validated $R^2=0.52$, and a fitted model has cross-validated $R^2=0.58$. Compute the improvement and determine whether it satisfies the criterion $\Delta R^2>0.05$.

---

Part IV has now equipped us with a powerful new language. Vectors let us describe multi-component states. Nonlinear functions let us model thresholds and saturation. Derivatives tell us where systems are sensitive. Integrals tell us how effects accumulate. Probability tells us how to reason under uncertainty. Statistics tells us how to learn from data.

An autonomous system changes, and mathematics must change with it.
