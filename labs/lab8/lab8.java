public int coinChange(int[] coins, int amount) {
    int n = coins.length;
    int[][] dp = new int[n + 1][amount + 1];

    // Initialize base cases
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 1; // There's one way to make sum 0 (by not selecting any coin)
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= amount; j++) {
            dp[i][j] = dp[i - 1][j]; // Exclude the current coin
            if (j >= coins[i - 1]) {
                dp[i][j] += dp[i][j - coins[i - 1]]; // Include the current coin
            }
        }
    }

    return dp[n][amount] == 0 ? -1 : dp[n][amount];
}
