def longest_palindrome(s):
    if not s:
        return ""

    n = len(s)
    longest_length = 1
    longest_start = 0

    # is_palindrome[i][j] will be 'true' if the string from index i to j is a palindrome.
    is_palindrome = [[False] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        is_palindrome[i][i] = True
 
    # Check for a sub-string of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
            longest_start = i
            longest_length = 2

    # Test each different length of potential 3+ length palindromes, k is the palindrome length testing
    for k in range(3, n + 1):
        # For each different length of palindrome you are testing, i is the starting index
        # if k=3, then i is from range(0, n- 3 + 1), so if len(s) = 7, then i is from range(0, 5)
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of current palendrome being tested
            # s[i] needs to equal s[j] for it to be a valid palindrome.
            # is_palindrome[i + 1][j - 1] is checking if the inner substring is a palindrome
            # so if len(s) = 7 and k = 3, then on first run if i = 0 and j = 2, then is_palindrome[1][1] is checked.
            # so if s = "abcdcba", then is_palindrome[1][1] is checking if "b" is a palindrome, which it is.
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
                if k > longest_length:
                    longest_start = i
                    longest_length = k

    return s[longest_start:longest_start + longest_length]


if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))  # Output: "bab"
