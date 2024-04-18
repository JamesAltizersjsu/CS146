def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Update distances based on edges
    for fromi, toi, weighti in edges:
        dist[fromi][toi] = weighti
        dist[toi][fromi] = weighti

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_neighbors = float('inf')
    result_city = -1

    # Count reachable neighbors for each city
    for i in range(n):
        neighbors = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if neighbors <= min_neighbors:
            min_neighbors = neighbors
            result_city = i

    return result_city
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))  # Output: 3
