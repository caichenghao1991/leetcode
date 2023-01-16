# 47. Permutations II
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, track, used = [], [], [False] * len(nums)

        def backtrack():
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                track.pop()

        nums.sort()
        backtrack()
        return res
