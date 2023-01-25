# 674. Longest Continuous Increasing Subsequence
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        dp[0] = 1
        for i in range(1, l):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        return max(dp)

        # l = len(nums)
        # cur, res = 1, 1
        # for i in range(1, l):
        #     if nums[i] > nums[i - 1]:
        #         cur = cur + 1
        #         res = max(cur, res)
        #     else:
        #         cur = 1
        #
        # return res