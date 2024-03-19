# Exercises

#### 1. 	Your wardrobe consists of 5 shirts, 3 pairs of pants, and 17 bow ties. How many different outfits can you make?

>*Assuming* that we will always use 1 shirt, 1 pair of pants and 1 bow tie

$5 * 3 * 17 = 255$
####	2. For your college interview, you must wear a tie. You own 3 regular (boring) ties and 5 (cool) bow ties. 
- How many choices do you have for your neck-wear? 

	$3 + 5 = 8$

- You realize that the interview is for clown college, so you should probably wear both a regular tie and a bow tie. How many choices do you have now?
	
	$3 * 5 =15$

- For the rest of your outfit, you have 5 shirts, 4 skirts, 3 pants, and 7 dresses. You want to select either a shirt to wear with a skirt or pants, or just a dress. How many outfits do you have to choose from?

	$(shirts * (skirts + pants)) + dress = Noutfits$\
	$(5 * (4+3)) + 7 = 42$
#### 3. Your Blu-ray collection consists of 9 comedies and 7 horror movies. Give an example of a question for which the answer is: 
-	16\
    You feel like watching a movie but **only one** because you are busy. how many options of movies do you have in your Blu-ray collection?
-	63\
You wanna organize your movies, but you can't decide how, by alphabet, by genre, by how much you like them, **Too much options!!**, how many options do you have to organize them?.

#### 4. We usually write numbers in decimal form (or base $10$), meaning numbers are composed using $10$ different "digits" $\{0,1,\dots,9\}$. Sometimes though it is useful to write numbers in hexadecimal or base $16$. Now there are $16$ distinct digits that can be used to form numbers: $\{0,1,\dots,9,A,B,C,D,E,F\}$. So for example, a $3$ digit hexadecimal number might be $2B8$.  

-	How many $2$-digit hexadecimals are there in which the first digit is $E$ or $F$? Explain your answer in terms of the additive principle (using either events or sets).  
>	If the first digit is an $E$, there are $16$ other digits (including $E$) the second digit could be. We have the same case with $F$.
	
	$16 + 16 = 32$  
  
-	Explain why your answer to the previous part is correct in terms of the multiplicative principle (using either events or sets). Why do both the additive and multiplicative principles give you the same answer?

> Because there are two digits (two spaces to fill) The multiplicative principle and additive principle gives you the same answer.
	$(2 x 16) = 32 $
  
-	How many $3$-digit hexadecimals start with a letter ($A$-$F$) and end with a numeral ($0$-$9$)? Explain.  
- $960$ as $(6\cdot 16\cdot 10 ) = 960$, the first digit of these hexadecimal numbers is any element from the set ($A$-$F$), the second digit is any element from the set ($0$-$F$), and the third digit is any element from the set ($0$-$9$), where the choice from any set does not impact any other set, so we use the **multiplicative principle**.  
  
d. How many $3$-digit hexadecimals start with a letter ($A$-$F$) or end with a numeral ($0$-$9$) (or both)? Explain.  
- The answer is $16^3$ or $4096$ because the statement allows every hexadecimal number with three digits.

---

#### 5. Suppose you have sets $A$ and $B$ with $|A| = 10$ and $|B| = 15$.
a) What is the largest possible value for $|A\cap B|$?
- $10$, if all of the elements in $A$ are in $B$

b) What is the smallest possible value for $|A\cap B|$?
- $0$. if none of the elements in $A$ are in $B$.

c) What are the possible values for $|A\cup B|$?
- the answer is between $15$ and $25$, depending on how many elements $A$ and $B$ share.

---

#### 6. If $|A| = 8$ and $|B| = 5$, what is $|A\cup B| + |A\cap B| = 13$?
> $|A\cup B| = 8$, and $|A\cap B| = 5$, then $8 + 5 =13$.

---

#### 7. A group of college students were asked about their TV watching habits.  Of those surveyed, $28$ students watch *The Walking Dead*, $19$ watch *The Blacklist*, and $24$ watch _Game of Thrones_. Additionally, $16$ watch _The Walking Dead_ and _The Blacklist_, $14$ watch _The Walking Dead_ and _Game of Thrones_, and $10$ watch _The Blacklist_ and _Game of Thrones_. There are $8$ students who watch all three shows. How many students surveyed watched at least one of the shows?

