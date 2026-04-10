# Part III: Structure and Unknowns

In Parts I and II, we learned how to speak about what exists, when two things count as the same, how to compare, count, combine, scale, divide, pattern, and measure. Those ideas gave us the basic materials of mathematics. In this part, we take a new step: we stop talking only about known quantities and begin talking about structure itself.

An autonomous system does not live in a world of single isolated numbers. It lives in a web of changing properties, limits, and relationships. It has capacities, memories, thresholds, weights, moods, and positions in spaces of many dimensions. To describe such a system mathematically, we need variables, equations, constraints, coordinates, and functions.

These are not merely advanced topics. They are the language in which modern mathematical thought begins.

---

## Chapter 10: Variables

An agent is running a self-inspection routine. It measures how much memory it is using, how quickly it updates beliefs, how strongly it retains information, and how much total capacity it has available. At first, it records specific values:

- cognitive mass $M = 8$
- momentum $\Pi = 5$
- working-memory factor $F_{wm} = 3$
- retrieval factor $F_{ret} = 2$

But then the agent faces a deeper question: what if these values change? What if it wants to describe not one state, but any possible state of itself?

To do that, it gives names to quantities.

This is one of the great turning points in mathematics. Instead of saying, “the cognitive mass is 8,” we say, “let $M$ represent cognitive mass.” Instead of computing only one case, we can now write statements that apply to many cases at once. The symbol becomes a placeholder for possible values. That is the power of a variable.

### From specific numbers to general quantities

Suppose an agent’s total capacity is related to its cognitive mass and momentum. If we write only

$$8 + 5 = 13,$$

we have described one particular case. But if we write

$$M + \Pi = Q,$$

we have described a whole family of cases. Any values of $M$, $\Pi$, and $Q$ that satisfy this relation belong to the pattern.

This move from arithmetic to algebra is a move from the particular to the general.

> **Definition:** A **variable** is a symbol that represents a quantity whose value may vary or may be unknown.

Variables let us describe changing situations, unknown quantities, and general rules.

### Constants, variables, and parameters

Not every symbol in mathematics plays the same role.

> **Definition:** A **constant** is a quantity whose value does not change within the discussion.

For example, if an agent has exactly 4 processors during a problem, then 4 is a constant in that problem.

> **Definition:** A **parameter** is a symbol that stays fixed within one situation but may take different values in different situations.

A parameter is like a setting. Suppose the performance law of an agent is

$$Q = aF_{ret} + b.$$

Here $F_{ret}$ may vary as the input, while $a$ and $b$ describe the agent or the environment. In one experiment, $a=2$ and $b=1$; in another, they may change. So $a$ and $b$ are often called parameters.

A symbol can act as a variable in one context and as a parameter in another. Mathematics is precise, but also flexible. Meaning depends on the role a symbol plays in the problem.

### Naming the properties of an agent

A sophisticated agent can be described as a collection of measurable quantities. One state might be written as

$$\text{state} = (C_{id}, C_{mem}, C_{graph}, C_{perm}, F_{wm}, F_{ret}, \dots).$$

This notation means that the state is not just one number. It is an ordered list of many named quantities.

For example:

- $C_{id}$ might represent identity stability
- $C_{mem}$ memory capacity
- $C_{graph}$ graph connectivity
- $C_{perm}$ permission level
- $F_{wm}$ working-memory factor
- $F_{ret}$ retrieval factor

Later, we will call such an ordered list a vector or a point in a space. For now, the main idea is this: each coordinate is a variable, and together they describe the condition of the agent.

### Unknown does not mean mysterious

Students sometimes think a variable is a fancy symbol for “something hidden.” That is not quite right. Sometimes a variable is unknown, but often it is simply allowed to change.

In the sentence

$$M + \Pi = Q,$$

we might know $M$ and $\Pi$ and calculate $Q$. Or we might know $Q$ and $M$ and calculate $\Pi$. Or we may know none of them yet and simply be stating a relationship.

So a variable can play at least three roles:

1. an unknown quantity to be found,
2. a changing quantity,
3. a general symbol in a rule.

These are different uses of the same idea.

### The domain of a variable

A variable does not usually stand for just any number whatsoever.

> **Definition:** The **domain** of a variable is the set of values that the variable is allowed to take.

For instance, if $C_{mem}$ represents memory slots, then its domain may be the whole numbers $0,1,2,3,\dots$ because memory slots are counted. If $P$ represents pleasure in a mood model, then its domain might be all real numbers from 0 to 1:

