# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s) + 1, len(t) + 1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(len(s)):
            dp[i][0] = 1
        # for j in range(1, len(t)):
        #     dp[0][j] = 0
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
