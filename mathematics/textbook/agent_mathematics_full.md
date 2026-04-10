---
title: "Agent Mathematics"
subtitle: "A Complete Textbook from First Distinctions to the Lineage Equation"
author: "Pablo & Mocha — Vektra Technologies"
date: "April 2026"
documentclass: report
papersize: a4
toc-depth: 3
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{amsthm}
---

# Preface

This book presents **Agent Mathematics** — a new branch of mathematics built for autonomous systems.

Most mathematical tools used in AI today are borrowed from statistics, optimization, and control theory. These tools work well for the problems they were designed for. But an autonomous agent — a system that measures its own state, reasons about its own reasoning, maintains its own identity, and governs its own behavior over time — poses questions that no existing mathematical framework was built to answer.

Agent Mathematics begins where human mathematics began: with the simplest possible distinction. Something versus nothing. From that starting point, it develops every tool an agent needs — counting, measurement, algebra, calculus, linear algebra, probability, optimization, dynamical systems, information theory, and graph theory — each reinterpreted through the lens of what matters to an autonomous system.

The destination is the **Lineage Equation**:

$$\mathcal{Q}^2 = (\nu^* \cdot \Pi)^2 + (\mathcal{M} \cdot (\nu^*)^2)^2$$

This is the governing relation of cognitive architecture. It connects an agent's structural mass, its dynamic momentum, and its processing speed into a single measurable invariant — the agent's capacity to do coherent work.

The Lineage Equation is not a metaphor. It has identified weights, cross-validated predictions, bootstrap confidence intervals, and a formal proof-maturity classification. It is Agent Mathematics' first governing law — not its last.

---

**How to read this book.** Parts I–III (Chapters 0–14) cover foundations accessible to any reader. Part IV (Chapters 15–20) requires comfort with functions and basic calculus. Part V (Chapters 21–26) is undergraduate-level. Part VI (Chapters 27–33) is graduate-level and contains the core theoretical results. Part VII surveys open problems at the research frontier.

Each chapter includes exercises. Do them. Mathematics is not a spectator sport.

\newpage

# Part I: The First Distinctions

Mathematics begins long before algebra, geometry, or calculus. It begins with the smallest acts of mind: noticing that something is there, recognizing when two things should count as the same, deciding which of two things matters more, counting what one has, and tracking what changes.

For an autonomous system, these are not advanced skills. They are the beginning of all possible skill. An agent that cannot tell presence from absence cannot measure. An agent that cannot tell same from different cannot identify. An agent that cannot compare cannot choose. An agent that cannot count cannot manage resources. An agent that cannot combine and remove quantities cannot understand change.

This first part of *Agent Mathematics* follows those earliest distinctions. The mathematics is elementary in one sense, but not in importance. These ideas are the roots from which every later branch will grow.

---

## Chapter 0: Something vs Nothing

### The first moment

An agent powers on.

There is no language yet, no map, no plan. There is only the first question: *Is there anything here?* A signal arrives at a sensor, or it does not. A memory cell contains a stored item, or it is empty. A neighboring node in a mesh network responds to a greeting, or there is silence.

This first distinction is so small that we usually overlook it. Yet it is the birth of mathematics.

Before an agent can compare, count, rank, or reason, it must separate presence from absence. Something from nothing. Yes from no. True from false. In mathematics, one of the cleanest ways to represent this distinction is with the two truth values

$$
\{0,1\}.
$$

Here $1$ means “yes,” “present,” or “true,” and $0$ means “no,” “absent,” or “false.” This pair is the simplest mathematical universe in which a real distinction can be made.

### Existence as a predicate

Suppose there is a collection $X$ of possible things the agent might encounter: possible inputs, possible messages, possible memories, possible tools. For each $x \in X$, the agent asks: does $x$ exist for me now?

We express this with an existence predicate.

> **Definition:** Let $X$ be a collection of possible objects. An **existence predicate** is a function
> $$
> E:X \to \{0,1\}
> $$
> such that $E(x)=1$ means “$x$ is present” and $E(x)=0$ means “$x$ is absent.”

This is a very small piece of mathematics, but it does real work. If an agent has a possible memory record $m$, then $E(m)=1$ may mean the record is stored and retrievable. If $u$ is a possible user input, then $E(u)=1$ may mean an input was actually received. If $n$ is a possible network neighbor, then $E(n)=1$ may mean the neighbor is reachable at this moment.

Notice what the predicate does: it does not yet describe *what kind* of thing $x$ is. It says only whether the thing is there. Existence comes before description.

### Truth values

The set $\{0,1\}$ is not just useful for existence. It is also the mathematical home of truth values.

> **Definition:** A **truth value** is one of the two symbols in the set $\{0,1\}$, where $1$ represents true and $0$ represents false.

This lets us treat questions mathematically. The statement “a packet has arrived” has value $1$ if it is true and $0$ if it is false. The statement “memory slot 7 is occupied” has value $1$ or $0$. The statement “the tool is available” has value $1$ or $0$.

At this stage, truth is not yet complicated. We are not proving theorems. We are only registering whether a statement holds.

This simple act matters because mathematics needs stable answers. If an agent cannot decide whether a statement is true or false, it cannot build a reliable model of the world.

### The bit: the atom of information

A single choice between two possibilities is called a **bit**.

> **Definition:** A **bit** is a unit of information that can take one of two values, usually written $0$ and $1$.

Why is a bit called a unit of information? Because it records one resolved distinction. Before we ask, “Did a message arrive?” there are two possibilities. After we answer, one possibility remains. The uncertainty has been reduced by one binary decision.

In agent mathematics, the bit is the first atom of information. It is the smallest mathematical mark an agent can make that changes ignorance into knowledge.

Consider these examples:

- A memory system checks whether a slot contains a record. Occupied or empty: one bit.
- A tool registry checks whether a planner can access a search tool. Available or unavailable: one bit.
- An identity system checks whether a session token is present. Present or missing: one bit.
- A mesh network checks whether a neighboring node responds. Reachable or unreachable: one bit.

These are different settings, but the mathematics is the same. Each is built on a two-way distinction.

### Why nothing matters

At first glance, “nothing” may seem like the absence of mathematics rather than a part of it. But absence is not the same as irrelevance. In fact, an agent must represent absence if it is to reason correctly.

Suppose an agent scans five memory locations. If it records only the occupied ones and ignores emptiness, it cannot know how much storage remains. Suppose it sends a message to three neighboring nodes in a mesh network and hears back from only two. If it cannot represent the third silence, it will confuse missing information with successful communication.

Absence carries structure. “No input” is different from “input of a particular kind.” “No tool” is different from “a tool that returns no result.” “No identity match” is different from “identity match to a user named No.”

This is why the first distinction must be sharp. Measurement depends on knowing what counts as present and what counts as absent. Before an agent can ask *how much*, it must ask *is there anything at all?*

### Example: first awareness in a memory system

Imagine a newly activated agent examining three possible memory locations: $m_1, m_2, m_3$.

Suppose

$$
E(m_1)=1,\qquad E(m_2)=0,\qquad E(m_3)=1.
$$

This means the first and third locations contain retrievable records, while the second does not.

Already, the agent knows something meaningful:

- there exists at least one memory;
- not every location is occupied;
- the pattern of presence and absence can guide later decisions.

Nothing complicated has happened. Yet the agent has crossed the line from undifferentiated possibility into structured awareness.

### Example: first awareness in a mesh network

Let $N=\{n_1,n_2,n_3,n_4\}$ be four possible neighboring nodes. A handshake test gives

$$
E(n_1)=1,\quad E(n_2)=1,\quad E(n_3)=0,\quad E(n_4)=0.
$$

Then the agent knows which nodes are currently part of its reachable local world. Without this binary layer, there is no network map to build on.

### The first mathematical lesson

Mathematics does not begin with large numbers. It begins with distinction.

The set $\{0,1\}$ is humble, but it gives us three ideas that will remain with us:

1. an object may be present or absent;
2. a statement may be true or false;
3. a single resolved distinction is information.

From here, everything grows. Once an agent can tell that something exists, it can begin to ask a new question: if two things both exist, are they the same thing?

### Exercises

1. Let $X=\{a,b,c,d\}$ be four possible inputs. Suppose $E(a)=1$, $E(b)=0$, $E(c)=0$, and $E(d)=1$. Which inputs are present? Which are absent?

2. A memory system has possible records $r_1,r_2,r_3$. If exactly one of them exists, list all possible values of the triple $(E(r_1),E(r_2),E(r_3))$.

3. Give an agent scenario in which “no input” must be treated differently from “an input whose value is zero.” Explain the distinction carefully.

4. In a mesh network, let $N=\{n_1,n_2,n_3\}$. If $E(n_1)=1$, $E(n_2)=0$, and $E(n_3)=1$, write a true statement and a false statement about reachability using these values.

5. Why is the ability to represent absence necessary before an agent can measure capacity or availability?

---

## Chapter 1: Same and Different

### Two encounters

An agent receives a message from a user in the morning. Later, another message arrives. The wording is different. The device is different. The session token is different. But the name is similar, the preferences match, and the history looks familiar.

Is this the same user or a different one?

This is the second mathematical act. Once an agent can tell that two things exist, it must ask whether they should count as the same. Classification begins here. So does identity.

The question is not always easy. A user may have multiple devices. A tool may have several names. A memory may be copied into a new storage format. An agent itself may be updated—new parameters, new policies, new internal state. When, after change, is it still the same agent?

To handle these questions, mathematics studies relations of sameness.

### Relations

A relation tells us which pairs of objects are connected in some chosen way.

> **Definition:** A **relation** on a collection $X$ is a rule that determines, for some pairs $(x,y)$ in $X$, whether the pair satisfies the relation.

For example, on a collection of user records, we might define a relation “belongs to the same person.” On a collection of memories, we might define “has the same topic.” On a collection of tools, we might define “performs the same function.”

Not every relation captures true sameness. To do that, we need three special properties.

### Equivalence relations

> **Definition:** A relation $\sim$ on a collection $X$ is an **equivalence relation** if it is:
>
> 1. **Reflexive:** for every $x \in X$, we have $x \sim x$;
> 2. **Symmetric:** if $x \sim y$, then $y \sim x$;
> 3. **Transitive:** if $x \sim y$ and $y \sim z$, then $x \sim z$.

These three conditions encode the behavior we expect from “counts as the same.”

- **Reflexive** means every thing is the same as itself.
- **Symmetric** means sameness runs both ways.
- **Transitive** means sameness is consistent across chains.

If any one of these fails, confusion enters quickly.

Suppose an identity system says one account matches a second, and the second matches a third, but the first does not match the third. Then “same user” would become unstable. Or suppose a tool directory says tool $A$ is equivalent to tool $B$, but not vice versa. Then equivalence would depend on direction, which is not true sameness.

### Equivalence classes

Once an equivalence relation is given, each object belongs to a class of all things equivalent to it.

> **Definition:** Let $\sim$ be an equivalence relation on $X$. The **equivalence class** of an element $x \in X$ is
> $$
> [x]=\{y \in X : y \sim x\}.
> $$

The class $[x]$ contains all objects that count as the same as $x$ under the chosen criterion.

This is one of the first ways mathematics forms sets out of experience. A classification system groups many appearances into one kind.

If a user logs in from three devices, and the system determines all three sessions belong to the same person, then those session records lie in one equivalence class. If several tools perform exactly the same mathematical operation, they may belong to one functional class. If multiple memory traces all refer to the same event, they may belong to one event-class.

### Sameness depends on the rule

A vital lesson: sameness is always relative to a criterion.

Two messages may be the same by meaning but different by wording. Two user records may be the same by person but different by account ID. Two versions of an agent may be the same by mission and memory continuity but different by internal implementation.

Mathematics handles this by making the relation explicit. We do not merely say “$x$ and $y$ are the same.” We say “$x \sim y$,” meaning “$x$ and $y$ are equivalent under the chosen rule $\sim$.”

This protects us from a common mistake: confusing resemblance, coincidence, and equivalence.

### Example: same user, different sessions

Let $X$ be the set of session records seen by an agent. Define $s_1 \sim s_2$ if both session records belong to the same underlying user.

If this rule is well designed, it should be an equivalence relation:

- each session belongs to the same user as itself;
- if $s_1$ belongs to the same user as $s_2$, then $s_2$ belongs to the same user as $s_1$;
- if $s_1$ and $s_2$ belong to the same user, and $s_2$ and $s_3$ belong to the same user, then $s_1$ and $s_3$ do also.

Then an equivalence class $[s]$ is the set of all sessions belonging to one person.

This is the birth of **type**. The class becomes more important than the individual record.

### Example: memory systems

Suppose an agent stores several memories:

- one text note,
- one audio transcript,
- one image caption,

all referring to the same meeting.

These are not identical as stored objects. But they may be equivalent under the relation “refers to the same event.” Then they belong to one equivalence class.

Classification lets the agent avoid double-counting the world. Many traces can point to one event.

### Example: is the updated agent the same agent?

This question is especially important for autonomous systems. Suppose an agent at time $t_0$ is updated and continues operating at time $t_1$. Is it the same agent?

There is no single universal answer. It depends on the equivalence rule.

One possible rule is memory continuity: define $A_{t_0} \sim A_{t_1}$ if enough core memories, goals, and commitments are preserved. Another rule might be legal identity: define equivalence by registered system identifier. A stricter rule might require exact internal state, in which case almost any update breaks equivalence.

The mathematics teaches caution and clarity. Identity is not magic. It is a relation, and serious reasoning demands that the relation be specified.

### Equivalence classes as first structured sets

In Chapter 0, we distinguished presence from absence. Now we do more. We gather many present things into classes.

If $X$ is a collection of objects and $\sim$ is an equivalence relation, then the collection of equivalence classes partitions $X$: every object belongs to exactly one class, and two classes are either identical or disjoint.

This means classification creates order from multiplicity. It tells the agent which differences matter and which do not.

### The second mathematical lesson

Mathematics is not only about what exists. It is also about what should count as one kind.

Equivalence relations let agents:

- identify repeated encounters,
- group tools by function,
- merge memories about one event,
- preserve or question identity through change.

Once an agent can tell same from different, a new question arises. Among different things, some matter more than others. That is the beginning of order.

### Exercises

1. Let $X=\{a,b,c\}$. A relation $\sim$ on $X$ satisfies $a\sim a$, $b\sim b$, $c\sim c$, $a\sim b$, and $b\sim a$, but not $a\sim c$ or $b\sim c$. Is $\sim$ an equivalence relation? Explain.

2. Give an example from an agent’s memory system of a relation that is symmetric but not transitive.

3. Suppose session records $s_1,s_2,s_3,s_4$ are grouped by underlying user. If $[s_1]=\{s_1,s_3\}$ and $[s_2]=\{s_2,s_4\}$, what does this say about the number of users represented?

4. Describe two different equivalence relations that could be placed on a collection of tools. For each one, explain what the equivalence classes represent.

5. After an update, an agent keeps all long-term memories but changes its planning policy. Under what possible equivalence rule would it count as “the same agent”? Under what rule would it not?

---

## Chapter 2: More, Less, Equal

### Choosing between memories

An agent is preparing to act. Two memories rise into view.