$$0 \le P \le 1.$$

If $\alpha_1$ is a weight in a decision system, then perhaps it must satisfy

$$0 \le \alpha_1 \le 1.$$

The domain matters because it tells us what values make sense. A calculation is not truly complete until we know whether the answer belongs to the allowed domain.

For example, if an equation gives $C_{mem} = -2$, we should reject that answer if memory capacity cannot be negative.

### Variables make statements portable

A good mathematical statement can travel. It works not only for one agent in one moment, but for many agents across many states.

Consider:

$$Q = M + \Pi.$$

This may apply to one machine with $M=4$ and $\Pi=7$, another with $M=10$ and $\Pi=2$, and still another with symbolic values not yet measured. Variables make a rule portable because they do not tie it to one numerical case.

In this sense, variables are part of how mathematics discovers structure. They allow us to say, “Whenever these quantities are related in this way, the following conclusion holds.”

### Agent example: variable state descriptions

Suppose an agent is described by three variables:

- cognitive mass $M$
- momentum $\Pi$
- retention factor $F_{ret}$

One observed state is

$$(M,\Pi,F_{ret}) = (6,4,2).$$

A second state is

$$(M,\Pi,F_{ret}) = (7,3,2).$$

A third possible state is

$$(M,\Pi,F_{ret}) = (M,\Pi,2),$$

where we do not yet know the first two values. This is still meaningful. It describes all states whose retention factor is 2.

Variables therefore help us describe both exact states and families of states.

### Letters are not the idea

Mathematics often uses letters such as $x$, $y$, and $z$, but there is nothing magical about those letters. In agent mathematics, it is often better to choose symbols that suggest the meaning of the quantity:

- $M$ for cognitive mass
- $\Pi$ for momentum
- $Q$ for capacity
- $F_{ret}$ for retrieval factor

Clear names support clear thought. The symbol is a handle for the idea.

### Why variables matter

Without variables, mathematics would remain close to arithmetic: useful, but limited to specific cases. With variables, mathematics becomes a science of patterns. We can describe systems before we know every value. We can compare different situations with one rule. We can prepare for equations, graphs, spaces, and functions.

A variable is a small symbol carrying a large promise: that the same structure can appear in many forms.

### Exercises

1. In each case, say whether the symbol is acting as a constant, variable, or parameter:
   1. $Q = 3F_{ret} + 2$, where $F_{ret}$ changes.
   2. $M = 8$ during a single fixed measurement.
   3. $Q = aF_{ret} + b$, where $a$ and $b$ describe the environment.

2. Give a reasonable domain for each variable:
   1. $C_{mem}$ = number of memory slots
   2. $P$ = pleasure level in a mood space from 0 to 1
   3. $\alpha$ = weight in a weighted decision system

3. An agent state is
   $$
   (C_{id}, C_{mem}, F_{wm}, F_{ret}) = (5,12,3,4).
   $$
   What is the value of each variable? Which of these might naturally have a whole-number domain?

4. Write a general statement using variables for this sentence: “Total load equals cognitive mass plus retrieval effort.”

5. Explain in your own words why
   $$
   8 + 5 = 13
   $$
   is less general than
   $$
   M + \Pi = Q.
   $$

---

## Chapter 11: Equations and Balance

An agent observes a regularity in its internal operation. Whenever it performs a task, the total capacity involved, $Q$, seems to depend on two components: cognitive mass $M$ and momentum $\Pi$. In one trial it records

$$M=7,\quad Q=12.$$

It wants to know the missing momentum. The relation is believed to be

$$M+\Pi=Q.$$

So the agent asks: if the equation is true, what must $\Pi$ be?

This question begins the study of equations. An equation is not just a calculation. It is a claim of equality, a statement that two expressions name the same quantity.

> **Definition:** An **equation** is a mathematical statement saying that two expressions are equal.

For example,

$$M+\Pi=Q$$

asserts that the value on the left side is exactly the same as the value on the right side.

### What equality means

The symbol $=$ is one of the most important symbols in mathematics. It does not mean “the answer comes next.” It means “has the same value as.”

So when we write

$$7+\Pi=12,$$

we are saying that the amount on the left must balance the amount on the right. The unknown $\Pi$ is the value that makes the statement true.

