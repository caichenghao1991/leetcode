# 46. Permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, track, used = [], [], [False] * len(nums)

        def backtrack():
            if len(track) == len(nums):
                res.append(track[:])
            elif len(track) > len(nums):
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                track.pop()

        nums.sort()
        backtrack()
        return res
