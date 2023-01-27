# 516. Longest Palindromic Subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][l - 1]
