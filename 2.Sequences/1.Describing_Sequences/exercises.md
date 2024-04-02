 
### 1. Find the closed formula for each of the following sequences by relating them to a well known sequence. Assume the first term given is $a_1$.

a. $2, 5, 10, 17, 26,...$
>$d_n = a_{n + 1} - a_n$<br>
$d_1 = 3, d_2 = 5, d_3 = 7, d_4 = 9$<br>

>Second difference $ = d_{2nd}$<br>
$d_{2nd} = d_{n+1} - d_{n}$<br>
$d_{2nd} = 9 - 7$<br>
$d_{2nd} = 2$<br>

>$2a = d_{2nd}$ <br>
$2a = 2$<br>
$a = 1$<br>
$3a + b = d_1$<br>
$3 + b = 3$<br>
$b = 0$<br>
$a + b + c = a_1$<br>
$1 + 0 + c = 2$<br>
$c = 1 $<br>
$an^2 + bn + c$<br>
$1n^2 + 0n + 1$<br>
$a(n)=n^2 + 1$<br>


b. $0, 2, 5, 9, 14, 20,...$
>$d_n = a_{n + 1} - a_n$<br>
$d_1 = 2, d_2 = 3, d_3 = 4, d_4 = 5,  d_4 = 6$<br>

>$d_{2nd} = d_{n+1} - d_{n}$<br>
$d_{2nd} = 1 $<br>

>$a = 1/2$<br>
$3a + b = 2$<br>
$3/2 + b = 2$<br>
$b = 1/ 2$<br>
$a + b + c = 0$<br>
$1 / 2 + 1 / 2 + c = 0$<br>
$c = -1$<br>
$an^2 + bn + c$<br>
$1/2n^2 + 1/2n - 1$<br>
$(n^2 + n)/2 - 1$<br>
$(n(n+1))/2 - 1$<br>

c. $8, 12, 17, 23, 30,...$<br>
>$a = 1 / 2$<br>
$3 a + b = 4$<br>
$b = 4 - 3 / 2$<br>
$b = 5 / 2$<br>
$a + b + c = 8$<br>
$1 / 2 + 5 / 2 + c = 8$<br>
$c=5$<br>
$\frac{1}{2} n^2 + \frac{5}{2} n + 5 $ $or$
$\frac{(n+2)(n+3)}{2} +2$<br>

d. $1, 5, 23, 119, 719,...$
>$(n+1)! - 1$ 


### 2. For each sequence given below, find a closed formula for $a_n$, the $n_{th}$ term of the sequence (assume the first terms are $a_0$) by relating it to another sequence for which you already know the formula. In each case, briefly say how you got your answers.

a. 4, 5, 7, 11, 19, 35, …
>Substract 3 to all the numbers in the sequence gives you a cuadratic sequence, therefore $a(n) = 2^n + 3$ 

b. 0, 3, 8, 15, 24, 35, …
> $2a = 2$<br>
$a = 1$ <br>
$3a + b = 3$<br>
$ b = 0$
$a + b + c = 0$<br>
$ 1 + 0 + c = 0 $<br>
$c = -1$ <br>
$(n+1)^2 - 1$<br>

c. 6, 12, 20, 30, 42, ...
> $2a = 2$<br>
$a = 1$ <br>
$3a + b = 6$<br>
$ b = 3$
$a + b + c = 6$<br>
$ 1 + 3 + c = 6$<br>
$c = 2$ <br>
$(n+1)^2 + 3(n+1) + 2$<br>

d. 0, 2, 7, 15, 26, 40, 57, …
> $ 2a = 3$<br>
$ a = 3/2$<br>
$ 3a + b = 2$<br>
$ b = 2 - 9/2$<br>
$ b = - 5 / 2 $ <br>
$ a + b + c = 0$<br>
$ 3/2 - 5/2 + c = 0$<br>
$ c = 1$<br>
$\frac{3}{2}(n+1)^2 -\frac{5}{2}(n+1) + 1$ $or$ $\frac{(3n+1)(n)}{2}$<br>

### 3.Write out the first 5 terms (starting with $a_0$ ) of each of the sequences described below. Then give either a closed formula or a recursive definition for the sequence (whichever is NOT given in the problem).

a. $a_n = \frac{1}{2}(n^2+n)$

> $a_0 = 0, a_1 = 1, a_2 = 3, a_3 = 6 + a_4 = 10$<br>
Triangular sequence

b. $a_n = 2a_{n-1} - a_{n-2}$ with $a_0 = 0$ and $a_1 = 1$

> $a_2 = 2, a_3 = 3, a_4 = 4, a_5 = 5, a_6 = 6$<br>
Recursive sequence