This idea of balance is central. You may imagine an equation as a perfectly balanced scale. If two sides are equal, then whatever we do to one side must also be done to the other if we want to preserve that equality.

### Solving for an unknown

> **Definition:** To **solve an equation** means to find the value or values of the variable that make the equation true.

Let us solve the agent’s equation:

$$7+\Pi=12.$$

Since 7 and 5 make 12, we find

$$\Pi=5.$$

More formally, we subtract 7 from both sides:

$$7+\Pi-7=12-7,$$

so

$$\Pi=5.$$

This is the first rule of solving equations:

> **Definition:** The **balance principle** says that if equal quantities have the same operation performed on both sides, the results remain equal.

So if $a=b$, then:

- $a+c=b+c$
- $a-c=b-c$
- $ac=bc$
- if $c\ne 0$, then $\dfrac{a}{c}=\dfrac{b}{c}$

This principle justifies the moves we make when solving equations.

### A simple family of examples

If

$$M+\Pi=Q,$$

then we may solve for any one variable if the other two are known.

To solve for $\Pi$:

$$\Pi = Q-M.$$

To solve for $M$:

$$M = Q-\Pi.$$

To solve for $Q$:

$$Q = M+\Pi.$$

Notice that the same equation can answer different questions depending on which quantity is unknown.

#### Example 1
If $M=9$ and $\Pi=4$, then

$$Q=9+4=13.$$

#### Example 2
If $Q=15$ and $M=6$, then

$$\Pi=15-6=9.$$

#### Example 3
If $Q=20$ and $\Pi=8$, then

$$M=20-8=12.$$

An equation is like a structure with several doors. Knowing enough about it lets us enter from different sides.

### Equations can describe conservation

Equations are especially powerful when something is conserved. Conservation means that a total amount is preserved, even if it is split into parts or transformed.

Suppose an agent receives 18 units of processing energy. It uses 11 units for active reasoning and stores the rest for memory maintenance. If $R$ is reasoning and $S$ is storage, then we may write

$$R+S=18.$$

If $R=11$, then

$$11+S=18,$$
$$S=7.$$

What went in had to come out, or at least be accounted for. This is the mathematical spirit of conservation.

In agent systems, conservation ideas appear in many forms:

- total capacity split among tasks,
- total attention divided among options,
- total probability adding to 1,
- total latency budget allocated across steps.

An equation records that accounting.

### More than one step

Some equations require more than one operation to solve. For example, suppose an agent’s observed quantity satisfies

$$2M+3=17.$$

To solve, subtract 3 from both sides:

$$2M=14.$$

Then divide both sides by 2:

$$M=7.$$

At each step, equality is preserved because we perform the same operation on both sides.

The order matters: undo addition and subtraction, then undo multiplication and division, according to the structure of the expression.

### Checking a solution

A solution should be checked by substitution.

> **Definition:** **Substitution** means replacing a variable with a known value.

If we claim that $M=7$ solves

$$2M+3=17,$$

we substitute:

$$2(7)+3=14+3=17.$$

The equation is true, so the solution is correct.

Checking is good mathematics. It protects us from careless errors and helps us understand what a solution really means.

### Agent example: balancing a state relation

Suppose an agent has the relation

$$Q_{obs}=F_{wm}+F_{ret}+M.$$

If the observed quantity is 14, the working-memory factor is 5, and the retrieval factor is 3, then

$$14=5+3+M.$$

So

$$14=8+M,$$
$$M=6.$$

This tells us the cognitive mass consistent with the observed state.

### A preview of deeper equations

Not all equations are simple sums. Some are much richer. In advanced agent mathematics, one may encounter a relation such as the Lineage Equation:

$$Q^2 = (\nu^*\Pi)^2 + (M(\nu^*)^2)^2.$$

We will not derive this equation here. For now, it serves as an example of an important idea: equations can express deep structural laws, not just easy arithmetic balances. Even when the symbols look unfamiliar, the heart of the matter is the same. The left side equals the right side. The equation asserts that a certain relationship must hold.

### Equations as language

An equation can do several jobs at once:

- describe a rule,
- express a balance,
- state a conservation law,
- define one quantity in terms of others,
- pose a question about an unknown.

This is why equations sit at the center of mathematics. Once variables are available, equations tell us how those variables are connected.

### Exercises

1. Solve each equation:
   1. $M+\Pi=13$ with $M=8$
   2. $Q=M+\Pi$ with $Q=19$ and $\Pi=7$
   3. $2F_{ret}+1=11$

