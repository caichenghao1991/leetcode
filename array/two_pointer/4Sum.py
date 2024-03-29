# 18. 4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums) - 2):
                if nums[j] == nums[j - 1] and j > i + 1: continue
                m, n = j + 1, len(nums) - 1
                while m < n:
                    req = target - nums[i] - nums[j]
                    if nums[m] + nums[n] == req:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        while m < n and nums[m + 1] == nums[m]:
                            m += 1
                        while m < n and nums[n - 1] == nums[n]:
                            n -= 1
                        m += 1
                    elif nums[m] + nums[n] < req:
                        m += 1
                    else:
                        n -= 1
        return res
