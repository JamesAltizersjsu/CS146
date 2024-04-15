import java.util.*;

public class Solution {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        List<int[]> edges = new ArrayList<>();
        int[] wellCosts = new int[n + 1];
        for (int i = 0; i < n; i++) {
            wellCosts[i + 1] = wells[i];
            edges.add(new int[] {0, i + 1, wells[i]});
        }
        for (int[] pipe : pipes) {
            edges.add(new int[] {pipe[0], pipe[1], pipe[2]});
        }
        // Use Collections.sort() to sort the list of integer arrays
        Collections.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));

        int[] parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        int totalCost = 0;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], cost = edge[2];
            int rootU = find(parent, u);
            int rootV = find(parent, v);
            if (rootU != rootV) {
                parent[rootU] = rootV;
                totalCost += cost;
            }
        }

        return totalCost;
    }

    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }

    public static void main(String[] args) {
        int n = 2;
        int[] wells = {1, 1};
        int[][] pipes = {{1, 2, 1}, {1, 2, 2}};
        Solution solution = new Solution();
        int minCost = solution.minCostToSupplyWater(n, wells, pipes);
        System.out.println("Minimum cost to supply water: " + minCost);  // Expected output: 2
    }
}