c. $a_n = na_{n-1} $ with $a_{0} = 1$ 
>$a_1 = 1, a_2 = 2, a_3 = 6, a_4 = 24, a_5 = 120$<br>
Factorial sequence $a_n = n !$

### 4.Consider the sequence $(a_n)_{n\geq1}$ that starts $1, 3, 5, 7, 9, ...$(i.e., the odd numbers in order). that starts  (i.e., the odd numbers in order).
a. Give a recursive definition and closed formula for the sequence.

>Closed:
$a_n = 2n - 1$<br>
Recursive:
$a_n = a_{n-1} + 2$

b. Write out the sequence $(b_n)_{n\geq2}$
 of partial sums of $(a_n)$.
 Write down the recursive definition for $(b_n)$
 and guess at the closed formula.

>The sequence of partial sums is $1, 4, 9, 16, 25, 36, ...$<br> 
Recursive: $b_n = b_{n-1} + 2n -1$<br>
Closed: $b_n = n ^2$<br>

### The Fibonacci sequence is $0,1,1, 2, 3, 5, 8, 13, ...$ (where f_0 = 0).

a. Write out the first few terms of the sequence of partial sums: 0,0+1,0+1+1,...
> $0, 1, 2, 4, 7, 12, 20, 33, ...$

b. Guess a formula for the sequence of partial sums expressed in terms of a single Fibonacci number.
> $F_0 + F_1 + ... + F_n = F_{n+2}-1$ 
### 6. Consider the three sequences below. For each, find a recursive definition. How are these sequences related?
a. $2, 4, 6, 10, 16, 26, 42, ...$
b. $5, 6, 11, 17, 28, 45, 73, ...$
c. $0, 0, 0, 0, 0, 0, 0 ...$
> They all use $a_n = a_{a-2} + a_{n-1}$ the only difference is the initial values or conditions.

### 7. Write out the first few terms of the sequence given by $a_1 = 3$; $a_n = 2a_{n-1} + 4$.Then find a recursive definition for the sequence $10, 24, 52, 108, ...$.

> The first terms are $3, 10, 24, 52, 108, ...$
> Recursive definition is $a_n =2a_{n-1} + 4$ with an initial condition of $a_1 = 10 $

### 8. Write out the first few terms of the sequence given by $a_n = n^2 - 3n + 1$.Then find a closed formula for the sequence (starting with $a_1$) $0,2,6,12,20,...$.

> The first terms: $-1, -1, 1, 5, 11, 19$
> Closed Formula: $(n+1)^2 - 3(n+1) + 2$

### 9. Show that $a_n = 3*2^n +7 * 5^n$ is a solution to the recurrence relation $a_n = 7a_{n-1} - 10a_{n-2}$.What would the initial conditions need to be for this to be the closed formula for the sequence? 

>$7a_{n-1} - 10a_{n-2} = 7(3*2^{n-1}+ 7*5^{n-1}) - 10(3*2^{n-2}+ 7*5^{n-2}) = 3*2^n +7*5^n$<br>
Initial terms: $a_0 = 10, a_1 = 41$

### 10. Show that $a_n = 2^n - 5^n $ is also a solution to the recurrence relation $a_n = 7a_{n-1} - 10a_{n-2}$. What would the initial conditions need to be for this to be the closed formula for the sequence?

>$a_n = 7(a_{n-1}) - 10(a_{n-2})$<br>
$a_n = 7(2^{n-1} - 5^{n-1}) - 10(2^{n-2} - 5^{n-2})$<br>
$a_n = 7*2^{n-1} - 7*5^{n-1} - 10*2^{n-2} + 10*5^{n-2}$<br>
$a_n = 7*2^{n-1} - 7*5^{n-1} - 5*2^{n-1} + 2*5^{n-1}$<br>
$a_n = 2*2^{n-1} - 5*5^{n-1}$<br>
$a_n = 2^n - 5^n$<br>
It works,<br> 
Initial terms: a_0 = 0, -3

### 12. Give two different recursive definitions for the sequence with closed formula $a_n = 3 + 2n$. Prove you are correct. At least one of the recursive definitions should makes use of two previous terms and no constants.

>a)<br>
$a_{0-3} = \{ 3 , 5 , 7 , 9\} $<br>
$a_n = 2a_{n-1} - a_{n-2}$<br>
$a_n = 2(3 + 2(n-1)) - (3 + 2(n-2))$<br>
$a_n = 6 + 4n - 4 - 3 - 2n + 4$<br>
$a_n = 3 + 2n $<br>

>b)<br>
$a_n = a_{0} + a_{n-1} - 1$<br>
$a_n = 3 + 2*0 + (3 + 2(n-1)) - 1$<br>
$a_n = 3 + (3 + 2n-2) - 1$<br>
$a_n = 2 + 1 + 2n $<br>
$a_n = 3 + 2n $<br>


