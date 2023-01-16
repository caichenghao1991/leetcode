# 40. Combination Sum II
from typing import List

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        track, res = [], []
        self.s = 0

        def backtrack(start):
            if self.s == target:
                res.append(track[:])
            elif self.s > target:
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                self.s += nums[i]
                track.append(nums[i])
                backtrack(i + 1)
                track.pop()
                self.s -= nums[i]

        nums.sort()
        backtrack(0)
        return res