# 1005. Maximize Sum Of Array After K Negations            need rework
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=lambda x: abs(x), reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 != 0:
            nums[-1] = -abs(nums[-1])
        return sum(nums)
