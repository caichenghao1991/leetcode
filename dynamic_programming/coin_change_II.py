# 518. Coin Change II
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # l, k = len(coins), 0
        # dp = [[0] * (amount + 1) for _ in range(l)]
        # while k * coins[0] < amount + 1:
        #     dp[0][k * coins[0]] = 1
        #     k += 1
        #
        # for i in range(1, l):
        #     for j in range(amount + 1):
        #         if j - coins[i] >= 0:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return dp[l - 1][amount]


        l, k = len(coins), 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(l):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]
