# 746. Min Cost Climbing Stairs
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = [1000000] * (len(cost) + 1)
        #
        # def dp(cur):
        #     if cur <= 1: return 0
        #     if memo[cur] != 1000000: return memo[cur]
        #     for i in [1, 2]:
        #         memo[cur] = min(memo[cur], dp(cur - i) + cost[cur - i])
        #     return memo[cur]
        #
        # dp(len(cost))
        # return memo[len(cost)]
        #
        #
        # dp = [1000000] * (len(cost) + 1)
        # dp[0], dp[1] = 0, 0
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[len(cost)]


        pre, cur = 0, 0
        for i in range(2, len(cost) + 1):
            cur, pre = min(cur + cost[i - 1], pre + cost[i - 2]), cur
        return cur