> $(28 + 19 + 24) - (16 + 14 + 10) + 8 = 39$, add the singles and triples, and subtract the doubles.

---

#### 8. In a recent survey, 30 students reported whether they liked their potatoes Mashed, French-fried, or Twice-baked. 15 liked them mashed, 20 liked French fries, and 9 liked twice baked potatoes. Additionally, 12 students liked both mashed and fried potatoes, 5 liked French fries and twice baked potatoes, 6 liked mashed and baked, and 3 liked all three styles. How many students _hate_ potatoes? Explain why your answer is correct.
> $(15 + 20 + 9) - (12 + 5 + 6) + 3 = 24$.  $24$ is the number of people who like potatoes, so we can do $30 - 24 = 6$ to get the number of people who don't like potatoes.

#### 9. For how many n ∈ {1, 2, . . . , 500} is n a multiple of one or more of 5, 6, or 7?
> $A = 500 / 5 = 100$
$B = 500 / 6 = 83.333 = 83$
$C = 500 / 7 = 71.43 = 71$
$A /cap B 500 / 30 = 16$
$A /cap C= 500 / 35 = 14$
$B /cap C = 500 / 42 = 11$
$A /cap B /cap C = 500 / 210 = 2$
$A /cup B /cup C = A + B + C - A /cap B - A/cap C - B /cap C + A /cap B /cap C$ 
> Answer = $ 215 $
#### 10. How many positive integers less than 1000 are multiples of 3, 5, or 7?
#### Explain your answer using the Principle of Inclusion/Exclusion.

>$A = 1000 / 3 = 333$ \
$B = 1000 / 5 = 200$ \
$C = 1000 / 7 =  = 142$\
$A /cap B 1000 / 15 = 66$\
$A /cap C= 1000 / 21 = 47$\
$B /cap C = 1000 / 35 = 28$\
$A /cap B /cap C = 1000 / 105 = 9$\
$A /cup B /cup C = A + B + C - A /cap B - A/cap C - B /cap C + A /cap B /cap C$ \
>Answer = $ 333 + 200 + 142 - 66 - 47 - 28 + 9 = 543$
#### 11. Let A, B, and C be sets. 
 - (a) Find $|(A \cup C) \setminus B|$ provided $|A| = 50$, $|B| = 45$, $|C| = 40$, $|A \cap B| = 20$, $|A \cap C| = 15$, $|B \cap C| = 23$, and $|A \cap B \cap C| = 12$. 
> $|(A \cup C) \setminus B| = 44.$
 - (b) Describe a set in terms of $A$, $B$, and $C$ with cardinality 26.
> $(A \cap B \cap C) - (C \setminus A) \setminus B$

#### 12. Consider all 5 letter “words” made from the letters a through h.(Recall, words are just strings of letters, not necessarily actual English words.)
- (a) $8^5 = 32768$ words.
- (b) $8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 = 6720$ words.
- (c) $8 \cdot 8 = 64$ words.
- (d) $64 + 64 - 0 = 128$ words.
- (e) $(8 \cdot 7 \cdot 6 \cdot 5 \cdot 4) - 3 \cdot (5 \cdot 4) = 6660$ words.

#### 13. For how many three digit numbers (100 to 999) is the sum of the digits even? (For example, 343 has an even sum of digits: $ 3 + 4 + 3 = 10 $ which is even.) Find the answer and explain why it is correct in at least two different ways.

I ran this python function and it gave me 450 ;p
```
def Three_four_three():
	tft = set()
    for a in range(1,9):
        for b in range(9):
            for c in range(9):
                if (a + b + c) % 2 == 0:
                    n = a*100 + b*10 + c
                    tft.add(n)
    return sorted(tft)
```
Since we have numbers from 100 to 999.
we will have a range of 900 numbers: Uplimit - Lowlimit + 1 = range
Every 10-number subrange as 100–109 or 110–119 has 5 elements the sum of whose digits is even.
we have 90 subets of 10 numbers inside the 900 numbers and we now that there are 5 numbers in each subset that the sum of their digits is even.
Equation:
> 900 / 10 = 90 
> 90 * 5 = 450

#### 14. The number 735000 factors as $2^3· 3 · 5^4· 7^2$. How many divisors does it have? Explain your answer using the multiplicative principle.
$4*2*5*3 + 1$ 