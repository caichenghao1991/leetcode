# 343. Integer Break
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            res = 0
            for j in range(1, i // 2 + 1):
                res = max(res, dp[i - j] * j, (i - j) * j)
            dp[i] = res
        return dp[n]
