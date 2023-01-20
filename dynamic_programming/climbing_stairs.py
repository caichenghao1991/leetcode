# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = [0] * (n + 1)
        #
        # def dp(n):
        #     if n <= 1: return 1
        #     if memo[n] != 0:
        #         return memo[n]
        #     res = 0
        #     for i in [1, 2]:
        #         res += dp(n - i)
        #     memo[n] = res
        #     return memo[n]
        #
        # return dp(n)
        #
        #
        # if n <= 1: return 1
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 1, 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]


        def climbStairs(self, n: int) -> int:
            if n == 1: return 1
            pre, cur = 1, 1
            for i in range(2, n + 1):
                tmp = cur
                cur = cur + pre
                pre = tmp
            return cur


