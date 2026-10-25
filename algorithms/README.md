## Algorithms

List of additional algorithms. The next list do not follow a particular order:

- [Grid DFS](grid-dfs.md)
- [Graph - Topological Sort](#graph---topological-sort)

### Graph - Topological Sort

i use the notes from Stanford:

- title: CS 106X, Lecture 25 Topological Sort

see: https://web.stanford.edu/class/archive/cs/cs106x/cs106x.1192/lectures/Lecture25/Lecture25.pdf.

the notes that i follow said this:

1. Find node with in-degree of 0.
2. Add it at the end of our topological ordering so far, and remove it and it's edges from the
graph.
3. Repeat it until no nodes left.

one of the lectures explain a little improvement

x. use a set to store the 0 in degree nodes
x. use a dict to store all in degrees

those two tables help us to "remove" the edges that we visit already, for example if we have this
graph:

```bash
a -> c
a -> f
b -> c
d -> e
```

in `c` in degree is 2, if we process `a` he will be removed and his edges, so,

x. the `c` in degree will be 1
x. the `f` in degree will be 0

one invariant is that we are assuming that the graph do not have cycles, if so, the path will be a
partial path

about the Big O, i am thinking that is O(V+E) as we are traversing the graph adjacency list

### Source Code

- [graph.py](graph.py)

### Todo

- Read about the type of edges in a DiGraph

see: https://home.cse.ust.hk/faculty/golin/COMP271Sp03/Notes/MyL08.pdf

- {Forward, Back, Cross} edge