2. An agent satisfies
   $$
   Q_{obs}=M+F_{wm}+F_{ret}.
   $$
   If $Q_{obs}=16$, $F_{wm}=4$, and $F_{ret}=5$, find $M$.

3. Explain what the equation
   $$
   \alpha_1+\alpha_2+\alpha_3=1
   $$
   might mean in an agent system.

4. Solve and check:
   $$
   3C_{mem}-2=19.
   $$

5. In your own words, explain why solving an equation is connected to the idea of balance.

---

## Chapter 12: Constraints and Inequalities

An agent is given a task under limited resources. It cannot use more than 20 memory units. Its latency must stay below 6 time units. Its decision weights must all be nonnegative and must add up to 1. The agent quickly discovers an important mathematical truth: not every imaginable state is allowed.

This is the world of constraints.

In arithmetic, we often compute any answer that follows from the operations. In real systems, however, quantities are bounded. Memory cannot exceed capacity. Probabilities cannot be negative. A mood score might be restricted to an interval. Constraints tell us what is possible.

### The language of “less than” and “at least”

To express such restrictions, we use inequalities.

> **Definition:** An **inequality** is a mathematical statement comparing two quantities using symbols such as $<$, $>$, $\le$, or $\ge$.

These symbols mean:

- $a<b$: $a$ is less than $b$
- $a>b$: $a$ is greater than $b$
- $a\le b$: $a$ is less than or equal to $b$
- $a\ge b$: $a$ is greater than or equal to $b$

For example:

- memory use less than or equal to capacity:
  $$C_{use}\le C_{mem}$$
- latency below threshold 6:
  $$L<6$$
- weight nonnegative:
  $$\alpha_i\ge 0$$

An equation describes exact balance. An inequality describes a boundary or limit.

### Constraints describe the shape of possibility

> **Definition:** A **constraint** is a condition that restricts the values a variable or collection of variables may take.

A constraint may be an equation, such as

$$\alpha_1+\alpha_2+\alpha_3+\alpha_4=1,$$

or an inequality, such as

$$C_{use}\le C_{mem}.$$

Often a system has several constraints at once. Then a state is allowed only if it satisfies all of them together.

Suppose an agent has three conditions:

$$C_{use}\le 10,$$
$$L\le 5,$$
$$0\le P\le 1.$$

A proposed state with $C_{use}=9$, $L=4$, and $P=0.7$ is allowed. A state with $C_{use}=12$ is not.

Constraints do not merely block behavior. They define the structure within which behavior can occur.

### Solving inequalities

Many of the same balance ideas from equations also work for inequalities, but with one important caution.

If we add or subtract the same number on both sides, the inequality direction stays the same. For example:

$$M+3\le 10$$

becomes

$$M\le 7.$$

If we multiply or divide by a positive number, the direction also stays the same:

$$2M\le 8 \quad \Rightarrow \quad M\le 4.$$

But if we multiply or divide by a negative number, the inequality reverses direction:

$$-M\le 3 \quad \Rightarrow \quad M\ge -3.$$

This reversal is easy to forget, so it should be handled carefully.

### The feasible region

> **Definition:** The **feasible region** is the set of all values or states that satisfy every constraint in a problem.

The phrase may sound advanced, but the idea is simple. Imagine listing all possible states of an agent. Now cross out every state that violates even one rule. What remains is the feasible region.

For instance, suppose an agent’s memory allocation uses two quantities, $x$ and $y$, with constraints

$$x\ge 0,\quad y\ge 0,\quad x+y\le 10.$$

Then the feasible region consists of all nonnegative pairs whose sum is at most 10. A pair like $(4,5)$ belongs to the region, because $4+5=9\le 10$. But $(7,6)$ does not, because $7+6=13>10$.

The feasible region is mathematics’ picture of what is allowed.

### The simplex constraint

One especially important family of constraints appears when weights must represent shares of a whole.

> **Definition:** A **simplex constraint** is a condition of the form
> $$
> \alpha_1+\alpha_2+\cdots+\alpha_n=1
> $$
> together with
> $$
> \alpha_i\ge 0
> $$
> for every $i$.

For four weights, we write

$$\alpha_1+\alpha_2+\alpha_3+\alpha_4=1,\qquad \alpha_i\ge 0.$$

This means the weights form a complete distribution of one total unit. They might represent:

