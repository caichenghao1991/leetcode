# 213. House Robber II
from typing import List


def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    l = len(nums)
    dp = [0] * (l + 1)
    dp[0], dp[1] = 0, nums[0]
    for i in range(2, l):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
    res = dp[l - 1]
    dp[1] = 0
    for i in range(2, l + 1):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
    return max(res, dp[l])
