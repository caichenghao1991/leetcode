# 39. Combination Sum
from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, track = [], []
        self.s = 0

        def backtrack(start):
            if self.s == target:
                res.append(track[:])
                return
            if self.s > target:
                return
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                self.s += candidates[i]
                backtrack(i)
                self.s -= candidates[i]
                track.pop()

        candidates.sort()
        backtrack(0)
        return res
