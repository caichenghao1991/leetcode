# 198. House Robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * (l + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, l + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[l]
5