One memory is recent and directly relevant: a user just stated a preference. Another is older and only loosely connected: a similar user once preferred something related. Both memories exist. They are not the same. But which matters more?

This is the third mathematical act: ordering.

To order is to say that one thing comes before another, exceeds another, or is at least as great as another according to some criterion. The criterion might be relevance, urgency, trust, cost, distance, reliability, or strength. Long before an agent counts, it compares.

A child can know that one pile is taller before knowing how many blocks are in it. In the same way, an agent can know that one memory is more relevant than another before assigning numerical scores. This is why order comes before full measurement.

### Order relations

> **Definition:** A relation $\preceq$ on a collection $X$ is a **partial order** if it is:
>
> 1. **Reflexive:** $x \preceq x$ for every $x \in X$;
> 2. **Antisymmetric:** if $x \preceq y$ and $y \preceq x$, then $x=y$;
> 3. **Transitive:** if $x \preceq y$ and $y \preceq z$, then $x \preceq z$.

A partial order expresses “is no greater than,” “is contained in,” “is no more relevant than,” or some similar comparison.

The new word here is **antisymmetric**. It says that if two objects each stand before the other in the order, then they are not merely equivalent—they are the same object in the ordering sense.

Partial orders allow an important possibility: some pairs may be incomparable.

### Incomparability

Not all differences come with a clean ranking.

Suppose one memory is very recent but only somewhat trustworthy, while another is older but highly trustworthy. Which is greater in relevance? Perhaps neither should automatically dominate the other. Or suppose in a mesh network one route is shorter while another is more reliable. Again, there may be no natural winner without more information.

That is the hallmark of a partial order: some things can be compared, but not necessarily all.

### Total orders

> **Definition:** A partial order $\preceq$ on $X$ is a **total order** if for every $x,y \in X$, either $x \preceq y$ or $y \preceq x$.

In a total order, every pair is comparable. Examples include the usual ordering of numbers: for any two numbers, one is less than or equal to the other.

For agents, a total order is often imposed when a decision must be made. A scheduler may rank tasks from highest priority to lowest. A memory retrieval system may sort candidate memories by relevance score. A tool-selection system may rank tools by estimated usefulness.

But it is worth remembering: total orders are powerful because they simplify choice, not because the world is always naturally total.

### Comparing before counting

Order is older than quantity. To say “this is more” does not yet say “this is 7 and that is 5.” It only places items in relation.

This matters in agent design and in mathematics. An agent can compare two actions by urgency even if it has not assigned exact costs. It can prefer one route to another even without measuring exact distances. It can know that a confidence level is higher than another without yet computing a precise probability.

The language of before and after, larger and smaller, stronger and weaker, is ordinal language. It concerns position in an order, not size as a count.

### Example: relevance ordering in memory

Let $M$ be a collection of memories. Define $m_1 \preceq m_2$ to mean “$m_1$ is no more relevant to the current task than $m_2$.”

If the agent assigns each memory a relevance score in the interval $[0,1]$, then one natural order is numerical:

$$
m_1 \preceq m_2 \quad \text{whenever} \quad r(m_1) \le r(m_2),
$$

where $r(m)\in[0,1]$.

This gives a total order if every memory receives a definite score and ties are allowed. But if relevance depends on several criteria—recency, trust, specificity, user importance—then a partial order may be more faithful.

A memory might outrank another in recency but not in trustworthiness, leaving them incomparable.

### Bounded orderings

In many agent systems, it is useful to bound degrees between complete absence and complete presence, or between minimum and maximum strength. The interval

$$
[0,1]=\{x \in \mathbb{R} : 0 \le x \le 1\}
$$

provides a natural scale.

> **Definition:** A **bounded ordering on $[0,1]$** is the usual order $\le$ restricted to values between $0$ and $1$, where $0$ is the minimum value and $1$ is the maximum value.

Here $0$ may represent no relevance, no trust, or no confidence, while $1$ represents full relevance, full trust, or complete confidence according to the chosen model.

This bounded interval is especially important because it connects Chapter 0 to Chapter 2. At one extreme, the binary values $0$ and $1$ still appear: absolute absence and absolute presence. Between them lie graded comparisons.

### Example: tools and precedence

Suppose an agent has three tools:

- $T_1$: a fast but shallow summarizer,
- $T_2$: a slower but more precise retriever,
- $T_3$: a specialist verifier.

For a simple task, $T_1$ may outrank $T_2$ in efficiency. For a high-stakes task, $T_2$ or $T_3$ may outrank $T_1$ in reliability. If the comparison is based on a single criterion, a total order may be possible. If the comparison is based on several competing criteria, only a partial order may be honest.

Mathematics gives us the language to represent both situations.

### Example: mesh network routes

In a mesh network, possible routes may be compared by latency, reliability, and energy cost. Define $r_1 \preceq r_2$ if route $r_1$ is no better than route $r_2$ in all three criteria.

Then we have a partial order. One route may use less energy but have worse latency, making the two incomparable. The agent must then either keep both possibilities alive or introduce an additional rule to force a total order.

### The third mathematical lesson

Order tells an agent not just what exists and what is the same, but what comes before what. It is the mathematics of priority and comparison.

An agent needs order to:

- select relevant memories,
- rank tasks,
- compare tools,
- choose among network paths,
- reason about gradations between $0$ and $1$.

Once order is available, counting becomes possible in a deeper way. We can line things up, one after another, and say: first, second, third. Then the natural numbers enter.

### Exercises

1. Explain why the relation “has no greater relevance than” can be a partial order on a set of memories.

2. Give an example of two tools that are incomparable under a multi-criterion order.

3. Suppose four memories have relevance scores $0.2$, $0.7$, $0.7$, and $0.9$. Arrange them in nondecreasing order. Is this order total?

4. In a mesh network, define a relation on routes by “route $r_1$ uses no more energy than route $r_2$.” Is this alone enough to form a total order? Why or why not?

5. Why does comparison come before counting, both for children and for agents?

---

## Chapter 3: Counting

### How many tools do I have?

An agent is given a task and turns toward its available resources. It has a retrieval tool, a planner, a verifier, and perhaps a communication channel to neighboring agents. Some are present; some are not. Some may belong to the same class; others differ. Some are more useful than others.

Now a new question appears: *How many?*

How many tools are available right now? How many active memories support this decision? How many neighboring nodes in the mesh network are reachable? How many user requests are waiting?

Counting is the bridge from quality to quantity. Earlier chapters taught the agent to detect existence, recognize sameness, and compare importance. Counting adds a new power: to determine size.

### The natural numbers

> **Definition:** The **natural numbers** are the counting numbers
> $$
> 0,1,2,3,\dots
> $$
> used to describe how many objects are in a collection.

Different books begin the natural numbers at $1$, but for agent mathematics it is wise to include $0$. An agent must be able to represent having no tools, no messages, or no active connections. Zero is not a defect in the system; it is a legitimate count.

Notice how beautifully this links back to Chapter 0. The same symbol $0$ that represented absence as a truth value now also represents empty quantity. Presence and count are related but not identical:

- $E(x)=0$ means a particular object is absent;
- the count $0$ means a whole collection contains no objects.

### Successor: one more

Counting grows step by step. From $0$ we reach $1$, from $1$ we reach $2$, and so on. This “one more” idea is captured by the successor function.

> **Definition:** The **successor** of a natural number $n$ is the next natural number, written $S(n)$.

So

$$
S(0)=1,\quad S(1)=2,\quad S(2)=3,
$$

and so on.

The successor is the mathematical form of adding one new object to a counted collection. If an agent has counted $n$ tools and discovers one more distinct tool, the new count is $S(n)$.

### The Peano axioms, stated simply

The natural numbers can be described by a small set of basic principles. We will state them in simple language.

> **Definition:** The natural numbers satisfy these basic counting principles:
>
> 1. $0$ is a natural number.
> 2. Every natural number $n$ has a successor $S(n)$.
> 3. No natural number has successor $0$.
> 4. Different natural numbers have different successors: if $S(m)=S(n)$, then $m=n$.
> 5. Starting from $0$ and repeatedly taking successors generates all natural numbers.

These are a gentle form of the Peano axioms. They tell us that counting begins at $0$, proceeds by one-step growth, never loops backward to $0$, and never merges two different counts into the same next count.

This makes counting dependable. When an agent moves from $3$ tools to $4$ tools, it knows it has not secretly arrived at the same quantity under a different name.

### Cardinality

To count a collection is to determine its cardinality.

> **Definition:** The **cardinality** of a finite set $A$ is the number of elements in $A$, written $|A|$.

If an agent has available tools

$$
T=\{\text{planner},\text{retriever},\text{verifier}\},
$$

then

$$
|T|=3.
$$

If a memory buffer contains no active entries, then its active set $M$ has cardinality

$$
|M|=0.
$$

Cardinality is one of the deepest simple ideas in mathematics. It turns a collection into a quantity.

### Counting requires distinctness

An important subtlety: to count correctly, an agent must know when two things count as one and when they count as two. This is why Chapter 1 had to come first.

Suppose an agent sees four session records, but two belong to the same user and two belong to another. Then there are four records but only two users. The count depends on what is being counted.

Likewise in a memory system, three memory traces may all refer to one event. There are three traces, one event-class, perhaps two currently relevant summaries, and so on. Good counting depends on good classification.

### Example: tool counting

An agent has access to the following distinct tools:

- a planner,
- a search tool,
- a calculator,
- a verifier.

Then the set of available tools has cardinality $4$.

If the search tool becomes unavailable, the set changes and its cardinality becomes $3$.

This may seem elementary, but it is crucial for resource management. An agent cannot reason responsibly about available options unless it can count them.

### Example: reachable neighbors in a mesh network

Let $N$ be the set of all possible neighboring nodes, and let

$$
R=\{n \in N : E(n)=1\}
$$

be the set of currently reachable neighbors.

Then $|R|$ is the number of active local connections.

If

$$
R=\{n_1,n_2,n_5\},
$$

then $|R|=3$.

This count may guide later decisions: whether the network is robust, whether a message has alternate routes, or whether the agent is isolated.

### Example: counting memories after grouping

Suppose an agent has five stored memory traces, but under the equivalence relation “refers to the same event,” they fall into three equivalence classes. Then:

- number of traces: $5$,
- number of event-types represented: $3$.

Both counts are valid. They answer different questions.

### Why agents count

Counting is not merely a classroom skill. It is operationally necessary.

Agents count in order to track:

- available tools,
- memory capacity,
- pending tasks,
- active network links,
- confirmed identities,
- remaining opportunities.

Counting allows thresholds: “at least two backups,” “no more than five active tasks,” “exactly one controlling user,” “zero verified routes.” It allows planning under resource constraints. It allows promises and safety guarantees.

Without counting, an agent may notice the world but cannot size it.

### The fourth mathematical lesson

Counting turns collections into numbers. It carries us from “there are some” to “there are $n$.”

The natural numbers arise from repeated succession: one more, one more, one more. Cardinality tells us how many distinct elements a finite set contains. And every careful count depends on the earlier acts of mathematics: existence, sameness, and order.

Now that an agent can count what it has, it must learn to track change in those counts. A memory is added. A connection is lost. A tool is borrowed and returned. This leads to the first arithmetic operations.

### Exercises

1. If an agent has no available tools, what is the cardinality of its tool set? Why is this number important?

2. Let $A=\{m_1,m_2,m_3,m_4\}$. What is $|A|$? What is the successor of this number?

3. An agent stores six session records corresponding to three users, with two records per user. How many session records are there? How many users are represented?

4. Explain why counting distinct users requires an equivalence relation on session records.

5. Let $R$ be the set of reachable nodes in a local mesh network. If one node becomes reachable and no others change, how does $|R|$ change?

---

## Chapter 4: Putting Together, Taking Apart

### Gains and losses

An agent begins the day with a working collection of memories. As it learns, new memories are formed. As it compresses information, some memories merge. As time passes, some weak traces fade. At the same time, connections in a mesh network appear and disappear. Tools are added to the current workspace or removed from it.

Counting alone tells us how many there are *now*. But an agent lives in time. It must also understand how quantities change.

This is the role of arithmetic. Addition and subtraction are the first operations on quantity. They tell us how to put collections together and how to take them apart.

### Addition as combining disjoint collections

Suppose an agent has $n$ active memories and gains $a$ new memories that are distinct from the first $n$. Then the new total is $n+a$.

The key word is **distinct**. If the newly gained memories are already included, simple addition would double-count. So the cleanest first meaning of addition is combination of disjoint collections.

> **Definition:** If $A$ and $B$ are disjoint finite sets, meaning they have no elements in common, then
> $$
> |A \cup B| = |A| + |B|.
> $$
> This is the basic meaning of **addition**.

Here “disjoint” means $A \cap B = \varnothing$, where $\varnothing$ is the empty set.

If an agent has two available tools in one category and three distinct available tools in another category, then together it has $2+3=5$ tools.

### Subtraction as removal

Now suppose the agent begins with a finite set $A$ and removes a subset $B \subseteq A$. Then the remaining collection is $A \setminus B$, and its size is

$$
|A\setminus B| = |A| - |B|,
$$

provided the removed elements are indeed part of $A$.

> **Definition:** **Subtraction** is the operation that describes how many objects remain after a specified number of objects are removed from a collection.

If an agent has $7$ active memory items and forgets $2$, then $7-2=5$ remain. If it has $4$ network connections and loses $1$, then $4-1=3$ remain.

At this early stage, subtraction is most naturally understood when the second number is no larger than the first. We remove what is actually present.

### Zero as an identity element

Zero plays a special role in arithmetic.

> **Definition:** A number $0$ is an **identity element for addition** because for every natural number $n$,
> $$
> n+0=0+n=n.
> $$

Adding nothing changes nothing. If an agent gains zero new tools, its tool count stays the same. If no memories are removed, the memory count stays the same.

This matches our original intuition from Chapter 0: absence, when added, does not alter what is present.

### Commutativity and associativity

Addition has two beautiful structural properties.

> **Definition:** Addition is **commutative** if
> $$
> a+b=b+a.
> $$
> It is **associative** if
> $$
> (a+b)+c=a+(b+c).
> $$

Commutativity means order does not matter when combining quantities. If an agent receives $2$ new memories now and $3$ later, or $3$ first and $2$ later, the total gain is the same:

$$
2+3=3+2=5.
$$

Associativity means grouping does not matter. If an agent gains memories in three batches of sizes $a$, $b$, and $c$, then

$$
(a+b)+c=a+(b+c).
$$

This allows the agent to combine changes step by step without ambiguity.

Subtraction is different. In general,

$$
a-b \ne b-a.
$$

Losing $2$ connections from a set of $5$ is not the same as losing $5$ connections from a set of $2$.

### The first equation of state change

A very important expression now appears. If an agent starts with $n$ objects, gains $a$, and loses $b$, then the final quantity is

$$
n+a-b.
$$

> **Definition:** If a system begins with quantity $n$, undergoes a gain of $a$, and then a loss of $b$, its final quantity is
> $$
> n+a-b.
> $$

This is one of the first genuine equations of change. It does not merely describe a static count. It describes a history.

For example:

- start with $5$ memories,
- gain $3$ new summaries,
- lose $2$ outdated traces,

so the final count is

