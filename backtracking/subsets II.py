# 90. Subsets II
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, track = [], []

        def backtrack(start, size):
            if len(track) == size:
                res.append(track[:])
            elif len(track) > size:
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                track.append(nums[i])
                backtrack(i + 1, size)
                track.pop()

        nums.sort()
        for i in range(len(nums) + 1):
            backtrack(0, i)
        return res
