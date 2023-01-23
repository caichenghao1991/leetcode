# 416. Partition Equal Subset Sum
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum(nums) % 2 != 0:
        #     return False
        # l, target = len(nums), sum(nums) // 2
        # dp = [[0] * (target + 1) for _ in range(l)]
        #
        # for i in range(l):
        #     for j in range(target + 1):
        #         if j >= nums[i]:
        #             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        #
        # return dp[l - 1][target] == target
        #
        #
        # if sum(nums) % 2 != 0:
        #     return False
        # l, target = len(nums), sum(nums) // 2
        # dp = [0] * (target + 1)
        # for i in range(l):
        #     for j in range(target, nums[i] - 1, -1):
        #         dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        # return dp[target] == target



        if sum(nums) % 2 != 0:
            return False
        l, target = len(nums), sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(l):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]