James Altizer SID:014485458
1. Converting Adjacency List to Adjacency Matrix
An adjacency list represents a graph by associating each vertex with a list of its neighboring vertices. On the other hand, an adjacency matrix is a 2D array where each cell (i, j) indicates whether there is an edge between vertices i and j.

Pseudocode for Converting Adjacency List to Adjacency Matrix:
function adjacencyListToMatrix(adjList):
    n = length(adjList)  # Number of vertices
    matrix = initialize n x n matrix with all zeros
    
    for each vertex v in adjList:
        for each neighbor u in adjList[v]:
            matrix[v][u] = 1  # Set the corresponding cell to 1
    
    return matrix
Explanation:
Initialize an empty n x n matrix (where n is the number of vertices).
For each vertex v in the adjacency list:
Iterate through its neighbors (u) in the adjacency list.
Set the corresponding cell in the matrix to 1 if there is an edge between v and u.
2. Converting Adjacency Matrix to Adjacency List
Pseudocode for Converting Adjacency Matrix to Adjacency List:
function matrixToAdjacencyList(matrix):
    n = length(matrix)  # Number of vertices
    adjList = initialize an empty dictionary
    
    for each vertex v in range(n):
        neighbors = []
        for each vertex u in range(n):
            if matrix[v][u] == 1:
                neighbors.append(u)
        adjList[v] = neighbors
3. Reversing the Direction of Edges in a Directed Graph
Given a directed graph, we want to reverse the direction of each edge.

Pseudocode for Reversing Edge Directions:
function reverseEdges(graph):
    reversedGraph = initialize an empty dictionary
    
    for each vertex v in graph:
        reversedGraph[v] = []  # Initialize an empty list for each vertex
    
    for each vertex v in graph:
        for each neighbor u in graph[v]:
            reversedGraph[u].append(v)  # Reverse the edge direction
nested edge detection#

return reversedGraph
 Initialize an empty dictionary (reversedGraph) to store the reversed graph.
For each vertex v in the original graph:
Initialize an empty list for the v in reversedGraph.
For each vertex v in the original graph:
For each neighbor u of v:
Add v to the list of neighbors for u in reversedGraph.

