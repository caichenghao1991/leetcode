# 239. Sliding Window Maximum   need rework
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1: return nums
        res = [-100000] * (len(nums) - k + 1)
        dq = deque([0])
        for i in range(1, len(nums)):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i - dq[0] >= k:
                dq.popleft()
            if i >= k - 1:
                res[i - k + 1] = nums[dq[0]]
        return res
