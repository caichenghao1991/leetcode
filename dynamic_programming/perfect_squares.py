# 279. Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, int(n ** 0.5 + 1)):
            for j in range(1, n + 1):
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[n]
