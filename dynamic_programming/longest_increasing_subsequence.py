# 300. Longest Increasing Subsequence
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        dp=[0]*l
        dp[0]=1
        for i in range(l):
            ma=0
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    ma=max(ma,dp[j])
                j-=1
            dp[i]=ma+1
        return max(dp)