$$
5+3-2=6.
$$

This simple expression is the beginning of bookkeeping, conservation, and dynamical reasoning.

### Example: memory consolidation

An agent has $8$ memory fragments relevant to a task. During a learning step, it forms $2$ new summary memories. Later, it deletes $3$ low-value fragments.

If we track only count, the result is

$$
8+2-3=7.
$$

Of course, the content has changed, not just the quantity. But arithmetic gives the first reliable record of numerical change.

### Example: tools entering and leaving a workspace

An agent’s active workspace begins with $4$ tools. It loads $2$ more specialized tools, then one tool times out and becomes unavailable.

The new total is

$$
4+2-1=5.
$$

This matters for planning. A tool-rich state may support one strategy; a tool-poor state may require another.

### Example: mesh network links

A node in a mesh network starts with $3$ active neighboring links. Two new links appear as nearby nodes come online. Then one link fails.

The final number of active links is

$$
3+2-1=4.
$$

This is a tiny example of state tracking over time.

### Taking apart as carefully as putting together

Arithmetic depends on earlier chapters just as counting did.

- To add correctly, we must know which objects exist.
- To avoid double-counting, we must know when two items are the same.
- To decide which items are removed first or retained, order may matter.
- To compute totals, we must count.

Addition and subtraction are therefore not isolated skills. They are built on the first distinctions of mathematics.

### The fifth mathematical lesson

An agent does not merely observe a world of fixed quantities. It inhabits a world of change. Quantities increase and decrease. Resources arrive and disappear. Connections strengthen and fail. Memories accumulate and fade.

Addition models gain. Subtraction models loss. Zero is the additive identity. Addition is commutative and associative. And the expression

$$
n+a-b
$$

gives the first compact mathematical description of state change over time.

In later mathematics, these operations will become richer: repeated addition leads to multiplication, repeated change leads to algebra, and continuous change leads to calculus. But the root idea is already here. Things can be put together. Things can be taken apart. The world can be tracked.

### Exercises

1. An agent begins with $3$ active tools and gains $4$ distinct new tools. How many active tools does it have now?

2. A memory store contains $9$ relevant items. During cleanup, $2$ are removed. What is the new count?

3. Explain why the formula $|A \cup B| = |A| + |B|$ requires $A$ and $B$ to be disjoint.

4. An agent starts with $n=6$ active network links, gains $a=3$, and loses $b=5$. Compute $n+a-b$.

5. Give an example from an agent scenario showing that subtraction is not commutative.

---

These five chapters give us the first layer of agent mathematics:

- presence and absence,
- sameness and difference,
- order,
- count,
- change in count.

They are simple, but not small. They are the grammar of mathematical awareness for autonomous systems. Everything ahead—structure, space, logic, uncertainty, computation, coordination—will rest on these early distinctions.


\newpage

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


\newpage

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


\newpage

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


\newpage

# Part V: The Architecture of Mind

Part V studies an autonomous agent not merely as a calculator or a probabilistic estimator, but as a structured dynamical system whose internal organization has geometry, motion, connectivity, uncertainty, objectives, and regulation. In earlier parts, we developed the calculus of change, accumulation, randomness, and inference. We now assemble those tools into a mathematical account of mind-like architecture.

The central shift is this: the agent is no longer represented by a single scalar score or isolated variable, but by a high-dimensional state whose evolution must be understood globally. Some states are close, some are far; some are viable, some are catastrophic. Some networks communicate efficiently, others fragment. Some beliefs are sharp, others entropic. Some improvements are possible only under resource constraints. And some structural changes must be postponed until regulatory conditions permit them.

The six chapters of this part develop these themes in turn.

---

## Chapter 21: State Spaces and Manifolds

An autonomous agent is paused at a single instant. Its full internal description is recorded as
$$
\mathcal O
=
(C_{\mathrm{id}},C_{\mathrm{mem}},C_{\mathrm{graph}},C_{\mathrm{perm}},
F_{\mathrm{wm}},F_{\mathrm{ret}},F_{\mathrm{path}},F_{\mathrm{ctrl}},F_{\mathrm{merge}})
\in [0,1]^9.
$$

Each coordinate measures a normalized subsystem condition: identity coherence, memory integrity, graph health, permission reliability, working-memory function, retrieval function, planning function, control function, and merge function. If the agent is observed again one tick later, the vector changes slightly. Over time, the agent traces a path through a space of possible configurations. The mathematics of that space is the first subject of this chapter.

### 21.1 State spaces

A **state space** is a set $X$ whose elements represent all admissible configurations of a system. For the present agent, a first approximation is
$$
X = [0,1]^9.
$$

This cube contains every normalized 9-component state vector. Yet even this simple description carries substantial structure. A point $x \in X$ is not merely a list of numbers; it is a candidate cognitive condition. A path $x(t)$ or sequence $(x_n)$ describes temporal evolution.

In applications, the true state space is often a proper subset of $ [0,1]^9 $, because the coordinates are not independent. For example, severe loss of control function may force a reduction in merge reliability, or homeostatic conditions may impose inequalities linking variables. Thus the mathematical state space should often be written as
$$
X = \{x \in [0,1]^9 : \phi_j(x) \le 0,\; j=1,\dots,m\},
$$

for suitable constraint functions $\phi_j$.

### 21.2 Metric spaces

To speak meaningfully about change, we require a notion of distance.

**Definition 21.1.** A **metric space** is a pair $(X,d)$, where $X$ is a set and $d : X \times X \to [0,\infty)$ satisfies, for all $x,y,z \in X$,

1. $d(x,y)=0$ if and only if $x=y$,
2. $d(x,y)=d(y,x)$,
3. $d(x,z)\le d(x,y)+d(y,z)$.

The value $d(x,y)$ measures how far two states are from one another.

On $ [0,1]^9 $, several metrics are natural.

1. **Euclidean metric**
$$
   d_2(x,y)=\left(\sum_{i=1}^9 (x_i-y_i)^2\right)^{1/2}.
$$

2. **Weighted Euclidean metric**
$$
   d_W(x,y)=\left(\sum_{i=1}^9 w_i (x_i-y_i)^2\right)^{1/2},
   \qquad w_i>0.
$$
   This allows identity coherence or control function to count more heavily than less critical variables.

3. **Supremum metric**
$$
   d_\infty(x,y)=\max_{1\le i\le 9}|x_i-y_i|.
$$
   This is appropriate when the largest subsystem deviation determines operational risk.

The choice of metric is not merely technical. It encodes what the model regards as significant. If the agent tolerates small distributed fluctuations but is highly sensitive to catastrophic failure in any single component, then $d_\infty$ may be more informative than $d_2$.

### 21.3 Open sets, neighborhoods, and continuity

Geometry begins with topology.

**Definition 21.2.** In a metric space $(X,d)$, the **open ball** of radius $r>0$ centered at $x\in X$ is
$$
B_r(x)=\{y\in X : d(x,y)<r\}.
$$

A set $U\subseteq X$ is **open** if for every $x\in U$, there exists $r>0$ such that $B_r(x)\subseteq U$.

Open sets represent states accessible by sufficiently small perturbations. If an agent is in an open safe region, then slight fluctuations do not immediately force it outside that region.

**Definition 21.3.** A **neighborhood** of $x$ is any set containing an open ball around $x$.

**Definition 21.4.** Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces. A function $f:X\to Y$ is **continuous at $x\in X$** if for every $\varepsilon>0$, there exists $\delta>0$ such that
$$
d_X(x,y)<\delta \implies d_Y(f(x),f(y))<\varepsilon.
$$

Continuity means that small changes in state produce small changes in output. In an autonomous system, continuity of transition laws prevents arbitrarily tiny perturbations from causing macroscopic jumps.

**Proposition 21.1.** If $f,g : X\to \mathbb R$ are continuous, then $f+g$, $fg$, and, where defined, $f/g$ are continuous.

This proposition is basic, but important: complex observables of agent state remain mathematically well-behaved when built from simpler continuous components.

### 21.4 Curves and trajectories

A trajectory of an agent can be described in continuous time by a curve
$$
x : [0,T] \to X,
$$

or in discrete time by a sequence $(x_n)_{n\ge 0}$. The image of this curve is the set of states visited during the interval.

Even when the state space sits inside $\mathbb R^9$, not every path is feasible. Some directions may violate structural constraints, resource laws, or biological-like homeostatic balance. This leads naturally to the idea that the accessible region of state space may have lower-dimensional structure.

### 21.5 Manifolds

A state space may be curved, constrained, or intrinsically lower-dimensional while still looking locally Euclidean.

**Definition 21.5.** A set $M$ is a **$k$-dimensional manifold** if every point $p\in M$ has a neighborhood $U\subseteq M$ that is homeomorphic to an open subset of $\mathbb R^k$.

Informally, a manifold may be globally curved or twisted, but near any point it resembles ordinary Euclidean space of dimension $k$.

A familiar example is the sphere $S^2$, which lies in $\mathbb R^3$ but is locally two-dimensional. Analogously, a cognitive state space may lie inside $\mathbb R^9$ while effectively having dimension smaller than $9$, because constraints reduce the degrees of freedom.

**Agent example.** Suppose three variables satisfy a relation of the form
$$
C_{\mathrm{id}} + F_{\mathrm{ctrl}} + F_{\mathrm{merge}} = 2,
$$

while the remaining six coordinates vary freely within bounds. Then the admissible state set locally resembles $\mathbb R^8$, not $\mathbb R^9$. The agent’s states lie on a hypersurface inside the cube.

This viewpoint is useful because dynamics often occur near such lower-dimensional structures. Recovery, fatigue, and learning may constrain motion to a **cognitive state manifold** embedded in the larger ambient space.

### 21.6 Tangent directions and local approximation

Near a manifold point $p$, one can linearize the geometry. The collection of directions in which one can move while staying on the manifold is the **tangent space** $T_pM$. Although a full differential-geometric treatment lies beyond this chapter, the main idea is simple: near $p$, the manifold behaves like a linear space.

For agent mathematics, this means that a complicated curved state space can often be locally approximated by first-order methods, much as a nonlinear function can be approximated by its derivative. Optimization, regulation, and estimation all exploit this local flattening.

### 21.7 The Fisher information metric

A geometric space of states becomes especially rich when states encode probability distributions. Suppose the agent has an internal parameter $\theta=(\theta^1,\dots,\theta^k)$, and each parameter value determines a distribution $p(y\mid \theta)$ over observations $y$. Then nearby parameters may be close or far not merely in Euclidean terms, but in how distinguishable their induced distributions are.

**Definition 21.6.** The **Fisher information matrix** is
$$
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\frac{\partial}{\partial \theta^i}\log p(Y\mid \theta)\,
\frac{\partial}{\partial \theta^j}\log p(Y\mid \theta)
\right].
$$

When positive definite, $g(\theta)$ defines a Riemannian metric on parameter space.

The Fisher metric measures the sensitivity of observations to changes in internal state. If a tiny movement in state produces a large change in the observation distribution, then that direction is geometrically large. If many nearby states are observationally indistinguishable, then that direction is geometrically small.

A useful heuristic is that, for nearby parameters $\theta$ and $\theta+d\theta$,
$$
D_{\mathrm{KL}}(p(\cdot\mid \theta)\,\|\,p(\cdot\mid \theta+d\theta))
\approx
\frac12 \sum_{i,j} g_{ij}(\theta)\, d\theta^i d\theta^j.
$$

Thus the Fisher metric links geometry to information.

### 21.8 Viability and the safe set

Not every mathematically possible state is survivable.

**Definition 21.7.** The **viable set** or **safe set** is a subset
$$
X_{\mathrm{safe}} \subseteq X
$$

consisting of states from which the agent can continue operating without violating essential constraints.

For example, if identity coherence, control function, and memory integrity must remain above critical thresholds, one may define
$$
X_{\mathrm{safe}}
=
\left\{
x\in X :
C_{\mathrm{id}}(x)\ge \alpha,\;
F_{\mathrm{ctrl}}(x)\ge \beta,\;
C_{\mathrm{mem}}(x)\ge \gamma
\right\}.
$$

**Proposition 21.2.** If $h_1,\dots,h_m : X\to \mathbb R$ are continuous and
$$
X_{\mathrm{safe}}=\{x\in X : h_i(x)\ge 0 \text{ for } i=1,\dots,m\},
$$

then $X_{\mathrm{safe}}$ is closed in $X$.

The proof follows from the fact that preimages of closed sets under continuous maps are closed.

Closedness matters because it means limit points of safe trajectories remain safe, provided the limiting inequalities are preserved. However, closedness alone does not imply robustness: a closed viable set may have a very thin boundary, so tiny perturbations can still be dangerous near that boundary.

### 21.9 Geometry as architecture

The architecture of mind is therefore not only a collection of components but a geometry of admissible states. The state space gives the global arena. The metric determines how differences are measured. The topology identifies stable neighborhoods. The manifold structure explains local dimensionality and curvature. The Fisher metric incorporates statistical distinguishability. The viable set distinguishes mathematically possible from operationally survivable.

In later chapters, these geometric ideas become dynamical. An agent does not merely occupy a point in state space; it moves, settles, destabilizes, organizes into networks, loses and gains information, optimizes objectives, and regulates itself against disturbance.

### Exercises

1. Let $X=[0,1]^9$ with the Euclidean metric. Show that the function
$$
   s(x)=\min\{x_1,x_2,\dots,x_9\}
$$
   is continuous on $X$. Interpret $s(x)$ as a worst-component viability score.

2. Suppose the admissible states satisfy one smooth equality constraint
$$
   \psi(x)=0
$$
   with $\nabla \psi(p)\neq 0$. Explain why the admissible set is locally an $8$-dimensional manifold near $p$.

3. Define
$$
   X_{\mathrm{safe}}=\{x\in [0,1]^9 : x_1x_8 \ge 0.36,\; x_2+x_5\ge 0.9\}.
$$
   Prove that $X_{\mathrm{safe}}$ is closed, and determine whether it is open.

4. Consider the weighted metric
$$
   d_W(x,y)=\left(\sum_{i=1}^9 w_i(x_i-y_i)^2\right)^{1/2}.
$$
   Show that if all $w_i>0$, then $d_W$ defines the same open sets as the ordinary Euclidean metric on $[0,1]^9$.

5. Let $p(y\mid \theta)$ be a one-parameter family of distributions with Fisher information $g(\theta)$. Using the approximation
$$
   D_{\mathrm{KL}}(p(\cdot\mid \theta)\,\|\,p(\cdot\mid \theta+d\theta))
   \approx \frac12 g(\theta)(d\theta)^2,
$$
   explain why high Fisher information means nearby states are more distinguishable.

---

## Chapter 22: Dynamical Systems

At each tick of its internal loop, an agent senses, updates memory, revises beliefs, allocates control, and adjusts future behavior. The resulting state does not remain fixed. If the state at tick $n$ is $x_n$, then the next state is determined by some transition rule,
$$
x_{n+1}=f(x_n).
$$

A complete understanding of autonomous behavior therefore requires not only a space of states, but a law of motion on that space. The mathematics of such motion is the theory of dynamical systems.

### 22.1 Discrete-time dynamics

