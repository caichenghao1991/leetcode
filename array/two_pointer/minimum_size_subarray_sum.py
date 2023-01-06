# 209. Minimum Size Subarray Sum
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        cur_sum = 0
        res = len(nums) + 1
        while r < len(nums):
            cur_sum += nums[r]
            r += 1
            while cur_sum >= target:
                if r - l < res:
                    res = r - l
                cur_sum -= nums[l]
                l += 1

        return res if res != len(nums) + 1 else 0
