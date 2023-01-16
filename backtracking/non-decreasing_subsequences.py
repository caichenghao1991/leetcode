# 491. Non-decreasing Subsequences     need rework
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, track = [], []

        def backtrack(start):
            if len(track) >= 2:
                res.append(track[:])
            used = set()
            for i in range(start, len(nums)):
                if track and nums[i] < track[-1] or nums[i] in used:
                    continue
                used.add(nums[i])
                track.append(nums[i])
                backtrack(i + 1)
                track.pop()

        backtrack(0)
        return res