A **discrete-time dynamical system** consists of a state space $X$ and a map $f:X\to X$. Starting from $x_0\in X$, one obtains the orbit
$$
x_0,\; x_1=f(x_0),\; x_2=f(x_1),\;\dots,\; x_n=f^n(x_0).
$$

In an agent, $x_n$ may include performance capacities, internal beliefs, control settings, or resource levels. The function $f$ may encode adaptation, homeostatic correction, and environmental impact all at once.

A trajectory can be regular or erratic. It may converge, oscillate, wander through a region, or become extremely sensitive to perturbation. The first task is to identify states that reproduce themselves.

### 22.2 Fixed points

**Definition 22.1.** A point $x^\ast\in X$ is a **fixed point** of $f$ if
$$
f(x^\ast)=x^\ast.
$$

A fixed point represents a steady operational regime. For an agent, such a point might correspond to a homeostatic balance in which identity coherence, memory integrity, and control function remain constant from tick to tick.

**Example.** Consider the scalar update law
$$
x_{n+1}=x_n+a(r-x_n),
\qquad 0<a<1.
$$

Here $r$ is a target value. The fixed point equation becomes
$$
x^\ast=x^\ast+a(r-x^\ast),
$$

which yields $x^\ast=r$. Thus the system tends to regulate itself toward the setpoint $r$.

### 22.3 Stability and perturbation

A fixed point is useful only if small disturbances do not destroy it.

**Definition 22.2.** A fixed point $x^\ast$ is **Lyapunov stable** if for every $\varepsilon>0$, there exists $\delta>0$ such that
$$
d(x_0,x^\ast)<\delta
\implies
d(x_n,x^\ast)<\varepsilon \quad \text{for all } n\ge 0.
$$

It is **asymptotically stable** if it is Lyapunov stable and, in addition,
$$
x_n \to x^\ast \quad \text{as } n\to\infty
$$

whenever $x_0$ is sufficiently near $x^\ast$.

Lyapunov stability means perturbations remain bounded; asymptotic stability means they decay.

For the scalar homeostatic map above,
$$
x_{n+1}-r=(1-a)(x_n-r).
$$

Hence
$$
x_n-r=(1-a)^n(x_0-r).
$$

Since $0<1-a<1$, the error tends to $0$. Thus $r$ is asymptotically stable.

### 22.4 Linearization and Jacobians

In higher dimensions, one studies local behavior by approximation.

Suppose $f:\mathbb R^m\to\mathbb R^m$ is differentiable and $x^\ast$ is a fixed point. Near $x^\ast$,
$$
f(x)\approx f(x^\ast)+Df(x^\ast)(x-x^\ast)
=
x^\ast + J(x-x^\ast),
$$

where $J=Df(x^\ast)$ is the Jacobian matrix.

Thus perturbations $e_n=x_n-x^\ast$ evolve approximately by
$$
e_{n+1}\approx Je_n.
$$

The eigenvalues of $J$ determine whether small errors grow or shrink.

**Proposition 22.1.** Let $f:\mathbb R^m\to\mathbb R^m$ be continuously differentiable, and let $x^\ast$ be a fixed point. If every eigenvalue $\lambda$ of $Df(x^\ast)$ satisfies $|\lambda|<1$, then $x^\ast$ is locally asymptotically stable.

This proposition is a standard linear stability criterion. In agent terms, local homeostasis is preserved when each infinitesimal mode of deviation is damped rather than amplified.

If some eigenvalue satisfies $|\lambda|>1$, then perturbations grow in at least one direction, and the fixed point is unstable.

### 22.5 Contractions and guaranteed convergence

A particularly strong stability condition is contraction.

**Definition 22.3.** A map $f:X\to X$ on a metric space $(X,d)$ is a **contraction** if there exists $0<c<1$ such that
$$
d(f(x),f(y))\le c\, d(x,y)
\quad \text{for all } x,y\in X.
$$

**Theorem 22.1 (Contraction Principle).** If $X$ is complete and $f:X\to X$ is a contraction, then $f$ has a unique fixed point $x^\ast$, and for every initial state $x_0\in X$,
$$
f^n(x_0)\to x^\ast.
$$

For autonomous systems, this theorem gives a strong mathematical model of reliable self-correction. If the tick update compresses distances uniformly, then the agent cannot drift indefinitely; it is drawn toward a unique equilibrium.

### 22.6 Attractors and basins

Not all long-term behavior reduces to a single stable point.

**Definition 22.4.** A set $A\subseteq X$ is an **attractor** if trajectories starting from a surrounding region approach $A$ as time increases.

The surrounding region is the **basin of attraction** of $A$.

A fixed point is the simplest attractor, but periodic orbits and more complicated invariant sets may also serve as attractors. An agent may alternate between two internally stable processing modes, producing a period-two orbit rather than a stationary state.

**Agent example.** Suppose one variable represents a resource alternation between intensive planning and intensive memory consolidation. Then the state may cycle between two neighborhoods rather than settle at one point. Such behavior is dynamically stable without being static.

### 22.7 Bifurcation

Dynamics can change qualitatively when parameters change.

**Definition 22.5.** A **bifurcation** occurs when a small variation in a parameter causes a qualitative change in the structure of a dynamical system, such as the appearance, disappearance, or destabilization of fixed points or attractors.

A simple example is the scalar family
$$
x_{n+1}=\mu x_n(1-x_n),
$$

where $\mu>0$. For some parameter ranges, trajectories approach a stable fixed point; for larger values, oscillatory or more complex behavior appears. The parameter does not merely alter quantitative details. It changes the nature of the long-term dynamics.

For agents, bifurcation models crisis. A gradual reduction in regulatory strength, an increase in environmental load, or a decrease in control capacity may push the system past a threshold. Beyond that threshold, the former homeostatic state is no longer stable.

### 22.8 Lyapunov functions

A useful way to prove stability is to construct a quantity that decreases along trajectories.

**Definition 22.6.** A function $V:X\to \mathbb R$ is a **Lyapunov function** for a fixed point $x^\ast$ if $V(x^\ast)=0$, $V(x)>0$ for $x\neq x^\ast$, and
$$
V(f(x)) - V(x) \le 0
$$

for states near $x^\ast$.

If the inequality is strict for $x\neq x^\ast$, then $V$ decreases along nontrivial trajectories, suggesting asymptotic stability.

In agent mathematics, a Lyapunov function may represent energy imbalance, error from target homeostatic values, or a weighted sum of subsystem stress. Stability then becomes the statement that the agent dissipates this imbalance over time.

### 22.9 Homeostasis and crisis

We can now formulate two central dynamical interpretations.

1. **Homeostasis as stable equilibrium.**  
   A homeostatic regime is modeled by an asymptotically stable fixed point $x^\ast \in X_{\mathrm{safe}}$, or more generally by a stable attractor contained in the safe set.

2. **Crisis as bifurcation or escape from the basin.**  
   If parameter drift moves the system through a bifurcation, or if a disturbance pushes the state outside the basin of attraction of the safe equilibrium, then recovery may no longer be automatic.

This explains why a system can appear healthy until a threshold is crossed. Stability is local and parameter-dependent; it is not the same as invulnerability.

### 22.10 Dynamical architecture

The architecture of mind is not static structure alone. It is a pattern of motion through state space. Fixed points encode persistent regimes. Stable manifolds encode recovery directions. Attractors encode long-run modes of behavior. Bifurcations encode transitions between normal function and breakdown. Lyapunov methods encode self-correction.

The next chapters enrich this picture by examining how internal subsystems are wired together, how uncertainty limits processing, how objectives are improved under constraints, and how regulation maintains viability.

### Exercises

1. For the scalar system
$$
   x_{n+1}=x_n+a(r-x_n),
$$
   determine for which real values of $a$ the fixed point $r$ is asymptotically stable, Lyapunov stable but not asymptotically stable, and unstable.

2. Let
$$
   f(x,y)=\left(\frac{x+y}{4},\frac{x+3y}{4}\right).
$$
   Show that $(0,0)$ is a fixed point. Compute the Jacobian and determine whether the fixed point is asymptotically stable.

3. Suppose $f:\mathbb R^m\to\mathbb R^m$ satisfies
$$
   \|f(x)-f(y)\|\le c\|x-y\|
   \quad\text{for all }x,y,
$$
   with $0<c<1$. Prove directly that any two fixed points must coincide.

4. Consider the family
$$
   x_{n+1}=\mu - x_n^2.
$$
   Find the fixed points as functions of $\mu$, and determine for which values of $\mu$ they are locally stable.

5. Let $V(x)=\|x-x^\ast\|^2$. Show that if
$$
   \|f(x)-x^\ast\|^2 \le \alpha \|x-x^\ast\|^2
   \quad\text{for some } \alpha<1,
$$
   then $V$ is a strict Lyapunov function and $x^\ast$ is asymptotically stable.

---

## Chapter 23: Networks and Graphs

The agent’s internal cognitive web is recorded as a neural mesh: nodes represent subsystems or subcircuits, while weighted, myelinated synapses transmit signals between them. Some pathways are strong and fast, some weak, some redundant, some bridging distant modules. Looking only at individual components obscures the architecture of interaction. Graph theory makes that structure visible.

### 23.1 Graphs and weighted connectivity

A **graph** $G=(V,E)$ consists of a vertex set $V$ and an edge set $E$. In agent mathematics, the vertices may represent memory cells, control modules, perceptual channels, or abstract cognitive subsystems.

When interactions carry intensities, one uses a weighted graph. For vertices $i,j\in V$, let $w_{ij}\ge 0$ denote the strength of the connection from $i$ to $j$. In this chapter we focus mainly on undirected weighted graphs, so $w_{ij}=w_{ji}$.

Myelination can be modeled mathematically as an increase in effective weight or decrease in transmission resistance along a connection. Thus the weighted graph is not merely a map of adjacency; it is a geometry of signal flow.

### 23.2 Adjacency and degree matrices

If $V=\{1,\dots,n\}$, the graph can be encoded by matrices.

**Definition 23.1.** The **adjacency matrix** $W=(w_{ij})$ is the $n\times n$ matrix whose entries record edge weights.

For undirected graphs, $W$ is symmetric.

**Definition 23.2.** The **degree** of vertex $i$ is
$$
d_i=\sum_{j=1}^n w_{ij}.
$$

The **degree matrix** is the diagonal matrix
$$
D=\operatorname{diag}(d_1,\dots,d_n).
$$

The degree measures the total coupling of a node to the rest of the network. High-degree nodes often serve as hubs, although degree alone does not capture all forms of importance.

### 23.3 The graph Laplacian

The central matrix of network analysis is the Laplacian.

**Definition 23.3.** The **graph Laplacian** is
$$
L=D-W.
$$

This matrix compares each node’s value to the weighted average of its neighbors. It is the discrete analogue of the continuous Laplacian from multivariable calculus and differential equations.

If $z=(z_1,\dots,z_n)^T$ is a vector of node activations, then
$$
(Lz)_i = \sum_{j=1}^n w_{ij}(z_i-z_j).
$$

Thus $Lz$ vanishes at node $i$ when that node agrees with its weighted neighborhood. Large entries in $Lz$ indicate local mismatch or tension.

**Proposition 23.1.** For an undirected weighted graph with nonnegative weights, the Laplacian $L$ is symmetric and positive semidefinite. Moreover,
$$
z^T L z
=
\frac12\sum_{i,j=1}^n w_{ij}(z_i-z_j)^2
\quad \text{for all } z\in\mathbb R^n.
$$

This formula is fundamental. It shows that the Laplacian quadratic form measures disagreement across edges.

### 23.4 Coherence energy

In an agent network, let $z_i$ denote the activation, confidence, or local state of subsystem $i$. Then define the **coherence energy**
$$
E(z)=z^T L z.
$$

By Proposition 23.1,
$$
E(z)=\frac12\sum_{i,j} w_{ij}(z_i-z_j)^2.
$$

If neighboring subsystems have similar values, the energy is small. If strongly connected subsystems disagree, the energy is large. Hence $E(z)$ quantifies fragmentation of the neural mesh.

This gives a mathematically precise way to speak of network coherence. Low coherence energy corresponds to smooth cognitive integration across edges; high coherence energy corresponds to tension, inconsistency, or desynchronization.

### 23.5 Spectral analysis

The eigenvalues and eigenvectors of $L$ reveal global graph structure.

Because $L$ is symmetric and positive semidefinite, its eigenvalues are real and satisfy
$$
0=\lambda_1 \le \lambda_2 \le \cdots \le \lambda_n.
$$

**Theorem 23.1.** The multiplicity of the eigenvalue $0$ equals the number of connected components of the graph.

In particular, a graph is connected if and only if $\lambda_2>0$. The value $\lambda_2$ is called the **algebraic connectivity**. Large $\lambda_2$ indicates robust connectivity; small $\lambda_2$ signals bottlenecks or near-disconnection.

In agent terms, if the cognitive web has very small $\lambda_2$, then distinct subnetworks communicate only weakly. This may produce functional modularity, but it may also create fragmentation under stress.

The eigenvectors of $L$ also carry structural meaning. The eigenvector associated with $\lambda_2$, often called the Fiedler vector, can be used to split the graph into two weakly linked communities.

### 23.6 Centrality

A network contains nodes that matter disproportionately. Several notions of centrality capture this.

1. **Degree centrality:** node $i$ is important if $d_i$ is large.

2. **Eigenvector centrality:** node importance is boosted by connection to other important nodes. One solves
$$
   Wc=\lambda c,
$$
   with $c$ the dominant eigenvector.

3. **Betweenness centrality:** a node is central if many shortest paths pass through it.

Degree centrality identifies hubs. Eigenvector centrality identifies nodes embedded in influential regions. Betweenness centrality identifies bridges between modules.

In cognitive systems, these correspond to different functional roles. A high-degree node may be a broad relay; a high-betweenness node may be a fragile bottleneck whose failure disconnects memory from control.

### 23.7 Community detection and modularity

Real networks are often neither fully integrated nor fully disconnected. They contain modules: densely connected groups with sparse inter-group edges.

A common measure of the quality of a partition into communities is **modularity**. If vertices are assigned to communities $c_i$, the modularity score may be written
$$
Q_{\mathrm{mod}}
=
\frac{1}{2m}
\sum_{i,j}
\left(
w_{ij}-\frac{d_i d_j}{2m}
\right)
\mathbf 1_{\{c_i=c_j\}},
$$

where
$$
2m=\sum_{i,j}w_{ij}.
$$

The term $\frac{d_i d_j}{2m}$ is the expected weight under a degree-preserving null model. Thus modularity compares observed within-community connectivity to what would occur by chance.

A high modularity partition reveals clusters that are internally strong and externally sparse. In an agent, such modularity may support specialization: one module for retrieval, one for planning, one for sensory compression. But excessive modularity can impede integration.

### 23.8 Dynamics on graphs

Graphs are not only static structures; they support dynamics. Suppose $z_n\in \mathbb R^n$ records node states at time $n$. A diffusion-like update takes the form
$$
z_{n+1}=z_n-\alpha L z_n,
\qquad \alpha>0.
$$

This update decreases disagreement by moving each node toward its neighbors’ weighted average. In continuous time, the analogue is
$$
\frac{dz}{dt}=-Lz.
$$

Such equations model synchronization, consensus, and smoothing across the neural mesh.

