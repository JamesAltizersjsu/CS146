Consider the following directed acyclic graph (DAG):
    1
   / \
  2   3
 / \   \
4   5   6
Vertices: 1, 2, 3, 4, 5, 6
Edges: (1 → 2), (1 → 3), (2 → 4), (2 → 5), (3 → 6)
1. Kahn’s Algorithm (BFS) for Topological Sorting
Initialize in-degrees for each vertex:
in_degree1 = 0
in_degree2 = 1
in_degree3 = 1
in_degree4 = 1
in_degree5 = 1
in_degree[6] = 1
Start with vertices having in-degree 0: {1}
Process vertices in BFS order:
Remove 1 from the queue, add it to the result.
Decrease in-degrees of 2 and 3.
Add 2 and 3 to the queue.
Repeat until the queue is empty.
Result: [1, 2, 3, 4, 5, 6]
2. Topological Sort using DFS
Start DFS from any unvisited vertex (e.g., 1).
Recursively visit neighbors:
Visit 2, then 4 and 5.
Backtrack to 2, visit 3, then 6.
Result: [4, 5, 2, 6, 3, 1]
3. Topological Sort using BFS
Initialize in-degrees and queue as in Kahn’s algorithm.
Process vertices in BFS order:
Remove 1 from the queue, add it to the result.
Decrease in-degrees of 2 and 3.
Add 2 and 3 to the queue.
Repeat until the queue is empty.
Result: [1, 2, 3, 4, 5, 6]
Some processes have to come before others, but not all have to be sequential
Key to understanding topological sort: node with indegree of 0 must come first, node with outdegree of 0 must come last
Ways to do it:
Kahn’s Algorithm: count and decrement indegrees
Add all nodes with in-degree 0 to a queue and add them to the list
While queue is not empty
Remove from queue
add to sorted result (if not already present)
