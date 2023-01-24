# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]

        for i in range(l):
            if i - 1 < 0:
                # dp[i][0]=0
                dp[i][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[l - 1][0]