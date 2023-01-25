# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1, l2 = len(s) + 1, len(t) + 1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1] == len(s)