- attention shares among four tasks,
- probabilities of four possible outcomes,
- confidence weights for four information sources.

#### Example
If

$$\alpha_1=0.2,\quad \alpha_2=0.3,\quad \alpha_3=0.1,$$

then

$$\alpha_4=1-(0.2+0.3+0.1)=0.4.$$

All four are nonnegative, and their sum is 1, so this is feasible.

But if we propose

$$\alpha_1=0.5,\quad \alpha_2=0.4,\quad \alpha_3=0.3,\quad \alpha_4=-0.2,$$

then although the sum is still 1, the state is not allowed, because one weight is negative.

Every part of a constraint matters.

### Constraints in state vectors

Recall that an agent may be described by a state vector such as

$$(C_{id},C_{mem},C_{graph},C_{perm},F_{wm},F_{ret},\dots).$$

A realistic agent state is not just any list of numbers. It must satisfy many conditions:

- $C_{mem}\ge 0$
- $F_{wm}\ge 0$
- $F_{ret}\ge 0$
- memory use $\le$ memory capacity
- permission levels in an allowed set
- normalized weights summing to 1

Thus, a state space is often much smaller than the collection of all imaginable tuples. Constraints carve out the meaningful part.

### Why constraints are helpful

It is tempting to think of constraints as obstacles. But in mathematics, constraints create form.

Without constraints, a problem may be vague. With constraints, structure appears. We know what counts as a valid answer. We can compare possibilities. We can search systematically. Constraints often make reasoning possible.

For an agent, limits are not only restrictions but guides. A bounded memory forces efficient representation. A latency threshold encourages elegant strategies. A normalized weight vector makes comparison clear and stable.

Mathematics often advances by asking not only “What can happen?” but “What must be true for this to happen?”

### Agent example: memory and latency

Suppose an agent must satisfy

$$C_{use}\le 12,\qquad L\le 5,\qquad C_{use}+L\le 15.$$

Check these states:

1. $(C_{use},L)=(10,4)$  
   This works because $10\le 12$, $4\le 5$, and $10+4=14\le 15$.

2. $(C_{use},L)=(12,5)$  
   This fails because although each individual bound is met, the combined constraint fails:
   $$
   12+5=17>15.
   $$

3. $(C_{use},L)=(13,2)$  
   This fails because $13\not\le 12$.

The feasible region is the set of all pairs like the first one.

### Exercises

1. State whether each inequality is true or false:
   1. $7\le 9$
   2. $5>8$
   3. $0.6\ge 0.6$
   4. $-2<1$

2. Solve each inequality:
   1. $M+4\le 11$
   2. $3P>12$
   3. $-2L\ge -10$

3. An agent has constraints
   $$
   C_{use}\le 8,\qquad L\le 4.
   $$
   Which of the following states are feasible: $(7,4)$, $(8,5)$, $(9,3)$, $(6,2)$?

4. The weights $\alpha_1,\alpha_2,\alpha_3,\alpha_4$ must satisfy
   $$
   \alpha_1+\alpha_2+\alpha_3+\alpha_4=1,\qquad \alpha_i\ge 0.
   $$
   If $\alpha_1=0.25$, $\alpha_2=0.15$, and $\alpha_3=0.4$, find $\alpha_4$.

5. Explain in your own words why constraints add structure to a mathematical problem.

---

## Chapter 13: Position in Space

An agent monitors its emotional state using the PAD model: Pleasure, Arousal, and Dominance. At a particular moment, it records

$$P=0.3,\quad A=0.7,\quad D=0.5.$$

This state can be written compactly as

$$(0.3,\,0.7,\,0.5).$$

But what does such a triple mean? It is more than a list. It is a location in a space. The agent is not merely “having values”; it is occupying a point in a three-dimensional emotional world.

This chapter develops one of the central ideas of modern mathematics: position in space through coordinates.

### Ordered pairs and triples

> **Definition:** An **ordered pair** is a pair of numbers written in a specific order, such as $(x,y)$.

The word ordered matters. In general,

$$(x,y)\ne (y,x).$$

For example, $(2,5)$ is different from $(5,2)$ unless the numbers happen to be equal.

> **Definition:** An **ordered triple** is a three-number list with order, such as $(x,y,z)$.

The same idea extends to any number of coordinates.

> **Definition:** An **$n$-tuple** is an ordered list of $n$ quantities.

