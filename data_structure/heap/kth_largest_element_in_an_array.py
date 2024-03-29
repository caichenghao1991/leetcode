# 215. Kth Largest Element in an Array
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]
