# 53. Maximum Subarray   need rework
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        cur_sum = 0
        for v in nums:

            cur_sum += v
            if cur_sum > res:
                res = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return res