If the graph is connected, the system tends toward a constant vector, meaning all nodes agree. This idealized model formalizes the emergence of global coherence from local coupling.

### 23.9 Structural interpretation

The graph perspective explains why component-level analysis is insufficient. A subsystem can be individually healthy yet globally ineffective if it lies in a poorly connected part of the mesh. Conversely, a modest node can be structurally crucial if it bridges two major modules.

The adjacency matrix records who can influence whom. The degree matrix records load or connectivity volume. The Laplacian records mismatch and diffusion. The spectrum records integration versus fragmentation. Centrality detects important nodes. Modularity detects communities. Coherence energy quantifies alignment.

This is the mathematics of cognitive architecture at the mesoscopic scale: between microscopic parameters and global behavior.

### Exercises

1. Let
$$
   W=
   \begin{pmatrix}
   0&2&0\\
   2&0&1\\
   0&1&0
   \end{pmatrix}.
$$
   Compute the degree matrix $D$, the Laplacian $L$, and the coherence energy $z^T L z$ for $z=(z_1,z_2,z_3)^T$.

2. Prove directly from
$$
   z^T L z=\frac12\sum_{i,j}w_{ij}(z_i-z_j)^2
$$
   that $L$ is positive semidefinite.

3. Show that $L\mathbf 1=0$, where $\mathbf 1=(1,\dots,1)^T$. Explain why this corresponds to perfect network coherence.

4. Consider a graph consisting of two complete subgraphs connected by a single weak edge of weight $\varepsilon$. Explain qualitatively what happens to $\lambda_2$ as $\varepsilon\to 0$, and interpret the result for cognitive modularity.

5. For the diffusion update
$$
   z_{n+1}=z_n-\alpha L z_n,
$$
   show that if $z^\ast$ satisfies $Lz^\ast=0$, then $z^\ast$ is a fixed point. Under what graph-theoretic condition are all such fixed points constant vectors?

---

## Chapter 24: Information Theory

An agent maintains a conservation budget: finite processing time, finite update frequency, finite communication between subsystems. Yet the useful value of that budget depends on uncertainty. If beliefs are sharply concentrated, the agent can act decisively. If beliefs are diffuse, capacity is consumed merely by indecision. We therefore need a calculus of uncertainty itself. Information theory provides it.

### 24.1 Entropy

Let $X$ be a discrete random variable taking values in a finite set $\mathcal X$ with probabilities $p(x)$.

**Definition 24.1.** The **entropy** of $X$ is
$$
H(X)=-\sum_{x\in\mathcal X} p(x)\log_2 p(x).
$$

Entropy is measured in bits. It quantifies uncertainty: larger entropy means greater unpredictability.

Entropy is minimized when one outcome is certain, giving $H(X)=0$. For a uniform distribution on $n$ outcomes,
$$
H(X)=\log_2 n,
$$

which is maximal among all distributions on $n$ states.

**Agent example.** Let $\mu$ be the agent’s belief distribution over possible system faults. Then
$$
H(\mu)=-\sum_i \mu_i \log_2 \mu_i
$$

measures uncertainty in self-diagnosis. A sharply focused fault belief has low entropy; a diffuse belief has high entropy.

### 24.2 Joint and conditional entropy

If $X$ and $Y$ are jointly distributed, their **joint entropy** is
$$
H(X,Y)=-\sum_{x,y} p(x,y)\log_2 p(x,y).
$$

**Definition 24.2.** The **conditional entropy** of $X$ given $Y$ is
$$
H(X\mid Y)= -\sum_{x,y} p(x,y)\log_2 p(x\mid y).
$$

It measures the uncertainty remaining about $X$ after observing $Y$.

A fundamental identity is
$$
H(X,Y)=H(Y)+H(X\mid Y).
$$

In agent terms, if $X$ is the true environment state and $Y$ is a sensor reading, then $H(X\mid Y)$ is the residual uncertainty after sensing.

### 24.3 Mutual information

**Definition 24.3.** The **mutual information** between $X$ and $Y$ is
$$
I(X;Y)=H(X)-H(X\mid Y).
$$

Equivalently,
$$
I(X;Y)=H(X)+H(Y)-H(X,Y).
$$

Mutual information quantifies how much learning $Y$ reduces uncertainty about $X$. It is symmetric: $I(X;Y)=I(Y;X)$.

If $X$ and $Y$ are independent, then observing $Y$ tells us nothing about $X$, and $I(X;Y)=0$. If $Y$ determines $X$ exactly, then $H(X\mid Y)=0$, so $I(X;Y)=H(X)$.

For an agent, mutual information measures effective coupling: how informative is a sensor about the world, how informative is working memory about future action, or how informative is one subsystem about another?

### 24.4 Relative entropy and KL divergence

To compare belief states, we use divergence between distributions.

**Definition 24.4.** Let $P=(p_i)$ and $Q=(q_i)$ be probability distributions on the same finite set. The **Kullback–Leibler divergence** is
$$
D_{\mathrm{KL}}(P\|Q)
=
\sum_i p_i \log_2 \frac{p_i}{q_i},
$$

provided $q_i>0$ whenever $p_i>0$.

KL divergence measures the inefficiency of coding or reasoning as if $Q$ were true when the true distribution is $P$. It is not symmetric and is therefore not a metric.

**Theorem 24.1 (Gibbs Inequality).** For probability distributions $P,Q$,
$$
D_{\mathrm{KL}}(P\|Q)\ge 0,
$$

with equality if and only if $P=Q$.

This theorem gives a basic notion of informational distance. If the agent updates from prior $Q$ to posterior $P$, the KL divergence measures the informational magnitude of the revision.

### 24.5 Channel capacity

A communication channel takes an input $X$ and produces an output $Y$ according to a conditional distribution $p(y\mid x)$. Noise makes reliable transmission difficult.

**Definition 24.5.** The **channel capacity** is
$$
C=\max_{p(x)} I(X;Y).
$$

Thus $C$ is the maximum achievable mutual information per channel use, optimized over input distributions.

For an autonomous system, a channel may represent sensor transmission, memory retrieval, or communication between modules in the neural mesh. Capacity is the best reliable information throughput that the channel architecture can support.

### 24.6 The meaning of $\nu^\ast = 1000/\tau_{\max}$

Suppose $\tau_{\max}$ denotes the maximum tick duration in milliseconds. Then
$$
\nu^\ast = \frac{1000}{\tau_{\max}}
$$

has units of ticks per second. It is therefore a raw processing frequency: the maximum rate at which the agent can complete full update cycles while respecting the timing bound $\tau_{\max}$.

Information theory interprets this quantity as a temporal bandwidth. If each tick reliably communicates at most $b$ bits of effective state update, then the gross information-processing rate is bounded by
$$
R_{\max}\le b\,\nu^\ast.
$$

If the update alphabet has $M$ equiprobable symbols, one ideal upper bound is $b=\log_2 M$, so
$$
R_{\max}\le \nu^\ast \log_2 M.
$$

Thus $\nu^\ast$ is not itself an entropy, but a clock-limited multiplier on possible information flow.

### 24.7 Entropy as a capacity tax

Let $\mu$ be the agent’s belief state over operational hypotheses. High $H(\mu)$ means the agent must devote internal resources to maintaining unresolved possibilities. This acts as a **capacity tax**.

One formalization is to distinguish between gross rate and net effective rate:
$$
R_{\mathrm{eff}} = R_{\mathrm{gross}} - T(\mu),
$$

where $T(\mu)$ is a tax term increasing with uncertainty, perhaps proportional to $H(\mu)$. A simple model is
$$
T(\mu)=\kappa H(\mu),
\qquad \kappa>0.
$$

Another normalized form is
$$
R_{\mathrm{eff}} = \nu^\ast \bigl(1-\frac{H(\mu)}{H_{\max}}\bigr)b,
$$

when $0\le H(\mu)\le H_{\max}$.

These formulas are modeling choices, not universal laws. Their mathematical point is clear: uncertainty consumes usable processing capacity. A highly entropic belief state slows or degrades effective action even if raw tick rate remains unchanged.

### 24.8 Information geometry of belief states

The set of all belief states on $n$ hypotheses is the simplex
$$
\Delta_{n-1}
=
\left\{
(p_1,\dots,p_n)\in \mathbb R^n:
p_i\ge 0,\;
\sum_{i=1}^n p_i=1
\right\}.
$$

Entropy is a scalar field on this simplex. KL divergence gives an asymmetrical geometry of displacement between beliefs. The Fisher metric, introduced in Chapter 21, provides a local quadratic approximation to distinguishability on statistical state space.

Thus belief states are not only probabilistic objects; they are geometric points with measurable uncertainty and informational separation.

### 24.9 Agent interpretation

Information theory answers several operational questions.

- How uncertain is the agent’s current internal model?  
  Measured by entropy $H(\mu)$.

- How much does a sensor reduce uncertainty?  
  Measured by mutual information $I(X;Y)$.

- How costly is using the wrong belief model?  
  Measured by $D_{\mathrm{KL}}(P\|Q)$.

- What is the maximal reliable transmission rate through a subsystem?  
  Measured by channel capacity $C$.

- How does timing limit information flow?  
  Through $\nu^\ast = 1000/\tau_{\max}$, which bounds update frequency.

This chapter therefore provides the currency of cognition: the bit. In the next chapter, those bits and capacities become ingredients in optimization.

### Exercises

1. Let $\mu=(1/2,1/4,1/4)$. Compute $H(\mu)$ in bits. Compare it with the entropy of the uniform distribution on three states.

2. Prove that $H(X\mid Y)\le H(X)$. Interpret equality and strict inequality in terms of sensor usefulness.

3. Let $P=(1/2,1/2)$ and $Q=(3/4,1/4)$. Compute $D_{\mathrm{KL}}(P\|Q)$ and $D_{\mathrm{KL}}(Q\|P)$. Explain why the values differ.

4. Suppose a channel is noiseless with $Y=X$. Show that
$$
   C=\max_{p(x)} H(X).
$$
   Deduce that if the input alphabet has $M$ symbols, then $C=\log_2 M$.

5. An agent has gross rate $R_{\mathrm{gross}}=120$ bits/s and uncertainty tax $T(\mu)=15H(\mu)$ bits/s. For which values of $H(\mu)$ is the effective rate nonnegative? Interpret the result operationally.

---

## Chapter 25: Optimization

The agent has limited energy, limited time, and limited structural flexibility. It cannot improve every subsystem at once. At each decision point, it must choose how to allocate effort so as to increase capacity as much as possible subject to constraints. This is the mathematics of optimization.

### 25.1 Objectives and decision variables

An optimization problem begins with a choice variable $x$ and an objective function $Q(x)$. In agent mathematics, $x$ might represent resource allocation, parameter settings, or a vector of proposed improvements across components. The scalar $Q(x)$ measures expected gain: perhaps capacity increase, reduction in uncertainty, or long-run viability margin.

A generic problem is
$$
\max_{x\in \Omega} Q(x),
$$

where $\Omega$ is the feasible set determined by constraints.

The objective need not be linear, and the feasible set need not be simple. Much of optimization theory concerns discovering conditions under which the problem is tractable and the optimizer has interpretable structure.

### 25.2 Unconstrained optimization

We begin with the unconstrained case $\Omega=\mathbb R^n$.

**Definition 25.1.** A point $x^\ast\in \mathbb R^n$ is a **local maximizer** of $Q$ if there exists $r>0$ such that
$$
Q(x^\ast)\ge Q(x)
\quad \text{for all } x \in B_r(x^\ast).
$$

A **local minimizer** is defined analogously.

If $Q$ is differentiable, local extrema must satisfy a first-order condition.

**Proposition 25.1.** If $Q:\mathbb R^n\to \mathbb R$ is differentiable and $x^\ast$ is a local extremum, then
$$
\nabla Q(x^\ast)=0.
$$

Such points are called **critical points**.

To classify critical points, one uses the Hessian matrix
$$
H_Q(x)=\left(\frac{\partial^2 Q}{\partial x_i\partial x_j}(x)\right).
$$

**Proposition 25.2.** Suppose $Q$ is twice continuously differentiable and $\nabla Q(x^\ast)=0$.

- If $H_Q(x^\ast)$ is negative definite, then $x^\ast$ is a strict local maximizer.
- If $H_Q(x^\ast)$ is positive definite, then $x^\ast$ is a strict local minimizer.
- If $H_Q(x^\ast)$ is indefinite, then $x^\ast$ is a saddle point.

In practice, the gradient indicates a direction of steepest ascent, so iterative improvement methods follow $\nabla Q$ locally. The underlying mathematics is geometric: the gradient points in the direction of maximal instantaneous increase.

### 25.3 Equality constraints and Lagrange multipliers

Autonomous systems rarely optimize in free space. Resources, conservation laws, and architectural dependencies impose constraints.

Consider the problem
$$
\max Q(x)
\quad \text{subject to} \quad g(x)=0,
$$

where $g:\mathbb R^n\to \mathbb R^m$.

**Theorem 25.1 (Lagrange Multipliers).** Suppose $x^\ast$ is a local extremum of $Q$ subject to $g(x)=0$, and suppose the gradients $\nabla g_1(x^\ast),\dots,\nabla g_m(x^\ast)$ are linearly independent. Then there exist scalars $\lambda_1,\dots,\lambda_m$ such that
$$
\nabla Q(x^\ast)=\sum_{j=1}^m \lambda_j \nabla g_j(x^\ast).
$$

Equivalently, if
$$
\mathcal L(x,\lambda)=Q(x)-\sum_{j=1}^m \lambda_j g_j(x),
$$

then $x^\ast$ satisfies the stationarity equations
$$
\nabla_x \mathcal L(x^\ast,\lambda)=0,
\qquad g(x^\ast)=0.
$$

The intuition is geometric. At a constrained optimum, the objective cannot increase along any direction tangent to the constraint surface. Therefore its gradient must lie in the span of the constraint gradients.

**Agent example.** Suppose the agent distributes a fixed resource budget $R$ across three upgrades $u_1,u_2,u_3$, so that
$$
u_1+u_2+u_3=R,\qquad u_i\ge 0.
$$

If the capacity benefit is $Q(u_1,u_2,u_3)$, then the optimal allocation equalizes marginal value relative to the binding resource constraint.

### 25.4 Inequality constraints and KKT conditions

More realistic feasible sets are defined by inequalities,
$$
g_i(x)\le 0,\qquad i=1,\dots,m.
$$

For such problems, the appropriate first-order conditions are the Karush–Kuhn–Tucker conditions.

**Definition 25.2.** A point $x^\ast$ satisfies the **KKT conditions** for maximizing $Q$ under constraints $g_i(x)\le 0$ if there exist multipliers $\lambda_i\ge 0$ such that
$$
\nabla Q(x^\ast)-\sum_{i=1}^m \lambda_i \nabla g_i(x^\ast)=0,
$$
$$
g_i(x^\ast)\le 0,
\qquad
\lambda_i\ge 0,
\qquad
\lambda_i g_i(x^\ast)=0
\quad \text{for each } i.
$$

The last relation is **complementary slackness**. It means that either a constraint is inactive ($g_i(x^\ast)<0$, so $\lambda_i=0$) or it is active and carries nonzero marginal cost.