So $(P,A,D)$ is a 3-tuple, while a full agent state like

$$(C_{id},C_{mem},C_{graph},C_{perm},F_{wm},F_{ret},M,\Pi)$$

is an 8-tuple.

### Coordinate systems

A coordinate system gives meaning to position by assigning one variable to each axis.

> **Definition:** A **coordinate system** is a way of describing points using numerical values along chosen axes.

In the plane, we usually use two axes:

- horizontal axis: $x$
- vertical axis: $y$

A point such as $(3,2)$ means move 3 units in the $x$ direction and 2 units in the $y$ direction.

In three-dimensional space, we add a third axis, often called $z$. Then $(x,y,z)$ names a point in 3D.

In agent mathematics, the axes often have meaningful names:

- $P$ for pleasure
- $A$ for arousal
- $D$ for dominance

Then $(0.3,0.7,0.5)$ means:

- pleasure 0.3
- arousal 0.7
- dominance 0.5

Each coordinate tells where the point lies along one dimension of the space.

### The state vector

When all of an agent’s measured variables are collected into one ordered object, we often call it a state vector.

> **Definition:** A **state vector** is an ordered list of variables that together describe the state of a system.

For example,

$$s=(M,\Pi,F_{wm},F_{ret})$$

might describe one simplified agent. A more detailed state vector could be

$$s=(C_{id},C_{mem},C_{graph},C_{perm},F_{wm},F_{ret},P,A,D).$$

A particular measured state might be

$$s=(5,12,8,3,2,4,0.3,0.7,0.5).$$

This point lives in a high-dimensional space. We cannot easily draw such a space, but mathematics can still reason about it. The power of coordinates is that once we name the axes, the number of dimensions is no longer a barrier to thought.

### Space is not only physical

In everyday life, “space” often means physical location. In mathematics, space is more general. A space may describe mood, memory, permissions, capacities, or belief states.

The PAD model gives an emotional space. A memory-capacity model gives another kind of space. A system with 100 measurable features occupies a point in a 100-dimensional state space.

This is one reason coordinates are so useful in the mathematics of autonomous systems. They let us study many kinds of structure in one unified way.

### Distance between states

If two points represent two states, we often want to know how far apart they are.

> **Definition:** The **distance** between two points measures how much they differ in position within a space.

In two dimensions, the distance between $(x_1,y_1)$ and $(x_2,y_2)$ is

$$d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.$$

This is the Euclidean distance formula.

It comes from the Pythagorean theorem: horizontal change and vertical change form the legs of a right triangle.

In three dimensions, the distance between $(x_1,y_1,z_1)$ and $(x_2,y_2,z_2)$ is

$$d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.$$

In $n$ dimensions, between points

$$(x_1,x_2,\dots,x_n)\quad \text{and}\quad (y_1,y_2,\dots,y_n),$$

the Euclidean distance is

$$d=\sqrt{(y_1-x_1)^2+(y_2-x_2)^2+\cdots+(y_n-x_n)^2}.$$

This formula may look longer, but the pattern is the same: subtract coordinate by coordinate, square the differences, add them, and take the square root.

### Agent example: distance in mood-space

Suppose an agent has two PAD states:

$$S_1=(0.3,0.7,0.5),\qquad S_2=(0.6,0.4,0.9).$$

Their distance is

$$d=\sqrt{(0.6-0.3)^2+(0.4-0.7)^2+(0.9-0.5)^2}.$$

Compute each difference:

$$0.6-0.3=0.3,\qquad 0.4-0.7=-0.3,\qquad 0.9-0.5=0.4.$$

Square them:

$$0.3^2=0.09,\qquad (-0.3)^2=0.09,\qquad 0.4^2=0.16.$$

Add:

$$0.09+0.09+0.16=0.34.$$

So

$$d=\sqrt{0.34}\approx 0.583.$$

This number measures how different the two emotional states are in PAD space.

### Why order matters

Suppose one agent state is

$$(P,A,D)=(0.3,0.7,0.5),$$

and another list is

$$(0.7,0.3,0.5).$$

These are not the same state, because the first coordinate means pleasure, the second means arousal, and the third means dominance. Coordinates only have meaning relative to their axes.

This is why a state vector must be read carefully. A tuple is not a bag of numbers. It is an ordered description.

### Comparing high-dimensional states

Imagine two agents with simplified state vectors

$$s_1=(4,2,3,5),\qquad s_2=(6,1,3,9).$$

