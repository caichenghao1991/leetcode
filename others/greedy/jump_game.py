# 55. Jump Game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums) - 1):
            step = max(step - 1, nums[i])
            if step <= 0:
                return False
        return True
