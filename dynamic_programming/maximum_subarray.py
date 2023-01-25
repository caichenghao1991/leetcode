# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # l = len(nums)
        # dp = [nums[0]] * l
        # for i in range(1, l):
        #     dp[i] = max(nums[i], dp[i - 1] + nums[i])
        # return max(dp)


        l = len(nums)
        res, cur = nums[0], nums[0]
        for i in range(1, l):
            cur = max(nums[i], cur + nums[i])
            res = max(res, cur)
        return res
