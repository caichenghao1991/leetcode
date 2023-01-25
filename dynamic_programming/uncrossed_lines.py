# 1035. Uncrossed Lines     need rework
from typing import List


class Solution:          # equivalent to longest common sequence
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1) + 1, len(nums2) + 1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]