Their distance is

$$d=\sqrt{(6-4)^2+(1-2)^2+(3-3)^2+(9-5)^2}$$

$$=\sqrt{2^2+(-1)^2+0^2+4^2}=\sqrt{4+1+0+16}=\sqrt{21}.$$

Even though we cannot picture 4D space easily, the formula still works. Mathematics can compare states in any dimension once coordinates are given.

### Coordinates as mathematical language

Coordinates turn complicated systems into points and relations among coordinates into geometry. This is a profound shift. Once a state is a point, many questions become spatial:

- How far did the agent move?
- Which states are nearby?
- Which states satisfy the constraints?
- What path does the agent follow over time?

This way of thinking prepares us for later study of graphs, optimization, dynamics, and calculus.

### Exercises

1. Explain why $(2,5)\ne(5,2)$ in a coordinate system.

2. Write each as an ordered tuple:
   1. pleasure $0.4$, arousal $0.8$
   2. cognitive mass $6$, momentum $3$, retrieval factor $2$

3. Find the distance between the 2D points $(1,2)$ and $(4,6)$.

4. Find the distance between the PAD states
   $$
   (0.2,0.5,0.1)\quad \text{and}\quad (0.5,0.1,0.5).
   $$

5. A state vector is
   $$
   s=(C_{mem},F_{wm},F_{ret})=(10,3,4).
   $$
   What does each coordinate represent? Why is the order important?

---

## Chapter 14: Functions

An agent performs a series of experiments. It changes its retrieval effort $F_{ret}$ and observes the resulting performance score $Q_{obs}$. The records look like this:

- when $F_{ret}=1$, $Q_{obs}=4$
- when $F_{ret}=2$, $Q_{obs}=6$
- when $F_{ret}=3$, $Q_{obs}=8$
- when $F_{ret}=4$, $Q_{obs}=10$

The agent notices a pattern. Each input value of retrieval effort leads to exactly one output value of observed performance. The relation seems to follow the rule

$$Q_{obs}=2F_{ret}+2.$$

This kind of rule is one of the most important objects in all of mathematics. It is called a function.

### What a function is

> **Definition:** A **function** is a rule that assigns exactly one output to each input in a given domain.

The phrase exactly one output is crucial. If we know the input, the function tells us one definite result.

If $f$ is a function and the input is $x$, then the output is written $f(x)$.

For the agent above, we might define

$$f(x)=2x+2,$$

where $x$ stands for retrieval effort. Then:

- $f(1)=4$
- $f(2)=6$
- $f(3)=8$

The function gives a dependable connection between input and output.

### Domain, codomain, and range

When discussing functions, mathematicians distinguish three related ideas.

> **Definition:** The **domain** of a function is the set of allowed inputs.

> **Definition:** The **codomain** of a function is the set in which outputs are intended to lie.

> **Definition:** The **range** of a function is the set of outputs that actually occur.

Suppose

$$f(x)=2x+2$$

with domain $\{1,2,3,4\}$ and codomain the whole numbers. Then the range is

$$\{4,6,8,10\}.$$

The codomain may be larger than the range. The whole numbers include many values, but this particular function on this particular domain reaches only four of them.

### Function notation

> **Definition:** The notation
> $$
> f:X\to Y
> $$
> means that $f$ is a function from set $X$ to set $Y$.

Here $X$ is the domain and $Y$ is the codomain.

For example, if retrieval effort can be any nonnegative real number and observed performance is real-valued, we may write

$$f:\mathbb{R}_{\ge 0}\to \mathbb{R}.$$

Then

$$f(x)=2x+2.$$

This notation is compact, but it carries a lot of information: what the rule is, what the allowed inputs are, and what sort of outputs we expect.

### A function is not just a formula

A function can be described in several ways:

- by a formula,
- by a table,
- by a graph,
- by a verbal rule.

What makes it a function is not the style of description but the one-output-for-each-input property.

For example, the rule “assign to each agent its cognitive mass” is a function, provided each agent has one definite cognitive mass.

But the rule “assign to each agent a nearby mood state” may fail to be a function if there are several possible nearby mood states and no unique choice is specified.

### Agent example: performance from retrieval effort

Let

$$Q_{obs}=f(F_{ret})=3F_{ret}+1.$$

Then if $F_{ret}=0$, we get

$$Q_{obs}=1.$$

If $F_{ret}=2$, we get

