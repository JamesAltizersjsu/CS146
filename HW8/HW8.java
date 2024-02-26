public class LongestPalindromicSubstring {

    public static String longestPalindrome(String s) {
        if (s.isEmpty()) {
            return "";
        }

        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int start = 0; // Start index of the longest palindromic substring
        int maxLength = 1; // Length of the longest palindromic substring

        // All substrings of length 1 are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        // Check for palindromes of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                start = i;
                maxLength = 2;
            }
        }

        // Check for palindromes of length 3 or more
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1; // Ending index of the current substring
                // Check if the current substring is a palindrome
                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    // Update the longest palindrome information if needed
                    if (len > maxLength) {
                        start = i;
                        maxLength = len;
                    }
                }
            }
        }

        // Extract and return the longest palindromic substring
        return s.substring(start, start + maxLength);
    }

    public static void main(String[] args) {
        String inputString = "forgeeksskeegfor";
        String result = longestPalindrome(inputString);
        System.out.println("Longest palindrome substring is: " + result);
        System.out.println("Length is: " + result.length());
    }
}
