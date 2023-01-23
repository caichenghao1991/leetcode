# 63. Unique Paths II
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # memo = [[0] * n for i in range(m)]
        # for i in range(n):
        #     if obstacleGrid[0][i] == 1:
        #         break
        #     memo[0][i] = 1
        # for i in range(m):
        #     if obstacleGrid[i][0] == 1:
        #         break
        #     memo[i][0] = 1
        #
        # def dp(i, j):
        #     if memo[i][j] != 0 or i == 0 or j == 0:
        #         return memo[i][j]
        #     if obstacleGrid[i][j] != 1:
        #         memo[i][j] = dp(i - 1, j) + dp(i, j - 1)
        #     return memo[i][j]
        #
        # return dp(m - 1, n - 1)

        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        #
        # dp = [[0] * n for i in range(m)]
        # for i in range(n):
        #     if obstacleGrid[0][i] == 1:
        #         break
        #     dp[0][i] = 1
        # for i in range(m):
        #     if obstacleGrid[i][0] == 1:
        #         break
        #     dp[i][0] = 1
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] != 1:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[m - 1][n - 1]


        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[i] = 1

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if j > 0:
                        dp[j] = dp[j] + dp[j - 1]
                else:
                    dp[j] = 0
        return dp[n - 1]
