public int findTheCity(int n, int[][] edges, int distanceThreshold) {
    // Initialize the distance matrix
    int[][] dist = new int[n][n];
    for (int i = 0; i < n; i++) {
        Arrays.fill(dist[i], Integer.MAX_VALUE);
        dist[i][i] = 0;
    }

    // Update distances based on edges
    for (int[] edge : edges) {
        int from = edge[0];
        int to = edge[1];
        int weight = edge[2];
        dist[from][to] = weight;
        dist[to][from] = weight;
    }

    // Floyd-Warshall algorithm
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    int minNeighbors = Integer.MAX_VALUE;
    int resultCity = -1;

    // Count reachable neighbors for each city
    for (int i = 0; i < n; i++) {
        int neighbors = 0;
        for (int j = 0; j < n; j++) {
            if (i != j && dist[i][j] <= distanceThreshold) {
                neighbors++;
            }
        }
        if (neighbors <= minNeighbors) {
            minNeighbors = neighbors;
            resultCity = i;
        }
    }

    return resultCity;
}
