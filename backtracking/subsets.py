# 78. Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        track, res = [], []

        def backtrack(start, size):
            if len(track) == size:
                res.append(track[:])
            elif len(track) > size:
                return
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i + 1, size)
                track.pop()

        nums.sort()
        for s in range(len(nums) + 1):
            backtrack(0, s)
        return res