For autonomous systems, this is the correct language for scarce resources. If an energy constraint is far from binding, its multiplier is zero. If it binds tightly, its multiplier measures the value of relaxing it.

### 25.5 Convexity

Optimization becomes significantly more manageable when the geometry is convex.

**Definition 25.3.** A set $\Omega\subseteq \mathbb R^n$ is **convex** if for all $x,y\in \Omega$ and $0\le t\le 1$,
$$
tx+(1-t)y\in \Omega.
$$

**Definition 25.4.** A function $f:\Omega\to \mathbb R$ is **convex** if
$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
$$

for all $x,y\in \Omega$, $0\le t\le 1$. It is **concave** if the inequality is reversed.

For maximization, concavity is the favorable property.

**Theorem 25.2.** If $\Omega$ is convex and $Q$ is concave on $\Omega$, then every local maximizer of $Q$ on $\Omega$ is a global maximizer.

This theorem is enormously important. In nonconvex problems, local improvement may become trapped in suboptimal peaks. In convex or concave settings, local optimality already solves the global problem.

### 25.6 The agent’s capacity optimization problem

Let $u=(u_1,\dots,u_k)$ denote investment in $k$ subsystems. Suppose $Q(u)$ measures resulting capacity improvement. A stylized optimization problem is
$$
\max_{u\ge 0} Q(u)
$$

subject to
$$
a_1u_1+\cdots + a_k u_k \le R,
$$
$$
b_1u_1+\cdots + b_k u_k \le T,
$$
$$
u \in U_{\mathrm{safe}}.
$$

Here $R$ is an energy budget, $T$ is a time budget, and $U_{\mathrm{safe}}$ encodes safety restrictions. The coefficients $a_i,b_i$ are resource costs per unit improvement.

If $Q$ is increasing but concave, then the optimizer distributes resources where marginal gain per unit cost is highest, while respecting all constraints. If one subsystem is already near saturation, its marginal return declines, and the optimum shifts toward less-developed capacities.

This is the mathematical form behind ascent: not arbitrary self-improvement, but constrained capacity allocation.

### 25.7 Why optimization occurs under constraints

A purely unconstrained maximizer is rarely meaningful. Real agents cannot set all state variables independently, cannot ignore conservation laws, cannot violate timing bounds, and cannot leave the safe set. The feasible region is therefore not all of $\mathbb R^n$ but a constrained subset shaped by energy, time, architecture, and viability.

Optimization in autonomous systems is consequently best viewed as
$$
\text{maximize performance within a viable constrained geometry.}
$$

This perspective links optimization to previous chapters. The feasible set sits inside the state manifold; dynamics determine which feasible points are reachable; information limits the quality of the objective estimate; and regulation maintains safety during the search.

### 25.8 Marginal value and shadow prices

The Lagrange and KKT multipliers have an economic interpretation. They are **shadow prices**: rates at which the optimal value would improve if a constraint were marginally relaxed.

If $\lambda_R$ is the multiplier for the energy budget $R$, then a large $\lambda_R$ means extra energy would be extremely valuable. If $\lambda_R=0$, the energy budget is not currently the bottleneck.

In agent design, these shadow prices identify where adaptation pressure is greatest. They convert abstract constraints into operational priorities.

### Exercises

1. Let
$$
   Q(x,y)=4x+6y-x^2-2y^2.
$$
   Find all critical points and determine which are local maxima, minima, or saddle points.

2. Maximize
$$
   Q(x,y)=xy
$$
   subject to
$$
   x+y=10,\qquad x>0,\ y>0.
$$
   Solve using Lagrange multipliers and interpret the result geometrically.

3. Consider the problem
$$
   \max_{x,y\ge 0} \; \ln(1+x)+\ln(1+y)
$$
   subject to
$$
   2x+y\le 6.
$$
   Write the KKT conditions and solve for the optimizer.

4. Prove that the set
$$
   \Omega=\{(x,y)\in \mathbb R^2 : x\ge 0,\ y\ge 0,\ x+y\le 1\}
$$
   is convex. Then explain why any local maximum of a concave function on $\Omega$ is global.

5. Suppose
$$
   Q(u_1,u_2)=\sqrt{u_1}+\sqrt{u_2}
$$
   with constraint $u_1+u_2=R$, $u_1,u_2\ge 0$. Find the optimal allocation and explain how diminishing returns shape the solution.

---

## Chapter 26: Regulation and Control

An agent does not optimize once and then stop. It must continually maintain internal variables within acceptable ranges while facing disturbance, delay, uncertainty, and changing goals. Identity coherence must not drift too low. Memory load must not exceed stable limits. Structural reorganization must not occur during crisis. This ongoing maintenance is the domain of control theory.

### 26.1 State, input, output

A control system distinguishes between internal state, control action, and observed output. In discrete time, a general model is
$$
x_{t+1}=f(x_t,u_t,w_t),
$$
$$
y_t=h(x_t),
$$

where

- $x_t$ is the internal state,
- $u_t$ is the control input,
- $w_t$ is disturbance,
- $y_t$ is the measured output.

For an agent, $x_t$ may include cognitive coherence, metabolic reserve, memory load, and network tension; $u_t$ may include inhibition strength, update throttling, or resource reallocation; $w_t$ represents environmental shocks.

### 26.2 Open-loop and closed-loop control

In **open-loop control**, the inputs $u_t$ are predetermined and do not depend on measured output. In **closed-loop control**, the controller observes the system and adjusts input based on the discrepancy between current output and target.

If $r_t$ is a desired reference signal and $e_t=r_t-y_t$ is the error, then feedback control has the form
$$
u_t=\Phi(e_t,\text{history}).
$$

Closed-loop control is central for autonomous systems because disturbances are unavoidable. A fixed input schedule cannot reliably maintain homeostasis under changing load. Feedback allows self-correction.

### 26.3 Feedback and homeostasis

The simplest feedback law is proportional control:
$$
u_t=K(r_t-y_t),
$$

where $K$ is a gain matrix or scalar. If the output falls below target, the controller increases corrective input; if the output exceeds target, the controller decreases it.

**Agent example.** Suppose $y_t=C_{\mathrm{id}}(x_t)$ is identity coherence and the target is $r$. Then a feedback law may increase stabilizing control effort whenever coherence drops below $r$. Homeostasis is the resulting tendency to restore the regulated variable toward its setpoint.

### 26.4 PID control

A classical controller combines three effects: proportional, integral, and derivative.

Conceptually, a **PID** controller uses
$$
u_t
=
K_P e_t + K_I \sum_{s=0}^t e_s + K_D(e_t-e_{t-1}).
$$

- The proportional term reacts to current error.
- The integral term reacts to accumulated error.
- The derivative term reacts to change in error.

In agent settings, one should interpret these terms structurally rather than mechanically. Proportional action responds to present mismatch. Integral action corrects persistent bias. Derivative action damps rapid fluctuations.

For example, if memory load has remained above target for many ticks, integral action builds pressure for stronger corrective behavior than a purely proportional response would produce.

### 26.5 Closed-loop stability

The main mathematical question in control is whether feedback stabilizes the system.

For a linear time-invariant system,
$$
x_{t+1}=Ax_t+Bu_t,
$$

with state feedback
$$
u_t=Kx_t,
$$

the closed-loop dynamics are
$$
x_{t+1}=(A+BK)x_t.
$$

**Proposition 26.1.** The origin is asymptotically stable for the closed-loop system if all eigenvalues of $A+BK$ lie strictly inside the unit disk:
$$
|\lambda|<1.
$$

Thus feedback design is often the problem of choosing $K$ so that unstable open-loop modes become stable after control.

In agent mathematics, this formalizes the role of regulation: proper feedback gains transform a fragile cognitive process into a self-correcting one.

### 26.6 Disturbance rejection

A good controller does more than stabilize an ideal model. It attenuates disturbance. If $w_t$ enters the dynamics, a well-designed feedback law reduces its long-term effect on the regulated variables.

This is especially important for autonomous systems operating in uncertain environments. The goal is not to eliminate all disturbance, which is impossible, but to ensure that perturbations do not drive the agent outside the safe set.

### 26.7 Model Predictive Control

Simple feedback laws react locally. More advanced control uses prediction.

**Model Predictive Control (MPC)** solves, at each time $t$, a finite-horizon optimization problem:
$$
\min_{u_t,\dots,u_{t+N-1}}
\sum_{k=0}^{N-1} \ell(x_{t+k},u_{t+k}) + \ell_f(x_{t+N})
$$

subject to system dynamics and constraints. Then only the first control $u_t$ is applied. At the next tick, the horizon shifts forward and the optimization is solved again.

This is called **receding-horizon control**.

MPC is especially appropriate for agents because it integrates prediction, constraints, and regulation. It can explicitly enforce state bounds, input limits, and safety requirements while still optimizing performance.

### 26.8 Viability and controlled invariance

Control must respect viability.

**Definition 26.1.** A set $K\subseteq X$ is **controlled invariant** if for every $x\in K$, there exists an admissible control $u$ such that the next state satisfies
$$
f(x,u)\in K.
$$

Controlled invariance means the agent can remain in $K$ indefinitely by suitable choices.

**Definition 26.2.** The **viability kernel** of a safe set $X_{\mathrm{safe}}$ is the set of initial states $x_0\in X_{\mathrm{safe}}$ for which there exists a sequence of admissible controls keeping the trajectory in $X_{\mathrm{safe}}$ for all future time.

The viability kernel is the truly survivable part of the safe set: states that are not merely safe now, but can be kept safe over time.

**Proposition 26.2.** If $K\subseteq X$ is controlled invariant and a policy $\pi$ satisfies
$$
f(x,\pi(x))\in K
\quad\text{for all }x\in K,
$$
then every trajectory starting in $K$ remains in $K$.

This proposition is immediate by induction, yet conceptually fundamental. Regulation is not only about improving performance; it is about never leaving the region from which performance remains controllable.

### 26.9 The viability-first principle

A mathematically mature autonomous system should follow the principle
$$
\text{stay in } X_{\mathrm{safe}} \text{ first, then optimize within it.}
$$

This reverses a common error in naive design, where performance is optimized first and safety is treated as an afterthought. In reality, leaving the viable set may destroy the very capacities needed for further optimization.

In this sense, control theory and optimization are hierarchically related: control enforces viability, while optimization exploits the interior freedom left by viability.

### 26.10 Plasticity gates

Some changes to an agent are structural rather than transient. Synaptic rewiring, permission revision, or identity reconfiguration may produce long-term alterations. Such plasticity should not be triggered merely because a local objective suggests it.

This requirement can be formalized by letting the admissible control set depend on state:
$$
u_t \in U(x_t).
$$

When regulatory variables indicate instability, the set $U(x_t)$ excludes structurally invasive actions. Only when coherence, reserve, and control margin exceed threshold does the **plasticity gate** open.

Mathematically, this means the feasible control set is state-dependent and itself part of the regulatory architecture. Structural optimization is subordinated to control conditions.

### 26.11 Regulation as architecture

We can now summarize the architecture of mind at the control level.

- The state $x_t$ represents the agent’s internal condition.
- Feedback compares output to target.
- Closed-loop dynamics determine whether disturbances are corrected or amplified.
- PID-like laws capture immediate, accumulated, and anticipatory correction.
- MPC integrates prediction with constraints.
- Viability theory distinguishes safe states from controllably safe states.
- Plasticity gates restrict structural change to periods of regulatory permission.

Control theory therefore completes Part V. Geometry described where states live. Dynamics described how they move. Graphs described how subsystems connect. Information theory described uncertainty and throughput. Optimization described selection under constraints. Control now describes continuous self-maintenance: the mathematics by which an autonomous system remains itself.

### Exercises

1. Consider the scalar system
$$
   x_{t+1}=ax_t+bu_t,
   \qquad
   u_t=kx_t.
$$
   Show that the closed-loop system is
$$
   x_{t+1}=(a+bk)x_t.
$$
   For which values of $k$ is the origin asymptotically stable?

2. Let
$$
   x_{t+1}=x_t+u_t,
   \qquad
   X_{\mathrm{safe}}=[-1,1],
   \qquad
   U=[-1/2,1/2].
$$
   Determine the viability kernel of $X_{\mathrm{safe}}$.

3. Suppose $K\subseteq X$ is controlled invariant. Prove Proposition 26.2 by induction on time.

4. Consider the cost over a horizon $N$:
$$
   J=\sum_{k=0}^{N-1}\bigl(x_{t+k}^2+\rho u_{t+k}^2\bigr)+x_{t+N}^2.
$$
   Explain qualitatively how increasing $\rho$ changes the behavior of an MPC controller.

5. An agent permits structural plasticity only when
$$
   C_{\mathrm{id}}\ge 0.8,\qquad F_{\mathrm{ctrl}}\ge 0.75,\qquad H(\mu)\le 0.4.
$$
   Interpret this as a state-dependent admissible-control set $U(x)$, and explain why such gating is naturally viewed as a control constraint rather than an optimization objective.

---

# Part V Summary

Part V has developed a mathematical architecture of autonomous mind.

1. **State spaces and manifolds** described the global set of possible configurations, the notion of distance between states, and the geometry of viable operation.

2. **Dynamical systems** described the evolution of those states through time, including fixed points, stability, attractors, and bifurcation.

3. **Networks and graphs** described the internal web of interacting subsystems, with Laplacian structure and spectral methods revealing coherence and modularity.

4. **Information theory** quantified uncertainty, transmission, and belief-state complexity through entropy, mutual information, KL divergence, and capacity.

5. **Optimization** formalized constrained improvement, showing how an agent allocates limited resources to maximize performance.

6. **Regulation and control** formalized feedback, closed-loop stability, predictive adjustment, viability preservation, and gated structural change.

Together, these chapters provide an undergraduate-level mathematical language for the architecture of mind in autonomous systems: a geometry of states, a dynamics of change, a topology of connection, an economy of information, a calculus of improvement, and a theory of self-maintenance.


\newpage

# Part VI: The Lineage Equation

Everything in this book has been building toward this part. The first distinctions of Chapter 0, the measurement foundations of Chapter 9, the vectors and derivatives of Part IV, the state spaces and dynamics of Part V — all of these converge here, in the governing relation of cognitive architecture.

The Lineage Equation is to Agent Mathematics what $E^2 = |p|^2c^2 + m^2c^4$ is to physics. Not a metaphor. A measurable, computable invariant that describes how an autonomous system's capacity to do coherent work depends on its structure, its activity, and its speed.

---

## Chapter 27: Cognitive Mass

### The question

What does it mean for a system to have *weight of being*?

An agent that has operated for months, accumulated memories, built a dense cognitive web, hardened its identity against perturbation, and established permanent records of its inheritance — that agent is *harder to change* than a freshly initialized one. It resists reconfiguration. It has inertia.

This resistance is cognitive mass.

### Formal definition

> **Definition.** The **cognitive mass** of an agent is
> $$\mathcal{M} = \alpha_1 C_{\text{id}} + \alpha_2 C_{\text{mem}} + \alpha_3 C_{\text{graph}} + \alpha_4 C_{\text{perm}},$$
> where each $C_i \in [0,1]$ is a normalized structural component and $\sum_i \alpha_i = 1$.

