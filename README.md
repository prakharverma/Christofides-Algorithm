# Christofides Algorithm

## Introduction
Consider a day in a salesman's life. 
He wants to visit a number of cities in a day. 
Each city is separated by a distance and he wants to visit each city and 
return to the origin city with the minimum traveling distance possible. 
This problem of finding the shortest 
possible route is termed as **"Traveling Salesman Problem (TSP)"**.


TSP problem can be defined in the 
graph terms as each city being represented as a node and the edge connecting the two nodes representing the distance between them. The solution is a shortest possible path in the graph which traverses through each node and reach the origin node with the minimum possible weight.


Traveling salesman problem is an NP-hard problem.

**Christofides algorithm** is an approximate algorithm for solving 
Traveling Salesman Problem (TSP) in a metric space. 
It was first published by  Nicos Christofides in 1976. 
It guarantees that its solutions will be within a factor of 1.5 
of the optimal solution length.

By metric space we mean that the distance function satisfies the 
following properties:

 1. **Positive:** $D(x,y)>=0$
 2. **Symmetry:** $D(x,y) = D(y,x)$
 3. **Reflexive:** $D(x,y) = 0$ iff $x=y$
 4. **Triangle Inequaltiy:** $D(x,z) + D(z,y) >= D(x,y)$

## Algorithm details

The algorithm consists of the following steps:

1. Minimum Spanning Tree
2. Odd Degree Vertices
3. Minimum Weight Perfect Matching
4. Connected Multigraph
5. Eulerian Circuit
6. Hamiltonian Circuit

More details about the algorithm can be found on the [wikipedia page](https://en.wikipedia.org/wiki/Christofides_algorithm).
 
## Time Complexity
Christofides algorithm is O(n<sup>3</sup>) because this is the 
time it takes to calculate minimum weight perfect matching.

## Execution

```
python main.py
```

## Parameters
To change the parameters of the code, open **main.py**. 
Different parameters available are:
```
txt_file        : Input graph file
debug           : Whether to save intermediate outputs as well
source_node     : Source Node
debug_folder    : Debug folder where intermediate outputs will be saved
```
