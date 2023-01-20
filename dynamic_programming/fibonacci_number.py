# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        # memo = [0] * (n + 1)
        #
        # def dp(n):
        #     if n <= 1:
        #         return n
        #     if memo[n] != 0:
        #         return memo[n]
        #     res = 0
        #     for i in [1, 2]:
        #         res += dp(n - i)
        #     memo[n] = res
        #     return memo[n]
        #
        # return dfs(n)


        # if n <= 1: return n
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 0, 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]


        if n <= 1:
            return n
        pre, cur = 0, 1
        for i in range(2, n + 1):
            cur, pre = cur + pre, cur
        return cur