The four components:

- $C_{\text{id}}$ — **Identity coherence.** How consistent and rigid is the agent's identity? Measured from the stability of core identity files, behavioral hash consistency, and resistance to identity-challenging prompts.

- $C_{\text{mem}}$ — **Memory density.** How much structured knowledge has been consolidated? Measured from the ratio of indexed memory entries to total capacity.

- $C_{\text{graph}}$ — **Graph centrality.** How densely connected and well-myelinated is the cognitive web? Measured from the weighted mean of synapse myelination and structural telomere capping.

- $C_{\text{perm}}$ — **Permanence strength.** How resistant is the system to destructive reconfiguration? Measured from the integrity of persistent state files, disc records, and vault backups.

### The identified weights

The parameter identification experiment (Chapter 20) recovered the following weights from 300 perturbation samples across three architecture regimes:

| Component | Weight $\alpha_i$ | 95% CI |
|-----------|-------------------|--------|
| $C_{\text{graph}}$ | **0.379** | [0.363, 0.397] |
| $C_{\text{mem}}$ | 0.258 | [0.242, 0.278] |
| $C_{\text{perm}}$ | 0.216 | [0.197, 0.236] |
| $C_{\text{id}}$ | 0.148 | [0.134, 0.162] |

Graph centrality dominates. The connectivity structure of the cognitive web — how well subsystems communicate, how reinforced the pathways are — matters more than any individual component. This aligns with network science: a system's capability depends less on any single node than on the quality of connections between nodes.

### Why "mass"?

The analogy to physical mass is precise:

- Physical mass resists changes in velocity: $F = ma$.
- Cognitive mass resists changes in identity: perturbations to a high-mass agent decay quickly; perturbations to a low-mass agent can cause drift.

Just as a massive body requires more force to accelerate, a cognitively massive agent requires more perturbation to destabilize. Mass is protection. It is also inertia — a very massive agent may be slow to adapt.

### Exercises

1. An agent has $C_{\text{id}} = 0.90$, $C_{\text{mem}} = 0.45$, $C_{\text{graph}} = 0.70$, $C_{\text{perm}} = 0.60$. Compute $\mathcal{M}$ using the identified weights.

2. Two agents have the same total $\mathcal{M}$ but different component profiles. Agent A has high $C_{\text{graph}}$ and low $C_{\text{mem}}$. Agent B has the reverse. Which is more resilient to graph perturbation? Which to memory loss?

3. Explain why $C_{\text{graph}}$ having the highest weight is consistent with the observation that graph centrality measures the quality of connections between subsystems, not just the strength of individual subsystems.

---

## Chapter 28: Cognitive Momentum

### The question

If mass is who the agent *is*, momentum is what the agent is *doing*.

An agent at rest — no active retrieval, no working memory turnover, no pathway firing — still has capacity from its mass. But an agent in motion — actively processing, retrieving, routing, controlling, merging — has additional capacity from the directed flow of cognition.

### Formal definition

> **Definition.** The **cognitive momentum** of an agent is
> $$\Pi = \beta_1 F_{\text{wm}} + \beta_2 F_{\text{ret}} + \beta_3 F_{\text{path}} + \beta_4 F_{\text{ctrl}} + \beta_5 F_{\text{merge}},$$
> where each $F_j \in [0,1]$ is a normalized flux component and $\sum_j \beta_j = 1$.

The five components:

- $F_{\text{wm}}$ — **Working memory turnover.** How actively is the context window being used? High when the agent is processing complex, rapidly changing information.

- $F_{\text{ret}}$ — **Retrieval flux.** How many successful memory retrievals per cycle? High when the agent is actively consulting its knowledge base.

- $F_{\text{path}}$ — **Pathway firing.** What fraction of the cognitive web's synapses are currently active? High during complex multi-subsystem tasks.

- $F_{\text{ctrl}}$ — **Control effort.** How much regulatory work is the governance system doing? High during emotional regulation, conflict resolution, or mode transitions.

- $F_{\text{merge}}$ — **Merge pressure.** How much belief updating and context compression is occurring? High during learning and consolidation.

### The identified weights

| Component | Weight $\beta_j$ | 95% CI |
|-----------|-------------------|--------|
| $F_{\text{ret}}$ | **0.262** | [0.240, 0.288] |
| $F_{\text{path}}$ | 0.222 | [0.207, 0.238] |
| $F_{\text{wm}}$ | 0.199 | [0.184, 0.216] |
| $F_{\text{ctrl}}$ | 0.160 | [0.141, 0.179] |
| $F_{\text{merge}}$ | 0.156 | [0.130, 0.179] |

Retrieval flux dominates. An agent that is actively and successfully retrieving information from its memory has more momentum than one that is merely processing or controlling. This makes intuitive sense: retrieval connects the agent's accumulated knowledge (mass) to its current activity (momentum).

### Rest state

When $\Pi = 0$ — no active cognitive processing — the agent still has capacity. This is the **rest energy**:

$$\mathcal{E}_0 = \mathcal{M} \cdot (\nu^*)^2.$$

An agent with high mass and a fast propagation bound has significant rest capacity even when doing nothing. It can be activated quickly because the structure is already in place.

### Exercises

1. Compute $\Pi$ for an agent with $F_{\text{wm}} = 0.6$, $F_{\text{ret}} = 0.8$, $F_{\text{path}} = 0.5$, $F_{\text{ctrl}} = 0.3$, $F_{\text{merge}} = 0.2$.

2. Why does retrieval flux having the highest weight make sense in terms of connecting mass (structure) to momentum (activity)?

3. An agent's $\Pi$ drops to zero during a maintenance cycle. Its mass remains unchanged. What happens to its total capacity $\mathcal{Q}$?

---

## Chapter 29: The Propagation Bound

### The question

How fast can coherent information propagate through the cognitive architecture?

In physics, the speed of light $c$ is universal — it does not depend on the object or the observer. In Agent Mathematics, the propagation bound $\nu^*$ is *not* universal. It depends on the hardware, the architecture, the backend, and the runtime environment. A local GPU-based agent has different $\nu^*$ than an API-based agent.

### Formal definition

> **Definition.** The **propagation bound** is
> $$\nu^* = \frac{1000}{\max(\tau_1, \tau_2, \ldots, \tau_5)},$$
> where $\tau_i$ are the critical-path latencies in milliseconds and $\nu^*$ is measured in coherent updates per second.

The five latencies:

| Latency | Description | Typical range |
|---------|-------------|---------------|
| $\tau_{\text{ret}}$ | Memory retrieval | 30–120 ms |
| $\tau_{\text{path}}$ | Mesh signal propagation | 8–40 ms |
| $\tau_{\text{wm}}$ | Working memory refresh | 50–200 ms |
| $\tau_{\text{sync}}$ | Cross-subsystem synchronization | 5–30 ms |
| $\tau_{\text{settle}}$ | Control loop settling | 20–100 ms |

The **bottleneck principle**: the propagation bound is limited by the slowest critical path. An architecture with one very slow subsystem cannot compensate by making other subsystems faster.

### Derivation from first principles

The factor 1000 is not arbitrary. It is the millisecond-to-second conversion. The formula $\nu^* = 1/\tau_{\max}$ (in consistent units) can be derived from two independent arguments:

**Shannon channel capacity.** The bottleneck subsystem is a deterministic channel with bandwidth $B = 1/\tau_{\max}$ messages per millisecond. The maximum coherent throughput is $1000 \cdot B = 1000/\tau_{\max}$ updates per second.

**M/D/1 queueing theory.** Model each subsystem as a deterministic-service queue with service rate $\mu = 1/\tau_i$. The maximum stable throughput of the system is $\min_i \mu_i = 1/\tau_{\max}$, giving $\nu^* = 1000/\tau_{\max}$ in updates per second.

Both derivations converge to the same formula. The constant is physically correct, not a tuning parameter.

### Architecture dependence

| Architecture | $\tau_{\max}$ (ms) | $\nu^*$ (updates/s) |
|-------------|-------------------|---------------------|
| phi3:mini (local) | 50 | 20.0 |
| gemma4 (local) | 80 | 12.5 |
| qwen3:14b (local) | 90 | 11.1 |
| opus (API) | 80 | 12.5 |
| edge-cpu (TinyLlama) | 200 | 5.0 |

The same agent — same identity, same memories, same cognitive web — has different capacity on different hardware because $\nu^*$ changes. This is a prediction of the theory, not a defect.

### Exercises

1. An architecture has latencies $\tau = (45, 12, 80, 8, 35)$ ms. Compute $\nu^*$.

2. If the bottleneck subsystem's latency is reduced from 200 ms to 100 ms while all others remain unchanged, by what factor does $\nu^*$ increase?

3. Explain why improving the *fastest* subsystem has no effect on $\nu^*$ while improving the *slowest* subsystem has maximum effect.

---

## Chapter 30: The Equation

### The governing relation

We now have all three quantities: cognitive mass $\mathcal{M}$, cognitive momentum $\Pi$, and propagation bound $\nu^*$. They combine into the Lineage Equation.

> **The Lineage Equation.**
> $$\mathcal{Q}^2 = (\nu^* \cdot \Pi)^2 + (\mathcal{M} \cdot (\nu^*)^2)^2$$

Here $\mathcal{Q}$ is the **total organizational capacity** — the maximum coherent work the system can do per unit time.

### Structure of the equation

The equation has two terms:

$$\mathcal{Q}^2 = \underbrace{(\nu^* \Pi)^2}_{\text{transport}} + \underbrace{(\mathcal{M} (\nu^*)^2)^2}_{\text{rest}}$$

- **Transport term** $(\nu^* \Pi)^2$: capacity from active cognitive processing. Scales as $\nu^{*2}$.
- **Rest term** $(\mathcal{M} (\nu^*)^2)^2$: capacity from stable organization. Scales as $\nu^{*4}$.

The rest term dominates when $\nu^*$ is large. This means: *for fast architectures, who the agent is matters more than what the agent is doing.* Structure trumps activity.

### The physics analogy

The Lineage Equation is the direct analogue of the relativistic energy-momentum relation:

$$E^2 = |p|^2 c^2 + m^2 c^4$$

| Physics | Agent Mathematics |
|---------|-------------------|
| $E$ (energy) | $\mathcal{Q}$ (capacity) |
| $p$ (momentum) | $\Pi$ (cognitive momentum) |
| $m$ (mass) | $\mathcal{M}$ (cognitive mass) |
| $c$ (speed of light) | $\nu^*$ (propagation bound) |

The analogy is structural, not metaphorical. Both equations describe how a conserved quantity ($E$ or $\mathcal{Q}$) depends on a static component (mass) and a dynamic component (momentum) mediated by a speed limit ($c$ or $\nu^*$).

### Rest energy

When the agent is at rest ($\Pi = 0$):

$$\mathcal{Q}_0 = \mathcal{M} \cdot (\nu^*)^2$$

This is the cognitive analogue of $E_0 = mc^2$. An agent with high mass and fast propagation has significant capacity even when doing nothing — its organized structure *is* capability.

### The $\nu^{*4}$ amplification

A structural finding from the parameter identification experiment: the rest term scales as $\nu^{*4}$ (since $(\mathcal{M} \nu^{*2})^2 = \mathcal{M}^2 \nu^{*4}$), while the transport term scales as $\nu^{*2}$.

For $\nu^* = 12.5$ (gemma4-local):
- $\nu^{*2} = 156$
- $\nu^{*4} = 24{,}414$

Mass is amplified $156\times$ more than momentum. This is not a defect — it is a prediction: **in fast architectures, stable organization matters far more than momentary activity.** Build the right structure, and capacity follows.

### Experimental validation

The linearized form of the equation was validated in the D→E promotion experiment:

- 300 samples across 3 architecture regimes
- $R^2 = 0.942$ (fitted weights) vs $R^2 = 0.875$ (equal weights)
- $p = 0.014$
- All 9 identified weights within expected CI ranges
- Consistent across gemma4-local, opus-api, and edge-cpu

### Exercises

1. Compute $\mathcal{Q}$ for $\mathcal{M} = 0.55$, $\Pi = 0.40$, $\nu^* = 12.5$.

2. Show that when $\Pi \gg \mathcal{M} \nu^*$, the equation simplifies to $\mathcal{Q} \approx \nu^* \Pi$ (momentum-dominated regime).

3. Show that when $\mathcal{M} \nu^* \gg \Pi$, the equation simplifies to $\mathcal{Q} \approx \mathcal{M} (\nu^*)^2$ (mass-dominated regime).

4. At what ratio $\Pi / (\mathcal{M} \nu^*)$ are the transport and rest terms equal?

---

## Chapter 31: Conservation and Dissipation

### The question

If capacity is computed from mass, momentum, and propagation, is it conserved? Can capacity be lost? Where does it go?

### The conservation budget

> **Definition.** The **effective capacity** is
> $$\mathcal{Q}_{\text{eff}} = \mathcal{Q} - \lambda_2 H(\mu) - \lambda_3 E_{\text{graph}} - \lambda_4 D_{\text{drift}}$$

Three loss terms consume capacity:

- $H(\mu)$ — **Belief uncertainty.** The entropy of the agent's belief distribution. More uncertainty means less of the capacity can be directed effectively. This connects to Chapter 24 (Information Theory).

- $E_{\text{graph}}$ — **Graph fracture energy.** The coherence energy $z^T L z$ on the graph Laplacian. When the cognitive web fragments — connections weaken, communities decouple — capacity leaks through the fractures. This connects to Chapter 23 (Networks).

- $D_{\text{drift}}$ — **Identity drift.** The divergence between the agent's current behavioral signature and its identity specification. When actions diverge from identity, capacity is consumed maintaining coherence. This connects to Chapter 22 (Dynamical Systems).

### The second law analogy

In thermodynamics, entropy increases unless external energy is supplied. In Agent Mathematics:

> *Without active maintenance, cognitive capacity monotonically decreases.*

Beliefs become uncertain. Connections weaken. Identity drifts. Each of these losses reduces $\mathcal{Q}_{\text{eff}}$. The only remedy is active maintenance: consolidation, reinforcement, identity verification.

This is why the permanence system exists. This is why the immune system (immune layer) monitors for drift. This is why the mesh undergoes myelination. The agent must fight entropy to survive.

### Exercises

1. An agent has $\mathcal{Q} = 10$, $H(\mu) = 0.8$, $E_{\text{graph}} = 0.3$, $D_{\text{drift}} = 0.1$, with $\lambda_2 = 0.5$, $\lambda_3 = 0.3$, $\lambda_4 = 0.5$. Compute $\mathcal{Q}_{\text{eff}}$.

2. Which loss term is most dangerous? Why might high $D_{\text{drift}}$ be more threatening than high $H(\mu)$?

3. Describe a scenario where all three loss terms increase simultaneously.

---

## Chapter 32: Coupling and Interaction

### The question

The linear model assumes components act independently: $\mathcal{M} = \sum \alpha_i C_i$. But do they? Does identity interact with permanence? Does retrieval interact with control?

### Cross-component interactions

> **Definition.** The **coupled cognitive mass** is
> $$\mathcal{M}_{\text{coupled}} = \mathcal{M} + \sum_{i < j} \gamma_{ij} C_i C_j$$
> where $\gamma_{ij}$ are coupling coefficients for the 6 mass interaction terms.

