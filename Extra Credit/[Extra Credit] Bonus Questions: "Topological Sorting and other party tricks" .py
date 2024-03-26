def topological_sort_kahn(adj, V):
    indegree = [0] * V
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1

    queue = []
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != V:
        print("Graph contains a cycle!")
        return []

    return result

# Example usage
n = 6
edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)

print("Topological sorting using Kahn's algorithm:", topological_sort_kahn(adj, n))
###DFS-based topological sorting explores the graph in depth-first order. We’ll use a stack to keep track of the ordering.
def dfs_topological_sort(adj, visited, stack, node):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs_topological_sort(adj, visited, stack, neighbor)
    stack.append(node)

def topological_sort_dfs(adj, V):
    visited = [False] * V
    stack = []
    for i in range(V):
        if not visited[i]:
            dfs_topological_sort(adj, visited, stack, i)
    return stack[::-1]

# Example usage (same graph as above)
print("Topological sorting using DFS:", topological_sort_dfs(adj, n))
##BFS-based topological sorting is similar to Kahn’s algorithm. We’ll use a queue to maintain the ordering.
def topological_sort_bfs(adj, V):
    indegree = [0] * V
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1

    queue = []
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != V:
        print("Graph contains a cycle!")
        return []

    return result

# Example usage (same graph as above)
print("Topological sorting using BFS:", topological_sort_bfs(adj, n))


