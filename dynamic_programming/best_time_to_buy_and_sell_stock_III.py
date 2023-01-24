# 123. Best Time to Buy and Sell Stock III
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        l = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(l)]
        for i in range(l):
            # dp[i][0][0]=0
            dp[i][0][1] = -10 ** 10

        for i in range(l):
            for k in range(1, k):
                if i - 1 < 0:
                    # dp[i][1][0] = 0
                    dp[i][k][1] = -prices[0]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[l - 1][2][0]