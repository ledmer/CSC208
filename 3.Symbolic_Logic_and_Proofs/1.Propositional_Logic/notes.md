### Closed formula
Truth Tables
Here's a question about playing Monopoly:

>If you get more doubles than any other player then you will lose, or if you lose then you must have bought the most properties.

True or false? We will answer this question, and won't need to know anything about Monopoly. Instead we will look at the logical form of the statement.

We need to decide when the statement $(P \rightarrow Q)\vee(Q \rightarrow R) $ is true. Using the definitions of the connectives in Section 0.2, we see that for this to be true, either $P \rightarrow Q$ must be true or $Q \rightarrow R$ must be true (or both). Those are true if either $P$ is false or $Q$ is true (in the first case) and $Q$ is false or $R$ is true (in the second case). So—yeah, it gets kind of messy. Luckily, we can make a chart to keep track of all the possibilities. Enter truth tables. The idea is this: on each row, we list a possible combination of T's and F's (for true and false) for each of the sentential variables, and then mark down whether the statement in question is true or false in that case. We do this for every possible combination of T's and F's. Then we can clearly see in which cases the statement is true or false. For complicated statements, we will first fill in values for each part of the statement, as a way of breaking up our task into smaller, more manageable pieces.

Since the truth value of a statement is completely determined by the truth values of its parts and how they are connected, all you really need to know is the truth tables for each of the logical connectives. Here they are:

<img src="img/3.1_Truth_Table.png" width="500" height="300">

None of these truth tables should come as a surprise; they are all just restating the definitions of the connectives. Let's try another one.

### TAUTOLOGY
<img src="img/3.1Tautology" width="500" height="400">

The statement about monopoly is an example of a tautology, a statement which is true on the basis of its logical form alone. Tautologies are always true but they don't tell us much about the world. No knowledge about monopoly was required to determine that the statement was true. In fact, it is equally true that “If the moon is made of cheese, then Elvis is still alive, or if Elvis is still alive, then unicorns have 5 legs.”
### Logical Equivalence