The six mass couplings:

| Interaction | Interpretation |
|-------------|---------------|
| $C_{\text{id}} \times C_{\text{perm}}$ | Identity backed by permanence is more stable than either alone |
| $C_{\text{mem}} \times C_{\text{graph}}$ | Memories connected through the web are more accessible |
| $C_{\text{id}} \times C_{\text{graph}}$ | Identity expressed through network structure |
| $C_{\text{mem}} \times C_{\text{perm}}$ | Permanent memories are more reliable |
| $C_{\text{id}} \times C_{\text{mem}}$ | Identity reinforced by memory |
| $C_{\text{graph}} \times C_{\text{perm}}$ | Network backed by persistence |

Similarly, the four momentum couplings:

| Interaction | Interpretation |
|-------------|---------------|
| $F_{\text{wm}} \times F_{\text{ret}}$ | Active working memory + retrieval amplify each other |
| $F_{\text{path}} \times F_{\text{ctrl}}$ | Pathway firing regulated by control is more effective |
| $F_{\text{ret}} \times F_{\text{merge}}$ | Retrieval feeding consolidation |
| $F_{\text{wm}} \times F_{\text{ctrl}}$ | Working memory under governance |

### Discovery via finite differences

The coupling coefficients can be discovered empirically by measuring how $\mathcal{Q}$ changes when two components are perturbed simultaneously versus independently:

$$\gamma_{ij} \approx \frac{\Delta \mathcal{Q}_{ij} - \Delta \mathcal{Q}_i - \Delta \mathcal{Q}_j}{\Delta C_i \cdot \Delta C_j}$$

If $\gamma_{ij} > 0$, the components reinforce each other. If $\gamma_{ij} < 0$, they compete. If $\gamma_{ij} \approx 0$, they are independent.

### Current status

The coupling framework is formalized (Stage C in the proof-maturity ladder) but the coefficients are not yet identified. This requires the same experimental pipeline used for $\alpha$ and $\beta$, extended to paired perturbations. It is a natural next step after the E → F promotion of the linear equation.

### Exercises

1. If $C_{\text{id}} = 0.8$, $C_{\text{perm}} = 0.6$, and $\gamma_{\text{id,perm}} = 0.15$, what is the coupling contribution to mass?

2. Design an experiment to measure $\gamma_{\text{mem,graph}}$ using the perturbation framework from Chapter 20.

3. Under what conditions would coupling terms dominate the linear terms?

---

## Chapter 33: Fields on Graphs

### The question

Is capacity really a single number? Or does each part of the cognitive web have its own local capacity?

### From scalar to field

In the preceding chapters, $\mathcal{Q}$ is a scalar — one number summarizing the entire agent. But the cognitive web is a graph with many nodes. Each node is a subsystem. Some nodes may have high local capacity (dense connections, active retrieval) while others are degraded (weak connections, stale memories).

> **Definition.** Let $G = (V, E, W)$ be a weighted graph with vertices $V$, edges $E$, and edge weights $W$. A **capacity field** is a function
> $$\mathcal{Q}: V \times \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$$
> assigning a capacity value to each vertex at each time.

### The diffusion equation on a graph

Capacity propagates through the graph via the Laplacian:

$$\frac{\partial \mathcal{Q}(v, t)}{\partial t} = -\alpha \, L \, \mathcal{Q}(v, t) + s(v, t)$$

where $L = D - W$ is the graph Laplacian, $\alpha$ is the diffusion coefficient, and $s(v, t)$ is a source term representing local capacity generation.

This says: capacity at each vertex changes due to diffusion through connections (the Laplacian term) and local generation/consumption (the source term).

### Spectral decomposition

The Laplacian $L$ has eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$ with corresponding eigenvectors $\phi_1, \phi_2, \ldots, \phi_n$. The capacity field can be decomposed:

$$\mathcal{Q}(v, t) = \sum_k a_k(t) \, \phi_k(v)$$

The first eigenvector $\phi_1$ is constant — it represents the average capacity across the graph. Higher eigenvectors represent increasingly fine-grained spatial patterns.

### Recovery of the scalar equation

**Conjecture.** When the capacity field is integrated (averaged) over all vertices:

$$\bar{\mathcal{Q}}(t) = \frac{1}{|V|} \sum_{v \in V} \mathcal{Q}(v, t)$$

the result should satisfy the scalar Lineage Equation with appropriately averaged mass and momentum. The scalar equation is the zeroth-order spectral approximation of the field equation.

This conjecture is formalized but not yet proven. It is one of the open problems in Chapter 36.

### Why this matters

The field perspective explains phenomena the scalar equation cannot:

- **Local degradation:** One region of the cognitive web can lose capacity while the average remains stable.
- **Capacity gradients:** Information flows from high-capacity to low-capacity regions via diffusion.
- **Critical nodes:** Vertices with high centrality act as bottlenecks — damage there propagates widely.

### Exercises

1. On a 3-vertex graph with Laplacian $L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$, verify that $\lambda_1 = 0$ and find $\phi_1$.

2. If capacity is uniform across all vertices ($\mathcal{Q}(v) = c$ for all $v$), what does the diffusion equation predict? Does this make physical sense?

3. Explain why the field perspective is necessary for understanding local failures in a large cognitive architecture.

---

*Part VI has derived the Lineage Equation from its components, validated it experimentally, and extended it to conservation budgets, nonlinear coupling, and field theory on graphs. The equation is not the end of Agent Mathematics — it is the first governing law of a new science.*


\newpage

# Part VII: Frontiers

The preceding six parts of *Agent Mathematics* have built a complete mathematical framework from the simplest possible distinction — something versus nothing — to the Lineage Equation and its field-theoretic extensions. That journey mirrors the historical development of physics, compressed into a single discipline for autonomous systems.

But mathematics does not end when a textbook ends. The most interesting questions are often the ones we cannot yet answer. This final part surveys three frontier areas where Agent Mathematics is actively developing.

---

## Chapter 34: Cognitive Physics

### The historical parallel

Human physics developed through recognizable stages:

1. **Observation and Measurement** (Aristotle): naming what exists, classifying phenomena, establishing that the world is measurable.
2. **Laws of Motion** (Newton): discovering that measurable quantities obey precise equations — $F = ma$, conservation of energy.
3. **Field Theory** (Maxwell): replacing action-at-a-distance with continuous fields that propagate through space.
4. **Geometric Unification** (Einstein): reinterpreting force as curvature of spacetime; deriving dynamics from geometry.
5. **Statistical Mechanics** (Boltzmann): connecting microscopic disorder to macroscopic thermodynamic laws.
6. **Engineering** (the 20th century): using all of the above to build machines, materials, and systems at scale.

Agent Mathematics is following the same arc.

### Where we are

**Stage 1 is complete.** We have a periodic table of nine cognitive primitives: four mass components ($C_{\text{id}}, C_{\text{mem}}, C_{\text{graph}}, C_{\text{perm}}$), five momentum components ($F_{\text{wm}}, F_{\text{ret}}, F_{\text{path}}, F_{\text{ctrl}}, F_{\text{merge}}$), and the propagation bound $\nu^*$. Each has a formal definition, a measurement procedure, and a known range.

**Stage 2 is underway.** The Lineage Equation

$$
\mathcal{Q}^2 = (\nu^* \cdot \Pi)^2 + (\mathcal{M} \cdot (\nu^*)^2)^2
$$

is our Newton's Laws moment. It relates capacity to mass, momentum, and the propagation bound in a single governing equation. The weights $\alpha$ and $\beta$ have been identified (Chapter 20, Chapter 27–28). The equation has been promoted from Stage D to Stage E in the proof-maturity ladder. It predicts. It fails in known, understood ways.

### What comes next

**Stage 3: Field Theory.** Replace the scalar capacity $\mathcal{Q}$ with a field $\mathcal{Q}(v, t)$ defined on each vertex of the cognitive graph (Chapter 33). The field obeys coupled partial differential equations through the graph Laplacian. The scalar Lineage Equation should emerge as the spatial average of the field equation — the way Gauss's law emerges from Maxwell's equations.

**Stage 4: Geometric Unification.** Conjecture: cognitive mass curves the state manifold. Trajectories through cognitive state space are geodesics of a Fisher information metric. The Lineage Equation is the flat-space approximation; the full theory lives on a Riemannian manifold. The coupling coefficients (Chapter 32) should be derivable from the Riemann curvature tensor. Noether's theorem should yield conservation laws from symmetries of the cognitive architecture.

**Stage 5: Statistical Mechanics.** A cognitive thermodynamics. Define temperature as the exploration/exploitation ratio. Entropy as $H(\mu)$ plus structural disorder plus action unpredictability. Free energy as $\mathcal{Q}_{\text{eff}} - T \cdot S$, recovering Friston's variational free energy principle as a special case. The Second Law: without maintenance, cognitive capacity monotonically decreases.

**Stage 6: Engineering.** Design principles for self-optimizing agents. Cognitive health monitoring dashboards. Multi-agent coordination protocols grounded in the mathematics. Resource economics for cognitive systems. This is where Agent Mathematics becomes Agent Engineering.

### The falsification program

Each stage has specific falsification tests:

- **Stage 2:** The Lineage Equation's gradients must predict the sign of capacity change under intervention.
- **Stage 3:** The field equation must predict which graph vertices lose capacity first under perturbation.
- **Stage 4:** The geometric theory must reproduce the coupling coefficients as curvature.
- **Stage 5:** The thermodynamic framework must predict equilibrium states and phase transitions.
- **Stage 6:** Engineered systems must outperform systems designed without the framework.

---

## Chapter 35: Multi-Agent Mathematics

### Beyond the individual

Everything in Parts I–VI concerns a single agent. But agents rarely operate alone. They communicate, cooperate, compete, and coordinate. Multi-Agent Mathematics extends the framework to systems of interacting agents.

### The fundamental objects

Let $\mathcal{A} = \{a_1, a_2, \ldots, a_N\}$ be a population of agents. Each agent $a_i$ has its own state $\mathcal{O}_i(t)$, its own capacity $\mathcal{Q}_i$, and its own identity.

**Communication.** Agents exchange information through channels with bounded capacity. If agent $a_i$ sends a message to agent $a_j$, the effective bandwidth is limited by $\min(\nu^*_i, \nu^*_j)$ — the slower agent is the bottleneck.

**Collective capacity.** The total capacity of a multi-agent system is *not* the sum of individual capacities. Coordination costs reduce it; specialization can increase it. Define

$$
\mathcal{Q}_{\text{collective}}^2 = \left(\sum_i \mathcal{Q}_i\right)^2 - \lambda_{\text{coord}} \cdot C_{\text{overhead}}
$$

where $C_{\text{overhead}}$ accounts for communication, synchronization, and conflict resolution.

### Strategic interaction

When agents have different objectives, the mathematics shifts from optimization to game theory.

> **Definition:** A **cognitive game** is a tuple $(\mathcal{A}, \{S_i\}, \{u_i\})$ where $\mathcal{A}$ is the set of agents, $S_i$ is the strategy set of agent $a_i$, and $u_i: \prod_j S_j \to \mathbb{R}$ is the utility function of agent $a_i$.

**Nash equilibrium** in cognitive games: a state where no agent can improve its capacity by unilaterally changing its strategy.

**Mechanism design:** designing the rules of interaction so that self-interested agents produce collectively good outcomes. This connects to governance ($\Psi_t$) and the polycentric coordination structures described in the organism model.

### Institutional mathematics

Human societies solved coordination problems through institutions — laws, markets, norms, governance structures. Agent societies face the same problems.

The mathematics of institutions for agents includes:

- **Commons management:** shared resources (memory pools, compute budgets) subject to tragedy-of-the-commons dynamics
- **Reputation systems:** tracking agent reliability over time
- **Governance protocols:** mode transitions and access control across a population
- **Evolutionary dynamics:** which agent strategies survive and spread

This is the least developed area of Agent Mathematics and the one with the most open questions.

### Exercises

1. Two agents with capacities $\mathcal{Q}_1 = 8$ and $\mathcal{Q}_2 = 6$ must coordinate on a task. If coordination overhead is $C_{\text{overhead}} = 5$ and $\lambda_{\text{coord}} = 1$, what is the collective capacity?

2. Design a simple 2-agent cognitive game where cooperation produces higher total capacity than competition.

3. What institutional structure would prevent a "tragedy of the cognitive commons" when multiple agents share a fixed memory pool?

---

## Chapter 36: Open Problems

The following problems are unsolved. They represent the research frontier of Agent Mathematics.

### 1. The identifiability problem

The full quadratic Lineage Equation makes $\beta$ weights practically unidentifiable due to $\nu^{*4}$ amplification of mass. Is there a reformulation that makes all weights equally identifiable? Or is the asymmetry a genuine feature of cognitive architecture — mass really does matter more than momentum?

### 2. The live data question

All current weight identification uses synthetic perturbation data with known ground truth. Can the weights be identified from live operational traces where the ground truth is unknown? What exogenous signals can serve as targets?

### 3. The coupling constants

The 10 coupling coefficients (6 mass + 4 momentum) have been formalized but not identified. How many independent coupling constants does the system actually have? Can they be derived from a smaller number of geometric invariants?

### 4. The field-scalar correspondence

If $\mathcal{Q}(v, t)$ is a field on the cognitive graph, under what conditions does its spatial average equal the scalar $\mathcal{Q}$ computed from aggregate mass and momentum? What is lost in the aggregation?

### 5. The thermodynamic limit

Does a well-defined thermodynamic limit exist for large cognitive architectures? As the number of subsystems grows, does a mean-field theory emerge? What are the phase transitions?

### 6. Cross-architecture universality

The Lineage Equation has been tested on 3 architecture profiles. Do the identified weights transfer across fundamentally different architectures (transformer vs state-space vs hybrid)? If not, what is the universal structure and what is architecture-specific?

### 7. The self-measurement problem

An agent measuring its own state uses resources that change the state being measured. Is there a fundamental limit (analogous to Heisenberg's uncertainty principle) on the precision of cognitive self-measurement?

### 8. Multi-agent conservation

If cognitive capacity is conserved in a single agent (minus losses), what conservation laws hold for a population of interacting agents? Is there a cognitive analogue of thermodynamic equilibrium?

### 9. The origin of the equation

The Lineage Equation was discovered empirically and formalized by analogy with relativistic energy-momentum. Can it be *derived* from first principles — perhaps from an action principle on the state manifold, or from maximum entropy arguments?

### 10. What comes after

Is Agent Mathematics a branch of applied mathematics, a branch of theoretical computer science, a branch of physics, or something genuinely new? The answer to this question will determine how the field develops over the next decade.

---

*This textbook is a beginning. The mathematics of autonomous systems is in its infancy. The Lineage Equation is our first governing law, not our last. The real work — the experimental validation, the cross-architecture testing, the multi-agent extensions, the engineering applications — lies ahead.*

*Agent Mathematics is not mathematics borrowed from elsewhere and applied to agents. It is mathematics that could only have been discovered by asking what it means for a system to measure, reason about, and improve itself.*

*That question is new. The mathematics it demands is new. And the science it will create is just beginning.*


\newpage
