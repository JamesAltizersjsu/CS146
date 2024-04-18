4/17/24 james altizer
for this lab i used the O(n^3) polynomial time complexity floyd-warshall algorithmn to find the number of citites reachable in a certain
distance. basically initialize a matrix [i][j] and then use the floyd-warshall algo given by this line to iterate and add up the cities
reachable through a certain distance in this case 4 
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
Example 1: Input:

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

Output: 3 (City 3 has 2 neighboring cities within the distanceThreshold)

Example 2: Input:

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

Output: 0 (City 0 has 1 neighboring city within the distanceThreshold)
