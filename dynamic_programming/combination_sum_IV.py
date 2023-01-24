# 377. Combination Sum IV            need rework
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        l, k = len(nums), 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(target + 1):
            for i in range(l):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]
        return dp[target]