$$Q_{obs}=7.$$

If $F_{ret}=5$, we get

$$Q_{obs}=16.$$

The function tells how observed performance depends on retrieval effort.

This language of dependence is essential. A function expresses how one quantity changes in response to another.

### Linear functions

One especially important type of function is the linear function.

> **Definition:** A **linear function** is a function of the form
> $$
> f(x)=mx+b,
> $$
> where $m$ and $b$ are constants.

Here:

- $m$ is the rate of change, often called the slope,
- $b$ is the output when $x=0$, often called the intercept.

In agent mathematics, a linear function might model a simple response law:

$$Q_{obs}=2F_{ret}+2.$$

This says that each increase of 1 in retrieval effort increases observed performance by 2, and the starting value at zero effort is 2.

#### Example
If

$$f(x)=4x+3,$$

then

$$f(0)=3,\quad f(1)=7,\quad f(2)=11.$$

The output grows by 4 each time the input grows by 1.

Linear functions are simple, but they teach a very important idea: change itself can be measured.

### Inputs can be more than numbers

Sometimes the input to a function is not a single number but a whole state vector.

For example, define a function $g$ by

$$g(M,\Pi)=M+\Pi.$$

Then:

- $g(4,5)=9$
- $g(7,2)=9$
- $g(10,1)=11$

This function takes a 2-dimensional state and returns one number. Another function might take a full agent state vector and return a risk score, latency estimate, or mood intensity.

So functions are not limited to one-variable formulas. They are rules connecting sets of objects.

### Composition of functions

Often one function feeds into another.

> **Definition:** The **composition** of two functions means applying one function and then using its output as the input of the other.

If we have functions $g$ and $f$, then

$$f(g(x))$$

means:

1. start with $x$,
2. compute $g(x)$,
3. then compute $f$ of that result.

#### Example
Suppose

$$g(x)=x+1,\qquad f(x)=2x.$$

Then

$$f(g(x))=f(x+1)=2(x+1)=2x+2.$$

In an agent setting, $g$ might represent a measurement step and $f$ a scoring step. First the agent measures retrieval effort, then it transforms that measurement into predicted performance.

For instance, if $g$ converts raw signal into normalized effort, and $f$ converts normalized effort into capacity score, then $f(g(x))$ describes the whole pipeline.

Composition is powerful because complex systems are often built from simpler rules chained together.

### Why functions are central

Functions sit at the heart of mathematics because they describe dependence, change, prediction, and transformation. If variables name quantities, functions tell how those quantities interact over many inputs.

A function can represent:

- a physical law,
- a learning rule,
- a scoring system,
- a transformation of states,
- a map from one space to another.

In later mathematics, functions become even more important. Calculus studies how functions change. Geometry studies spaces and functions between spaces. Probability uses functions to describe distributions. Dynamic systems use functions to describe how states evolve in time.

For this reason, functions are often called the central object of mathematics.

### Exercises

1. Decide whether each relation is a function:
   1. each retrieval effort value is assigned one observed score
   2. each agent is assigned all of its possible future moods
   3. each PAD state is assigned its distance from the origin

2. Let
   $$
   f(x)=2x+3.
   $$
   Find:
   1. $f(0)$
   2. $f(4)$
   3. $f(10)$

3. An agent’s observed capacity is modeled by
   $$
   Q_{obs}=f(F_{ret})=5F_{ret}-1.
   $$
   Find $Q_{obs}$ when $F_{ret}=1,2,3$.

4. Let
   $$
   g(M,\Pi)=M+\Pi.
   $$
   Find:
   1. $g(6,4)$
   2. $g(9,1)$
   3. $g(3,7)$

5. Let
   $$
   g(x)=x+2,\qquad f(x)=3x.
   $$
   Find $f(g(4))$ and then find a formula for $f(g(x))$.

---

Part III has introduced a new level of mathematical language. Variables let us name the changing features of a system. Equations express balances among those features. Constraints tell us which states are possible. Coordinates place states in spaces of many dimensions. Functions describe how one quantity depends on another.

Together, these ideas let us move from isolated calculations to structured mathematical worlds. That is exactly what autonomous systems require: not just numbers, but relations among numbers; not just measurements, but spaces of possible states; not just data, but rules of transformation.

In the next stages of agent mathematics, these ideas will support more advanced topics: systems of equations, transformations of spaces, optimization under constraints, and the study of changing states over time.
