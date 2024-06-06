## 7. The two problems below can be solved using graph coloring. For each problem, represent the situation with a graph, say whether you should be coloring vertices or edges and why, and use the coloring to solve the problem.

a. Your Quidditch league has 5 teams. You will play a tournament next week in which every team will play every other team once. Each team can play at most one match each day, but there is plenty of time in the day for multiple matches. What is the fewest number of days over which the tournament can take place?

![completegrap]((a).png)

> It would be 5 days since each of the 5 colors would represent the 5 days and the edges would represent the 2 days that they can play per day.  

b. Ten members of Math Club are driving to a math conference in a neighboring state. However, some of these students have dated in the past, and things are still a little awkward. Each student lists which other students they refuse to share a car with; these conflicts are recorded in the table below. What is the fewest number of cars the club needs to make the trip? Do not worry about running out of seats, just avoid the conflicts.

![completegrap](student_conflicts.png)

$Vertex set: {A,B,C,D,E,F,G,H,I,J}$

$Edge set: (A−B),(A−E),(A−J),(B−A),(B−D),(B−G),(C−H),(C−J),(D−B),(D−F),(E−A),$
$(E−I),(F−D),(F−J),(G−B),(H−C),(H−I),(I−E),(I−H),(I−J),(J−A),(J−C),(J−F),(J−I)$

> We use the conflicting sets that conflict to make our graphs

$Conflictsets:{(A−B),(A−E),(A−J),(B−D),(B−G),(C−H),(C−J),(D−F),(E−I),(F−J),(H−I)}$



![completegrap](b.png)



## 9. Not all graphs are perfect. Give an example of a graph with chromatic number 4 that does not contain a copy of $K_4$. That is, there should be no 4 vertices all pairwise adjacent.
The wheel graph below has this property. The outside of the wheel forms an odd cycle, so requires 3 colors, the center of the wheel must be different than all the outside vertices.

![completegrap](9img.png)

## 10. Find the chromatic number of the graph below and prove you are correct.
![alt text](10.png)

This is a Grötzsch graph and it has the following properties: 11 vertices and 20 edges. It is triangle-free and it has a chromatic number of 4. 
The graph can be constructed by taking a 5-cycle and replacing each vertex with a "fan" of three vertices.

Let's attempt to color the vertices using 3 colors: Red (R), Blue (B), and Green (G).

Assign color to vertex 0:

Without loss of generality, color vertex 0 with Red (R).
Assign colors to adjacent vertices 1, 2, 3, 4:

Vertices 1, 2, 3, and 4 must be colored with either Blue (B) or Green (G) since they are all adjacent to vertex 0.
Suppose vertex 1 is Blue (B), vertex 2 is Green (G), vertex 3 is Blue (B), and vertex 4 is Green (G).
Continue with vertices 5, 6, 7, 8, 9, 10:

Vertex 5 must be adjacent to vertices 1 (B) and 2 (G), so it must be Red (R).
Vertex 6 must be adjacent to vertices 1 (B) and 3 (B), creating a conflict since both adjacent vertices have the same color and cannot use either Blue (B) or Green (G). Thus, vertex 6 cannot be colored with Red (R).
At this point, we encounter a contradiction:

Vertex 6 is adjacent to two vertices (1 and 3), both of which are Blue (B). According to our assumption, we cannot color vertex 6 with Blue (B) or Green (G) because both colors are already used by its adjacent vertices.
 
This contradiction demonstrates that Grötzsch graph is not 3-colorable

what is left to do is show that the Grötzsch graph has a chromatic number of four by 

![alt text](image.png)