### 13. Use summation ($\sum$) or product ($\prod$) notation to rewrite the following.

>a. $2 + 4 + 6 + 8 + ... + 2n$ <br>
$\sum_{k=1}^{n} 2k$<br>

>b. $1 + 5 + 9 + 13 + ... + 425$ <br>   
$\sum_{k=0}^{106}(1 + 4k)$<br>

>c. $1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + ... + \frac{1}{50}$ <br>
$\sum_{k=1}^{50} \frac{1}{k}$<br>

>d. $2 * 4  * 6 * ... * 2n$ <br>
$\prod_{k=1}^{n} 2k$<br>

>e. $\frac{1}{2} + \frac{2}{3} + \frac{3}{4} + ... + \frac{100}{101}$ <br>
$\prod_{k=1}^{100} \frac{k}{k+1}$<br>

### 14. Expand the following sums and products. That is, write them out the long way.
>a) $\sum_{k=1}^{100}(3+4k)$<br>
$7 + 11 + 15 + ... + 403$

>b) $\sum_{k=0}^{n}2^k$<br>
$1 + 2 + 4 + 8 +... + 2^n$

>c) $\sum_{k=2}^{50}\frac{1}{(k^2 - 1)}$<br>
$\frac{1}{3} + \frac{1}{8} + \frac{1}{15} + \frac{1}{24} + ... + \frac{1}{2499}$

>d) $\prod_{k=2}^{100}\frac{k^2}{(k^2 - 1)}$<br>
$\frac{4}{3} * \frac{9}{8} * \frac{16}{15} * \frac{25}{24} * ... * \frac{10000}{9999}$

>e) $\prod_{k=0}^{n}(2 + 3k)$<br>
$2 * 5 * 8 * 11 * 14 * ... *(2 + 3n)$

### 15. Suppose you draw $n$ lines in the plane so that every pair of lines cross (no lines are parallel) and no three lines cross at the same point. This will create some number of regions in the plane, including some unbounded regions. Call the number of regions $R_n$. Find a recursive formula for the number of regions created by $n$ lines, and justify why your recursion is correct.

>Knowing that $NumberofSegments_{1}= 2$ By drawing lines that are not parallel each time you make a new line you create $n_{lines}-1$ ($n_{lines}$ = the number of lines) segments more meaning that: <br>
$NumberofSegments_{n_{lines}} = NumberofSegments_{n_{lines} - 1} + n_{lines}$ <br>
$NumberofSegments_{n_{lines}} = NumberofSegments_{n_{lines} - 2} + n_{lines} - 1 + n_{lines}$ <br>
$NumberofSegments_{n_{lines}} = NumberofSegments_{n_{lines} - 3} + n_{lines} - 2 + n_{lines} - 1 + n_{lines}$ <br>
$...$<br>
$NumberofSegments_{n_{lines}} = \frac{n_{lines}(n_{lines} + 1)}{2} + 1$<br>

### 16. A ternary string is a sequence of 0's, 1's and 2's. Just like a bit string, but with three symbols. Let's call a ternary string good provided it never contains a 2 followed immediately by a 0. Let $G_n$ be the number of good strings of length $n$. For example, $G_1 = 3$, and $G_2 = 8$ (since of the 9 ternary strings of length 2, only one is not good). Find, with justification, a recursive formula for , and use it to compute . Find, with justification, a recursive formula for $G_n$, and use it to compute $G_5$.


>$G_n = 2G_{n−1}+G_{n−2}$<br>
$G_5 = 2G_{4}+G_{3}$<br>
$G_5 = 2(2G_{3}+G_2)+G_{3}$<br>
$G_5 = 5G_{3}+2G_2$<br>
$G_5 = 5(2G_{2}+1G_{1})+2G_2$
$G_5 = 12G_{2}+5G_{1}$<br>
$G_5 = 12(8)+5(3)$<br>
$G_5 = 111$

### 17. Consider bit strings with length $l$ and weight $k$ (so strings of $l$ 0's and 1's, including $k$ 1's). We know how to count the number of these for a fixed $l$ and $k$. Now, we will count the number of strings for which the sum of the length and the weight is fixed. For example, let's count all the bit strings for which $l + k = 11$.

a) Find examples of these strings of different lengths. What is the longest string possible? What is the shortest?
>00000000000
>111110
b) How many strings are there of each of these lengths. Use this to count the total number of strings (with sum 11).

c) The other approach: Let 
 vary. How many strings have sum ?
 How many have sum ?
 And so on. Find and explain a recurrence relation for the sequence 
 which gives the number of strings with sum .

d) Describe what you have found above in terms of Pascal's Triangle. What pattern have you discovered?


